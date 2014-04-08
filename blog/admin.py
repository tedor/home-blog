from settings import STATIC_URL
from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug')
    list_filter = ('title', )
    date_hierarchy = 'created_at'
    ordering = ('-updated_at', )
    search_fields = ('title', 'text')
    ordering = ['-created_at']
        
#    fields = ('title', 'text', 'slug', )

admin.site.register(Post, PostAdmin)