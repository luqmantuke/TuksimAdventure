from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('blog/', views.BlogPageList.as_view(), name='blog'),
    path('post/new', views.addpost, name='post_form'),
    path('<slug:slug>/', views.detail, name='post_detail'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/dashboard/', views.dashboard, name='dashboard'),
    path('post/<slug:slug>/update', views.updatepost, name='update_post'),
    path('post/<slug:slug>/delete', views.deletepost, name='delete_post'),
]
