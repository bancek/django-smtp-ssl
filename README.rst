django-smtp-ssl
===============

SMTP SSL email backend for Django

**NOTE: Django >=1.7 includes support for SMTP with SSL/TLS; hence django-smtp-ssl is obsolete.**


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
