from django.contrib import admin
from django.urls import path,include
from home import views

#Django admin header customization

admin.site.site_header="Shreya's Portfolio"
admin.site.site_title="Welcome to Shreya's Dashboard"
admin.site.index_title="Welcome to this Portal"


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('work/',views.work,name='work'),
    path('relax/',views.relax,name='relax'),
    path('beauty/',views.beauty,name='beauty'),
]