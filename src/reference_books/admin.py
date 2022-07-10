from multiprocessing.context import ForkProcess
from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Author)
admin.site.register(models.BookSeries)
admin.site.register(models.LiteraryGenre)
admin.site.register(models.PublishingHouse)
