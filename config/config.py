# config/config.py

class Config:
    """Базовый конфигурационный класс."""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Конфигурация для разработки."""
    DEBUG = True

class TestingConfig(Config):
    """Конфигурация для тестирования."""
    TESTING = True

class ProductionConfig(Config):
    """Конфигурация для производства."""
