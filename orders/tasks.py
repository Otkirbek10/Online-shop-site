
from django.core.mail import send_mail
from .models import Order


def order_created(order_id):
    """"
    desvsdkmk
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'olimovotkirbek49@gmail.com', [order.email])

    return mail_sent
  