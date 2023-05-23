from . import views
from django.urls import path,include









urlpatterns = [
    path('post/' , views.post , name = "post"),
    path('get/' , views.get , name = "get"),
    # path('postnew/' , views.indexNew , name = "inputNew"),
    path('getnew/' , views.getNew , name = "getNew"),
    path('get1/' , views.get1 , name = "get1"),
    # path('new/' , views.new , name = "new"),
    
]
