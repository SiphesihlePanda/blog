from django.urls import path

from blog.views import Myview, displayTime, displaycontact, book_list
from blog.views import post_list, post_detail

app_name = 'blog'

urlpatterns =[
   
    path("book list/", book_list),
    path("contact/", displaycontact),
   # path(" ", Myview.as_view(), name="home"),
    path("", post_list),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
    
    
]