from django.db import models

PRODUCT_TYPE_CHOICES = (
	('dress', 'dress'),
	('brudgom', 'brudgom'),
	('skjorte', 'skjorte'),
	('sko', 'sko'),
	('smoking', 'smoking'),
	('slips', 'slips'),
	('mansjett', 'mansjett'),
	('sloyfe', 'sloyfe')
)

COLLECT_CONTENT_MAX_LENGTH = 5000

class Collection(models.Model):
	type_of_collection 	= models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
	collection_content	= models.TextField()
	collection_image	= models.FileField()

	def __str__(self):
		return self.type_of_collection
