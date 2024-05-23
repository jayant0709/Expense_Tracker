class ExpensesRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'expenses':
            return 'expenses_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'expenses':
            return 'expenses_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'expenses':
            return db == 'expenses_db'
        return None
