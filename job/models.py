from django.db import models

JOP_TYPE = [
    ('FULL_TIME', 'FULL_TIME'),
    ('PART_TIME', 'PART_TIME'),
]


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

    def __str__(self):
        return self.title + ", " + self.jop_type


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
