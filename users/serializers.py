from rest_framework import serializers

from . models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('username', 'password', 'is_librarian')

        def create(self, validated_data):
            password = validated_data.pop('password')
            res = self.Meta.model(**validated_data)
            if password is not None:
                res.set_password(password)
            res.save()
            return res
