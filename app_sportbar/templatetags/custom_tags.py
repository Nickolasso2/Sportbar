from django import template
from app_sportbar.models import Category
from django.urls import reverse
from ..forms import SubscriptionForm

register = template.Library()

@register.inclusion_tag('navbar.html')
def show_navbar(request_user):
    categories = Category.objects.all()
    return {'categories':categories, 'request_user':request_user}

@register.inclusion_tag('app_sportbar/form_template.html')
def show_form(form, button_text, form_action=''):
    return {'form':form, 'button_text':button_text, 'form_action':form_action}

@register.inclusion_tag('app_sportbar/menu.html')
def category(category, cart_form):
    return {'category':category, 'cart_form':cart_form}

# get dinamic url when passing in template
@register.filter
def get_url(form_action_url):
    if form_action_url:
        return reverse(form_action_url)
    else:
        return form_action_url
    
@register.simple_tag()
def subscription_form():
    return SubscriptionForm()