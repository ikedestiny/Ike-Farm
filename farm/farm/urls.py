"""farm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from livestock import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.hello),
    path('contact',views.contactUs, name="contact-page"),
    path('confirmation/', views.confirmation, name='confirmation-page'),
    path('make_order/', views.make_order,name='order-form' ),
    path('homepage/', views.homepage, name='home'),
    path('order_list/', views.order_list, name='order-list'),
    path('order_detail/<int:id>/', views.order_detail,name='order-detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

