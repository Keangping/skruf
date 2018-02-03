from django.contrib import admin

from .models import Collection, Tip, Dress_Guide, Dressen_Sitte
from .models import Dress, Stoff, Brudgom, Skjorte, Sko, Smoking, Slips, Sløyfe, Mansjettknapper
from .models import News_Image, Index_Content

admin.site.register(Collection)

admin.site.register(Tip)
admin.site.register(Dress_Guide)
admin.site.register(Dressen_Sitte)

admin.site.register(Stoff)
admin.site.register(Dress)
admin.site.register(Brudgom)
admin.site.register(Skjorte)
admin.site.register(Sko)
admin.site.register(Smoking)
admin.site.register(Slips)
admin.site.register(Sløyfe)
admin.site.register(Mansjettknapper)

admin.site.register(News_Image)
admin.site.register(Index_Content)
