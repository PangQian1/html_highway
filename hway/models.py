from django.db import models


# Create your models here.

class ProvinceNumber(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)


class Province(models.Model):
    number = models.CharField(max_length = 5, default = '11')
    province = models.CharField(max_length = 20)
    enweight = models.BigIntegerField(default = 0)
    exweight = models.BigIntegerField(default = 0)
    entrafficvolume = models.BigIntegerField(default = 0)
    extrafficvolume = models.BigIntegerField(default = 0)
    fee = models.BigIntegerField(default = 0)
    greenentrafficvolume = models.BigIntegerField(default = 0)
    greenextrafficvolume = models.BigIntegerField(default = 0)
    cardtrans = models.BigIntegerField(default = 0)


class Weight(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 50)
    date = models.DateTimeField()
    stationname = models.CharField(max_length = 50)
    enweight = models.BigIntegerField(default = 0)
    exweight = models.BigIntegerField(default = 0)
    trafficvolume = models.BigIntegerField(default = 0)
    fee = models.BigIntegerField(default = 0)


class Area(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 50)
    date = models.DateTimeField()
    stationname = models.CharField(max_length = 50)
    enweight = models.BigIntegerField(default = 0)
    exweight = models.BigIntegerField(default = 0)
    entrafficvolume = models.BigIntegerField(default = 0)
    extrafficvolume = models.BigIntegerField(default = 0)
    engreentrafficvolume = models.BigIntegerField(default = 0)
    exgreentrafficvolume = models.BigIntegerField(default = 0)
    fee = models.BigIntegerField(default = 0)


class China(models.Model):
    province = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    longi = models.FloatField()
    lati = models.FloatField()


class CardTrans(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    date = models.DateTimeField()
    enstation = models.CharField(max_length = 50)
    exstation = models.CharField(max_length = 50)
    count = models.IntegerField()


class IdealTrans(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    date = models.DateTimeField()
    enstation = models.CharField(max_length = 50)
    exstation = models.CharField(max_length = 50)
    count = models.IntegerField()


# class Station(models.Model):
#   number = models.CharField(max_length = 5)
#   province = models.CharField(max_length = 50)
#   stationname = models.CharField(max_length = 50)
#   enweight = models.IntegerField(default = 0)
#   exweight = models.IntegerField(default = 0)
#   trafficvolume = models.IntegerField(default = 0)
#   fee = models.BigIntegerField(default = 0)
class Diff(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    date = models.DateTimeField()
    stationname = models.CharField(max_length = 50)
    trafficdiff = models.IntegerField(default = 0)
    carddiff = models.IntegerField(default = 0)
    cardnum = models.IntegerField(default = 0)
    encard = models.IntegerField(default = 0)
    excard = models.IntegerField(default = 0)
    acccard = models.IntegerField(default = 0)
    accmtc = models.IntegerField(default = 0)


class TrafficVolume(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    date = models.DateTimeField()
    total = models.IntegerField(default = 0)
    mtc = models.IntegerField(default = 0)
    etc = models.IntegerField(default = 0)
    tp1 = models.IntegerField(default = 0)
    tp2 = models.IntegerField(default = 0)
    tp3 = models.IntegerField(default = 0)
    tp4 = models.IntegerField(default = 0)
    tp11 = models.IntegerField(default = 0)
    tp12 = models.IntegerField(default = 0)
    tp13 = models.IntegerField(default = 0)
    tp14 = models.IntegerField(default = 0)
    tp15 = models.IntegerField(default = 0)


class Fee(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    date = models.DateTimeField()
    total = models.IntegerField(default = 0)
    tp1 = models.IntegerField(default = 0)
    tp2 = models.IntegerField(default = 0)
    tp3 = models.IntegerField(default = 0)
    tp4 = models.IntegerField(default = 0)
    tp11 = models.IntegerField(default = 0)
    tp12 = models.IntegerField(default = 0)
    tp13 = models.IntegerField(default = 0)
    tp14 = models.IntegerField(default = 0)
    tp15 = models.IntegerField(default = 0)


class Daycount(models.Model):
    province = models.CharField(max_length = 5)
    date = models.CharField(max_length = 20)
    etc = models.IntegerField()
    mtc = models.IntegerField()
    fee = models.IntegerField()


class Truckdaycount(models.Model):
    province = models.CharField(max_length = 5)
    date = models.CharField(max_length = 20)
    truck11 = models.IntegerField()
    truck12 = models.IntegerField()
    truck13 = models.IntegerField()
    truck14 = models.IntegerField()
    truck15 = models.IntegerField()


class Map(models.Model):
    number = models.CharField(max_length = 5, default = "0")
    province = models.CharField(max_length = 20)
    stationname = models.CharField(max_length = 50)
    longi = models.FloatField()
    lati = models.FloatField()


class Cardaycount(models.Model):
    province = models.CharField(max_length = 5)
    date = models.CharField(max_length = 20)
    car1 = models.IntegerField()
    car2 = models.IntegerField()
    car3 = models.IntegerField()
    car4 = models.IntegerField()


class Carddaycount(models.Model):
    province = models.CharField(max_length = 5)
    date = models.DateTimeField()
    card = models.IntegerField()
    mtc = models.IntegerField()
    ratio = models.FloatField()


class OD(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    enstation = models.CharField(max_length = 50)
    exstation = models.CharField(max_length = 50)
    tp = models.CharField(max_length = 20)  # 包含txl,weight,grenntxl,greenweight
    count = models.BigIntegerField(default = 0)


class Cycle(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    cycle = models.IntegerField()
    count = models.IntegerField()


class CardIndex(models.Model):
    number = models.CharField(max_length = 5)
    province = models.CharField(max_length = 20)
    stock = models.IntegerField()
    cycle = models.FloatField()
    turnover = models.FloatField()
    deposition = models.FloatField()
    safestock = models.IntegerField()


### added by weixiang

class Chargebytype(models.Model):
    province = models.CharField(max_length = 20)
    date = models.DateField()
    vtype = models.IntegerField()
    weightfee = models.FloatField()
    feelow = models.FloatField()
    feehigh = models.FloatField()


class Chargebytype_avg(models.Model):
    province = models.CharField(max_length = 20)
    vtype = models.IntegerField()
    weightfee = models.FloatField()
    feelow = models.FloatField()
    feehigh = models.FloatField()
    low_change_rate = models.FloatField()
    high_change_rate = models.FloatField()


class Potential_c(models.Model):
    province = models.CharField(max_length = 20)
    date = models.DateField()
    vtype = models.IntegerField()
    p_loss_low = models.FloatField()
    p_loss_high = models.FloatField()
    traffic_loss_low = models.FloatField()
    traffic_loss_high = models.FloatField()
    c = models.FloatField()


class Overload(models.Model):
    province = models.CharField(max_length = 20)
    date = models.DateField()
    vtype = models.IntegerField()
    loss_money = models.FloatField()
    add_traffic = models.FloatField()
    loss_ratio = models.FloatField()
    add_ratio = models.FloatField()


class Axischarge(models.Model):
    province = models.CharField(max_length = 20)
    traffic_amount = models.IntegerField()
    date = models.DateField()
    axis_low = models.FloatField()
    axis_low_percar = models.FloatField()
    weightfee_amount = models.FloatField()
    weightfee_percar = models.FloatField()
    axis_ref = models.FloatField()
    axis_ref_percar = models.FloatField()
    axis_high = models.FloatField()
    axis_high_percar = models.FloatField()

class LinkToOD(models.Model):
    link_id = models.CharField(max_length=10)
    number = models.CharField(max_length=5)
    province = models.CharField(max_length=20)
    enstation = models.CharField(max_length=50)
    exstation = models.CharField(max_length=50)
    txl = models.BigIntegerField(default=0)


class ZhangXingTong(models.Model):
    station_id = models.CharField(max_length=20)
    station_name = models.CharField(max_length=50)
    province = models.CharField(max_length=20)
    longi = models.FloatField()
    lati = models.FloatField()

# class Chongqing_od(models.Model):
#     link_id = models.IntegerField()
#     toll = models.TextField()