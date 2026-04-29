from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Name: {self.name}"

    def __repr__(self):
        return f"Pk: {self.pk}, Name: {self.name}"

class New(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"Title: {self.title}, Category: {self.category}"

    def __repr__(self):
        return f"Pk: {self.pk}, Title: {self.title}, Text: {self.text}, Category: {self.category}"
