from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. 用户表（存用户信息）
class User(AbstractUser):
    ROLE_CHOICES = (
        ('normal', '普通用户'),
        ('supervisor', '监管用户'),
        ('admin', '管理员'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='normal')
    
    # 加上这两行，解决冲突
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    def __str__(self):
        return self.username

# 2. 法规表（存法律条文）
class Law(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')  # 标题
    content = models.TextField(verbose_name='内容')  # 内容
    publish_date = models.DateField(verbose_name='发布日期', null=True, blank=True)
    source = models.CharField(max_length=100, verbose_name='来源', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __str__(self):
        return self.title

# 3. 同义词表（存同义词，比如"飞机"和"飞行器"）
class Synonym(models.Model):
    term = models.CharField(max_length=100, unique=True, verbose_name='原词')
    synonyms = models.TextField(verbose_name='同义词列表（用逗号分隔）')
    
    def __str__(self):
        return self.term
    
    def get_synonyms_list(self):
        """把逗号分隔的文字变成列表"""
        return [s.strip() for s in self.synonyms.split(',') if s.strip()]

# 4. 订阅表（用户关注了什么）
class Subscription(models.Model):
    SCENE_CHOICES = (
        ('flight_permit', '低空飞行申请'),
        ('compliance', '通航企业合规'),
        ('drone_reg', '无人机注册'),
        ('pilot_license', '飞行员执照'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    scene = models.CharField(max_length=50, choices=SCENE_CHOICES, verbose_name='场景')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='订阅时间')
    
    def __str__(self):
        return f"{self.user.username} - {self.get_scene_display()}"
    
    class Meta:
        unique_together = ('user', 'scene')  # 防止重复订阅