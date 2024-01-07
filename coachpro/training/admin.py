from django.contrib import admin

from .models import TrainingPage, Training

# from .models import TrainingPage, TrainingDay, Training
admin.site.register(TrainingPage)
admin.site.register(Training)
