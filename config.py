import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kraft:admin123@localhost/pitches"
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY='bc29199ac8b2b522fd951d97e0da5c62'

    @staticmethod
    def init_app(app):
        pass  
  


class ProdConfig(Config):

    pass

class DevConfig(Config):
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}