from rest_framework import serializers
from .models import *


class HomeImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeImg
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class BoburArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoburArena
        fields = '__all__'


class RahbariyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = '__all__'
