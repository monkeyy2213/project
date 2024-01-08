from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    email = models.CharField(verbose_name="Email")
    password_ow = models.CharField(max_length=20, verbose_name="Пароль")
    username = models.CharField(max_length=20, verbose_name="Имя пользователя")

    def __str__(self):
       return self.last_name
    
    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
        ordering = ['last_name', 'first_name']

class Patient(models.Model):  
    name = models.CharField(max_length=100, verbose_name="Имя")  
    animal_type = models.CharField(max_length=30, verbose_name="Вид животного")
    date_of_birth = models.DateField(default='2023-01-01', verbose_name="Дата рождения")  
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name="Владалец")
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото", null=True)

    def __str__(self):
       return self.name
    
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

class Service(models.Model):
   name = models.CharField(max_length=100, verbose_name="Название услуги")  
   price = models.DecimalField(max_digits=10, decimal_places=2, default='100', verbose_name="Цена")

   def __str__(self):
       return self.name
   
   class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Veterinarian(models.Model):
   first_name = models.CharField(max_length=30, verbose_name="Имя")
   last_name = models.CharField(max_length=30, verbose_name="Фамилия")  
   position = models.CharField(max_length=20, verbose_name="Должность")

   def __str__(self):
       return self.last_name
   
   class Meta:
        verbose_name = 'Ветеринар'
        verbose_name_plural = 'Ветеринары'
   
class Visit(models.Model):
   visit_date = models.DateField(verbose_name="Дата посещения")  
   patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="id пациента")
   veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, verbose_name="Принимающий врач")  
   visit_time = models.CharField(verbose_name="Время посещения")
   service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="id услуги")
  
   def __str__(self):
       return self.visit_date
   
   class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
      
class Anamnesis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="id пациента")
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, verbose_name="Номер посещения")
    complaints = models.TextField(verbose_name="Жалобы")
    diagnosis = models.TextField(verbose_name="Диагноз")
    prescriptions = models.TextField(verbose_name="Предписания")

    def __str__(self):
       return self.title
   
    class Meta:
        verbose_name = 'Мед. книжка'
        verbose_name_plural = 'Мед. книжка'
