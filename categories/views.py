from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
from .models import Category

def show_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories:show_categories')
    else:
        form = CategoryForm()
    return render(request, 'categories/add_category.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:show_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/edit_category.html', {'form': form, 'category': category})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:show_categories')
    return render(request, 'categories/delete_category.html', {'category': category})
