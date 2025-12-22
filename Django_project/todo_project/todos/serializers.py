from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):


    def validate_title(self, value):
        if len(value)<3:
            raise serializers.ValidationError("Title must be at least 3 characters ")
        return value
    
    
    class Meta:
        model = Todo
        fields = '__all__'
