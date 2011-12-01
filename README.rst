django-smtp-ssl
===============

SMTP SSL email backend for Django

Installation
------------

``settings.py``:

::

    EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
    EMAIL_HOST = 'mail.example.com'
    EMAIL_PORT = 465
