
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('save_blog/', views.save_blog, name='save_blog'),
    path('saved_blog',views.saved_blog,name='saved_blog'),
   path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
      path('logout/', views.logout_view, name='logout_view'),
]
