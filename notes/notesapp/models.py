from django.db import models

class document(models.Model):
	title = models.CharField(max_length=200)
	content=models.TextField(blank=True,null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	modified_at=models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ('title', )
