from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Sender(models.Model):
    email           =   models.EmailField()
    clave           =   models.CharField(max_length=20)
    servidor_smtp   =   models.CharField(max_length=30)
    puerto_smtp     =   models.IntegerField()
    
class Receiver(models.Model):
    email           =   models.EmailField();
    descripcion     =   models.CharField(max_length=256)
    group           =   models.ForeignKey(Group,        on_delete=models.CASCADE)
    
class Reminder(models.Model):
    sender          =   models.ForeignKey(Sender,       on_delete=models.CASCADE)
    receiver        =   models.ForeignKey(Receiver,     on_delete=models.CASCADE)
    min_date_to_send=   models.DateTimeField()
    max_date_to_send=   models.DateTimeField()
    sender          =   models.ForeignKey(Sender,       on_delete=models.CASCADE)
    receiver        =   models.ForeignKey(Receiver,     on_delete=models.CASCADE)