from django.db import models

# -*- coding: utf-8 -*-

PRODUCT_TYPE_CHOICES = (
	('dress', 'dress'),
	('brudgom', 'brudgom'),
	('skjorte', 'skjorte'),
	('sko', 'sko'),
	('smoking', 'smoking'),
	('slips', 'slips'),
	('mansjettknapper', 'mansjettknapper'),
	('sløyfe', 'sløyfe'),
	('stoff', 'stoff'),
)

PRODUCT_COLOR_CHOICES = (
	# the value of object, the value that show in admin
	('blå', 'blå'),
	('grå', 'grå'),
	('sort', 'sort'),
	('ivory', 'ivory'),
	('hvit', 'hvit'),
	('brun', 'brun'),
	('lilla', 'lilla'),
	('rosa', 'rosa'),
	('beige', 'beige'),
	('grønn', 'grønn'),
	('gul', 'gul'),
	('rød', 'rød'),

)

BLOG_HEADLINE_MAX_LENGTH = 100
BLOG_CONTENT_MAX_LENGTH = 3000

class Tip(models.Model):
	tip_headline	= models.CharField(max_length=BLOG_HEADLINE_MAX_LENGTH)
	tip_image		= models.FileField()
	tip_content		= models.TextField(max_length=BLOG_CONTENT_MAX_LENGTH)

	def __str__(self):
		return self.tip_headline

class Dress_Guide(models.Model):
	dress_guide_headline	= models.CharField(max_length=BLOG_HEADLINE_MAX_LENGTH)
	dress_guide_image		= models.FileField()
	dress_guide_content		= models.TextField(max_length=BLOG_CONTENT_MAX_LENGTH)

	def __str__(self):
		return self.dress_guide_headline

class Dressen_Sitte(models.Model):
	dressen_sitte_headline	= models.CharField(max_length=BLOG_HEADLINE_MAX_LENGTH)
	dressen_sitte_image		= models.FileField()
	dressen_sitte_content	= models.TextField(max_length=BLOG_CONTENT_MAX_LENGTH)

	def __str__(self):
		return self.dressen_sitte_headline

PRODUCT_TYPE_MAX_LENGTH = 20
PRODUCT_COLOR_MAX_LENGTH = 20
PRODUCT_NAME_MAX_LENGTH = 50
PRODUCT_DESCRIPTION_MAX_LENGTH = 50
PRODUCT_CONTENT_MAX_LENGTH = 5000
PRODUCT_GALLERY_CONTENT_MAX_LENGTH = 150
PRODUCT_KEYWORD_MAX_LENGTH = 50

class Dress(models.Model):
	# for url, and title
	product_name			= models.CharField(max_length=PRODUCT_NAME_MAX_LENGTH, unique=True)

	# for matatag:description, Top text in gallery
	product_description		= models.CharField(max_length=PRODUCT_DESCRIPTION_MAX_LENGTH)

	# for main text below image
	product_content			= models.TextField(max_length=PRODUCT_CONTENT_MAX_LENGTH)

	# maybe dont need it since we saperate the database
	product_type 			= models.CharField(max_length=PRODUCT_TYPE_MAX_LENGTH, choices=PRODUCT_TYPE_CHOICES)

	product_image			= models.FileField()
	
	# for Below text in gallery
	product_gallery_content = models.TextField(max_length=PRODUCT_GALLERY_CONTENT_MAX_LENGTH)

	# for matatag:keyword
	product_keyword			= models.CharField(max_length=PRODUCT_KEYWORD_MAX_LENGTH)

	# for detail's gallery to get the same type of color to show, **unique
	product_color			= models.CharField(max_length=PRODUCT_COLOR_MAX_LENGTH, choices=PRODUCT_COLOR_CHOICES)


class Collection(models.Model):
	type_of_collection 	= models.CharField(max_length=PRODUCT_TYPE_MAX_LENGTH, choices=PRODUCT_TYPE_CHOICES)
	collection_content	= models.TextField()
	collection_image	= models.FileField()

	def __str__(self):
		return self.type_of_collection
