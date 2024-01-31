from django.contrib import admin

from .models import TrainingPage, TrainingDay, Training, TrainingStats


admin.site.register(TrainingPage)
admin.site.register(TrainingDay)
admin.site.register(Training)
admin.site.register(TrainingStats)
