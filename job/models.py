from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

JOP_TYPE = [
    ('FULL_TIME', 'FULL_TIME'),
    ('PART_TIME', 'PART_TIME'),
]


def image_upload(instance, filename):
    image_name, extinction = filename.split(".")


# Create your models here.
class Jop(models.Model):
    title = models.CharField(max_length=100)
    # location
    jop_type = models.CharField(max_length=15, choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to='jobs/')
    job_img = models.FileField(upload_to='jobs/', validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jop, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
