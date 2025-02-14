from django.contrib import admin
from .models import Memo, Tag
# Register your models here.

admin.site.register(Memo)
admin.site.register(Tag)