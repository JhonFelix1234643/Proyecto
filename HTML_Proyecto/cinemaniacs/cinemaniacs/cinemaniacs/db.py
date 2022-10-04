import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'cine_maniacs.sqlite3')
    }
}

MYSQL = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD':'felipe',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}