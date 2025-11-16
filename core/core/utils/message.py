from django.utils.translation import gettext_lazy as _, pgettext_lazy


class Message:
    def __init__(self, resource="Data"):
        self.resource = resource

    # -------------------
    # CREATE
    # -------------------
    def created_success(self):
        return pgettext_lazy('CRUD create', '%(resource)s created successfully') % {
            'resource': self.resource
        }

    def created_failed(self):
        return pgettext_lazy('CRUD create', 'Failed to create %(resource)s') % {
            'resource': self.resource
        }

    # -------------------
    # READ
    # -------------------
    def retrieved(self):
        return pgettext_lazy('CRUD read', '%(resource)s retrieved successfully') % {
            'resource': self.resource
        }

    def not_found(self):
        return pgettext_lazy('CRUD read', '%(resource)s not found') % {
            'resource': self.resource
        }

    # -------------------
    # UPDATE
    # -------------------
    def updated(self):
        return pgettext_lazy('CRUD update', '%(resource)s updated successfully') % {
            'resource': self.resource
        }

    # -------------------
    # DELETE
    # -------------------
    def deleted(self):
        return pgettext_lazy('CRUD delete', '%(resource)s deleted successfully') % {
            'resource': self.resource
        }

    # -------------------
    # AUTH
    # -------------------
    @staticmethod
    def login_success():
        return pgettext_lazy('Auth', 'Login successful')

    @staticmethod
    def login_failed():
        return pgettext_lazy('Auth', 'Invalid credentials')

    @staticmethod
    def logout():
        return pgettext_lazy('Auth', 'Logout successful')

    # -------------------
    # GENERAL
    # -------------------
    @staticmethod
    def error():
        return pgettext_lazy('General', 'An error occurred')

    @staticmethod
    def validation_error():
        return pgettext_lazy('General', 'Validation failed')

    @staticmethod
    def unauthorized():
        return pgettext_lazy('General', 'Authentication required')

