import os


class Config:
    SECRET_KEY = "a5476dff809f1c090bcc6daa3df92ffa"     # put SECRET_KEY into environment variable
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'       # put SQLALCHEMY_DATABASE_URI into environment variable
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("PROJECT_EMAIL")     # in environment value
    MAIL_PASSWORD = os.environ.get("PROJECT_PASS")      # in environment value