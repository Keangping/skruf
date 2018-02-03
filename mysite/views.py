# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

from .models import Collection, Dress, Tip, Dressen_Sitte, Dress_Guide

# should be set up like dictionary in saperate file.
class Metatag():
	title = 'BRIZ - Beste kvalitet til folkelige priser'
	description = 'BRIZ of Norway - Vi lager klær av beste kvalitet til folkelige priser. Som de eneste i Norge produserer vi dress og brudgom antrekk som er tilpasset din kropp og dine ønsker. Ditt design - vår jobb.'
	keywords = 'dress, skjorte, brudgom dress, smoking, skreddersydd dress, skreddersydd skjorte, bryllup, kjole & hvitt, livkjole, sjakett, brudgom vest, sko, slips, sløyfe, mansjettknapper, dress guide, dress tips, bryllups tips'
	page_topic = 'dress, skjorte, brudgom antrekk, smoking, skreddersydd dress, sko, slips, sløyfe, mansjettknapper'




def index(request):
	metatag = Metatag()
	return render(request, 'mysite/index.html', {'metatag':metatag})

def contact(request):
	metatag = Metatag()
	metatag.title = 'BRIZ - Veien til den beste kvaliteten til folkelige priser'
	metatag.description = 'BRIZ - Veien til den beste kvaliteten til folkelige priser. Telefon, adresse og epostadresse, kart'
	metatag.keywords = 'Telefon, adresse og epostadresse, kart'
	metatag.page_topic = 'BRIZ'
	return render(request, 'mysite/contact.html', {'metatag':metatag})

def tips(request):
	metatag = Metatag()
	metatag.title = 'BRIZ - 10 tips til ditt bryllup'
	metatag.description = ''
	metatag.keywords = ''
	metatag.page_topic = ''

	tips = Tip.objects.all()
	if not tips:
		return HttpResponseNotFound('<h1>Cant find tip in database</h1><p>   ***might have to return render instead</p>')

	return render(request, 'mysite/tips.html', {'metatag':metatag, 'tips':tips})

def dressen_sitte(request):
	metatag = Metatag()
	metatag.title = 'BRIZ - 10 tips til ditt bryllup'
	metatag.description = ''
	metatag.keywords = ''
	metatag.page_topic = ''

	dressen_sittes = Dressen_Sitte.objects.all()
	if not dressen_sittes:
		return HttpResponseNotFound('<h1>Cant find dressen_sitte in database</h1><p>   ***might have to return render instead</p>')

	return render(request, 'mysite/dressen_sitte.html', {'metatag':metatag, 'dressen_sittes':dressen_sittes})

def dress_guide(request):
	metatag = Metatag()
	metatag.title = 'BRIZ - 10 tips til ditt bryllup'
	metatag.description = ''
	metatag.keywords = ''
	metatag.page_topic = ''

	dress_guides = Dress_Guide.objects.all()
	if not dress_guides:
		return HttpResponseNotFound('<h1>Cant find dress_guide in database</h1><p>   ***might have to return render instead</p>')
	
	return render(request, 'mysite/dress_guide.html', {'metatag':metatag, 'dress_guides':dress_guides})

def detail(request):
	metatag = Metatag()
	metatag.title = 'BRIZ - 10 tips til ditt bryllup'
	metatag.description = ''
	metatag.keywords = ''
	metatag.page_topic = ''
	product = Dress.objects.get(product_name="briz-navy-blå")
	print(product)
	return render(request, 'mysite/detail.html', {'metatag':metatag, 'product': product})

# collection's model contains 		type_of_collection, collection_content, collection_image.
# collection's template requires 	collection's image, collection's content, callection_gallery?, matatag? 
def collection(request, collection_type):
	metatag = Metatag()
	metatag.title = 'BRIZ - 10 tips til ditt bryllup'
	metatag.description = ''
	metatag.keywords = ''
	metatag.page_topic = ''
	try:
		# for /skreddersydd with collection_type = 'skreddersydd', need to change for collection database.
		if collection_type == 'skreddersydd':
			collection_type = 'stoff'

		collection = Collection.objects.get(type_of_collection=collection_type)
		# collection_gallery = 
	except Collection.DoesNotExist:
		return HttpResponseNotFound('<h1>Cant find collection in database</h1><p>   ***might have to return render instead</p>')

	print(collection)
	return render(request, 'mysite/collection.html', {'metatag':metatag, 'collection':collection})