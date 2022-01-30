from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
	title = models.CharField(max_length=100)
	blogCat_id = models.AutoField(primary_key=True)
	content = models.TextField()
	url = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'category/',null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)

	def image_tag(self):
		return format_html('<img src="/uploads/{}" style="width:50px;height:50px;border-radius:50%;"/>'.format(self.image))

	def __str__(self):
		return self.title

class Blog(models.Model):
	blog_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	content = RichTextUploadingField()
	url = models.CharField(max_length=255)
	cat = models.ForeignKey(Category, on_delete=models.CASCADE)
	image = models.ImageField(upload_to = 'blog/')
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']


	def __str__(self):
		return self.title
