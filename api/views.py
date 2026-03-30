from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from core.models import Law, Subscription
from .serializers import LawSerializer, SubscriptionSerializer

# 登录接口
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return Response({'detail': '登录成功', 'username': user.username})
    else:
        return Response({'detail': '用户名或密码错误'}, status=status.HTTP_401_UNAUTHORIZED)

# 登出接口
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'detail': '已登出'})

# 搜索接口（支持关键词模糊搜索）
@api_view(['GET'])
def search_law(request):
    keyword = request.query_params.get('keyword', '')
    if keyword:
        # 按标题或内容模糊匹配
        laws = Law.objects.filter(title__icontains=keyword) | Law.objects.filter(content__icontains=keyword)
    else:
        laws = Law.objects.all()
    serializer = LawSerializer(laws, many=True)
    return Response(serializer.data)

# 订阅接口（新增/取消）
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe(request):
    user = request.user
    scene = request.data.get('scene')
    if not scene:
        return Response({'detail': '缺少场景参数'}, status=400)
    # 如果已经存在则删除（取消订阅），否则创建
    sub, created = Subscription.objects.get_or_create(user=user, scene=scene)
    if not created:
        sub.delete()
        return Response({'detail': '取消订阅成功'})
    return Response({'detail': '订阅成功'})