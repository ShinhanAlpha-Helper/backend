from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    member_username = serializers.SerializerMethodField()
    tstamp = serializers.DateTimeField(
        read_only = True, format = '%Y-%m-%d'
    )

    def get_member_username (self, obj):
        return obj.member.username

    class Meta:
        model = Note
        fields = '__all__'


class NoteCreateSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(default=serializers.CurrentUserDefault(), required=False)
    tstamp = serializers.DateTimeField(
        read_only = True, format = '%Y-%m-%d'
    )

    def validate_member(self, value):
        if not value.is_authenticated: 
            raise serializers.ValidationError("member is required")
        return value

    class Meta:
        model = Note
        fields = '__all__'