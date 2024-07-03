from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def travelguide(request):
    return render(request, 'travelguide.html')

def invest(request):
    return render(request, 'invest.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def place(request):
    return render(request, 'place.html')

def food(request):
    return render(request, 'food.html')
def wildlife(request):
    return render(request, 'wildlife.html')

def art(request):
    return render(request, 'art.html')

def culture(request):
    return render(request, 'culture.html')

def top10(request):
    return render(request, 'top10.html')

def guidelines(request):
    return render(request, 'guidelines.html')



