from  django.urls import path
from api.views import product_list , product_details
urlpatterns=[
    path('products/',product_list),
    path('products/<int:p_id>/',product_details)
]