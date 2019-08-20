from rest_framework import serializers

from django.utils.text import gettext_lazy as _

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    UserRegisterSerializer is a model serializer which includes the
    attributes that are required for registering a user.
    """

    @staticmethod
    def validate_mobile(value: str):
        """
        If pre-validated mobile number is required, this function
        checks if the mobile is pre-validated using OTP.
        Parameters
        ----------
        value: str

        Returns
        -------
        value: str

        """

        from . import user_settings

        from .utils import check_validation

        if user_settings['MOBILE_VALIDATION']:
            if check_validation(value=value):
                return value
            else:
                raise serializers.ValidationError('The mobile must be '
                                                  'pre-validated via OTP.')
        else:
            return value

    class Meta:
        from .models import User

        model = User
        fields = ('id', 'username', 'name', 'email', 'mobile', 'password',
                  'is_superuser', 'is_staff')
        read_only_fields = ('is_superuser', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}


class UserShowSerializer(serializers.ModelSerializer):
    """
    UserShowSerializer is a model serializer which shows the attributes
    of a user.
    """

    class Meta:
        from .models import User

        model = User
        fields = ('id', 'username', 'name', 'mobile', 'is_delivery_boy')
        read_only_fields = ('username', 'name', 'mobile', 'is_delivery_boy')


class OTPSerializer(serializers.Serializer):
    """
    This Serializer is for sending OTP & verifying destination via otp.
    is_login: Set is_login true if trying to login via OTP
    destination: Required. Place where sending OTP
    verify_otp: OTP in the 2nd step of flow

    Examples
    --------
    1. Request an OTP for verifying
    For mobile number as destination
    >>> OTPSerializer(data={"destination": "88xx6xx5xx"})

    2. Send OTP to verify
    >>> OTPSerializer(data={"destination": "88xx6xx5xx",
    >>>                     "verify_otp": 2930432})

    For log in, just add is_login to request
    >>> OTPSerializer(data={"destination": "88xx6xx5xx",
    >>>                     "is_login": True})
    >>> OTPSerializer(data={"destination": "88xx6xx5xx",
    >>>                     "verify_otp": 2930433, "is_login": True})

    3. For logging in delivery boy
    >>> OTPSerializer(data={"destination": "88xx6xx5xx",
    >>>                     "is_login": True, "is_delivery_boy": True})
    >>> OTPSerializer(data={"destination": "88xx6xx5xx",
    >>>                     "verify_otp": 2930433, "is_login": True, "is_delivery_boy": True})
    """

    is_login = serializers.BooleanField(default=False)
    is_delivery_boy = serializers.BooleanField(default=False)
    verify_otp = serializers.CharField(required=False)
    destination = serializers.CharField(required=True)

    def get_user(self, prop: str, destination: str) -> User:
        """
        Provides current user on the basis of property and destination
        provided.
        Parameters
        ----------
        prop: str
            Can be M
        destination: str
            Provides value of property
        Returns
        -------
        user: User

        """
        from .models import User
        from .variables import MOBILE

        try:
            user = User.objects.get(mobile=destination)
        except User.DoesNotExist:
            user = None

        return user

    def validate(self, attrs: dict) -> dict:
        """
        Performs custom validation to check if any user exists with
        provided details.
        Parameters
        ----------
        attrs: dict

        Returns
        -------
        attrs: dict

        Raises
        ------
        NotFound: If user is not found
        """
        from django.core.validators import ValidationError
        from rest_framework.exceptions import NotFound
        from .variables import MOBILE

        attrs['prop'] = MOBILE

        user = self.get_user(attrs.get('prop'), attrs.get('destination'))

        if not user:
            if attrs['is_login']:
                raise NotFound(_('No user exists with provided details'))
        else:
            if attrs['is_delivery_boy']:
                if user.is_delivery_boy:
                    attrs['user'] = user
                else:
                    raise serializers.ValidationError(
                        _("Not a valid delivery boy."))
            else:
                try:
                    attrs['mobile'] = user.mobile
                except Exception:
                    pass
                attrs['user'] = user

        return attrs


class CheckUniqueSerializer(serializers.Serializer):
    """
    This serializer is for checking the uniqueness of
    username/mobile of user.
    """
    prop = serializers.ChoiceField(choices=('mobile', 'username'))
    value = serializers.CharField()


class OTPLoginRegisterSerializer(serializers.Serializer):
    """
    Registers a new user with auto generated password or login user if
    already exists

    Params
    name: Name of user
    mobile: Mobile of user
    is_delivery_boy: Is Delivery Boy?
    verify_otp: Required in step 2, OTP from user
    """

    from rest_framework import serializers

    name = serializers.CharField(required=True)
    verify_otp = serializers.CharField(default=None, required=False)
    is_delivery_boy = serializers.BooleanField(default=False, required=False)
    mobile = serializers.CharField(required=True)

    @staticmethod
    def get_user(mobile: str, is_delivery_boy: bool):
        try:
            user = User.objects.get(mobile=mobile, is_delivery_boy=is_delivery_boy)
        except User.DoesNotExist:
            user = None

        return user

    def validate(self, attrs: dict) -> dict:
        attrs['user'] = self.get_user(
            mobile=attrs.get('mobile'),
            is_delivery_boy=attrs.get('is_delivery_boy'))
        return attrs
