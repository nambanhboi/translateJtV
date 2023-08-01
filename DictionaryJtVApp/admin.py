from django.contrib import admin
<<<<<<< HEAD
from .models import Sentence, Paragraph, Comment, Report, Contribute
=======
from .models import Sentence, Paragraph, Comment, Report, Contribute, CustomerUser
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b
# Register your models here.

admin.site.register(Sentence)
admin.site.register(Comment)
admin.site.register(Paragraph)
admin.site.register(Report)
admin.site.register(Contribute)
<<<<<<< HEAD
=======
admin.site.register(CustomerUser)
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b

