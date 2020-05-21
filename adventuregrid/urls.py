from django.urls import path

import grid.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path(r'', grid.views.home, name='home'),
    path(r'<int:x>/<int:y>', grid.views.grid, name='grid')
]