from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Post,Comment
from.models import Book
from .forms import CommentForm


# Create your views here.
def displayTime(request):
    now= datetime.datetime.now
    html="The Time is{}".format(now)
    return HttpResponse(html)

def displaycontact(request):
    return HttpResponse('Welcome to my contact')
#Class based View
class Myview (TemplateView):
    template_name="Index.html"

def book_list(request):
    books= Book.objects.all()
    return render(request, "book_list.html",{"books":books})


def post_list(request):
    post=Post.objects.all()
    paginator= Paginator(post,3)
    page=request.GET.get('page')
    try: 
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
           posts = paginator.page(paginator.num_pages) 
    return render(request,"index.html",{'page':page,'posts':posts})

#view for single post
def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    comments= post.comments.filter(active=True)
    new_comment=None
    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()

    else:
         comment_form= CommentForm()        
    return render(request, "post_details.html", {'post': post,'comments':comments,'comment_form':comment_form,'new_comment':new_comment})