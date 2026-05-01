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
    if request.user.is_authenticated:
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
    else:
        redirect('home')

def update_new(request: HttpRequest, new_id):
    if request.user.is_authenticated:
        new = New.objects.get(id = new_id)
        if request.method == 'POST':
            form = NewForm(data=request.POST, files=request.FILES, instance=new)
            if form.is_valid():
                form.save()
                return  redirect('detail', new_id=new.pk)
        form = NewForm(instance=new)
        context = {
            'form': form
        }

        return render(request, 'main/add_news.html', context)
    else:
        redirect('home')

def delete_new(request: HttpRequest, new_id):
    if request.user.is_authenticated:
        new = New.objects.get(id=new_id)
        if request.method == 'POST':
            new.delete()
            return redirect('home')
        context = {
            'new': new
        }
        return render(request, 'main/conform_delete.html', context)
    else:
        redirect('home')