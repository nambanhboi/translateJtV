from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
#doan van
<<<<<<< HEAD
=======
# class Users(models.Model):
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     def __str__(self):
#         return self.username

class CustomerManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Tên người dùng là bắt buộc")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Mã hóa mật khẩu
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomerUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)  # Thêm ràng buộc duy nhất
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Mặc định là False

    objects = CustomerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    class Meta:
        # Khắc phục xung đột related_name
        # Đổi 'groups' và 'user_permissions' thành 'custom_groups' và 'custom_user_permissions'
        # Bạn có thể đặt tên related_name khác tùy ý
        permissions = (("custom_groups", "Custom groups"), ("custom_user_permissions", "Custom user permissions"))
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
    )
    
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b

class Paragraph(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#
class Sentence(models.Model):
    # id = models.AutoField(primary_key=True)
    sentenceJV = models.CharField(max_length=100)
    sentenceVN = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    # stt = models.AutoField
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    def __str__(self):
        return self.sentenceVN
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         listsen = Sentence.objects.                                                                                                                                                                                                                         

    #         max_id = Sentence.objects.aggregate(models.Max('id'))['id__max']
    #         if(max_id is None):
    #             max_id = 0
    #         self.id = max_id + 1
    #     super().save(*args, **kwargs)

    def getImage(self):
        if(self.image):
            return 'http://localhost:8000' + self.image.url
        return ''

#dong gop cau moi
class Report(models.Model):
    typeName = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.typeName
    
class Contribute(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    sentenceJv = models.CharField(max_length=100)
    sentenceVn = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)