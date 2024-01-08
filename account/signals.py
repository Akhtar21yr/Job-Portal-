from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()
@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    if kwargs['created']:
        print('->>>>>>>>> iam working')
        UserProfile.objects.create(user=kwargs['instance'])
    # else:
    #     print('->>>>>>>>>>> updated')
    #     kwargs['instance'].profile.save()

