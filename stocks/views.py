from django.shortcuts import render
from django.http import HttpResponse

from stocks.models import Book

# Create your views here.
def home(request):
	return HttpResponse("hi")

def books(request):
	books = Book.objects.all()[:5]
	return render(request,"stocks/books.html",{"books":books})