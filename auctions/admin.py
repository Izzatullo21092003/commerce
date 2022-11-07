from django.contrib import admin

from auctions.models import Listing, User, Category, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Comment)