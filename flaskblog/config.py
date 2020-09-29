import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres://twxygqxsnxhzwi:4fcc327b61b60265a981f0f6331a95dd11db3a9429a641059be2ae57d18d26c4@ec2-54-146-142-58.compute-1.amazonaws.com:5432/d76n6u926b0smg'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/quotes.json'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://timothy:index506119056@localhost:5432/flaskblog'
    DEBUG = True



config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}


# app.config['SECRET_KEY'] = '9425c6cec9f7c12e5f836cf482fcf7b1'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://timothy:index506119056@localhost:5432/flaskblog'