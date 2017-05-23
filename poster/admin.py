from django.contrib import admin
from poster.models import UserProfile,ArtistProfile,CustomerProfile,poster,Category

admin.site.register(UserProfile)
admin.site.register(ArtistProfile)
admin.site.register(Category)
admin.site.register(poster)
admin.site.register(CustomerProfile)
