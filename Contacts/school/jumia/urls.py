from django.urls import path
from . import views

urlpatterns = [
    path('shop/',views.shopping, name='jumia'),
    path('about/',views.about,name='about'),
    path('products/<int:pk>',views.product,name='products'),
    path('categorise/<str:imems>',views.categorise,name='categorise'),
]