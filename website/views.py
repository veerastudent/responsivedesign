from django.shortcuts import render

# Create your views here.

def productsresponsive(request):
    context = {}
    return render(request, 'website/productsresponsive.html', context)
