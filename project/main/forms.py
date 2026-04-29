from django import forms

from .models import New

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
        })
    }
    labels = {
        'title': 'Yangilik sarlavhasi',
        'text': "Yangilik matni",
        'category': 'Yangilik turi',
        'created': 'Yaratilgan vaqti',
        'updated': 'Yangilangan vaqti',
        'published': 'Chop etilgan',
        'image': "Yangilik uchun rasm"
    }