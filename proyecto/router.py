# DB router for proyecto


class PPDBRouter(object):
    """
    A router to control proyecto db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on proyecto models to 'ppdb'"
        from django.conf import settings
        if not settings.DATABASES.has_key('proyecto'):
            return None
        if model._meta.app_label == 'proyecto':
            return 'ppdb'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on proyecto models to 'ppdb'"
        from django.conf import settings
        if not settings.DATABASES.has_key('proyecto'):
            return None
        if model._meta.app_label == 'proyecto':
            return 'ppdb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in proyecto is involved"
        from django.conf import settings
        if not settings.DATABASES.has_key('proyecto'):
            return None
        if obj1._meta.app_label == 'proyecto' or obj2._meta.app_label == 'proyecto':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the proyecto app only appears on the 'proyecto' db"
        from django.conf import settings
        if not settings.DATABASES.has_key('proyecto'):
            return None
        if db == 'ppdb':
            return model._meta.app_label == 'proyecto'
        elif model._meta.app_label == 'proyecto':
            return False
        return None