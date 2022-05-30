from time import sleep, time 
from datetime import date
from django.conf import settings
from django.core.mail import send_mass_mail
import wisher
from wisher.models import Birth, prop
#from wisher.models import Wishes

from celery import shared_task
@shared_task
def wish():
   B = date.today()
   births = Birth.objects.filter(bday = B )
   Wishs = prop.objects.only('greet')
   for Prop in Wishs:
        X = Prop.greet
        
   for birth in births:
        subject = 'Code is working bro'
        message = "Greetings from Re,   "+ " " + X +birth.name
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [birth.email]
        mail1 = (subject, message, email_from, recipient_list)
        subject2 = 'Birthdays -- Regarding'
        names = birth.name
        message2 = 'Dear Reasearch cell Executive,..' + 'Today the following members are celebrating their birthdays ....' + names + 'kindly do wish'
        recipient_list2 = ['kabilansanjai@gmail.com']
        mail2 = (subject2, message2, email_from, recipient_list2)
        send_mass_mail((mail1,mail2)),
       
      





