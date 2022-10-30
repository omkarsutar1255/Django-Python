from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # This is way to pass values with variables to html
    context = {
        'variable1' : 'value1',
        'variable2' : 'value2'
    }
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
