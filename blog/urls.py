from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', views.PostView.as_view(), name='posts'),
    path('blog/<slug:slug>', views.PostDetailView.as_view(), name='post'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('about/', views.AboutView.as_view(), name='about'),
    path('postBlog/', views.PostBlog.as_view(), name='postBlog'),
]