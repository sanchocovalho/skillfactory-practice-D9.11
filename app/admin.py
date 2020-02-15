from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Category, PostAuthor
from .forms import PostAuthorCreationForm, PostAuthorChangeForm
from django.contrib import messages

class PostAuthorAdmin(UserAdmin):
    add_form = PostAuthorCreationForm
    form = PostAuthorChangeForm
    model = PostAuthor
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active']

admin.site.register(PostAuthor, PostAuthorAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not Category.objects.filter(title=obj.title).exists():
            super().save_model(request, obj, form, change)
            messages.success(request,'Категория “%s” была создана...' % obj.title)
            messages.set_level(request, messages.ERROR)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request,'Категория “%s” не создана, поскольку уже существует.' % obj.title)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
