# _*_coding:utf-8_*_
from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from Gmooc.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGBHJKLMNOPQRSTUVWXYZabcdefgbhjklmnopqrstuvwxyz01234567989'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return  str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    print code
    email_record.code = code
    email_record.send_type = send_type
    email_record.email = email
    email_record.save()

    if send_type == "register":
        email_title = "Register active link."
        email_body = "please click the link active your account: http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "Reset your password link."
        email_body = "please click the link reset your password: http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "Reset your password link."
        email_body = "your password code: {0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

