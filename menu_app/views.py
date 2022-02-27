from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import redirect, render
from menu_app.forms import UserLoginForm, ProductForm, CategoryForm
from menu_app.models import Product, Category, Restaurant


class MainView(TemplateView):
    template_name = "main.html"


class MenuView(DetailView):
    model = Restaurant
    template_name = "menu/menu2.html"
    context_object_name = "restaurant"

    def get_context_data(self, **kwargs):
        if kwargs.get('object').slug == 'bybrothers':
            self.template_name = 'menu/menu4.html'
        if kwargs.get('object').slug == 'almahanym':
            self.template_name = 'menu/menu5.html'

        context = super(MenuView, self).get_context_data(**kwargs)
        context['form_login'] = UserLoginForm(self.request.POST or None)
        context['form_product'] = ProductForm(self.request.POST or None)
        context['form_category'] = CategoryForm(self.request.POST or None)
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


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'category', 'img', 'description']

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'img', 'description']

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


def update_product_status(request, pk):
    product = Product.objects.get(pk=pk)
    if product.is_active:
        product.is_active = False
    else:
        product.is_active = True
    product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'place_order', 'img', 'restaurant']

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'img', 'place_order']

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class CategoryDeleteView(DeleteView):
    model = Category

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
