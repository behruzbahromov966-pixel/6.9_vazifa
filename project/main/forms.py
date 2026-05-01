from django import forms
from django.core.exceptions import ValidationError

from .models import New, Category, Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'name': 'Nomi'
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 20:
            raise ValidationError("Category nomi juda uzun bo'lishi kerak emas!!!✖️")

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Sarlavha',
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Yangilik matni',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'created': forms.DateTimeInput(attrs={
                'class': 'form-control'
            }),
            'updated': forms.DateTimeInput(attrs={
                'class': 'form-control'
            }),
            'published': forms.CheckboxInput(),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'video': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'title': 'Yangilik sarlavhasi',
            'text': "Yangilik matni",
            'category': 'Yangilik turi',
            'created': 'Yaratilgan vaqti',
            'updated': 'Yangilangan vaqti',
            'published': 'Chop etilgan',
            'image': "Yangilik uchun rasm",
            'video': 'Yangilik uchun video'
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)