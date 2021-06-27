
from .models import Category
def categorylist(request):

    return{
       'categories': Category.objects.all()
    }