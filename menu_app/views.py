from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from menu_app.forms import UserLoginForm
from menu_app.models import Product, Category, Restaurant


class MenuView(DetailView):
  model = Restaurant
  template_name = "menu/menu2.html"
  context_object_name = "restaurant"

  def get_context_data(self, **kwargs):
    context = super(MenuView, self).get_context_data(**kwargs)
    context['categories'] = Category.objects.filter(is_active=True)
    context['Restaurant'] = get_object_or_404(Restaurant,pk=1)
    context['form'] = UserLoginForm(self.request.POST or None)
    return context

@csrf_exempt
def login_view(request):
  next = request.GET.get('next')
  form = UserLoginForm(request.POST or None)
  if form.is_valid():

    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    user = authenticate(username=username, password=password)
    slug = user.restaurant.first().slug
    login(request, user)
    if next:
      return redirect(next)
    return redirect('/menu/{}'.format(slug))
  return render(request, "404.html")



def logout_view(request):
  logout(request)
  return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))