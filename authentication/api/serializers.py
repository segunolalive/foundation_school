from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account, Profile


class ProfileSerializer(serializers.ModelSerializer):
    image_thumb = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ('image_thumb','last_name', 'region', 'zone', 'church',)

    def get_image_thumb(self, obj):
        return str(obj.image_thumb)


class AccountSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True, partial=True)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)


    class Meta:
        model = Account
        fields = ('id', 'email', 'created_at', 'updated_at',
                  'first_name', 'password', 'confirm_password', 'profile')
        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):
        new_account = Account.objects.create(**validated_data)

        profile_data = validated_data.pop('profile')

        profile = Profile.objects.create(
        account = new_account,
        last_name = profile_data['last_name'],
        region = profile_data['region'],
        church = profile_data['church'],
        zone = profile_data['zone'],
        # etc...
        )
        return new_account

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save()

        profile.last_name = profile_data.get('last_name', profile.last_name)#['last_name'],
        profile.region = profile_data.get('region', profile.region)
        profile.church = profile_data.get('church', profile.church)
        profile.zone = profile_data.get('zone', profile.zone)

        profile.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance
