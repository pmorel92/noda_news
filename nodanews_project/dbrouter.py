

class DbRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to nodasfdb.
        """
        if model._meta.app_label == 'nodasf':
            return 'nodasfdb'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to nodasfdb.
        """
        if model._meta.app_label == 'nodasf':
            return 'nodasfdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'nodasf' or \
           obj2._meta.app_label == 'nodasf':
           return True
        return None

    def allow_migrate(self, db, app_app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'nodasfdb'
        database.
        """
        if app_app_label == 'nodasf':
            return db == 'nodasfdb'
        return None