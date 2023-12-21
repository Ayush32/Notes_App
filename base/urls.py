from django.urls import path
from . import views

# step 2 - create urls.py file in base directory(app directoy), import views and path from django.urls 
urlpatterns = [
    # create urlsconf in base(appname) directory
    # name = 'views function name'
    path("",views.index,name = 'index')
]



