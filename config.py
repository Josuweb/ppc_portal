import os

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'ppc_portal'

SECRET_KEY = os.urandom(24)  # En producción puedes usar una cadena fija
