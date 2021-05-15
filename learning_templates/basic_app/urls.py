# from django.conf.urls import url
from django.urls import path
from basic_app import views

# Template Tags Global Name
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    # url(r'^$',views.users,name='users'),
    path('other/', views.other, name='other'),
]
