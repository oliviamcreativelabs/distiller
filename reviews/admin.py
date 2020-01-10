from django.contrib import admin
from .models import Whiskey, Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('whiskey', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']


admin.site.register(Whiskey)
admin.site.register(Review, ReviewAdmin)
