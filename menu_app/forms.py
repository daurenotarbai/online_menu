from django import forms
from django.contrib.auth import authenticate

from menu_app.models import Product, Category


class UserLoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
  password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))

  def clean(self, *args, **kwargs):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

    if username and password:
      user = authenticate(username=username,password=password)
      if not user:
        raise forms.ValidationError('This user does not exist. PLease check your username and password again')
      if not user.check_password(password):
        raise forms.ValidationError('incorrect passowrd')
      if not user.is_active:
        raise forms.ValidationError('This user is not active')
    return super(UserLoginForm,self).clean(*args, **kwargs)



class ProductForm(forms.ModelForm):
  category = forms.IntegerField(widget=forms.NumberInput(attrs={"type":"hidden","id":"category_input"}))
  class Meta:
    model = Product
    fields = ['name','price','description','img','category']
    widgets = {
      'name': forms.TextInput(attrs={"class":"form-control","placeholder":"Product name"}),
      'price': forms.NumberInput(attrs={"class":"form-control","placeholder":"Price"}),
      'description': forms.Textarea(attrs={"class":"form-control product-description","placeholder":"Description"})
    }

class CategoryForm(forms.ModelForm):
  restaurant = forms.IntegerField(widget=forms.NumberInput(attrs={"type":"hidden","id":"restaurant_input"}))
  class Meta:
    model = Category
    fields = ['name','place_order','img','restaurant']
    widgets = {
      'name': forms.TextInput(attrs={"class":"form-control","placeholder":"Category name"}),
      'place_order': forms.NumberInput(attrs={"class":"form-control","placeholder":"Place Order"}),
    }