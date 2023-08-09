from django.db import models
import uuid
from django.contrib.auth.models import User
    

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
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    def __str__(self):
        return self.sentenceVN

    def getImage(self):
        if(self.image):
            return 'http://localhost:8000' + self.image.url
        return ''

#dong gop cau moi
class Report(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, null=True)
    typeName = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.typeName
    
class Contribute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentenceJv = models.CharField(max_length=100)
    sentenceVn = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)