from django.shortcuts import render

def index(request):
	return render(request, 'mysite/index.html', {})

def contact(request):
	return render(request, 'mysite/contact.html', {})

