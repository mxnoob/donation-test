from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_email_task(to_email):
    subject = 'Успешно отправленный донат'
    message = 'Спасибо что помогаете нам!'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)
