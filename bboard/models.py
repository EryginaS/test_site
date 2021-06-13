from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models



from django.contrib.auth.models import AbstractUser
 

class Dept(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование отдела')
    main_person = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Начальник', related_name='+')
    desc = models.TextField(null=True, blank=True, verbose_name='Описание и комментарии')
    class Meta:
        verbose_name_plural = 'Отделы'
        verbose_name = 'Отдел'

    def __str__(self):
        return 'Отдел: %s' % self.name

class Clients(models.Model):
    first_name = models.CharField(null=True, blank=True,max_length=50, verbose_name='Имя')
    last_name = models.CharField(null=True, blank=True,max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(null=True, blank=True, max_length=50, verbose_name='Отчество')
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Пользователь')
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Отдел')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='телефон')
    email = models.CharField(max_length=500, blank=True, null=True, verbose_name='почта')
    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
   
        
    def __str__(self):
        return 'Клиент: %s %s' % (self.first_name, self.last_name)

        
class ItPerson(models.Model):
    first_name = models.CharField(null=True, blank=True,max_length=50, verbose_name='Имя')
    last_name = models.CharField(null=True, blank=True,max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(null=True, blank=True, max_length=50, verbose_name='Отчество')
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Пользователь')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='телефон')

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'
    
    def __str__(self):
        return 'Cотрудник: %s %s' % (self.first_name, self.last_name)


class Applications(models.Model):

    theme = models.CharField(max_length=50, verbose_name='Тема заявки', blank=True, null=True,)
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Клиент')
    date = models.DateTimeField(verbose_name='Плановая дата решения', blank=True, null=True,)
    responsible = models.ForeignKey(ItPerson, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Ответсвтенный сотрудник')
    TYPE_CHOICES_FOR_PRIORITY = (
        (0, "Низкий"), 
        (1, "Средний"), 
        (2, "Высокий"), 
    
    )
    priority = models.IntegerField(verbose_name='Приоритет', null=True, choices=TYPE_CHOICES_FOR_PRIORITY) 
    TYPE_CHOICES_FOR_STATUS = (
        (0, "Непрочитанный"), 
        (1, "К исполнению"), 
        (2, "Выполненный"), 
    
    )
    TYPE_CHOICES_FOR_TYPE = (
        (0, "Обслуживание"), 
        (1, "Консультация"), 
    
    )
    status= models.IntegerField(verbose_name='Статус заявки', null=True, choices=TYPE_CHOICES_FOR_STATUS, default=0)
    type_app= models.IntegerField(verbose_name='Тип заявки', null=True, choices=TYPE_CHOICES_FOR_TYPE, default=0)
    
    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'
        ordering = ['status']

    def __str__(self):
        return 'Заявка: %s' % str(self.pk)


class Report(models.Model):
    application = models.ForeignKey(Applications, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Заявка', unique=True)
    theme = models.CharField(max_length=50, verbose_name='Тема заявки', blank=True, null=True,)
    desc = models.TextField(null=True, blank=True, verbose_name='Описание')
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Клиент')
    date = models.DateTimeField(verbose_name='Плановая дата решения', blank=True, null=True,)
    responsible = models.ForeignKey(ItPerson, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Ответсвтенный сотрудник')
    TYPE_CHOICES_FOR_PRIORITY = (
        (0, "Низкий"), 
        (1, "Средний"), 
        (2, "Высокий"), 
    
    )
    priority = models.IntegerField(verbose_name='Приоритет', null=True, choices=TYPE_CHOICES_FOR_PRIORITY) 
    TYPE_CHOICES_FOR_STATUS = (
        (0, "Непрочитанный"), 
        (1, "К исполнению"), 
        (2, "Выполненный"), 
    
    )
    TYPE_CHOICES_FOR_TYPE = (
        (0, "Обслуживание"), 
        (1, "Консультация"), 
    
    )
    status= models.IntegerField(verbose_name='Статус заявки', null=True, choices=TYPE_CHOICES_FOR_STATUS, default=0)
    type_app= models.IntegerField(verbose_name='Тип заявки', null=True, choices=TYPE_CHOICES_FOR_TYPE, default=0)
    done_work = models.TextField(null=True, blank=True, verbose_name='Проделанная работа')
    report_maker = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Пользователь, создавший отчет')
    
    class Meta:
        verbose_name_plural = 'Отчеты'
        verbose_name = 'Отчет'
        ordering = ['status']

    def __str__(self):
        return 'Отчет: %s' % str(self.pk)

    