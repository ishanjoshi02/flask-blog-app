

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    database_metadata = {
        "username": "root",
        "password": "toor",
        "dialect": "",
        "driver": "mysql",
        "host": "localhost",
        "port": "3306",
        "database": "sys"
    }

    @classmethod
    def get_database_conn_string(cls):
        db = cls.database_metadata
        return f"{db.dialect}{db.driver}://{db.username}:{db.password}@{db.host}:{db.port}/{db.database}"

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    database_metadata.host = "localhost"
    database_metadata.password = "toor"

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
