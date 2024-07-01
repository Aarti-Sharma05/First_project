from django.contrib import admin
from .models import Post, Category,Profile

admin.site.register(Category)
admin.site.register(Profile)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('js/custom.js','js/tinymce.min.js',)
