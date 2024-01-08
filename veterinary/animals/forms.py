from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import psycopg2
from django.db import connection

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

class VisitForm(forms.ModelForm):
    aa = (
        ('10:00',"10:00"),
        ('11:00',"11:00"),
        ('12:00',"12:00"),
        ('13:00',"13:00"),
        ('14:00',"14:00"),
        ('15:00',"15:00"),
        ('16:00',"16:00"),
        ('17:00',"17:00"),
    )

    visit_date = forms.DateField(initial='2023-01-01', label="Дата")
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), label="Питомец")
    veterinarian = forms.ModelChoiceField(queryset=Veterinarian.objects.all(), label="Врач")
    visit_time = forms.ChoiceField(choices=aa, label="Время")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="Услуга")
    # conn = psycopg2.connect("dbname='app2' user='postgres' host='127.0.0.1' password='froster-1'")
    # cur = conn.cursor()
    # query_id = "SELECT id FROM (SELECT MAX(last_login) FROM auth_user) AS i, auth_user WHERE i.max = auth_user.last_login"
    # cur.execute(query_id)
    # p_id = cur.fetchall()
    # cur.close()
    # id = int(p_id[0][0])

    # cur.execute("SELECT p.id, p.name FROM animals_patient as p WHERE p.owner_id = 2")
    # cur.execute("SELECT p.id, p.name FROM animals_patient as p WHERE p.owner_id = %s", (id,))
    # q1 = cur.fetchall()

    # print(q1)
    # print(idd)
    # print(q1[1])
    # for i in range(len(q1)):
    #     q1[i] = (Patient, q1[i][1])
    # print(psycopg2.InternalError)  
    # print(Patient.objects.all())
    # print(Patient.objects.all().filter(owner_id = 2))
    # print(a)

    #.filter(owner_id = 2)
    # patient = forms.ModelChoiceField(Patient.objects.all().filter(owner_id = 1),label="Питомец")
    # #patient = forms.ModelChoiceField(queryset=Patient.objects.all(),label="Питомец")
    # #visit_date = forms.DateField(label="Дата", initial='2023-01-01')    
    # visit_date = forms.DateField( 
    #     label="Дата", 
    #     required=True, 
    #     widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}), 
    #     input_formats=["%Y-%m-%d"]
    # )
    # #.filter(position = "Ветеринарный врач")
    # veterinarian = forms.ModelChoiceField(Veterinarian.objects.all().filter(position = "Ветеринарный врач"),label="Врач")
    # visit_time = forms.ChoiceField(choices=aa,label="Время")  
    # service = forms.ModelChoiceField(Service.objects.all(),label="Услуга")

    # query2 = "SELECT id, last_name FROM animals_veterinarian"
    # cur.execute(query2)
    # q2 = cur.fetchall()
    # #print(q2[2][0])
    # if service == "Вакцинация":
    #     vet = q2[0][0]
    # elif service == "Чистка зубов":
    #     vet = q2[1][0]
    # else:
    #     vet = q2[2][0]
    #veterinarian=forms.CharField(initial=q2,label="Врач")
    #veterinarian=vet
    #owner = forms.ModelChoiceField(queryset=Owner.objects.all(), label="Владелец")
    #queryset=MyModel.objects.all().values_list('name',flat=True).order_by('name').distinct()
    class Meta:
        model = Visit
        fields = '__all__'