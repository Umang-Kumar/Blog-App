from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # blogs
    path('', views.IndexView.as_view(), name='index'),
    path('blog/', views.PostView.as_view(), name='posts'),
    path('blog/<slug:slug>', views.PostDetailView.as_view(), name='post'),
    path('postBlog/', views.PostBlog.as_view(), name='postBlog'),
    path('blog/<slug:slug>/edit/', views.EditPostView.as_view(), name='edit_post'),
    path('search/', views.SearchBlog.as_view(), name='search'),
    path('blog/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('page/<int:page_number>/', views.IndexView.as_view(), name='index_paginated'),
    
    # profile
    path("profile/", views.DashboardView.as_view(), name="profile"),
    path("profile/edit/", views.EditProfileView.as_view(), name="edit_profile"),

    # authentication
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    # admin
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # contact & about
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
]
