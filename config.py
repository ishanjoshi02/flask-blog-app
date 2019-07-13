import os

config = {
    "development": "blog.config.DevelopmentConfig",
    "testing": "blog.config.TestingConfig",
    "default": "blog.config.BaseConfig"
}

def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(config[config_name])