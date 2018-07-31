from django.db import models

from uuid import uuid4
# Create your models here.


class BaseEntity(models.Model):
    class Meta:
        abstract = True
    oid = models.UUIDField(verbose_name="ID d'objet", default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Campus(BaseEntity):
    class Meta:
        verbose_name_plural = "campus"
    name = models.CharField(max_length=140, verbose_name="nom")

    def __str__(self):
        return self.name


class Group(BaseEntity):
    class Meta:
        verbose_name = "groupe"
    name = models.CharField(max_length=140, verbose_name="nom")

    def __str__(self):
        return self.name


class Person(BaseEntity):
    class Meta:
        verbose_name = "personne"

    first_name = models.CharField(verbose_name="prénom", max_length=140)
    last_name = models.CharField(verbose_name="nom", max_length=140)
    phone_number = models.CharField(
        verbose_name="numéro de téléphone",
        max_length=11,
        blank=True, null=True
    )
    email = models.CharField(max_length=255, blank=True, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name="people")
    groups = models.ManyToManyField(Group, related_name="people")

    def save(self, *args, **kwargs):
        if self.pk is None and self.email is None:
            self.email = '{}.{}@insa-cvl.fr'.format(str(self.first_name).lower(), str(self.last_name).lower())
        return super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return '{} <{}>'.format(str(self), self.email)