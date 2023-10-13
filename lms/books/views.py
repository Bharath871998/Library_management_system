from django.shortcuts import  render, redirect
from .models import Book
# from django.views import View
from .forms import BookForm
# Create your views here.

def home(request):
    data = Book.objects.all()
    return render(request ,"crud/home.html", {"bdata": data})

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()   
    return render(request, 'crud/add.html', {'form': form})
    
    
def edit(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            my_book = Book.objects.get(id = id)
            bform = BookForm(instance=my_book)
        return render(request, 'crud/edit.html', {'form': bform})
    else:
        if id == 0:
            bform = BookForm(request.POST)
        else:
            book = Book.objects.get(id=id)
            bf = BookForm(request.POST, instance = book)
            if bf.is_valid():
                bf.save()
                return redirect('/')
            else:
                return render(request, 'crud/edit.html', {'form': bform})
    
    
def delete(request,id):
    dform = Book.objects.get(id=id)
    dform.delete()
    return redirect('/')