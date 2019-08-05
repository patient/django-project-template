from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User

__all__ = ('CustomUserChangeForm', 'CustomUserCreationForm')


class CustomUserChangeForm(UserChangeForm):
    """Custom change form for ``User`` model.

    This class overrides ``UserChangeForm`` to provide different ``User``
    model in Meta.

    """

    class Meta:
        model = User
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    """Custom creation form for ``User`` model.

    This class overrides ``UserCreationForm`` to provide different ``User``
    model in Meta and also replaces ``username`` field with ``email`` field.

    """

    class Meta:
        model = User
        fields = ('email',)
