

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


from django.views.generic import FormView

from .forms import ShopCreationForm

# Create your views here.
class LoginView(LoginView,LoginRequiredMixin):
   
    template_name='registration/login.html'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('store:home')


class LogOutView(LogoutView):
    next_page='account:login'





class  SingupView(FormView):

    template_name='registration/singup.html'
    form_class=ShopCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('account:login')


    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(SingupView,self).form_valid(form)
    

    def get(self, *args, **kwargs ):
        if self.request.user.is_authenticated:
            return  redirect('account:login')
        return super(SingupView,self).get(*args,**kwargs)
         
    



