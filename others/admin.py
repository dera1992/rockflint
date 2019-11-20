from django.contrib import admin


from .models import  Information,Testimony

class InfoModelAdmin(admin.ModelAdmin):
    list_display = ["name", "subject", "email","pub_date"]
    list_filter = ["pub_date",]

    class Meta:
        model = Information

admin.site.register(Information, InfoModelAdmin)
admin.site.register(Testimony)
