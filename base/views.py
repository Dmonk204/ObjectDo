from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')

def service_details1(request):
    return render(request, 'base/service-details1.html')

def service_details2(request):
    return render(request, 'base/service-details2.html')

def service_details3(request):
    return render(request, 'base/service-details3.html')

def service_details4(request):
    return render(request, 'base/service-details4.html')

def service_details5(request):
    return render(request, 'base/service-details5.html')

def services(request):
    return render(request, 'base/services.html')

def portfolio(request):
    return render(request, 'base/portfolio.html')

def contact(request):
    return render(request, 'base/contact.html')