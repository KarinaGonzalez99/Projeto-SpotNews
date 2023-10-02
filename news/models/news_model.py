from django.db import models
from django.core.exceptions import ValidationError
from .user_model import Users
from .category_model import Categories


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_title], blank=False, null=False
    )
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField(blank=False, null=False)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title
