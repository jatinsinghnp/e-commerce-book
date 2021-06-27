from django.urls import path
from .views import HomePageView,PrductDetailView,CategoryListView
app_name='store'
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path("productdetails<slug:prod_slug>/", PrductDetailView.as_view(), name="product_detail"),
    path("categoriesdetail/<slug:cat_slug>/", CategoryListView.as_view(), name="category_list"),
    
]
