from distutils.core import setup

setup(
    name='django-smtp-ssl',
    version='1.0',
    description='SMTP SSL email backend for Django',
    author='Luka Zakrajsek',
    author_email='luka@bancek.net',
    url='https://github.com/bancek/django-smtp-ssl',
    license='MIT',
    py_modules=('django_smtp_ssl',),
    zip_safe=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)