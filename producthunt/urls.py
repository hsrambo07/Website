
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('base/',views.base),
    path('corona/',views.corona, name='corona'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('count/',views.coronas, name='count')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()