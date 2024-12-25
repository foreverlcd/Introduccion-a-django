from django.urls import path
from .views import BlogListView, BlogCreateView, BLogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    # Tenemos que pasarle un id para que sepa que post mostrar
    path('<int:pk>/', BLogDetailView.as_view(), name='detail'),
]