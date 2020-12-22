from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_mail_to_func(template, context, mail_subject, mail_to=[], mail_sender=""):
    # msg_plain = render_to_string(template + ".txt", context)
    msg_html = render_to_string(template + ".html", context)
    mail_sender = mail_sender if mail_sender else settings.EMAIL_HOST_USER

    # send_mail(
    #     mail_subject,
    #     msg_plain,
    #     mail_sender,
    #     mail_to,
    #     html_message=msg_html,
    #     fail_silently=False
    # )
    msg = EmailMessage(mail_subject, msg_html, mail_sender, mail_to)
    msg.content_subtype = "html"
    msg.send(fail_silently=True)


send_mail_to = send_mail_to_func
