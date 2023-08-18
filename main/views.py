from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def home_img_get(request):
    que = HomeImg.objects.last()
    ser = HomeImgSerializer(que).data
    return Response({'data': ser})


@api_view(['GET'])
def player_get(request):
    que = Player.objects.all()
    ser = PlayerSerializer(que, many=True).data
    return Response({'data': ser})


@api_view(['GET'])
def blog_get(request):
    que = Blog.objects.all()
    ser = BlogSerializer(que, many=True).data
    return Response({'data': ser})


@api_view(['GET'])
def table_get(request):
    que = Statistic.objects.all()
    ser = TableSerializer(que, many=True).data
    return Response({'data': ser})


@api_view(['GET'])
def sponsor_get(request):
    que = Sponsor.objects.all()
    ser = SponsorSerializer(que, many=True).data
    return Response({'data': ser})


@api_view(['GET'])
def boburArena_get(request):
    que = BoburArena.objects.last()
    ser = BoburArenaSerializer(que).data
    return Response({'data': ser})


@api_view(['GET'])
def rahbariyat_get(request):
    que = Rahbariyat.objects.all()
    ser = RahbariyatSerializer(que, many=True).data
    return Response({'data': ser})


@api_view(['GET'])
def club_get(request):
    que = Club.objects.last()
    ser = ClubSerializer(que, many=True).data
    return Response({'data': ser})


@api_view(['GET'])
def advice_get(request):
    que = Advice.objects.all().order_by("-id")[:4]
    ser = AdviceSerializer(que, many=True).data
    return Response({'data': ser})
