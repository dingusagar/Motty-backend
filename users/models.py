from django.contrib.auth.models import AbstractUser
from django.db import models

from Motty import settings


class User(AbstractUser):
    NORMAL_USER = 'NORMAL_USER'
    ADMIN_USER = 'ADMIN_USER'
    USER_MODE_CHOICES = (
        (NORMAL_USER, 'Normal User'),
        (ADMIN_USER, 'Admin'),
    )
    mode = models.CharField(max_length=50, choices=USER_MODE_CHOICES, default=NORMAL_USER)

    def __str__(self):
        return self.username




# Todo password reset
from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)
    }

    print('sending email')

    subject = 'Sign In to Sales Discovery Platform'
    message = """
        Hai,

        Use the token to login back.
        Click the link : http://sales-discovery-platform.herokuapp.com/login

    """
    message = message + str(context)
    message = message + """
    
    Bye
    """
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [reset_password_token.user.email])
