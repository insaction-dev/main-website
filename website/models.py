from django.db import models

# Create your models here.


class News(models.Model):
    class Meta:
        verbose_name_plural = "News"

    title = models.CharField(max_length=40, verbose_name="Titre")
    subtitle = models.CharField(max_length=60, verbose_name="Sous-titre")
    image = models.ImageField(upload_to="news")
    pub_date = models.DateField(verbose_name="Date de publication")
    blog_post = models.ForeignKey(
        'blog.Article', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Article")

    # Manager
    news = models.Manager()

    def __str__(self):
        return self.title
