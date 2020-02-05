from django.contrib import admin
from . models import Contact,Post,Category


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Category)

# Register your models here.
