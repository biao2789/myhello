DIALECT = "postgresql"
DRIVER = "psycopg2"
DATABASE = "sayhello"
USERNAME = "postgres"
PASSWORD = "postgres"
HOST = "localhost"
PORT = "5432"

# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?client_encoding=utf8".format(
#     DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/sayhello"
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "secret string"