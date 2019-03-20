from django.contrib import admin

# Register your models here.

from hway import models


admin.site.register(models.ProvinceNumber)
admin.site.register(models.Daycount)
admin.site.register(models.Truckdaycount)
admin.site.register(models.Map)
admin.site.register(models.Cardaycount)
admin.site.register(models.Province)
#admin.site.register(models.Station)
admin.site.register(models.Carddaycount)
admin.site.register(models.TrafficVolume)
admin.site.register(models.Fee)
admin.site.register(models.Area)
admin.site.register(models.OD)
admin.site.register(models.China)
admin.site.register(models.CardTrans)
admin.site.register(models.IdealTrans)
admin.site.register(models.Diff)
admin.site.register(models.Cycle)
admin.site.register(models.CardIndex)
admin.site.register(models.Chargebytype)
admin.site.register(models.Chargebytype_avg)
admin.site.register(models.Potential_c)
admin.site.register(models.Axischarge)
admin.site.register(models.Overload)


