from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField


class Category(MPTTModel):

    name = models.CharField(
        max_length=255
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Request(models.Model):

    handled = models.BooleanField(
        default=False
    )

    creation = models.DateTimeField(
        auto_now_add=True
    )

    update = models.DateTimeField(
        auto_now=True
    )

    name = models.CharField(
        max_length=255
    )

    description = models.CharField(
        max_length=255
    )

    location = models.ForeignKey(
        'geodata.NPA',
        on_delete=models.SET_NULL,
        null=True,
        related_name='located_request'
    )

    website = models.URLField(
        blank=False
    )

    phone = PhoneNumberField(
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    category = models.CharField(
        max_length=255
    )

    delivery = models.CharField(
        max_length=255
    )

class Business(models.Model):

    name = models.CharField(
        max_length=255
    )

    location = models.ForeignKey(
        'geodata.NPA',
        on_delete=models.SET_NULL,
        null=True,
        related_name='located'
    )

    description = models.TextField(
        blank=True
    )

    main_category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='as_main_category'
    )

    other_categories = models.ManyToManyField(
        'Category',
        related_name='as_other_category',
        blank=True
    )

    delivers_to = models.ManyToManyField(
        'geodata.NPA',
        related_name='delivers',
        blank=True
    )

    website = models.URLField(
        blank=False
    )

    phone = PhoneNumberField(
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    class Meta:
        verbose_name_plural = 'businesses'

    def __str__(self):
        return '%s (%s)' % (self.name, self.location)
