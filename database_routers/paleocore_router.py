class PaleocoreRouter(object):

    def db_for_read(self, model, **hints):
        """
        Attempts to read drp models go to drp_carmen.
        """
        if model._meta.app_label == 'drp':
            return 'drp_carmen'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write drp models go to drp_carmen.
        """
        if model._meta.app_label == 'drp':
            return 'drp_carmen'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the drp app is involved.
        """
        if obj1._meta.app_label == 'drp' or \
           obj2._meta.app_label == 'drp':
           return True
        return None

    def allow_syncdb(self, db, model):

        if db == 'drp_carmen':
            return model._meta.app_label == 'drp'
        elif model._meta.app_label == 'drp':
            return False
        return None