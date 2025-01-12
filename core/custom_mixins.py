import json
from rest_framework import permissions
from backend.models.coremodels import UserRolePrivileges

'''this is how base permission works :

from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

'''
'''
allowed_resources:
1- LMS
2- Course Customer Registration
3- Course Enrollment
4- Courses
5- Course Management
6- Dashboard
'''

# class BaseAccessMixin:
#     permission_classes = [permissions.IsAuthenticated]
#     allowed_resources = set()
    
#     def has_access(self, request):
#         user = request.user
#         user_privileges = UserRolePrivileges.objects.filter(role=user.role)
#         privileged_resources = {privilege.resource.id for privilege in user_privileges}
        
#         return self.allowed_resources == privileged_resources

# class SuperAdminMixin(BaseAccessMixin):
#     allowed_resources = {1, 2, 4, 5, 6}

# class ClientAdminMixin(BaseAccessMixin):
#     allowed_resources = {1, 3, 4, 6}

# class ClientMixin(BaseAccessMixin):
#     allowed_resources = {1, 4, 6}

import json
from django.core.exceptions import ObjectDoesNotExist  # Import the appropriate exception

class SuperAdminMixin:
    # permission_classes = [permissions.IsAuthenticated]

    def has_super_admin_privileges(self, request):
        try:
            user_header = request.headers.get("user")
            if user_header:
                user = json.loads(user_header)
                role_id = user.get("role")

            super_admin_resources = {1, 2, 4, 5, 6}  

            # user = request.user
            user_privileges = UserRolePrivileges.objects.filter(role=role_id) # role= user.role
            print(user_privileges)
            privileged_resources = {privilege.resource.id for privilege in user_privileges}
            print(privileged_resources)
            print('super admin')

            return super_admin_resources == privileged_resources

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return False  # Return False indicating failure
        except ObjectDoesNotExist as e:
            print(f"Error fetching user privileges: {e}")
            return False  # Return False indicating failure
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False  # Return False indicating failure

    
import json
from django.core.exceptions import ObjectDoesNotExist  # Import the appropriate exception

class ClientAdminMixin:
    # permission_classes = [permissions.IsAuthenticated]
    
    def has_client_admin_privileges(self, request):
        try:
            user_header = request.headers.get("user")
            if user_header:
                user = json.loads(user_header)
                role_id = user.get("role")

            client_admin_resources = {1}  
            
            # user = request.user
            print(user)

            try:
                user_privileges = UserRolePrivileges.objects.filter(role=role_id)
            except ObjectDoesNotExist as e:
                print(f"Error fetching user privileges: {e}")
                return False  # Return False indicating failure

            privileged_resources = {privilege.resource.id for privilege in user_privileges}
            print(privileged_resources)
            print('client admin')
            
            return client_admin_resources == privileged_resources

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return False  # Return False indicating failure
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False  # Return False indicating failure

    
class ClientMixin:
    # permission_classes = [permissions.IsAuthenticated]
    
    def has_client_privileges(self, request):
        try:
            user_header = request.headers.get("user")
            if user_header:
                user = json.loads(user_header)
                role_id = user.get("role")

            client_resources = {2}
            
            # user = request.user
            print(user)

            try:
                user_privileges = UserRolePrivileges.objects.filter(role=role_id)
            except ObjectDoesNotExist as e:
                print(f"Error fetching user privileges: {e}")
                return False  # Return False indicating failure

            privileged_resources = {privilege.resource.id for privilege in user_privileges}
            print(privileged_resources)
            print('client')
            
            return client_resources == privileged_resources

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return False  # Return False indicating failure
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False  # Return False indicating failure