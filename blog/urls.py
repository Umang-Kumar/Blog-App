from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    # blogs
    path('', views.IndexView.as_view(), name='index'),
    path('blog/', views.PostView.as_view(), name='posts'),
    path('blog/<slug:slug>', views.PostDetailView.as_view(), name='post'),
    path('postBlog/', views.PostBlog.as_view(), name='postBlog'),
    path('search/', views.Search.search, name='search'),

    # authentication
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),

    # admin
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # contact & about
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),

]