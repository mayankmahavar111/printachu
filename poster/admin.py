from django.contrib import admin
from poster.models import UserProfile,ArtistProfile,CustomerProfile,Category

admin.site.register(UserProfile)
admin.site.register(ArtistProfile)
admin.site.register(CustomerProfile)
admin.site.register(Category)
