from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AddAnimalForm(forms.ModelForm):
    at = (
        ('Кот',"Кот"),
        ('Собака',"Собака"),
    )
    name = forms.CharField(label="Имя")  
    animal_type = forms.ChoiceField(choices=at,label="Вид животного")
    date_of_birth = forms.DateField(label="Дата рождения", initial='2023-01-01')  
    photo = forms.ImageField(label="Фото")
    owner = forms.ModelChoiceField(queryset=Owner.objects.all(), label="Владелец")
    #queryset=MyModel.objects.all().values_list('name',flat=True).order_by('name').distinct()
    class Meta:
        model = Patient
        fields = ('name', 'animal_type', 'date_of_birth', 'photo', 'owner')
    
    

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

