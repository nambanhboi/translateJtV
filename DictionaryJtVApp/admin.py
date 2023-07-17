from django.contrib import admin
from .models import Sentence, Paragraph, Comment, Report, Contribute,Users
# Register your models here.

admin.site.register(Sentence)
admin.site.register(Comment)
admin.site.register(Paragraph)
admin.site.register(Report)
admin.site.register(Contribute)
admin.site.register(Users)

