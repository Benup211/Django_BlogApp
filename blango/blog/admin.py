from django.contrib import admin
from blog.models import Tag,Post,Comment
# Register your models here.
admin.site.register(Tag)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}#slug field update when title field is changed
    list_display = ('slug', 'published_at','title')#display inside value in Post outside
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)