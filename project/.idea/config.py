
class Config:
    SECRET_KEY = 'hard to guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    CSRF_ENABLED = True

    @staticmethod
    def init_app(app):
        pass
