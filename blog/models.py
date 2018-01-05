"""Blog models for Django

Models needed to setup a general blog."""

from django.db import models
from django.conf import settings
from django.utils import timezone, text
import shortuuid
# Create your models here.


class Profile(models.Model):
    """The `Profile` model is an extension to the base Django User model."""
    class Meta:
        verbose_name = "profil"

    CAMPUSES = (
        ('blois', 'Blois'),
        ('bourges', 'Bourges')
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="utilisateur")
    headshot = models.ImageField(
        blank=True, null=True, verbose_name="photo de profil")
    campus = models.CharField(max_length=24, choices=CAMPUSES)

    # Manager
    profiles = models.Manager()

    @property
    def full_name(self):
        """Gets the full name of a user.

        For example: `<User: John Doe>.full_name` will give `John Doe`."""
        return "{} {}".format(self.user.first_name, self.user.last_name)

    @property
    def full_name_short(self):
        """Gets the short 'full name' of a user.

        For example: `<User: John Doe>.full_name_short` will give `J. Doe`."""
        return "{}. {}".format(str(self.user.first_name)[:1], self.user.last_name)

    def __str__(self):
        return self.full_name_short


class Category(models.Model):
    """Model that regroups several articles under one category."""
    class Meta:
        verbose_name = "catégorie"
    name = models.CharField(max_length=140, verbose_name="nom", unique=True)
    description = models.TextField(max_length=350)
    slug = models.SlugField(unique=True, max_length=50)

    # Manager
    categories = models.Manager()

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.name[:50])
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    """Piece of a blog, owned by a category."""
    title = models.CharField(max_length=140, verbose_name="titre")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="catégorie")
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="auteur")
    intro = models.TextField(max_length=350)
    image = models.ImageField(blank=True, null=True, upload_to="blog/articles")
    contents = models.TextField(verbose_name="contenu")
    created = models.DateTimeField(verbose_name="créé", auto_now_add=True)
    modified = models.DateTimeField(verbose_name="modifié", auto_now=True)
    views = models.IntegerField(default=0, verbose_name="vue")
    slug = models.SlugField(unique=True, max_length=50)

    # Manager
    articles = models.Manager()

    @property
    def trending_weight(self):
        """Gets a popularity metric through a simple calculation: number of views over time."""
        lifetime = timezone.now() - self.created
        return self.views / lifetime.total_seconds()

    def get_absolute_url(self):
        """Returns a `reverse`-able tuple that points to the public resource."""
        return 'blog:article', (self.slug,)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = "{}-{}".format(
                        text.slugify(self.title)[:42],  # slug.max_length - 8
                        shortuuid.ShortUUID().random(length=8))
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return "#{}. {}".format(self.id, self.title)
