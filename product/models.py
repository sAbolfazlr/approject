from django.db import models


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='s_category', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField()
    time = models.TimeField(null=True, blank=True)
    released = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='media/thumbnail/', null=True, blank=True)
    main_file = models.FileField(upload_to='media/main_file/', null=True, blank=True)

    def __str__(self):
        return self.name