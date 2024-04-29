from django.contrib import admin

from AppCRUD.models import ProdectDetails
# # Register your models here.
#admin.site.register(ProdectDetails)

#from django.contrib import admin
#from.models import ProdectDetails
# Register your models here.

@admin.register(ProdectDetails)
class ProdectDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','description','quantity','Price')



