SECRET_KEY = 'django-insecure-6oe8xf#7fi7uxxgy!ckpvfjv+!qml7q7tb13#yydc^0k18#ux2'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Jared0351!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}