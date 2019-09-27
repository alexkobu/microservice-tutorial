# services/users/project/config.py

class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True

class ProductonConfig(BaseConfig):
    """Production configuration"""
    pass