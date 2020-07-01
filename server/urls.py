from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'My Site Title'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls'),name="accounts"),
    path('',include('gestion_document_app.urls'))
]
