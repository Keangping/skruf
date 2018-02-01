from django.shortcuts import render

def index(request):
	return render(request, 'mysite/index.html', {})

def contact(request):
	return render(request, 'mysite/contact.html', {})

def tips(request):
	return render(request, 'mysite/tips.html', {})

def dressen_sitte(request):
	return render(request, 'mysite/dressen_sitte.html', {})

def dress_guide(request):
	return render(request, 'mysite/dress_guide.html', {})

def collection(request, collection_type):
	collection_type = collection_type
	return render(request, 'mysite/collection.html', {'collection_type':collection_type})