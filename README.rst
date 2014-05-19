django-smtp-ssl
===============

SMTP SSL email backend for Django

Installation
------------

Run

::

    pip install django-smtp-ssl


and add following to your ``settings.py``:

::

    EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
    EMAIL_HOST = 'mail.example.com'
    EMAIL_PORT = 465
