import os

class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = 'bc29199ac8b2b522fd951d97e0da5c62'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://kraft:admin123@localhost/blog'
    UPLOADED_PHOTOS_DEST='app/static/photos' 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    QUOTE_URL='http://quotes.stormconsultancy.co.uk/random.json'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
   
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
   


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://kraft:admin123@localhost/blog'
    DEBUG = True 


config_options = {
'development':DevConfig,
'production':ProdConfig,

}






