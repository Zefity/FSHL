from django.urls import path, include

from FSHL.views import products, basket_add, basket_remove

app_name = 'FSHL'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_num>', products, name='paginator'),
    path('baskets/add/<int:thing_id>', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', basket_remove, name='basket_remove')
]
