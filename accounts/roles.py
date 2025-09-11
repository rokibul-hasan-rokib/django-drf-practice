from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'view_product': True,
        'add_product': True,
        'edit_product': True,
        'delete_product': True,
    }

class Manager(AbstractUserRole):
    available_permissions = {
        'view_product': True,
        'add_product': True,
        'edit_product': True,
    }

class Staff(AbstractUserRole):
    available_permissions = {
        'view_product': True,
    }
