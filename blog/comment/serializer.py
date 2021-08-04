from rest_framework import serializers
from .models import Comments,Blog

class sComment(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class sCommentCreate(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class sSerializerBlogCreate(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class sSerializerBlogShow(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'