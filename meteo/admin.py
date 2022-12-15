from django.contrib import admin

# Register your models here.
from .models import MeteoRecord
from .models import WindRecord

#admin.site.register(MeteoRecord)
# Define the admin class
class MeteoRecordAdmin(admin.ModelAdmin):
    list_display= ('id','DATE', 'TA', 'DP', 'WC','RH','PA','PR','PR1H','PR24H','SR_1M','SR_1D','SR_45_1M','SR_45_1D','SD_1H','SD_1D','SD_45_1H','SD_45_1D')
    list_filter = ('DATE', 'TA', 'DP')
    list_per_page = 25

class WindRecordAdmin(admin.ModelAdmin):
    list_display= ('id','DATE', 'WS1AVG', 'WD1AVG', 'WS1MIN2', 'WS1AVG2', 'WS1MAX2', 'WD1MIN2', 'WD1AVG2', 'WD1MAX2', 'WS1MIN10', 'WS1AVG10', 'WS1MAX10', 'WD1MIN10', 'WD1AVG10',
        'WD1MAX10',)
    list_filter = ('id','DATE', 'WS1AVG', 'WD1AVG',)
    list_per_page = 25

# Register the admin class with the associated model
admin.site.register(MeteoRecord, MeteoRecordAdmin)

admin.site.register(WindRecord, WindRecordAdmin)
