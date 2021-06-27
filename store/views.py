from django.db import models
from django.shortcuts import get_object_or_404, render


from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category, Product
# Create your views here.


class HomePageView(TemplateView):
    template_name='store/home.html'

    def get_context_data(self):
        context = super().get_context_data()
        context["prods"] = Product.objects.filter(isavaliabe=True)
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['prods']=context['prods'].filter(prod_title__contains=search_input)
        
        return context

    
   
    


  
class PrductDetailView(DetailView):
    
    template_name='store/details.html'
    context_object_name='product'
    def get_object(self, queryset=None):
        
        return Product.objects.get(prod_slug=self.kwargs.get("prod_slug"))





class CategoryListView(ListView):
    template_name="store/products/category.html"
    context_object_name='prods'
    def get_queryset(self):
      self.category=get_object_or_404(Category,cat_slug=self.kwargs.get("cat_slug"))  

      return Product.objects.filter(category=self.category)





     

