from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Category, New
from .forms import NewForm

# Create your views here.
def home(request: HttpRequest):
    categories = Category.objects.all()
    news = New.objects.all()
    context = {
        'categories': categories,
        'news': news
    }

    return render(request, 'main/index.html', context)

def detail(request: HttpRequest, new_id):
    categories = Category.objects.all()
    new = New.objects.get(id=new_id)
    context = {
        'categories': categories,
        'new': new
    }

    return render(request, 'main/detail.html', context)

def new_by_category(request: HttpRequest, category_id):
    categories = Category.objects.all()
    news = New.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'categories': categories,
        'news': news,
        'title': category.name
    }

    return render(request, 'main/index.html', context)

def add_new(request: HttpRequest):
    if request.method == 'POST':
        form = NewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect('detail', new_id=new.pk)
    form = NewForm()
    context = {
        'form': form
    }

    return render(request, 'main/add_news.html', context)