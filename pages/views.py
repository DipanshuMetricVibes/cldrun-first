from django.shortcuts import render

def home(request):
    """View for the home page"""
    return render(request, 'pages/home.html')

def about(request):
    """View for the about page"""
    return render(request, 'pages/about.html')

def contact(request):
    """View for the contact page"""
    return render(request, 'pages/contact.html')
