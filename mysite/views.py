from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

from .models import Collection, Dress

# -*- coding: utf-8 -*-

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

def detail(request):
	product = Dress.objects.get(product_name="briz-navy-blå")
	print(product)
	return render(request, 'mysite/detail.html', {'product': product})

# collection's model contains 		type_of_collection, collection_content, collection_image.
# collection's template requires 	collection's image, collection's content, callection_gallery?, matatag? 
def collection(request, collection_type):
	try:
		collection = Collection.objects.get(type_of_collection=collection_type)
		# collection_gallery = 
	except Collection.DoesNotExist:
		return HttpResponseNotFound('<h1>Cant find collection in database</h1><p>   ***might have to return render instead</p>')

	print(collection)
	return render(request, 'mysite/collection.html', {'collection':collection})