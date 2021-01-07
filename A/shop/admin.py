from django.contrib import admin

from .models import Categories , Product , Comment








class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name'],
    }
    list_display = ('name','price','available')
    list_editable=('price','available')
    actions = ('make_available',)
    def make_available(self,request,queryset):

        rows =queryset.update(available=True)
        self.message_user(request,f'{rows} Updated')





class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name'],
    }





admin.site.register(Product,ProductAdmin)
admin.site.register(Categories,CategoriesAdmin)

admin.site.register(Comment)