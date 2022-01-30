from django.contrib import admin
from .models import Blog, Category

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('image_tag', 'title','url', 'created_at')
	search_fields = ('title',)
	list_per_page = 30

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','url', 'created_at')
	search_fields = ('title',)
	list_filter = ('cat',)
	list_per_page = 30


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)