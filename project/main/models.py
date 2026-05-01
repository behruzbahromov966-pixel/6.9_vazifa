from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator

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
    video = models.FileField(upload_to='videos/', blank=True, null=True, validators=[FileExtensionValidator(
        allowed_extensions=['mp4', 'avi'],
        message='Faqat .mp4 va .avi fayllar uchun ruxsat etilgan!!!'
    )])
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(1, 'Bitta yulduzdan kam baholash mumkin emas!'),
        MaxValueValidator(5, 'Beshta yulduzdan ko\'p baholay olmaysiz!')
    ], default=0)

    def __str__(self):
        return f"Title: {self.title}, Category: {self.category}"

    def __repr__(self):
        return f"Pk: {self.pk}, Title: {self.title}, Text: {self.text}, Category: {self.category}"

class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"Pk: {self.pk}, Name: {self.text}"