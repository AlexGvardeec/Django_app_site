from django.db import models


# Создаем модель статьи Article
class Article(models.Model):
    title = models.CharField(max_length=256, null=False)
    slug = models.SlugField(max_length=50, db_index=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]