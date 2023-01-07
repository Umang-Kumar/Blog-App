from django.contrib import admin

# Register your models here.
from .models import(
    UserProfile,
    Post,
    ContactProfile,
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_active')
    readonly_fields = ('slug',)

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)