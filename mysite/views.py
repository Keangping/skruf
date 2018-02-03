# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound

# for database model
from .models import Collection, Tip, Dress_Guide, Dressen_Sitte
from .models import Dress, Stoff, Brudgom, Skjorte, Sko, Smoking, Slips, Sløyfe, Mansjettknapper
from .models import News_Image, Index_Content

# for apps.get_model('app_name', 'model_name')
from django.apps import apps

# In index(request):, for combine result of 3 querysets.
from itertools import chain

# should be set up like dictionary in saperate file.
class Metatag():
	title = 'BRIZ - Beste kvalitet til folkelige priser'
	description = 'BRIZ of Norway - Vi lager klær av beste kvalitet til folkelige priser. Som de eneste i Norge produserer vi dress og brudgom antrekk som er tilpasset din kropp og dine ønsker. Ditt design - vår jobb.'
	keywords = 'dress, skjorte, brudgom dress, smoking, skreddersydd dress, skreddersydd skjorte, bryllup, kjole & hvitt, livkjole, sjakett, brudgom vest, sko, slips, sløyfe, mansjettknapper, dress guide, dress tips, bryllups tips'
	page_topic = 'dress, skjorte, brudgom antrekk, smoking, skreddersydd dress, sko, slips, sløyfe, mansjettknapper'

# to get previous and next objects from QuerySet
def get_prev_and_next_items(target, items):
    found = False
    prev = None
    next = None
    for item in items:
        if found:
            next = item
            break
        if item.id == target.id:
            found = True
            continue
        prev = item
    return (prev, next)


def index(request):
	metatag = Metatag()
	# slide images & index content
	news_images = News_Image.objects.all()
	index_content = Index_Content.objects.all().first()

	# gallery, 5 from dress, smoking, brudgom's db
	dress = Dress.objects.all()[:5]
	brudgom = Brudgom.objects.all()[:5]
	smoking = Smoking.objects.all()[:5]
	index_gallery = list(chain(dress, brudgom, smoking))

	return render(request, 'mysite/index.html', {'metatag':metatag, 'news_images':news_images, 'index_content':index_content, 'index_gallery':index_gallery})

def contact(request):
	metatag = Metatag()
	metatag.title = 'BRIZ - Veien til den beste kvaliteten til folkelige priser'
	metatag.description = 'BRIZ - Veien til den beste kvaliteten til folkelige priser. Telefon, adresse og epostadresse, kart'
	metatag.keywords = 'Telefon, adresse og epostadresse, kart'
	metatag.page_topic = 'BRIZ'
	return render(request, 'mysite/contact.html', {'metatag':metatag})

def tips(request):
	metatag = Metatag()
	metatag.title = 'BRIZ - 10 tips for ditt perfekte bryllup'
	metatag.description = 'Gode tips og ideer til ditt perfekte bryllup'
	metatag.keywords = 'tips, perfekte, bryllup, bryllup planlegging, råd'
	metatag.page_topic = 'tips, bryllup'

	tips = Tip.objects.all()
	if not tips:
		return HttpResponseNotFound('<h1>Cant find tip in database</h1><p>   ***might have to return render instead</p>')

	return render(request, 'mysite/tips.html', {'metatag':metatag, 'tips':tips})

def dressen_sitte(request):
	metatag = Metatag()
	metatag.title = 'Dressekspert - Slik skal dressen sitte'
	metatag.description = 'Slik skal dressen sitte – Beste dresstips'
	metatag.keywords = 'Slik skal dressen sitte, Slik finner du den perfekte dressen, Tips til å kjøpe dress, Beste dresstips noensinne, Julebord, 17 mai, bryllup'
	metatag.page_topic = 'Slik skal dressen sitte, dress guide'

	dressen_sittes = Dressen_Sitte.objects.all()
	if not dressen_sittes:
		return HttpResponseNotFound('<h1>Cant find dressen_sitte in database</h1><p>   ***might have to return render instead</p>')

	return render(request, 'mysite/dressen_sitte.html', {'metatag':metatag, 'dressen_sittes':dressen_sittes})

def dress_guide(request):
	metatag = Metatag()
	metatag.title = 'Dressekspert gir sine beste tips – Norges bestes Dress guide'
	metatag.description = 'Norges beste Dress guide'
	metatag.keywords = 'Norges beste Dress guide, for menn, Kan du disse dressreglene, Dette må du vite når du skal kjøpe dress, Dressekspert gir sine beste tips, Julebord, 17 mai, Bryllup'
	metatag.page_topic = 'Dress guide'

	dress_guides = Dress_Guide.objects.all()
	if not dress_guides:
		return HttpResponseNotFound('<h1>Cant find dress_guide in database</h1><p>   ***might have to return render instead</p>')
	
	return render(request, 'mysite/dress_guide.html', {'metatag':metatag, 'dress_guides':dress_guides})

def detail(request, product_type, product_name):

	product_model = apps.get_model('mysite', product_type.capitalize())
	try:
		product = product_model.objects.get(product_name=product_name)

		# .filter for multiple objects
		product_gallery = product_model.objects.filter(product_color=product.product_color)
		
	except Dress.DoesNotExist:
		return HttpResponseNotFound('<h1>Cant find product in database</h1><p>   ***might have to return render instead</p>')

	metatag = Metatag()
	metatag.title = product.product_description
	metatag.description = product.product_description
	metatag.keywords = product.product_keyword
	metatag.page_topic = product.product_type + " " + product.product_color

	pre_and_next = get_prev_and_next_items(product, product_gallery)
	prev_product = pre_and_next[0]
	next_product = pre_and_next[1]
	return render(request, 'mysite/detail.html', {'metatag':metatag, 'product':product, 'product_gallery':product_gallery, 'prev_product':prev_product, 'next_product':next_product})

# collection's model contains 		type_of_collection, collection_content, collection_image.
# collection's template requires 	collection's image, collection's content, callection_gallery?, matatag? 
def collection(request, collection_type):
	metatag = Metatag()
	metatag.title = 'BRIZ - Dress i beste kvalitet til folkelige priser'
	metatag.description = 'BRIZ of Norway - Vi lager dress av beste kvalitet til folkelige priser. Som de eneste i Norge produserer vi dress som er tilpasset din kropp og dine ønsker. Ditt design - vår jobb.'
	metatag.keywords = 'dress, brudgom dress, skreddersydd dress, bryllup dress, slim fit dress'
	metatag.page_topic = collection_type
	
	# for /skreddersydd with collection_type = 'skreddersydd', need to change for collection database.
	if collection_type == 'skreddersydd':
		collection_type = 'stoff'
	
	try:
		collection = Collection.objects.get(type_of_collection=collection_type)
	except Collection.DoesNotExist:
		return HttpResponseNotFound('<h1>Cant find collection in database</h1><p>   ***might have to return render instead</p>')

	# apps.get_model('app_name', 'model_name')
	product_model = apps.get_model('mysite', collection_type.capitalize())
	collection_gallery = product_model.objects.all()
	if not collection_gallery:
		return HttpResponseNotFound('<h1>Cant find collection_gallery in database</h1><p>   ***might have to return render instead</p>')
	
	return render(request, 'mysite/collection.html', {'metatag':metatag, 'collection':collection, 'collection_gallery':collection_gallery})








