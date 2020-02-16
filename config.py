import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kraft:admin123@localhost/pitches"
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY=os.environ.get('SECRET_KEY')
  
  


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kraft:admin123@localhost/pitches"
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}