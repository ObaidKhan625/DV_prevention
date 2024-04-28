# user/routers.py

class UserDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'user':
            return 'user'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'user':
            return 'user'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both objects are in the user app
        if obj1._meta.app_label == 'user' and obj2._meta.app_label == 'user':
            return True
        # No opinion if neither object is in the user app
        elif 'user' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None
        # Block relationship if one object is in the user app and the other isn't
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'user':
            # Ensure user app models are migrated only to 'UserDB' database
            return db == 'user'
        # No opinion for all other models/databases
        return None
