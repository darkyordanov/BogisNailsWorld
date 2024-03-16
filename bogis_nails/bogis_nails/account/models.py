from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth import base_user as auth_base
# from django.contrib.auth.models import Group

from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib import auth


class AccountUserManager(auth_base.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
            self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()



# # A few helper functions for common logic between User and AnonymousUser.
# def _user_get_permissions(user, obj, from_name):
#     permissions = set()
#     name = "get_%s_permissions" % from_name
#     for backend in auth.get_backends():
#         if hasattr(backend, name):
#             permissions.update(getattr(backend, name)(user, obj))
#     return permissions


# def _user_has_perm(user, perm, obj):
#     """
#     A backend can raise `PermissionDenied` to short-circuit permission checking.
#     """
#     for backend in auth.get_backends():
#         if not hasattr(backend, "has_perm"):
#             continue
#         try:
#             if backend.has_perm(user, perm, obj):
#                 return True
#         except PermissionDenied:
#             return False
#     return False


# def _user_has_module_perms(user, app_label):
#     """
#     A backend can raise `PermissionDenied` to short-circuit permission checking.
#     """
#     for backend in auth.get_backends():
#         if not hasattr(backend, "has_module_perms"):
#             continue
#         try:
#             if backend.has_module_perms(user, app_label):
#                 return True
#         except PermissionDenied:
#             return False
#     return False

    

class AccountUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        }
    )
        
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
              
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    
    USERNAME_FIELD = "email"
    
    objects = AccountUserManager()
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    birth_date = models.DateField(
        default=None,
        blank=True,
        null=True,
    )
    
    profile_picture = models.ImageField(
        upload_to='account_pictures/',
        
    )
    
    user = models.OneToOneField(
        AccountUser,
        on_delete=models.DO_NOTHING,
        primary_key=True,
        related_name='profile',
    )