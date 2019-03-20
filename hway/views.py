# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from hway import models
import json
from datetime import datetime
import time
# Create your views here.
from django.db import transaction
import os

def home(request):
    return render(request, 'index.html')


def etcmtcdaytranscount(request, pro):
    data = models.TrafficVolume.objects.filter(province = pro).values('etc', 'mtc', 'date')
    fdata = models.Fee.objects.filter(province = pro).values('total')
    dAxis = []
    detc = []
    dmtc = []
    dfee = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        # return HttpResponse(strtime)
        dAxis.append(strtime)
        detc.append(d['etc'])
        dmtc.append(d['mtc'])
    for f in fdata:
        dfee.append(f['total'])
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})
    # dfee.append(d.fee)
    # return HttpResponse(tv)
    # province = models.ProvinceNumber.objects.filter(number = pro).values('province')
    # p = province[province]
    # return HttpResponse(province)
    return render(request, 'etcmtcdaytranscount.html',
                  {'province': json.dumps(pro), 'dAxis': json.dumps(dAxis), 'detc': json.dumps(detc),
                   'dmtc': json.dumps(dmtc), 'dfee': json.dumps(dfee), 'trafficvolume': tv})


def datavolum(request):
    return render(request, 'datavolum.html')


def errordatavolum(request):
    return render(request, 'errordatavolum.html')


def datarepairvolum(request):
    return render(request, 'datarepairvolum.html')


def instation_plate(request):
    return render(request, 'instation_plate.html')


def outstation_plate(request):
    return render(request, 'outstation_plate.html')


def cxErrStation(request):
    return render(request, 'cxErrStation.html')


def cartypedaytranscount(request, pro):
    data = models.TrafficVolume.objects.filter(province = pro).values('date', 'tp1', 'tp2', 'tp3', 'tp4')
    dAxis = []
    car1 = []
    car2 = []
    car3 = []
    car4 = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        dAxis.append(strtime)
        car1.append(d['tp1'])
        car2.append(d['tp2'])
        car3.append(d['tp3'])
        car4.append(d['tp4'])
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})
    return render(request, 'cartypedaytranscount.html',
                  {'trafficvolume': tv, 'province': json.dumps(pro), 'dAxis': json.dumps(dAxis),
                   'car1': json.dumps(car1), 'car2': json.dumps(car2), 'car3': json.dumps(car3),
                   'car4': json.dumps(car4)})


def trucktypedaytranscount(request, pro):
    data = models.TrafficVolume.objects.filter(province = pro).values('date', 'tp11', 'tp12', 'tp13', 'tp14', 'tp15')
    dAxis = []
    truck11 = []
    truck12 = []
    truck13 = []
    truck14 = []
    truck15 = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        dAxis.append(strtime)
        truck11.append(d['tp11'])
        truck12.append(d['tp12'])
        truck13.append(d['tp13'])
        truck14.append(d['tp14'])
        truck15.append(d['tp15'])
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})
    return render(request, 'trucktypedaytranscount.html',
                  {'trafficvolume': tv, 'province': json.dumps(pro), 'dAxis': json.dumps(dAxis),
                   'truck11': json.dumps(truck11), 'truck12': json.dumps(truck12), 'truck13': json.dumps(truck13),
                   'truck14': json.dumps(truck14), 'truck15': json.dumps(truck15)})


def vehicletypedaytranscount(request, pro):
    data = models.TrafficVolume.objects.filter(province = pro).values('date', 'tp1', 'tp2', 'tp3', 'tp4', 'tp11',
                                                                      'tp12',
                                                                      'tp13', 'tp14', 'tp15')
    dAxis = []
    dcar = []
    dtruck = []
    vec1 = []
    vec2 = []
    vec3 = []
    vec4 = []
    vec11 = []
    vec12 = []
    vec13 = []
    vec14 = []
    vec15 = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        dAxis.append(strtime)
        car = int(d['tp1']) + int(d['tp2']) + int(d['tp3']) + int(d['tp4'])
        dcar.append(car)
        truck = int(d['tp11']) + int(d['tp12']) + int(d['tp13']) + int(d['tp14']) + int(d['tp15'])
        dtruck.append(truck)
        vec1.append(d['tp1'])
        vec2.append(d['tp2'])
        vec3.append(d['tp3'])
        vec4.append(d['tp4'])
        vec11.append(d['tp11'])
        vec12.append(d['tp12'])
        vec13.append(d['tp13'])
        vec14.append(d['tp14'])
        vec15.append(d['tp15'])
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})

    # eturn HttpResponse(vec1)
    return render(request, 'vehicletypedaytranscount.html',
                  {'trafficvolume': tv, 'province': json.dumps(pro), 'dAxis': json.dumps(dAxis),
                   'dcar': json.dumps(dcar), 'dtruck': json.dumps(dtruck), 'vec1': json.dumps(vec1),
                   'vec2': json.dumps(vec2), 'vec3': json.dumps(vec3), 'vec4': json.dumps(vec4),
                   'vec11': json.dumps(vec11), 'vec12': json.dumps(vec12), 'vec13': json.dumps(vec13),
                   'vec14': json.dumps(vec14), 'vec15': json.dumps(vec15)})
    # return render(request,'vehicletypedaytranscount.html')


def vehicletransfeepie(request, pro1, pro2, pro3, st, ed):
    stime = st.split('-')
    etime = ed.split('-')
    data1 = []
    data2 = []
    data3 = []
    data1.append({'name': '1型车', 'value': 0})
    data1.append({'name': '2型车', 'value': 0})
    data1.append({'name': '3型车', 'value': 0})
    data1.append({'name': '4型车', 'value': 0})
    data1.append({'name': '11型车', 'value': 0})
    data1.append({'name': '12型车', 'value': 0})
    data1.append({'name': '13型车', 'value': 0})
    data1.append({'name': '14型车', 'value': 0})
    data1.append({'name': '15型车', 'value': 0})

    feedata1 = models.Fee.objects.filter(province = pro1,
                                         date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                         date__lte = datetime(int(etime[0]), int(etime[1]), int(etime[2]))).values(
        'tp1',
        'tp2',
        'tp3',
        'tp4',
        'tp11',
        'tp12',
        'tp13',
        'tp14',
        'tp15')
    for fd in feedata1:
        data1[0]['value'] = data1[0]['value'] + fd['tp1']
        data1[1]['value'] = data1[1]['value'] + fd['tp2']
        data1[2]['value'] = data1[2]['value'] + fd['tp3']
        data1[3]['value'] = data1[3]['value'] + fd['tp4']
        data1[4]['value'] = data1[4]['value'] + fd['tp11']
        data1[5]['value'] = data1[5]['value'] + fd['tp12']
        data1[6]['value'] = data1[6]['value'] + fd['tp13']
        data1[7]['value'] = data1[7]['value'] + fd['tp14']
        data1[8]['value'] = data1[8]['value'] + fd['tp15']

    data2.append({'name': '1型车', 'value': 0})
    data2.append({'name': '2型车', 'value': 0})
    data2.append({'name': '3型车', 'value': 0})
    data2.append({'name': '4型车', 'value': 0})
    data2.append({'name': '11型车', 'value': 0})
    data2.append({'name': '12型车', 'value': 0})
    data2.append({'name': '13型车', 'value': 0})
    data2.append({'name': '14型车', 'value': 0})
    data2.append({'name': '15型车', 'value': 0})
    feedata2 = models.Fee.objects.filter(province = pro2,
                                         date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                         date__lte = datetime(int(etime[0]), int(etime[1]), int(etime[2]))).values(
        'tp1',
        'tp2',
        'tp3',
        'tp4',
        'tp11',
        'tp12',
        'tp13',
        'tp14',
        'tp15')
    for fd in feedata2:
        data2[0]['value'] = data2[0]['value'] + fd['tp1']
        data2[1]['value'] = data2[1]['value'] + fd['tp2']
        data2[2]['value'] = data2[2]['value'] + fd['tp3']
        data2[3]['value'] = data2[3]['value'] + fd['tp4']
        data2[4]['value'] = data2[4]['value'] + fd['tp11']
        data2[5]['value'] = data2[5]['value'] + fd['tp12']
        data2[6]['value'] = data2[6]['value'] + fd['tp13']
        data2[7]['value'] = data2[7]['value'] + fd['tp14']
        data2[8]['value'] = data2[8]['value'] + fd['tp15']

    data3.append({'name': '1型车', 'value': 0})
    data3.append({'name': '2型车', 'value': 0})
    data3.append({'name': '3型车', 'value': 0})
    data3.append({'name': '4型车', 'value': 0})
    data3.append({'name': '11型车', 'value': 0})
    data3.append({'name': '12型车', 'value': 0})
    data3.append({'name': '13型车', 'value': 0})
    data3.append({'name': '14型车', 'value': 0})
    data3.append({'name': '15型车', 'value': 0})
    feedata2 = models.Fee.objects.filter(province = pro3,
                                         date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                         date__lte = datetime(int(etime[0]), int(etime[1]), int(etime[2]))).values(
        'tp1',
        'tp2',
        'tp3',
        'tp4',
        'tp11',
        'tp12',
        'tp13',
        'tp14',
        'tp15')
    for fd in feedata2:
        data3[0]['value'] = data3[0]['value'] + fd['tp1']
        data3[1]['value'] = data3[1]['value'] + fd['tp2']
        data3[2]['value'] = data3[2]['value'] + fd['tp3']
        data3[3]['value'] = data3[3]['value'] + fd['tp4']
        data3[4]['value'] = data3[4]['value'] + fd['tp11']
        data3[5]['value'] = data3[5]['value'] + fd['tp12']
        data3[6]['value'] = data3[6]['value'] + fd['tp13']
        data3[7]['value'] = data3[7]['value'] + fd['tp14']
        data3[8]['value'] = data3[8]['value'] + fd['tp15']
        # weight.append({'name':wd['stationname'],'value':wd['enweight']})
    #  geo.append(sd.stationname:[sd.longi,sd.lati])
    # return HttpResponse(weight['杨林收费站']
    fee = models.Province.objects.all().values('province', 'fee')
    f = []
    for d in fee:
        f.append({'name': d['province'], 'value': d['fee']})
    # return HttpResponse(f)
    return render(request, 'vehicletransfeepie.html',
                  {'fee': json.dumps(f), 'data1': json.dumps(data1), 'data2': json.dumps(data2),
                   'data3': json.dumps(data3), 'pro1': json.dumps(pro1), 'pro2': json.dumps(pro2),
                   'pro3': json.dumps(pro3), 'st': json.dumps(st), 'ed': json.dumps(ed)})


def cartypedayfee(request, pro):
    data = models.Fee.objects.filter(province = pro).values('date', 'tp1', 'tp2', 'tp3', 'tp4')
    dAxis = []
    car1 = []
    car2 = []
    car3 = []
    car4 = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        dAxis.append(strtime)
        car1.append(d['tp1'])
        car2.append(d['tp2'])
        car3.append(d['tp3'])
        car4.append(d['tp4'])

    fee = models.Province.objects.all().values('province', 'fee')
    f = []
    for d in fee:
        f.append({'name': d['province'], 'value': d['fee']})
    return render(request, 'cartypedayfee.html',
                  {'fee': f, 'province': json.dumps(pro), 'dAxis': json.dumps(dAxis), 'car1': json.dumps(car1),
                   'car2': json.dumps(car2), 'car3': json.dumps(car3), 'car4': json.dumps(car4)})


def trucktypedayfee(request, pro):
    data = models.Fee.objects.filter(province = pro).values('date', 'tp11', 'tp12', 'tp13', 'tp14', 'tp15')
    dAxis = []
    truck11 = []
    truck12 = []
    truck13 = []
    truck14 = []
    truck15 = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        dAxis.append(strtime)
        truck11.append(d['tp11'])
        truck12.append(d['tp12'])
        truck13.append(d['tp13'])
        truck14.append(d['tp14'])
        truck15.append(d['tp15'])
    trafficvolume = models.Province.objects.all().values('province', 'fee')
    f = []
    for d in trafficvolume:
        f.append({'name': d['province'], 'value': d['fee']})
    return render(request, 'trucktypedayfee.html',
                  {'fee': f, 'province': json.dumps(pro), 'dAxis': json.dumps(dAxis), 'truck11': json.dumps(truck11),
                   'truck12': json.dumps(truck12), 'truck13': json.dumps(truck13), 'truck14': json.dumps(truck14),
                   'truck15': json.dumps(truck15)})


def vehicletypedayfee(request, pro):
    data = models.Fee.objects.filter(province = pro).values('date', 'tp1', 'tp2', 'tp3', 'tp4', 'tp11', 'tp12', 'tp13',
                                                            'tp14', 'tp15')
    dAxis = []
    dcar = []
    dtruck = []
    vec1 = []
    vec2 = []
    vec3 = []
    vec4 = []
    vec11 = []
    vec12 = []
    vec13 = []
    vec14 = []
    vec15 = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        dAxis.append(strtime)
        car = int(d['tp1']) + int(d['tp2']) + int(d['tp3']) + int(d['tp4'])
        dcar.append(car)
        truck = int(d['tp11']) + int(d['tp12']) + int(d['tp13']) + int(d['tp14']) + int(d['tp15'])
        dtruck.append(truck)
        vec1.append(d['tp1'])
        vec2.append(d['tp2'])
        vec3.append(d['tp3'])
        vec4.append(d['tp4'])
        vec11.append(d['tp11'])
        vec12.append(d['tp12'])
        vec13.append(d['tp13'])
        vec14.append(d['tp14'])
        vec15.append(d['tp15'])
    trafficvolume = models.Province.objects.all().values('province', 'fee')
    f = []
    for d in trafficvolume:
        f.append({'name': d['province'], 'value': d['fee']})

    # eturn HttpResponse(vec1)
    return render(request, 'vehicletypedayfee.html',
                  {'fee': f, 'province': json.dumps(pro), 'dAxis': json.dumps(dAxis), 'dcar': json.dumps(dcar),
                   'dtruck': json.dumps(dtruck), 'vec1': json.dumps(vec1), 'vec2': json.dumps(vec2),
                   'vec3': json.dumps(vec3), 'vec4': json.dumps(vec4), 'vec11': json.dumps(vec11),
                   'vec12': json.dumps(vec12), 'vec13': json.dumps(vec13), 'vec14': json.dumps(vec14),
                   'vec15': json.dumps(vec15)})


def truckheavycount(request, pro, tp, st, ed):
    if tp == '入口':
        data = models.Province.objects.all().values('province', 'enweight')
        dat = []
        for d in data:
            dat.append({'name': d['province'], 'value': d['enweight']})

    else:
        data = models.Province.objects.all().values('province', 'exweight')
        dat = []
        for d in data:
            dat.append({'name': d['province'], 'value': d['exweight']})
    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    stime = st.split('-')
    etime = ed.split('-')
    weight = {}
    if tp == '入口':
        weightdata = models.Area.objects.filter(province = pro,
                                                date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                                date__lte = datetime(int(etime[0]), int(etime[1]),
                                                                     int(etime[2]))).values(
            'enweight', 'stationname')
        for wd in weightdata:
            if wd['stationname'] in weight:
                weight[wd['stationname']] = weight[wd['stationname']] + wd['enweight']
            else:
                weight[wd['stationname']] = wd['enweight']
    else:
        weightdata = models.Area.objects.filter(province = pro,
                                                date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                                date__lte = datetime(int(etime[0]), int(etime[1]),
                                                                     int(etime[2]))).values(
            'exweight', 'stationname')
        for wd in weightdata:
            if wd['stationname'] in weight:
                weight[wd['stationname']] = weight[wd['stationname']] + wd['exweight']
            else:
                weight[wd['stationname']] = wd['exweight']

        # weight.append({'name':wd['stationname'],'value':wd['enweight']})
    #  geo.append(sd.stationname:[sd.longi,sd.lati])
    # return HttpResponse(weight['杨林收费站'])
    value = []
    for wd in weight:
        value.append({'name': wd, 'value': weight[wd]})
    return render(request, 'truckheavycount.html',
                  {'dat': json.dumps(dat), 'province': json.dumps(pro), 'geo': json.dumps(geo),
                   'weight': json.dumps(value), 'tp': json.dumps(tp), 'st': json.dumps(st), 'ed': json.dumps(ed)})


def exheavycount(request):
    data = models.Province.objects.all().values('province', 'exweight')
    dat = []
    for d in data:
        dat.append({'name': d['province'], 'value': d['exweight']})
    return render(request, 'exheavycount.html', {'dat': json.dumps(dat)})


def extruckheavycount(request, pro):
    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    weightdata = models.Station.objects.filter(province = pro).values('stationname', 'exweight')
    weight = []
    for wd in weightdata:
        weight.append({'name': wd['stationname'], 'value': wd['exweight']})
    # geo.append(sd.stationname:[sd.longi,sd.lati])
    # return HttpResponse(geo)
    return render(request, 'extruckheavycount.html',
                  {'province': json.dumps(pro), 'geo': json.dumps(geo), 'weight': json.dumps(weight)})


def protrafficvolume(request):
    data = models.Province.objects.all().values('province', 'trafficvolume')
    dat = []
    for d in data:
        dat.append({'name': d['province'], 'value': d['trafficvolume']})
    return render(request, 'protrafficvolume.html', {'dat': json.dumps(dat)})


def trafficvolume(request, pro, tp, st, ed):
    if tp == '入口':
        data = models.Province.objects.all().values('province', 'entrafficvolume')
        dat = []
        for d in data:
            dat.append({'name': d['province'], 'value': d['entrafficvolume']})
    else:
        data = models.Province.objects.all().values('province', 'extrafficvolume')
        dat = []
        for d in data:
            dat.append({'name': d['province'], 'value': d['extrafficvolume']})

    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    stime = st.split('-')
    etime = ed.split('-')
    weight = {}
    if tp == '入口':
        weightdata = models.Area.objects.filter(province = pro,
                                                date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                                date__lte = datetime(int(etime[0]), int(etime[1]),
                                                                     int(etime[2]))).values(
            'entrafficvolume', 'stationname')
        for wd in weightdata:
            if wd['stationname'] in weight:
                weight[wd['stationname']] = weight[wd['stationname']] + wd['entrafficvolume']
            else:
                weight[wd['stationname']] = wd['entrafficvolume']
    else:
        weightdata = models.Area.objects.filter(province = pro,
                                                date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                                date__lte = datetime(int(etime[0]), int(etime[1]),
                                                                     int(etime[2]))).values(
            'extrafficvolume', 'stationname')
        for wd in weightdata:
            if wd['stationname'] in weight:
                weight[wd['stationname']] = weight[wd['stationname']] + wd['extrafficvolume']
            else:
                weight[wd['stationname']] = wd['extrafficvolume']

        # weight.append({'name':wd['stationname'],'value':wd['enweight']})
    #  geo.append(sd.stationname:[sd.longi,sd.lati])
    # return HttpResponse(weight['杨林收费站'])
    value = []
    for wd in weight:
        value.append({'name': wd, 'value': weight[wd]})
    return render(request, 'trafficvolume.html',
                  {'dat': json.dumps(dat), 'province': json.dumps(pro), 'geo': json.dumps(geo), 'tv': json.dumps(value),
                   'tp': json.dumps(tp), 'st': json.dumps(st), 'ed': json.dumps(ed)})


# return render(request,'stationtrafficvolume.html')
def protrafficfee(request):
    data = models.Province.objects.all().values('province', 'fee')
    dat = []
    for d in data:
        dat.append({'name': d['province'], 'value': d['fee']})
    return render(request, 'protrafficfee.html', {'dat': json.dumps(dat)})


def trafficfee(request, pro, st, ed):
    data = models.Province.objects.all().values('province', 'fee')
    dat = []
    for d in data:
        dat.append({'name': d['province'], 'value': d['fee']})
    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    stime = st.split('-')
    etime = ed.split('-')
    weight = {}
    weightdata = models.Area.objects.filter(province = pro,
                                            date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                            date__lte = datetime(int(etime[0]), int(etime[1]), int(etime[2]))).values(
        'fee', 'stationname')
    for wd in weightdata:
        if wd['stationname'] in weight:
            weight[wd['stationname']] = weight[wd['stationname']] + wd['fee']
        else:
            weight[wd['stationname']] = wd['fee']

        # weight.append({'name':wd['stationname'],'value':wd['enweight']})
    #  geo.append(sd.stationname:[sd.longi,sd.lati])
    #   return HttpResponse(weight['杨林收费站'])
    value = []
    for wd in weight:
        value.append({'name': wd, 'value': weight[wd]})
    return render(request, 'trafficfee.html',
                  {'dat': json.dumps(dat), 'province': json.dumps(pro), 'geo': json.dumps(geo),
                   'fee': json.dumps(value), 'st': json.dumps(st), 'ed': json.dumps(ed)})


# return render(request,'stationtrafficfee.html')
def truck_transaction(request, pro):
    data = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in data:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})

    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    data = models.OD.objects.filter(province = pro, tp = 'txl').values('enstation', 'exstation', 'count')
    d1 = []
    d2 = []
    d3 = []
    t1 = {}
    for d in data:
        tmp = []
        tmp.append({'name': d['enstation']})
        tmp.append({'name': d['exstation'], 'value': d['count']})
        d1.append(tmp)
        if d['enstation'] in t1:
            t1[d['enstation']] = t1[d['enstation']] + d['count']
        else:
            t1[d['enstation']] = d['count']
        if d['exstation'] in t1:
            t1[d['exstation']] = t1[d['exstation']] + d['count']
        else:
            t1[d['exstation']] = d['count']
        d3.append({'name': d['enstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站',
                                                                                                           '') + '-' +
                           d['exstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站', ''),
                   'value': d['count']})
    for t in t1:
        d2.append({'name': t, 'value': t1[t]})

    # return HttpResponse(d3)

    return render(request, 'truck_transaction.html',
                  {'province': json.dumps(pro), 'geo': json.dumps(geo), 'd1': json.dumps(d1), 'd2': json.dumps(d2),
                   'd3': json.dumps(d3), 'tv': json.dumps(tv)})


def truck_cargo(request, pro):
    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    data = models.OD.objects.filter(province = pro, tp = 'weight').values('enstation', 'exstation', 'count')
    d1 = []
    d2 = []
    d3 = []
    t1 = {}
    for d in data:
        tmp = []
        tmp.append({'name': d['enstation']})
        tmp.append({'name': d['exstation'], 'value': d['count']})
        d1.append(tmp)
        if d['enstation'] in t1:
            t1[d['enstation']] = t1[d['enstation']] + d['count']
        else:
            t1[d['enstation']] = d['count']
        if d['exstation'] in t1:
            t1[d['exstation']] = t1[d['exstation']] + d['count']
        else:
            t1[d['exstation']] = d['count']
        d3.append({'name': d['enstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站',
                                                                                                           '') + '-' +
                           d['exstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站', ''),
                   'value': d['count']})
    for t in t1:
        d2.append({'name': t, 'value': t1[t]})
    weight = models.Province.objects.all().values('province', 'exweight')
    tv = []
    for d in weight:
        tv.append({'name': d['province'], 'value': d['exweight']})

    # return HttpResponse(d3)

    return render(request, 'truck_cargo.html',
                  {'province': json.dumps(pro), 'geo': json.dumps(geo), 'd1': json.dumps(d1), 'd2': json.dumps(d2),
                   'd3': json.dumps(d3), 'tv': json.dumps(tv)})


def freetranscount(request):
    return render(request, 'freetranscount.html')


def lvtong_transaction(request, pro):
    data = models.OD.objects.filter(province = pro, tp = 'greentxl').values('enstation', 'exstation', 'count')
    if data.count() == 0:
        data = models.OD.objects.filter(province = '北京', tp = 'greentxl').values('enstation', 'exstation', 'count')
        pro = '北京'
    data = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in data:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})

    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    data = models.OD.objects.filter(province = pro, tp = 'greentxl').values('enstation', 'exstation', 'count')
    if data.count() == 0:
        data = models.OD.objects.filter(province = '北京', tp = 'greentxl').values('enstation', 'exstation', 'count')
    d1 = []
    d2 = []
    d3 = []
    t1 = {}
    for d in data:
        tmp = []
        tmp.append({'name': d['enstation']})
        tmp.append({'name': d['exstation'], 'value': d['count']})
        d1.append(tmp)
        if d['enstation'] in t1:
            t1[d['enstation']] = t1[d['enstation']] + d['count']
        else:
            t1[d['enstation']] = d['count']
        if d['exstation'] in t1:
            t1[d['exstation']] = t1[d['exstation']] + d['count']
        else:
            t1[d['exstation']] = d['count']
        d3.append({'name': d['enstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站',
                                                                                                           '') + '-' +
                           d['exstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站', ''),
                   'value': d['count']})
    for t in t1:
        d2.append({'name': t, 'value': t1[t]})

    # return HttpResponse(data)

    return render(request, 'lvtong_transaction.html',
                  {'province': json.dumps(pro), 'geo': json.dumps(geo), 'd1': json.dumps(d1), 'd2': json.dumps(d2),
                   'd3': json.dumps(d3), 'tv': json.dumps(tv)})


def lvtong_cargo(request, pro):
    data = models.OD.objects.filter(province = pro, tp = 'greenweight').values('enstation', 'exstation', 'count')
    if data.count() == 0:
        data = models.OD.objects.filter(province = '北京', tp = 'greentxl').values('enstation', 'exstation', 'count')
        pro = '北京'

    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]

    # if data == None:
    #    data = models.OD.objects.filter(province = '北京',tp = 'greenweight').values('enstation','exstation','count')
    d1 = []
    d2 = []
    d3 = []
    t1 = {}
    for d in data:
        tmp = []
        tmp.append({'name': d['enstation']})
        tmp.append({'name': d['exstation'], 'value': d['count']})
        d1.append(tmp)
        if d['enstation'] in t1:
            t1[d['enstation']] = t1[d['enstation']] + d['count']
        else:
            t1[d['enstation']] = d['count']
        if d['exstation'] in t1:
            t1[d['exstation']] = t1[d['exstation']] + d['count']
        else:
            t1[d['exstation']] = d['count']
        d3.append({'name': d['enstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站',
                                                                                                           '') + '-' +
                           d['exstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站', ''),
                   'value': d['count']})
    for t in t1:
        d2.append({'name': t, 'value': t1[t]})
    weight = models.Province.objects.all().values('province', 'exweight')
    tv = []
    for d in weight:
        tv.append({'name': d['province'], 'value': d['exweight']})

    # return HttpResponse(d)

    return render(request, 'lvtong_cargo.html',
                  {'province': json.dumps(pro), 'geo': json.dumps(geo), 'd1': json.dumps(d1), 'd2': json.dumps(d2),
                   'd3': json.dumps(d3), 'tv': json.dumps(tv)})


def lvtongchestation(request, pro, tp, st, ed):
    if tp == '入口':
        data = models.Province.objects.all().values('province', 'enweight')
        dat = []
        for d in data:
            dat.append({'name': d['province'], 'value': d['enweight']})

    else:
        data = models.Province.objects.all().values('province', 'exweight')
        dat = []
        for d in data:
            dat.append({'name': d['province'], 'value': d['exweight']})

    stationdata = models.Map.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    stime = st.split('-')
    etime = ed.split('-')
    weight = {}
    if tp == '入口':
        weightdata = models.Area.objects.filter(province = pro,
                                                date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                                date__lte = datetime(int(etime[0]), int(etime[1]),
                                                                     int(etime[2]))).values(
            'engreentrafficvolume', 'stationname')
        for wd in weightdata:
            if wd['stationname'] in weight:
                weight[wd['stationname']] = weight[wd['stationname']] + wd['engreentrafficvolume']
            else:
                weight[wd['stationname']] = wd['engreentrafficvolume']
    else:
        weightdata = models.Area.objects.filter(province = pro,
                                                date__gte = datetime(int(stime[0]), int(stime[1]), int(stime[2])),
                                                date__lte = datetime(int(etime[0]), int(etime[1]),
                                                                     int(etime[2]))).values(
            'exgreentrafficvolume', 'stationname')
        for wd in weightdata:
            if wd['stationname'] in weight:
                weight[wd['stationname']] = weight[wd['stationname']] + wd['exgreentrafficvolume']
            else:
                weight[wd['stationname']] = wd['exgreentrafficvolume']

        # weight.append({'name':wd['stationname'],'value':wd['enweight']})
    #  geo.append(sd.stationname:[sd.longi,sd.lati])
    # return HttpResponse(weight['杨林收费站'])
    value = []
    for wd in weight:
        value.append({'name': wd, 'value': weight[wd]})
    return render(request, 'lvtongchestation.html',
                  {'dat': json.dumps(dat), 'province': json.dumps(pro), 'geo': json.dumps(geo), 'tv': json.dumps(value),
                   'tp': json.dumps(tp), 'st': json.dumps(st), 'ed': json.dumps(ed)})


def lvtongcheoutstation(request):
    return render(request, 'lvtongcheoutstation.html')


def lvtongchelist(request):
    return render(request, 'lvtongchelist.html')


def demo_lvtongche(request):
    return render(request, 'demo_lvtongche.html')


def profeedirection(request):
    gdata = models.China.objects.all()
    geo = {}
    for d in gdata:
        geo[d.city] = [d.longi, d.lati]
    #    return HttpResponse(geo)
    return render(request, 'profeedirection.html', {'geo': json.dumps(geo)})


def Ltransaction(request):
    return render(request, 'Ltransaction.html')


def uturn(request):
    return render(request, 'uturn.html')


def demo_uturn(request):
    return render(request, 'demo_uturn.html')


def HTransaction(request):
    return render(request, 'HTransaction.html')


def YouRuWuChulist(request):
    return render(request, 'YouRuWuChulist.html')


def YouRuWuChuStation(request):
    return render(request, 'YouRuWuChuStation.html')


def cardlist(request):
    return render(request, 'cardlist.html')


def carddaycount(request, pro):
    prodata = models.Province.objects.all().values('province', 'cardtrans')
    ct = []
    for d in prodata:
        ct.append({'name': d['province'], 'value': d['cardtrans']})
    data = models.Carddaycount.objects.filter(province = pro)
    dPro = []
    dAxis = []
    dcard = []
    dmtc = []
    dratio = []
    for d in data:
        dPro.append(d.province)
        strtime = d.date.strftime('%m-%d')
        # return HttpResponse(strtime)
        dAxis.append(strtime)
        # dAxis.append(d.date)
        dcard.append(d.card)
        dmtc.append(d.mtc)
        dratio.append(d.ratio)
    # return HttpResponse(ct)
    return render(request, 'carddaycount.html',
                  {'dAxis': json.dumps(dAxis), 'dcard': json.dumps(dcard), 'dmtc': json.dumps(dmtc),
                   'dratio': json.dumps(dratio), 'cardtrans': json.dumps(ct), 'province': json.dumps(pro)})


def cardtrans(request, pro):
    # pro = '浙江'
    diff = models.Diff.objects.filter(province = pro).values('date', 'stationname', 'carddiff', 'trafficdiff',
                                                             'cardnum',
                                                             'encard', 'excard')
    tdiff = {}
    cdiff = {}
    cardnum = {}
    encard = {}
    excard = {}
    for d in diff:
        strtime = d['date'].strftime('%m-%d')
        if strtime in tdiff:
            tdiff[strtime][d['stationname']] = d['trafficdiff']
        else:
            tdiff[strtime] = {}
            tdiff[strtime][d['stationname']] = d['trafficdiff']
        if strtime in cdiff:
            cdiff[strtime][d['stationname']] = d['carddiff']
        else:
            cdiff[strtime] = {}
            cdiff[strtime][d['stationname']] = d['carddiff']
        if strtime in cardnum:
            cardnum[strtime].append({'name': d['stationname'], 'value': d['cardnum']})
        else:
            cardnum[strtime] = []
            cardnum[strtime].append({'name': d['stationname'], 'value': d['cardnum']})
        if strtime in encard:
            encard[strtime][d['stationname']] = d['encard']
        else:
            encard[strtime] = {}
            encard[strtime][d['stationname']] = d['encard']
        if strtime in excard:
            excard[strtime][d['stationname']] = d['excard']
        else:
            excard[strtime] = {}
            excard[strtime][d['stationname']] = d['excard']
    prodata = models.Province.objects.all().values('province', 'cardtrans')
    ct = []
    for d in prodata:
        ct.append({'name': d['province'], 'value': d['cardtrans']})
    geodata = models.Map.objects.filter(province = pro)
    geo = {}
    for d in geodata:
        geo[d.stationname] = [d.longi, d.lati]
    data = models.CardTrans.objects.filter(province = pro)
    dat = {}
    t = {}
    dat2 = {}
    dat3 = {}
    for d in data:
        strtime = d.date.strftime('%m-%d')
        if strtime in dat:
            tmp = []
            tmp.append({'name': d.enstation})
            tmp.append({'name': d.exstation, 'value': d.count})
            dat[strtime].append(tmp)
            if d.enstation in t[strtime]:
                t[strtime][d.enstation] = t[strtime][d.enstation] + d.count
            else:
                t[strtime][d.enstation] = d.count
            if d.exstation in t[strtime]:
                t[strtime][d.exstation] = t[strtime][d.exstation] + d.count
            else:
                t[strtime][d.exstation] = d.count
            dat3[strtime].append({'name': d.enstation + "-" + d.exstation, 'value': d.count})
        else:
            dat[strtime] = []
            tmp = []
            tmp.append({'name': d.enstation})
            tmp.append({'name': d.exstation, 'value': d.count})
            dat[strtime].append(tmp)
            t[strtime] = {}
            t[strtime][d.enstation] = d.count
            t[strtime][d.exstation] = d.count
            dat3[strtime] = []
            dat3[strtime].append({'name': d.enstation + "-" + d.exstation, 'value': d.count})
    for key in t:
        dat2[key] = []
        for k in t[key]:
            dat2[key].append({'name': k, 'value': t[key][k]})

    # return HttpResponse(len(data))
    return render(request, 'cardtrans.html',
                  {'geo': json.dumps(geo), 'data': json.dumps(dat), 'province': json.dumps(pro),
                   'data2': json.dumps(dat2), 'cardnum': json.dumps(cardnum), 'encard': json.dumps(encard),
                   'excard': json.dumps(excard), 'data3': json.dumps(dat3), 'cardtrans': json.dumps(ct),
                   'trafficdiff': json.dumps(tdiff), 'carddiff': json.dumps(cdiff)})


def cardtran_over_province(request, pro):
    stationdata = models.Map.objects.filter(province = pro)

    '''
    added by weixiang start 2018-12-05
    '''
    path = []
    with open("hway/trace.csv") as file_object:
        for line in file_object:
            items = line.strip('\n').split(',')
            items = list(filter(None, items))
            items = [float(x) for x in items]
            time_stand_by = 0
            # print(len(items))
            # print(items)
            for i in range(int(len(items) / 2) - 1):
                temp_path = []
                temp_path.append([items[2 * i], items[2 * i + 1]])
                temp_path.append([items[2 * (i + 1)], items[2 * (i + 1) + 1]])
                temp_path.append(50)  # 切段数
                temp_path.append(0.2)  # 高度
                temp_path.append(i * 50)  # 开始绘制count数
                temp_path.append([255, 212, 19])
                temp_path.append(1.0)  # 透明度
                temp_path.append(10)  # 线宽
                path.append(temp_path)  # 当前路径加入所有path中汇总         
    '''
    added by weixiang end 2018 12-05
    '''
    geo = {}
    for sd in stationdata:
        geo[sd.stationname] = [sd.longi, sd.lati]
    data = models.OD.objects.filter(province = pro, tp = 'weight').values('enstation', 'exstation', 'count')
    d1 = []
    d2 = []
    d3 = [
        {'name': '北京', 'value': 926097},
        {'name': '河南', 'value': 861270},
        {'name': '山东', 'value': 800981},
        {'name': '湖南', 'value': 744912},
        {'name': '湖北', 'value': 692768},
        {'name': '天津', 'value': 644274},
        {'name': '辽宁', 'value': 599174},
        {'name': '吉林', 'value': 557231},
        {'name': '黑龙江', 'value': 518224},
        {'name': '浙江', 'value': 481948},
    ]
    t1 = {}
    for d in data:
        tmp = []
        tmp.append({'name': d['enstation']})
        tmp.append({'name': d['exstation'], 'value': d['count']})
        d1.append(tmp)
        if d['enstation'] in t1:
            t1[d['enstation']] = t1[d['enstation']] + d['count']
        else:
            t1[d['enstation']] = d['count']
        if d['exstation'] in t1:
            t1[d['exstation']] = t1[d['exstation']] + d['count']
        else:
            t1[d['exstation']] = d['count']
        # d3.append({'name':d['enstation'].replace('收费站','').replace('主线站','').replace('匝道站','').replace('站','')+'-'+d['exstation'].replace('收费站','').replace('主线站','').replace('匝道站','').replace('站',''),'value':d['count']})
    for t in t1:
        d2.append({'name': t, 'value': t1[t]})
    weight = models.Province.objects.all().values('province', 'exweight')
    tv = []
    for d in weight:
        tv.append({'name': d['province'], 'value': d['exweight']})
        # return HttpResponse(d3)

    return render(request, 'cardtrans_outprovince_new.html',
                  {'path': json.dumps(path), 'province': json.dumps(pro), 'geo': json.dumps(geo), 'd1': json.dumps(d1),
                   'd2': json.dumps(d2), 'd3': json.dumps(d3), 'tv': json.dumps(tv)})


def stationcard(request, pro, station):
    data = models.Diff.objects.filter(province = pro, stationname = station).values('date', 'acccard', 'accmtc')
    axis = []
    card = []
    mtc = []
    for d in data:
        strtime = d['date'].strftime('%m-%d')
        axis.append(strtime)
        card.append(d['acccard'])
        mtc.append(-d['accmtc'])
    # return HttpResponse(card)
    return render(request, 'stationcard.html',
                  {'dAxis': json.dumps(axis), 'dcard': json.dumps(card), 'dmtc': json.dumps(mtc),
                   'station': json.dumps(station), 'province': json.dumps(pro)})


def cardcycle(request, pro1, pro2, pro3, tp):
    prodata = models.Province.objects.all().values('province', 'cardtrans')
    ct = []
    for d in prodata:
        ct.append({'name': d['province'], 'value': d['cardtrans']})
    data1 = models.Cycle.objects.filter(province = pro1)
    data2 = models.Cycle.objects.filter(province = pro2)
    data3 = models.Cycle.objects.filter(province = pro3)
    d11 = []
    d12 = []
    d13 = []
    d21 = []
    d22 = []
    d23 = []
    dAxis1 = []
    dAxis2 = []
    dAxis3 = []
    day4 = 0
    day5 = 0
    for d in data1:
        d21.append(d.count)
        dAxis1.append(d.cycle)
        if (d.cycle == 1):
            d11.append({'name': '1天', 'value': d.count})
        elif (d.cycle == 2):
            d11.append({'name': '2天', 'value': d.count})
        elif (d.cycle == 3):
            d11.append({'name': '3天', 'value': d.count})
        elif (d.cycle >= 4 and d.cycle <= 7):
            day4 = day4 + d.count
        else:
            day5 = day5 + d.count
    if (day4 != 0):
        d11.append({'name': '4-7天', 'value': day4})
    else:
        d11.append({'name': '4-7天', 'value': None})
    if (day5 != 0):
        d11.append({'name': '>7天', 'value': day5})
    else:
        d11.append({'name': '>7天', 'value': None})
    day4 = 0
    day5 = 0
    for d in data2:
        d22.append(d.count)
        dAxis2.append(d.cycle)
        if (d.cycle == 1):
            d12.append({'name': '1天', 'value': d.count})
        elif (d.cycle == 2):
            d12.append({'name': '2天', 'value': d.count})
        elif (d.cycle == 3):
            d12.append({'name': '3天', 'value': d.count})
        elif (d.cycle >= 4 and d.cycle <= 7):
            day4 = day4 + d.count
        else:
            day5 = day5 + d.count
    if (day4 != 0):
        d12.append({'name': '4-7天', 'value': day4})
    else:
        d12.append({'name': '4-7天', 'value': None})
    if (day5 != 0):
        d12.append({'name': '>7天', 'value': day5})
    else:
        d12.append({'name': '>7天', 'value': None})
    day4 = 0
    day5 = 0
    for d in data3:
        d23.append(d.count)
        dAxis3.append(d.cycle)
        if (d.cycle == 1):
            d13.append({'name': '1天', 'value': d.count})
        elif (d.cycle == 2):
            d13.append({'name': '2天', 'value': d.count})
        elif (d.cycle == 3):
            d13.append({'name': '3天', 'value': d.count})
        elif (d.cycle >= 4 and d.cycle <= 7):
            day4 = day4 + d.count
        else:
            day5 = day5 + d.count
    if (day4 != 0):
        d13.append({'name': '4-7天', 'value': day4})
    else:
        d13.append({'name': '4-7天', 'value': None})
    if (day5 != 0):
        d13.append({'name': '>7天', 'value': day5})
    else:
        d13.append({'name': '>7天', 'value': None})
    # return HttpResponse(d12)
    return render(request, 'cardcycle.html',
                  {'cardtrans': json.dumps(ct), 'data11': json.dumps(d11), 'data12': json.dumps(d12),
                   'data13': json.dumps(d13), 'data21': json.dumps(d21), 'data22': json.dumps(d22),
                   'data23': json.dumps(d23), 'dAxis1': json.dumps(dAxis1), 'dAxis2': json.dumps(dAxis2),
                   'dAxis3': json.dumps(dAxis3), 'pro1': json.dumps(pro1), 'pro2': json.dumps(pro2),
                   'pro3': json.dumps(pro3), 'tp': json.dumps(tp)})


def cardindex(request, pro1, pro2, pro3):
    prodata = models.Province.objects.all().values('province', 'cardtrans')
    ct = []
    for d in prodata:
        ct.append({'name': d['province'], 'value': d['cardtrans']})

    data1 = models.CardIndex.objects.filter(province = pro1)
    data2 = models.CardIndex.objects.filter(province = pro2)
    data3 = models.CardIndex.objects.filter(province = pro3)

    dat1 = {}
    dat2 = {}
    dat3 = {}
    for d in data1:
        dat1['stock'] = d.stock
        dat1['cycle'] = d.cycle
        dat1['turnover'] = d.turnover
        dat1['deposition'] = d.deposition
        dat1['safestock'] = d.safestock
    for d in data2:
        dat2['stock'] = d.stock
        dat2['cycle'] = d.cycle
        dat2['turnover'] = d.turnover
        dat2['deposition'] = d.deposition
        dat2['safestock'] = d.safestock
    for d in data3:
        dat3['stock'] = d.stock
        dat3['cycle'] = d.cycle
        dat3['turnover'] = d.turnover
        dat3['deposition'] = d.deposition
        dat3['safestock'] = d.safestock
    # return HttpResponse(dat1)
    return render(request, 'cardindex.html',
                  {'cardtrans': json.dumps(ct), 'pro1': json.dumps(pro1), 'pro2': json.dumps(pro2),
                   'pro3': json.dumps(pro3), 'dat1': json.dumps(dat1), 'dat2': json.dumps(dat2),
                   'dat3': json.dumps(dat3)})


def idealtrans(request, pro):
    diff = models.Diff.objects.filter(province = pro).values('date', 'stationname', 'carddiff', 'trafficdiff',
                                                             'cardnum',
                                                             'encard', 'excard')
    tdiff = {}
    cdiff = {}
    cardnum = {}
    encard = {}
    excard = {}
    for d in diff:
        strtime = d['date'].strftime('%m-%d')
        if strtime in tdiff:
            tdiff[strtime][d['stationname']] = d['trafficdiff']
        else:
            tdiff[strtime] = {}
            tdiff[strtime][d['stationname']] = d['trafficdiff']
        if strtime in cdiff:
            cdiff[strtime][d['stationname']] = d['carddiff']
        else:
            cdiff[strtime] = {}
            cdiff[strtime][d['stationname']] = d['carddiff']
        if strtime in cardnum:
            cardnum[strtime].append({'name': d['stationname'], 'value': d['cardnum']})
        else:
            cardnum[strtime] = []
            cardnum[strtime].append({'name': d['stationname'], 'value': d['cardnum']})
        if strtime in encard:
            encard[strtime][d['stationname']] = d['encard']
        else:
            encard[strtime] = {}
            encard[strtime][d['stationname']] = d['encard']
        if strtime in excard:
            excard[strtime][d['stationname']] = d['excard']
        else:
            excard[strtime] = {}
            excard[strtime][d['stationname']] = d['excard']
    prodata = models.Province.objects.all().values('province', 'cardtrans')
    ct = []
    for d in prodata:
        ct.append({'name': d['province'], 'value': d['cardtrans']})
    geodata = models.Map.objects.filter(province = pro)
    geo = {}
    for d in geodata:
        geo[d.stationname] = [d.longi, d.lati]

    data = models.CardTrans.objects.filter(province = pro)
    dat = {}
    t = {}
    dat2 = {}
    dat3 = {}
    for d in data:
        strtime = d.date.strftime('%m-%d')
        if strtime in dat:
            tmp = []
            tmp.append({'name': d.enstation})
            tmp.append({'name': d.exstation, 'value': d.count})
            dat[strtime].append(tmp)
            if d.enstation in t[strtime]:
                t[strtime][d.enstation] = t[strtime][d.enstation] + d.count
            else:
                t[strtime][d.enstation] = d.count
            if d.exstation in t[strtime]:
                t[strtime][d.exstation] = t[strtime][d.exstation] + d.count
            else:
                t[strtime][d.exstation] = d.count
            dat3[strtime].append({'name': d.enstation + "-" + d.exstation, 'value': d.count})
        else:
            dat[strtime] = []
            tmp = []
            tmp.append({'name': d.enstation})
            tmp.append({'name': d.exstation, 'value': d.count})
            dat[strtime].append(tmp)
            t[strtime] = {}
            t[strtime][d.enstation] = d.count
            t[strtime][d.exstation] = d.count
            dat3[strtime] = []
            dat3[strtime].append({'name': d.enstation + "-" + d.exstation, 'value': d.count})
    for key in t:
        dat2[key] = []
        for k in t[key]:
            dat2[key].append({'name': k, 'value': t[key][k]})

    idealdata = models.IdealTrans.objects.filter(province = pro)
    idat = {}
    it = {}
    idat2 = {}
    idat3 = {}
    for d in idealdata:
        strtime = d.date.strftime('%m-%d')
        if strtime in idat:
            tmp = []
            tmp.append({'name': d.enstation})
            tmp.append({'name': d.exstation, 'value': d.count})
            idat[strtime].append(tmp)
            if d.enstation in it[strtime]:
                it[strtime][d.enstation] = it[strtime][d.enstation] + d.count
            else:
                it[strtime][d.enstation] = d.count
            if d.exstation in it[strtime]:
                it[strtime][d.exstation] = it[strtime][d.exstation] + d.count
            else:
                it[strtime][d.exstation] = d.count
            idat3[strtime].append({'name': d.enstation + "-" + d.exstation, 'value': d.count})
        else:
            idat[strtime] = []
            tmp = []
            tmp.append({'name': d.enstation})
            tmp.append({'name': d.exstation, 'value': d.count})
            idat[strtime].append(tmp)
            it[strtime] = {}
            it[strtime][d.enstation] = d.count
            it[strtime][d.exstation] = d.count
            idat3[strtime] = []
            idat3[strtime].append({'name': d.enstation + "-" + d.exstation, 'value': d.count})

    for key in it:
        idat2[key] = []
        for k in it[key]:
            idat2[key].append({'name': k, 'value': it[key][k]})
    return render(request, 'idealtrans.html',
                  {'province': json.dumps(pro), 'cardtrans': json.dumps(ct), 'geo': json.dumps(geo),
                   'data': json.dumps(dat), 'idata': json.dumps(idat), 'data2': json.dumps(dat2),
                   'idata2': json.dumps(idat2), 'data3': json.dumps(dat3), 'idata3': json.dumps(idat3),
                   'cardnum': json.dumps(cardnum), 'encard': json.dumps(encard), 'excard': json.dumps(excard),
                   'trafficdiff': json.dumps(tdiff), 'carddiff': json.dumps(cdiff)})


def demo(request):
    return render(request, 'demo.html')


def axis_charge(request, province = "贵州"):
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})
    axisdata = models.Axischarge.objects.filter(province = province).values(
        'traffic_amount', 'date', 'axis_low', 'axis_low_percar',
        'weightfee_amount', 'weightfee_percar', 'axis_ref', 'axis_ref_percar',
        'axis_high', 'axis_high_percar'
    )
    xAxis = [d['date'].strftime('%m-%d') for d in axisdata]
    senddata = {
        'low': [d['axis_low'] for d in axisdata], 'weight': [d['weightfee_amount'] for d in axisdata],
        'high': [d['axis_high'] for d in axisdata],
        'low_per': [d['axis_low_percar'] for d in axisdata], 'weight_per': [d['weightfee_percar'] for d in axisdata],
        'high_per': [d['axis_high_percar'] for d in axisdata]
    }
    returndata = {'province': json.dumps(province), 'trafficvolume': tv, 'data': json.dumps(senddata),
                  'xAxis': json.dumps(xAxis)}
    return render(request, 'Axis_charge.html', returndata)


def overload(request, province = "贵州", request_type = 'mloss'):
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})
    data1 = models.Overload.objects.filter(province = province, vtype = 11).values("date", 'loss_money', 'add_traffic',
                                                                                   'loss_ratio', 'add_ratio')
    data2 = models.Overload.objects.filter(province = province, vtype = 12).values("date", 'loss_money', 'add_traffic',
                                                                                   'loss_ratio', 'add_ratio')
    data3 = models.Overload.objects.filter(province = province, vtype = 13).values("date", 'loss_money', 'add_traffic',
                                                                                   'loss_ratio', 'add_ratio')
    data4 = models.Overload.objects.filter(province = province, vtype = 14).values("date", 'loss_money', 'add_traffic',
                                                                                   'loss_ratio', 'add_ratio')
    data5 = models.Overload.objects.filter(province = province, vtype = 15).values("date", 'loss_money', 'add_traffic',
                                                                                   'loss_ratio', 'add_ratio')
    xAxis = []
    for d in data1:
        strtime = d['date'].strftime('%m-%d')
        xAxis.append(strtime)
    senddata = {'11': {'loss_money': [d['loss_money'] for d in data1], 'add_traffic': [d['add_traffic'] for d in data1],
                       'loss_ratio': [d['loss_ratio'] for d in data1], 'add_ratio': [d['add_ratio'] for d in data1]},
                '12': {'loss_money': [d['loss_money'] for d in data2], 'add_traffic': [d['add_traffic'] for d in data2],
                       'loss_ratio': [d['loss_ratio'] for d in data2], 'add_ratio': [d['add_ratio'] for d in data2]},
                '13': {'loss_money': [d['loss_money'] for d in data3], 'add_traffic': [d['add_traffic'] for d in data3],
                       'loss_ratio': [d['loss_ratio'] for d in data3], 'add_ratio': [d['add_ratio'] for d in data3]},
                '14': {'loss_money': [d['loss_money'] for d in data4], 'add_traffic': [d['add_traffic'] for d in data4],
                       'loss_ratio': [d['loss_ratio'] for d in data4], 'add_ratio': [d['add_ratio'] for d in data4]},
                '15': {'loss_money': [d['loss_money'] for d in data5], 'add_traffic': [d['add_traffic'] for d in data5],
                       'loss_ratio': [d['loss_ratio'] for d in data5], 'add_ratio': [d['add_ratio'] for d in data5]}
                }
    returndata = {'province': json.dumps(province), 'trafficvolume': tv, 'data': json.dumps(senddata),
                  'xAxis': json.dumps(xAxis)}
    if request_type == 'mloss':
        return render(request, 'overload_mloss.html', returndata)
    if request_type == 'tloss':
        return render(request, 'overload_tloss.html', returndata)


def potential_influence(request, province = "贵州", request_type = "mloss", c = 0.5):
    c = float(c)
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})
    data_1 = models.Potential_c.objects.filter(province = province, c = c, vtype = 11).values('province', 'date',
                                                                                              'vtype',
                                                                                              'p_loss_low',
                                                                                              'p_loss_high',
                                                                                              'traffic_loss_low',
                                                                                              'traffic_loss_high', 'c')
    data_2 = models.Potential_c.objects.filter(province = province, c = c, vtype = 12).values('province', 'date',
                                                                                              'vtype',
                                                                                              'p_loss_low',
                                                                                              'p_loss_high',
                                                                                              'traffic_loss_low',
                                                                                              'traffic_loss_high', 'c')
    data_3 = models.Potential_c.objects.filter(province = province, c = c, vtype = 13).values('province', 'date',
                                                                                              'vtype',
                                                                                              'p_loss_low',
                                                                                              'p_loss_high',
                                                                                              'traffic_loss_low',
                                                                                              'traffic_loss_high', 'c')
    data_4 = models.Potential_c.objects.filter(province = province, c = c, vtype = 14).values('province', 'date',
                                                                                              'vtype',
                                                                                              'p_loss_low',
                                                                                              'p_loss_high',
                                                                                              'traffic_loss_low',
                                                                                              'traffic_loss_high', 'c')
    data_5 = models.Potential_c.objects.filter(province = province, c = c, vtype = 15).values('province', 'date',
                                                                                              'vtype',
                                                                                              'p_loss_low',
                                                                                              'p_loss_high',
                                                                                              'traffic_loss_low',
                                                                                              'traffic_loss_high', 'c')
    xAxis = []
    loss_low_1 = []
    loss_high_1 = []
    loss_low_2 = []
    loss_high_2 = []
    loss_low_3 = []
    loss_high_3 = []
    loss_low_4 = []
    loss_high_4 = []
    loss_low_5 = []
    loss_high_5 = []

    traffic_low_1 = []
    traffic_high_1 = []
    traffic_low_2 = []
    traffic_high_2 = []
    traffic_low_3 = []
    traffic_high_3 = []
    traffic_low_4 = []
    traffic_high_4 = []
    traffic_low_5 = []
    traffic_high_5 = []
    for d in data_1:
        strtime = d['date'].strftime('%m-%d')
        xAxis.append(strtime)
        loss_low_1.append(d['p_loss_low'])
        loss_high_1.append(d['p_loss_high'])
        traffic_low_1.append(d['traffic_loss_low'])
        traffic_high_1.append(d['traffic_loss_high'])
    for d in data_2:
        loss_low_2.append(d['p_loss_low'])
        loss_high_2.append(d['p_loss_high'])
        traffic_low_2.append(d['traffic_loss_low'])
        traffic_high_2.append(d['traffic_loss_high'])
    for d in data_3:
        loss_low_3.append(d['p_loss_low'])
        loss_high_3.append(d['p_loss_high'])
        traffic_low_3.append(d['traffic_loss_low'])
        traffic_high_3.append(d['traffic_loss_high'])
    for d in data_4:
        loss_low_4.append(d['p_loss_low'])
        loss_high_4.append(d['p_loss_high'])
        traffic_low_4.append(d['traffic_loss_low'])
        traffic_high_4.append(d['traffic_loss_high'])
    for d in data_5:
        loss_low_5.append(d['p_loss_low'])
        loss_high_5.append(d['p_loss_high'])
        traffic_low_5.append(d['traffic_loss_low'])
        traffic_high_5.append(d['traffic_loss_high'])
    # loss_low_sum=sum(loss_low_1.extend(loss_low_2).extend(loss_low_3).extend(loss_low_4).extend(loss_low_5))
    mydata = {"loss_low_1": loss_low_1, "loss_low_2": loss_low_2, "loss_low_3": loss_low_3, "loss_low_4": loss_low_4,
              "loss_low_5": loss_low_5,
              "loss_high_1": loss_high_1, "loss_high_2": loss_high_2, "loss_high_3": loss_high_3,
              "loss_high_4": loss_high_4, "loss_high_5": loss_high_5,
              "traffic_low_1": traffic_low_1, "traffic_low_2": traffic_low_2, "traffic_low_3": traffic_low_3,
              "traffic_low_4": traffic_low_4, "traffic_low_5": traffic_low_5,
              "traffic_high_1": traffic_high_1, "traffic_high_2": traffic_high_2, "traffic_high_3": traffic_high_3,
              "traffic_high_4": traffic_high_4, "traffic_high_5": traffic_high_5}
    returndata = {'province': json.dumps(province), 'trafficvolume': tv, 'data': json.dumps(mydata),
                  'xAxis': json.dumps(xAxis), 'c': json.dumps(c)}
    if request_type == 'mloss':
        return render(request, 'potentialloss.html', returndata)
    elif request_type == 'tloss':
        return render(request, 'p_traffic_loss.html', returndata)


def chargebytype(request, province = "贵州"):
    trafficvolume = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in trafficvolume:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})
    # dfee.append(d.fee)
    # return HttpResponse(tv)
    # province = models.ProvinceNumber.objects.filter(number = pro).values('province')
    # p = province[province]
    # return HttpResponse(province)
    data_1 = models.Chargebytype.objects.filter(vtype = 11).values('province', 'date', 'vtype', 'weightfee', 'feelow',
                                                                   'feehigh')
    data_2 = models.Chargebytype.objects.filter(vtype = 12).values('province', 'date', 'vtype', 'weightfee', 'feelow',
                                                                   'feehigh')
    data_3 = models.Chargebytype.objects.filter(vtype = 13).values('province', 'date', 'vtype', 'weightfee', 'feelow',
                                                                   'feehigh')
    data_4 = models.Chargebytype.objects.filter(vtype = 14).values('province', 'date', 'vtype', 'weightfee', 'feelow',
                                                                   'feehigh')
    data_5 = models.Chargebytype.objects.filter(vtype = 15).values('province', 'date', 'vtype', 'weightfee', 'feelow',
                                                                   'feehigh')
    avg_data_1 = models.Chargebytype_avg.objects.filter(vtype = 11).values('province', 'vtype', 'weightfee', 'feelow',
                                                                           'feehigh')
    avg_data_2 = models.Chargebytype_avg.objects.filter(vtype = 12).values('province', 'vtype', 'weightfee', 'feelow',
                                                                           'feehigh')
    avg_data_3 = models.Chargebytype_avg.objects.filter(vtype = 13).values('province', 'vtype', 'weightfee', 'feelow',
                                                                           'feehigh')
    avg_data_4 = models.Chargebytype_avg.objects.filter(vtype = 14).values('province', 'vtype', 'weightfee', 'feelow',
                                                                           'feehigh')
    avg_data_5 = models.Chargebytype_avg.objects.filter(vtype = 15).values('province', 'vtype', 'weightfee', 'feelow',
                                                                           'feehigh')
    avg_low_1 = [avg_data_1[0]['feelow']] * 31
    avg_low_2 = [avg_data_2[0]['feelow']] * 31
    avg_low_3 = [avg_data_3[0]['feelow']] * 31
    avg_low_4 = [avg_data_4[0]['feelow']] * 31
    avg_low_5 = [avg_data_5[0]['feelow']] * 31
    avg_low_sum = [avg_low_1[0] + avg_low_2[0] + avg_low_3[0] + avg_low_4[0] + avg_low_5[0]] * 31
    avg_weight_1 = [avg_data_1[0]['weightfee']] * 31
    avg_weight_2 = [avg_data_2[0]['weightfee']] * 31
    avg_weight_3 = [avg_data_3[0]['weightfee']] * 31
    avg_weight_4 = [avg_data_4[0]['weightfee']] * 31
    avg_weight_5 = [avg_data_5[0]['weightfee']] * 31
    avg_weight_sum = [avg_weight_1[0] + avg_weight_2[0] + avg_weight_3[0] + avg_weight_4[0] + avg_weight_5[0]] * 31

    avg_high_1 = [avg_data_1[0]['feehigh']] * 31
    avg_high_2 = [avg_data_2[0]['feehigh']] * 31
    avg_high_3 = [avg_data_3[0]['feehigh']] * 31
    avg_high_4 = [avg_data_4[0]['feehigh']] * 31
    avg_high_5 = [avg_data_5[0]['feehigh']] * 31
    avg_high_sum = [avg_high_1[0] + avg_high_2[0] + avg_high_3[0] + avg_high_4[0] + avg_high_5[0]] * 31
    avg_data = {'low': [avg_low_1, avg_low_2, avg_low_3, avg_low_4, avg_low_5, avg_low_sum],
                'high': [avg_high_1, avg_high_2, avg_high_3, avg_high_4, avg_high_5, avg_high_sum],
                'weight': [avg_weight_1, avg_weight_2, avg_weight_3, avg_weight_4, avg_weight_5, avg_weight_sum]
                }

    xAxis = []
    low_1 = []
    high_1 = []
    weight_1 = []
    low_2 = []
    high_2 = []
    weight_2 = []
    low_3 = []
    high_3 = []
    weight_3 = []
    low_4 = []
    high_4 = []
    weight_4 = []
    low_5 = []
    high_5 = []
    weight_5 = []
    low_sum = []
    high_sum = []
    weight_sum = []
    for d in data_1:
        strtime = d['date'].strftime('%m-%d')
        xAxis.append(strtime)
        low_1.append(d['feelow'])
        high_1.append(d['feehigh'])
        weight_1.append(d['weightfee'])
    for d in data_2:
        low_2.append(d['feelow'])
        high_2.append(d['feehigh'])
        weight_2.append(d['weightfee'])
    for d in data_3:
        low_3.append(d['feelow'])
        high_3.append(d['feehigh'])
        weight_3.append(d['weightfee'])
    for d in data_4:
        low_4.append(d['feelow'])
        high_4.append(d['feehigh'])
        weight_4.append(d['weightfee'])
    for d in data_5:
        low_5.append(d['feelow'])
        high_5.append(d['feehigh'])
        weight_5.append(d['weightfee'])

    for index in range(len(low_1)):
        low_sum.append(low_1[index] + low_2[index] + low_3[index] + low_4[index] + low_5[index])
    for index in range(len(high_1)):
        high_sum.append(high_1[index] + high_2[index] + high_3[index] + high_4[index] + high_5[index])
    for index in range(len(weight_1)):
        weight_sum.append(weight_1[index] + weight_2[index] + weight_3[index] + weight_4[index] + weight_5[index])
    senddata = {'low_1': low_1, 'low_2': low_2, 'low_3': low_3, 'low_4': low_4, 'low_5': low_5, 'low_sum': low_sum,
                'high_1': high_1, 'high_2': high_2, 'high_3': high_3, 'high_4': high_4, 'high_5': high_5,
                'high_sum': high_sum,
                'weight_1': weight_1, 'weight_2': weight_2, 'weight_3': weight_3, 'weight_4': weight_4,
                'weight_5': weight_5, 'weight_sum': weight_sum}
    returndata = {'province': json.dumps(province), 'trafficvolume': tv, 'data': json.dumps(senddata),
                  'xAxis': json.dumps(xAxis), 'avg_data': json.dumps(avg_data)}
    return render(request, 'chargebytype.html', returndata)


def markstaion(request):
    return render(request, 'mark_station.html')


def pathreduction(request):
    return render(request, 'path_reduction.html')


def chongqing_od(request):
    return render(request, 'chongqing_od.html')


def chongqing_od_search(request):
    result = {"status": "ok", "data": []}
    keyword = request.GET.get('keyword', default = 0)

    data = models.Chongqing_od.objects.filter(link_id = keyword)

    for row in data:
        result['data'].append(
            {
                'link_id': row.link_id,
                'toll': row.toll
            }
        )

    return JsonResponse(result)


def faultRoad_impact(request, pro, linkId, type):
    #print(linkId + "  " + pro)
    default_link = {'重庆':'550749', '贵州':'90530885', '北京':'90530885','天津':'90530885','上海':'90530885','宁夏':'90530885',
                    '新疆':'90530885','内蒙古':'90530885','广西':'90530885','河北':'90530885','山西':'90530885','辽宁':'90530885',
                    '吉林':'90530885','黑龙江':'90530885','江苏':'90530885','浙江':'90530885','安徽':'90530885','福建':'90530885',
                    '江西':'90530885','山东':'90530885','河南':'90530885','湖北':'90530885','湖南':'90530885','广东':'90530885',
                    '四川':'90530885','云南':'90530885','甘肃':'90530885','青海':'90530885',}
    flag = True
    data = models.LinkToOD.objects.filter(province = pro, link_id = linkId).values('enstation', 'exstation', 'txl')
    if (data.count() == 0) and (type == "map"):
        data = models.LinkToOD.objects.filter(province=pro, link_id=default_link[pro]).values('enstation', 'exstation', 'txl')
        linkId = default_link[pro]
    if (data.count() == 0) and (type == "button"):
        flag = False

    data = models.Province.objects.all().values('province', 'extrafficvolume')
    tv = []
    for d in data:
        tv.append({'name': d['province'], 'value': d['extrafficvolume']})

    stationdata = models.ZhangXingTong.objects.filter(province = pro)
    geo = {}
    for sd in stationdata:
        geo[sd.station_name] = [sd.longi, sd.lati]
    data = models.LinkToOD.objects.filter(province = pro, link_id = linkId).values('enstation', 'exstation', 'txl')
    print(linkId + "  " + pro)
    print(data.count())
    if data.count() == 0:
        data = models.LinkToOD.objects.filter(province = '重庆', link_id = linkId).values('enstation', 'exstation', 'txl')
    d1 = []
    d2 = []
    d3 = []
    t1 = {}
    for d in data:
        tmp = []
        tmp.append({'name': d['enstation']})
        tmp.append({'name': d['exstation'], 'value': d['txl']})
        d1.append(tmp)
        if d['enstation'] in t1:
            t1[d['enstation']] = t1[d['enstation']] + d['txl']
        else:
            t1[d['enstation']] = d['txl']
        if d['exstation'] in t1:
            t1[d['exstation']] = t1[d['exstation']] + d['txl']
        else:
            t1[d['exstation']] = d['txl']
        d3.append({'name': d['enstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站',
                                                                                                           '') + '-' +
                           d['exstation'].replace('收费站', '').replace('主线站', '').replace('匝道站', '').replace('站', ''),
                   'value': d['txl']})
    for t in t1:
        d2.append({'name': t, 'value': t1[t]})

    # return HttpResponse(data)
    #print(d3)

    return render(request, 'faultRoad_impact.html',
                  {'province': json.dumps(pro), 'geo': json.dumps(geo), 'd1': json.dumps(d1), 'd2': json.dumps(d2),
                   'd3': json.dumps(d3), 'tv': json.dumps(tv), 'dl': json.dumps(linkId), 'flag': json.dumps(flag)})


def db_handle(request):
    all_items = []

    rootdir = 'I:\\pangqian\\roadLink\\outTopology\\odToLink_txl'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):  # 你想对文件的操作
            with open(path) as file_object:
                for line in file_object:
                    line = line.strip('\n')  # 把这个字符串头和尾的空格，以及位于头尾的\n \t之类给删掉。
                    tmp = line.split(':')
                    link = tmp[0]  # 路链值
                    odInfo = tmp[1].split(';')  # 包括所有OD信息
                    for item in odInfo:
                        data = item.split(',')
                        obj = models.LinkToOD(link_id=link, number=data[3], province=data[4],
                                            enstation=data[0],
                                            exstation=data[1], txl=int(data[2]))
                        all_items.append(obj)
    models.IdealTrans.objects.bulk_create(all_items)

    # models.IdealTrans.objects.all().delete()
    # l = []
    # with open('G:\\出行系数\\结果\\指标\\CARD\\浙江\\理论3.csv') as file_object:
    #     for line in file_object:
    #         line = line.strip('\n')
    #         tmp = line.split(',')
    #         year = int(tmp[2][0:4])
    #         month = int(tmp[2][4:6])
    #         day = int(tmp[2][6:8])
    #         obj = models.IdealTrans(number = tmp[0], province = tmp[1], date = datetime(year, month, day),
    #                                 enstation = tmp[3],
    #                                 exstation = tmp[4], count = int(float(tmp[5])))
    #         l.append(obj)
    # models.IdealTrans.objects.bulk_create(l)

    # with open("G:\\出行系数\\结果\\指标\\CARD\\index.csv") as file_object:
    #    for line in file_object:
    #       tmp = line.split(',')
    #      obj = models.CardIndex(number = tmp[1],province = tmp[0],stock = int(tmp[2]),cycle = float(tmp[3]),turnover = float(tmp[4]),deposition = float(tmp[5]),safestock = int(tmp[6]))
    #     l.append(obj)
    # models.CardIndex.objects.bulk_create(l)

    # province = "贵州"
    # with open("E:\\实验室\\贵州\\data\\tmp\\exlist_axle.csv") as file_object:
    #   file_object.readline()
    #  all_items=[]
    # for line in file_object:
    #    items=line.split(',')
    #   date = items[0].split('-')
    #  year = int(date[0])
    #    month = int(date[1])
    #   day = int(date[2])
    #  date = datetime(year,month,day)
    #   traffic_amount = int(items[3])
    #   axis_low = float(items[2])
    #   axis_low_percar = float(items[4])
    #   weightfee_amount = float(items[1])
    #   weightfee_percar = float(items[5])
    #   axis_ref = float(items[6])
    #   axis_ref_percar = float(items[7])
    #   axis_high = float(items[8])
    #   axis_high_percar = float(items[9])
    #  obj = models.Axischarge(province=province,traffic_amount=traffic_amount,
    #  date=date,axis_low=axis_low,axis_low_percar=axis_low_percar,weightfee_amount=weightfee_amount,
    #  weightfee_percar=weightfee_percar,axis_ref=axis_ref,axis_ref_percar=axis_ref_percar,
    #  axis_high=axis_high,axis_high_percar=axis_high_percar)
    #  all_items.append(obj)
    # models.Axischarge.objects.bulk_create(all_items)

    # province="贵州"
    # data1 = models.Overload.objects.filter(province=province,vtype=11).values("date",'loss_money','add_traffic','loss_ratio','add_ratio')
    # data2 = models.Overload.objects.filter(province=province,vtype=12).values("date",'loss_money','add_traffic','loss_ratio','add_ratio')
    # data3 = models.Overload.objects.filter(province=province,vtype=13).values("date",'loss_money','add_traffic','loss_ratio','add_ratio')
    # data4 = models.Overload.objects.filter(province=province,vtype=14).values("date",'loss_money','add_traffic','loss_ratio','add_ratio')
    # data5 = models.Overload.objects.filter(province=province,vtype=15).values("date",'loss_money','add_traffic','loss_ratio','add_ratio')
    # senddata = {'11':{'loss_money':[d['loss_money'] for d in data1],'add_traffic':[d['add_traffic'] for d in data1],'loss_ratio':[d['loss_ratio'] for d in data1],'add_ratio':[d['add_ratio'] for d in data1]},
    #             '12':{'loss_money':[d['loss_money'] for d in data2],'add_traffic':[d['add_traffic'] for d in data2],'loss_ratio':[d['loss_ratio'] for d in data2],'add_ratio':[d['add_ratio'] for d in data2]},
    #             '13':{'loss_money':[d['loss_money'] for d in data3],'add_traffic':[d['add_traffic'] for d in data3],'loss_ratio':[d['loss_ratio'] for d in data3],'add_ratio':[d['add_ratio'] for d in data3]},
    #             '14':{'loss_money':[d['loss_money'] for d in data4],'add_traffic':[d['add_traffic'] for d in data4],'loss_ratio':[d['loss_ratio'] for d in data4],'add_ratio':[d['add_ratio'] for d in data4]},
    #             '15':{'loss_money':[d['loss_money'] for d in data5],'add_traffic':[d['add_traffic'] for d in data5],'loss_ratio':[d['loss_ratio'] for d in data5],'add_ratio':[d['add_ratio'] for d in data5]}
    #             }

    # with open("C:\\Users\\nlsde\\Desktop\\网站数据\\overload.csv") as file_object:
    #     file_object.readline()
    #     province="贵州"
    #     allitems=[]
    #     for line in file_object:
    #         items = line.split(',')
    #         date = items[0].split('-')
    #         year = int(date[0])
    #         month = int(date[1])
    #         day = int(date[2])
    #         date = datetime(year,month,day)
    #         vtype = int(items[1])
    #         add_ratio = float(items[-2])
    #         loss_ratio = float(items[-3])
    #         loss_money = float(items[-4])
    #         add_traffic = float(items[-5])
    #         obj = models.Overload(province=province,date=date,vtype=vtype,loss_money=loss_money,add_traffic=add_traffic,loss_ratio=loss_ratio,add_ratio=add_ratio)
    #         allitems.append(obj)
    #     models.Overload.objects.bulk_create(allitems)

    # with open("C:\\Users\\nlsde\\Desktop\\网站数据\\All_day.csv") as file_object:
    #     file_object.readline()
    #     province = "贵州"
    #     allitems = []
    #     for line in file_object:
    #         items = line.split(',')
    #         date = items[0].split('-')
    #         year = int(date[0])
    #         month = int(date[1])
    #         day = int(date[2])
    #         date = datetime(year,month,day)
    #         vtype = int(items[1])
    #         fee_low = float(items[2])
    #         weight_fee = float(items[3])
    #         fee_high = float(items[5])
    #         obj = models.Chargebytype(province=province,date=date,vtype=vtype,weightfee=weight_fee,feelow=fee_low,feehigh=fee_high)
    #         allitems.append(obj)
    #     models.Chargebytype.objects.bulk_create(allitems)
    # l = [] 
    # #models.Cycle.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\CARD\\江苏\\分布.csv') as file_object:
    #     c = 1 
    #     for line in file_object:
    #         obj = models.Cycle(province = "江苏",number = "32",cycle = c ,count = int(line))
    #         l.append(obj)
    #         c = c + 1
    # models.Cycle.objects.bulk_create(l)
    # l = []
    # with open('G:\\出行系数\\结果\\指标\\CARD\\cycle.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     obj = models.Cycle(province = tmp[0],number = tmp[1], cycle = tmp[2], count = int(tmp[3]))
    #    l.append(obj)
    # models.Cycle.objects.bulk_create(l)

    # l = []
    # models.OD.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\map.csv') as file_object:
    #    for line in file_object:
    #       tmp = line.split(',')
    #      obj = models.Map(number = tmp[0],province = tmp[1],stationname = tmp[2],longi = float(tmp[3]),lati = float(tmp[4]))
    #     l.append(obj)
    # models.Map.objects.bulk_create(l)
    # with open('G:\\出行系数\\结果\\指标\\全国\\ltweight.csv') as file_object:
    #    for line in file_object:
    #       tmp = line.split(',')
    #      obj = models.OD(number = tmp[0],province = tmp[1],enstation = tmp[2],exstation = tmp[3],count = int(tmp[4]),tp = "greenweight")
    #     l.append(obj)
    # models.OD.objects.bulk_create(l)
    # l = []

    # models.Area.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\weight.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     year = int(tmp[3][0:4])
    #    if year != 2018:
    #       continue
    #      month = int(tmp[3][4:6])
    #     day = int(tmp[3][6:8])
    #    d = datetime(year,month,day)
    # obj = models.Area(stationname = tmp[0],number = tmp[1], province = tmp[2], date = d ,enweight = int(tmp[4]),exweight = int(tmp[5]), entrafficvolume = int(tmp[6]), extrafficvolume = int(tmp[7]),fee = int(tmp[8]))
    #     obj = models.Area(stationname = tmp[0],number = tmp[1], province = tmp[2], date = d ,enweight = int(tmp[4]),exweight = int(tmp[5]), entrafficvolume = int(tmp[6]), extrafficvolume = int(tmp[7]),fee = int(tmp[8]), engreentrafficvolume = int(tmp[9]), exgreentrafficvolume = int(tmp[10]))
    #    l.append(obj)
    #  models.Area.objects.bulk_create(l)
    # return HttpResponse("finished!")
    # with open('G:\\出行系数\\结果\\指标\\全国\\enweightbyday.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #       year = int(tmp[3][0:4])
    #       month = int(tmp[3][4:6])
    #       day = int(tmp[3][6:8])
    #       obj = models.Area(number = tmp[1], province = tmp[3], date = datetime(year,month,day),enweight = int(tmp[4]),stationname = tmp[0])
    #       l.append(obj)
    #   models.Area.objects.bulk_create(l)
    #   return HttpResponse("finished!")

    # with open('G:\\出行系数\\结果\\指标\\全国\\exweightbyday.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     year = int(tmp[3][0:4])
    #     month = int(tmp[3][4:6])
    #     day = int(tmp[3][6:8])
    #    d = datetime(year,month,day)
    #    m = models.Area.objects.filter(stationname = tmp[0],date = d)
    #    if m == None:
    #        dic = {'number':tmp[1],'province':tmp[3],'date':datetime(year,month,day),'exweight':int(tmp[4]),'stationname':tmp[0]}
    #        models.Area.objects.create(**dic)
    #    else:
    #        m.update(exweight = int(tmp[4]))

    # with open('G:\\出行系数\\结果\\指标\\全国\\daycount.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     dic = {"province":tmp[0],"date":tmp[1],"etc":int(tmp[2]),"mtc":int(tmp[3]),"fee":(tmp[4])}
    #    models.Daycount.objects.create(**dic)
    # with open('G:\\出行系数\\结果\\指标\\全国\\truckdaycount2.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     dic = {'province':tmp[0],'date':tmp[1],'truck11':int(tmp[2]),'truck12':int(tmp[3]),'truck13':int(tmp[4]),'truck14':int(tmp[5]),'truck15':int(tmp[6])}
    #    models.Truckdaycount.objects.create(**dic)
    # return HttpResponse("finished!")
    # with open('G:\\出行系数\\结果\\指标\\全国\\map.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #      dic = {'number':tmp[0],'province':tmp[1],'stationname':tmp[2],'longi':float(tmp[3]),'lati':float(tmp[4])}
    #     models.Map.objects.create(**dic)
    # with open('G:\\出行系数\\结果\\指标\\全国\\provinceheavy.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     dic = {'province':tmp[0],'enweight':int(tmp[1])}
    #    models.Province.objects.create(**dic)
    # with open('G:\\出行系数\\结果\\指标\\全国\\enweight.csv') as file_object:
    #    for line in file_object:
    #       tmp = line.split(',')
    #      dic = {'number':tmp[0],'province':tmp[1],'stationname':tmp[2],'enweight':int(tmp[3])}
    #     models.Station.objects.create(**dic)
    # models.Enweight.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\cardaycount.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     dic = {'province':tmp[0],'date':tmp[1],'car1':int(tmp[2]),'car2':int(tmp[3]),'car3':int(tmp[4]),'car4':int(tmp[5])}
    #    models.Cardaycount.objects.create(**dic)
    # models.Provinceheavycount.objects.all().delete()
    # models.Enweight.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\txlbypro.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     models.Province.objects.filter(province = tmp[0]).update(trafficvolume = int(tmp[1]))
    # with open('G:\\出行系数\\结果\\指标\\全国\\feebypro.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     models.Province.objects.filter(province = tmp[0]).update(fee = int(tmp[1]))
    # with open('G:\\出行系数\\结果\\指标\\全国\\sttxl.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     obj = models.Station.objects.filter(stationname = tmp[2])
    #    if obj == None :
    #       dic = {'number':tmp[0],'province':tmp[1],'stationname':tmp[2],'trafficvolume':int(tmp[3])}
    #      models.Station.objects.create(**dic)
    # else :
    #    obj.update(trafficvolume = tmp[3])
    # with open('G:\\出行系数\\结果\\指标\\全国\\stfee.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     obj = models.Station.objects.filter(stationname = tmp[2])
    #    if obj == None :
    #       dic = {'number':tmp[0],'province':tmp[1],'stationname':tmp[2],'fee':int(tmp[3])}
    #      models.Station.objects.create(**dic)
    # else :
    #    obj.update(fee = tmp[3])
    # models.Station.objects.all().delete()
    # models.Carddaycount.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\card.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     dic = {'province':tmp[0],'date':tmp[1],'card':int(tmp[2]),'mtc':int(tmp[3]),'ratio':float(tmp[4])}
    #    models.Carddaycount.objects.create(**dic)
    # models.Carddaycount.objects.all().delete()
    # models.ProvinceNumber.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\provincenumber.csv') as file_object:

    # for line in file_object:
    #     line = line.strip('\n')
    #     tmp = line.split(',')
    #     dic = {'province':tmp[0],'number':tmp[1]}
    #    models.ProvinceNumber.objects.create(**dic)
    # data = models.Truckdaycount.objects.filter(date__gte = '3月20日')
    # fil = []
    # for d in data:
    #   fil.append(d.date)
    # with open('G:\\出行系数\\结果\\指标\\全国\\enweight.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     dic = {'number':tmp[0],'province':tmp[1],'stationname':tmp[2],'enweight':int(tmp[3])}
    #    models.Station.objects.create(**dic)
    # return HttpResponse(fil)
    # models.TrafficVolume.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\txl.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     year = int(tmp[1][0:4])
    #    month = int(tmp[1][4:6])
    #   day = int(tmp[1][6:8])
    #  dic = {'number':tmp[0],'province':tmp[2],'date':datetime(year,month,day),'total':int(tmp[3])}
    #  models.TrafficVolume.objects.create(**dic)
    # with open('G:\\出行系数\\结果\\指标\\全国\\mtctxl.csv') as file_object:
    #  for line in file_object:
    # tmp = line.split(",")
    # year = int(tmp[0][0:4])
    #  month = int(tmp[0][4:6])
    #   day = int(tmp[0][6:8])
    #    d = datetime(year,month,day)
    #     m = models.TrafficVolume.objects.filter(date = d,number = tmp[1])
    #     if m == None:
    #          continue ;
    #       else:
    #            m.update(mtc = int(tmp[2]))
    # with open('G:\\出行系数\\结果\\指标\\全国\\trucktxl.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     year = int(tmp[0][0:4])
    #    month = int(tmp[0][4:6])
    #     day = int(tmp[0][6:8])
    #     d = datetime(year,month,day)
    #       m = models.TrafficVolume.objects.filter(date = d,number = tmp[1])
    #      if m == None:
    #         continue ;
    #    else:
    #       if tmp[2] == "1":
    #          m.update(tp1 = int(tmp[3]))
    #       elif tmp[2] == "2":
    #          m.update(tp2 = int(tmp[3]))
    #       elif tmp[2] == "3":
    #           m.update(tp3 = int(tmp[3]))
    #      elif tmp[2] == "4":
    #         m.update(tp4 = int(tmp[3]))
    #    elif tmp[2] == "11":
    #       m.update(tp11 = int(tmp[3]))
    #      elif tmp[2] == "12":
    #          m.update(tp12 = int(tmp[3]))
    #      elif tmp[2] == "13":
    #          m.update(tp13 = int(tmp[3]))
    #      elif tmp[2] == "14":
    #          m.update(tp14 = int(tmp[3]))
    #      elif tmp[2] == "15":
    # m.update(tp15 = int(tmp[3])'''
    # with open('G:\\出行系数\\结果\\指标\\全国\\fee.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(",")
    #     year = int(tmp[1][0:4])
    #    month = int(tmp[1][4:6])
    #    day = int(tmp[1][6:8])
    #    dic = {'number':tmp[0],'province':tmp[2],'date':datetime(year,month,day),'total':int(tmp[3])}
    #    models.Fee.objects.create(**dic)
    # with open('G:\\出行系数\\结果\\指标\\全国\\feebyvec.csv') as file_object:
    #    for line in file_object:
    #       tmp = line.split(",")
    #      year = int(tmp[0][0:4])
    #     month = int(tmp[0][4:6])
    #     day = int(tmp[0][6:8])
    #     d = datetime(year,month,day)
    #    m = models.Fee.objects.filter(date = d,number = tmp[1])
    #   if m == None:
    #      continue ;
    #    else:
    #       if tmp[2] == "1":
    #          m.update(tp1 = int(tmp[3]))
    #     elif tmp[2] == "2":
    #        m.update(tp2 = int(tmp[3]))
    #   elif tmp[2] == "3":
    #      m.update(tp3 = int(tmp[3]))
    #      elif tmp[2] == "4":
    #         m.update(tp4 = int(tmp[3]))
    #    elif tmp[2] == "11":
    #       m.update(tp11 = int(tmp[3]))
    #       elif tmp[2] == "12":
    #           m.update(tp12 = int(tmp[3]))
    #      elif tmp[2] == "13":
    #         m.update(tp13 = int(tmp[3]))
    #    elif tmp[2] == "14":
    #       m.update(tp14 = int(tmp[3]))
    #    elif tmp[2] == "15":
    #       m.update(tp15 = int(tmp[3]))

    # with open('G:\\出行系数\\结果\\指标\\全国\\pentxl.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     dic = {'number':tmp[0],'province':tmp[1],'entrafficvolume':int(tmp[2])}
    #    models.Province.objects.create(**dic)
    # return HttpResponse('finished!')

    # with open('G:\\出行系数\\结果\\指标\\全国\\pentxl.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     models.Province.objects.filter(number = tmp[0]).update(entrafficvolume = tmp[2])
    # dic = {'number':tmp[0],'province':tmp[1],'entrafficvolume':int(tmp[2])}
    # models.Province.objects.create(**dic)
    # models.China.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\全国\\china.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     #return HttpResponse()
    #    dic = {'province':tmp[0],'city':tmp[1],'longi':float(tmp[2]),'lati':float(tmp[3])}
    #   models.China.objects.create(**dic)
    # l = []
    # models.Diff.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\CARD\\diff.csv') as file_object:

    #   for line in file_object:
    #      tmp = line.split(',')
    #     year = int(tmp[2][0:4])
    #    month = int(tmp[2][4:6])
    #   day = int(tmp[2][6:8])
    #  obj = models.Diff(number = tmp[0],province = tmp[1], stationname = tmp[3],date = datetime(year,month,day),encard = int(tmp[4]),excard = int(tmp[5]),carddiff = int(tmp[6]),cardnum = int(tmp[7]),trafficdiff = int(tmp[8]))
    # l.append(obj)
    # models.Diff.objects.bulk_create(l)
    # models.Carddaycount.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\CARD\\result.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     year = int(tmp[0][0:4])
    #    month = int(tmp[0][4:6])
    #   day = int(tmp[0][6:8])
    #  obj = models.Carddaycount(date=datetime(year,month,day),province=tmp[1],card=int(tmp[2]),mtc=int(tmp[3]),ratio=float(tmp[4]))
    # l.append(obj)
    # models.Carddaycount.objects.bulk_create(l)
    # models.Carddaycount.objects.all().delete()
    # with open('G:\\出行系数\\结果\\指标\\CARD\\province.csv') as file_object:
    #   for line in file_object:
    #      tmp = line.split(',')
    #     models.Province.objects.filter(province = tmp[0]).update(cardtrans = int(tmp[1]))
    # models.CardTrans.objects.filter(province = '浙江').delete()
    #  with open('G:\\出行系数\\结果\\指标\\CARD\\浙江\\调度方向.csv') as file_object:
    # file_object.readline()
    #  for line in file_object:
    #  tmp = line.split(',')
    #   year = int(tmp[2][0:4])
    #    month = int(tmp[2][4:6])
    #     day = int(tmp[2][6:8])
    #      obj = models.CardTrans(number = tmp[0],province = tmp[1], date = datetime(year,month,day),enstation = tmp[3], exstation = tmp[4], count = int(tmp[5]))
    #       l.append(obj)
    # models.CardTrans.objects.bulk_create(l)
    # return HttpResponse(len(l))

    # with open('G:\\出行系数\\结果\\指标\\CARD\\浙江.csv') as file_object:
    #    file_object.readline()
    #   for line in file_object:
    #      tmp = line.split(',')
    #     year = int(tmp[2][0:4])
    #     month = int(tmp[2][4:6])
    #    day = int(tmp[2][6:8])
    #   models.Diff.objects.filter(date = datetime(year,month,day),province = tmp[1],stationname = tmp[3]).update(acccard = tmp[9],accmtc = tmp[10])
    # with open("C:\\Users\\nlsde\\Desktop\\网站数据\\All_day.csv") as file_object:
    #     file_object.readline()
    #     for line in file_object:
    #         items = line.split(',')
    #         date = items[0].split('-')
    #         year = int(date[0])
    #         month = int(date[1])
    #         day = int(date[2])

    return HttpResponse("finished!")


