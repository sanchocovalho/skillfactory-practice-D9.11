from django.contrib import admin
from app.models import Post, Category, PostAuthor
from django.contrib.auth.admin import UserAdmin
from app.forms import PostAuthorCreationForm, PostAuthorChangeForm

class PostAuthorAdmin(UserAdmin):
    add_form = PostAuthorCreationForm
    form = PostAuthorChangeForm
    model = PostAuthor
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']

admin.site.register(PostAuthor, PostAuthorAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
