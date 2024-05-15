from .tasks import send_email_task


def success_created_collect_email(to_email):
    subject = 'Успешно созданный сбор'
    message = 'Спасибо что помогаете нам!'
    return send_email_task.delay(subject, message, to_email)


def success_created_payment_email(to_email):
    subject = 'Успешно отправленный донат'
    message = 'Спасибо что помогаете нам!'
    return send_email_task.delay(subject, message, to_email)
