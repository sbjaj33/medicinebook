from django.shortcuts import render
from django.views.generic import TemplateView , CreateView , UpdateView , DetailView ,ListView, DeleteView
from django.http import HttpResponse
from shop_app.forms import ProfileForm,UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from shop_app.models import  Profile,Medicine
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q

# Create your views here.
class Index(TemplateView):
    template_name='shop_app/index.html'

class Aboutus(TemplateView):
    template_name='shop_app/AboutUs.html'



def Register(request):
    Registered=False
    if request.method=='POST':
        profile_form=ProfileForm(request.POST)
        user_form=UserForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            Registered=True
        else:
            return HttpResponse('Invalid Login Id or Password')
    else:
        profile_form=ProfileForm
        user_form=UserForm
    return render(request,'shop_app/registration.html',{'Registered':Registered,'profile_form':profile_form,'user_form':user_form})

def User_login(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=user_name,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('shop_app:index')
                print('successfull')
            else:
                return HttpResponse('INVALID USERNAME OR PASSWORD')
        else:
            return HttpResponse('Invalid Login')
            print("SORRY WE CAN'T LET YOU LOG IN")
    else:
        return render(request,'shop_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return redirect('shop_app:index')
class Stocklist(LoginRequiredMixin,ListView):
    model=Medicine
    context_object_name="stock_list"
    template_name="shop_app/medicine_list.html"



class Stockdetail(LoginRequiredMixin,DetailView):
    model=Medicine
    context_object_name="stock_detail"
    template_name='shop_app/medicine_detail.html'

class Createstock(LoginRequiredMixin,CreateView):
    model=Medicine
    fields=('Shop','Name','Salt','Company','MRP','MFD','Expiry')
    login_url='/login/'
    redirect_field_name="shop_app/medicine_detail.html"





class StockUpdateView(LoginRequiredMixin,UpdateView):
    model=Medicine
    fields=('Shop','Name','Salt','Company','MRP','MFD','Expiry')
    template_name="shop_app/medicine_form.html"
    login_url='/login/'
    redirect_field_name="shop_app/medicine_detail.html"


class StockDeleteView(LoginRequiredMixin,DeleteView):
    model=Medicine
    success_url=reverse_lazy("shop_app:StockList")
    template_name="shop_app/medicine_confirm_delete.html"
    login_url='/login/'
    redirect_field_name="shop_app/medicine_detail.html"


class SearchResultView(ListView):
    model=Medicine
    template_name="shop_app/Searchpage.html"
    def get_queryset(self):
        query=self.request.GET.get('q')
        object_list= Medicine.objects.filter(
         Q(Name__icontains=query) | Q(Salt__icontains=query) | Q(MFD__icontains=query) | Q(Expiry__icontains=query)
        )
        return object_list
