import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

  @staticmethod
  def init_app(app):
    pass


class TestingConfig(Config):
  TESTING = True


config = {
    'default': Config,
    'development': Config,
    'production': Config,
    'testing': TestingConfig
}
