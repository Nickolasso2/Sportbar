from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Category
from django.views.generic import DetailView, ListView, CreateView
from cart.forms import CartAddProductForm
from .forms import BookTableForm, SubscriptionForm
from django.http import JsonResponse





class HomeView(View):
    def get(self, request):
        return render(request, 'app_sportbar/home.html')

        


class Register(View):
   
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'app_sportbar/register.html', {'form':form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        return render(request, 'app_sportbar/register.html', {'form':form})

class LoggingIn(View):
    def get(self, request):
        logging_form = AuthenticationForm()
        return render(request, 'app_sportbar/login.html', {'logging_form':logging_form})
    
    def post(self, request):
        logging_form = AuthenticationForm(data=request.POST)
        if logging_form.is_valid():
            user = logging_form.get_user()
            login(request, user)
            return redirect ('/')
        else:
            return render(request, 'app_sportbar/login.html', {'logging_form':logging_form})

def log_out(request):
    logout(request)
    return redirect('home')



class CategoryDetail(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = CartAddProductForm()
        return context

class CategoryList(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = CartAddProductForm()
        return context

class BookTable(View):
    def get(self, request):
        form = BookTableForm()
        return render(request, 'app_sportbar/book_table.html', {'form':form})
    
    def post(self,request):
        form = BookTableForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                booked_table = form.save(commit=False)
                booked_table.client = request.user
                booked_table.save()
            else:
                form.save()
            return JsonResponse({'response':'success'})
        else:
            form = BookTableForm()
            return render(request, 'app_sportbar/book_table.html', {'form':form})
        
class Subscription(CreateView):
    form_class = SubscriptionForm
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({'response':'success'})
    
    def form_invalid(self, form):
        return JsonResponse({'response':'ValidationError'})   

    
