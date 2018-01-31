import os

class Config(object):
    """
        Parent Configuration Class.
    """
    DEBUG                   = False
    CSRF_ENABLE             = False
    SECRET                  = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """
        DevelopmentConfig.
    """
    DEBUG = True

class TestingConfig(Config):
    """
        Testing config with test database.
    """
    TESTING                 = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/test_db"
    DEBUG                   = True

class StagingConfig(Config):
    """
        Configurations for Staging.
    """
    DEBUG = True

class ProductionConfig(Config):
    """
        Configurations for Production.
    """
    DEBUG   = False
    TESTING = False 

app_config = {
    'development' : DevelopmentConfig,
    'testing'     : TestingConfig,
    'staging'     : StagingConfig,
    'production'  : ProductionConfig
}
