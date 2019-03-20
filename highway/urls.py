"""highway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hway import views as hway_views

urlpatterns = [
    url(r'^$', hway_views.home, name="home"),
    url(r'^datavolum/$', hway_views.datavolum),
    url(r'^errordatavolum/$', hway_views.errordatavolum),
    url(r'^datarepairvolum/$', hway_views.datarepairvolum),
    url(r'^instation_plate/$', hway_views.instation_plate),
    url(r'^outstation_plate/$', hway_views.outstation_plate),
    url(r'^cxErrStation/$', hway_views.cxErrStation),
    url(r'^etcmtcdaytranscount/(.*)/$', hway_views.etcmtcdaytranscount),
    url(r'^cartypedaytranscount/(.*)/$', hway_views.cartypedaytranscount),
    url(r'^trucktypedaytranscount/(.*)/$', hway_views.trucktypedaytranscount),
    url(r'^vehicletypedaytranscount/(.*)$', hway_views.vehicletypedaytranscount),
    url(r'^vehicletransfeepie/(.*)/(.*)/(.*)/(.*)/(.*)/$', hway_views.vehicletransfeepie),
    url(r'^cartypedayfee/(.*)/$', hway_views.cartypedayfee),
    url(r'^trucktypedayfee/(.*)/$', hway_views.trucktypedayfee),
    url(r'^vehicletypedayfee/(.*)/$', hway_views.vehicletypedayfee),
    url(r'^truckheavycount/(.*)/(.*)/(.*)/(.*)/$', hway_views.truckheavycount),
    url(r'^trafficvolume/(.*)/(.*)/(.*)/(.*)/$', hway_views.trafficvolume),
    url(r'^trafficfee/(.*)/(.*)/(.*)/$', hway_views.trafficfee),
    url(r'^truck_transaction/(.*)/$', hway_views.truck_transaction),
    url(r'^truck_cargo/(.*)/$', hway_views.truck_cargo),
    url(r'^freetranscount/$', hway_views.freetranscount),
    url(r'^lvtong_transaction/(.*)/$', hway_views.lvtong_transaction),
    url(r'^lvtong_cargo/(.*)/$', hway_views.lvtong_cargo),
    url(r'^lvtongchestation/(.*)/(.*)/(.*)/(.*)/$', hway_views.lvtongchestation),
    url(r'^lvtongcheoutstation/$', hway_views.lvtongcheoutstation),
    url(r'^lvtongchelist/$', hway_views.lvtongchelist),
    url(r'^lvtongchelist/demo_lvtongche/$', hway_views.demo_lvtongche),
    url(r'^Ltransaction/$', hway_views.Ltransaction),
    url(r'^profeedirection/$', hway_views.profeedirection),
    url(r'^uturn/$', hway_views.uturn),
    url(r'^uturn/demo_uturn/$', hway_views.demo_uturn),
    url(r'^HTransaction/$', hway_views.HTransaction),
    url(r'^YouRuWuChulist/$', hway_views.YouRuWuChulist),
    url(r'^YouRuWuChuStation/$', hway_views.YouRuWuChuStation),
    url(r'^cardlist/$', hway_views.cardlist),
    url(r'^cardlist/demo/$', hway_views.demo),
    url(r'^carddaycount/(.*)/$', hway_views.carddaycount),
    url(r'^cardtransoverpro/(.*)/$', hway_views.cardtran_over_province),
    url(r'^cardtrans/(.*)/$', hway_views.cardtrans),
    url(r'^stationcard/(.*)/(.*)/$', hway_views.stationcard),
    url(r'^cardcycle/(.*)/(.*)/(.*)/(.*)/$', hway_views.cardcycle),
    url(r'^cardindex/(.*)/(.*)/(.*)/$', hway_views.cardindex),
    url(r'^idealtrans/(.*)/$', hway_views.idealtrans),
    url(r'^db_handle/$', hway_views.db_handle),
    url(r'^admin/', admin.site.urls),
    url(r'^chargebytype/(.*)/$', hway_views.chargebytype),
    url(r'^potentialloss/(.*)/(.*)/(.*)/$', hway_views.potential_influence),
    url(r'^overload/(.*)/(.*)/$', hway_views.overload),
    url(r'^axischarge/(.*)/', hway_views.axis_charge),
    url(r'^markstation', hway_views.markstaion),
    url(r'^pathreduction', hway_views.pathreduction),
    url(r'^chongqing_od/search', hway_views.chongqing_od_search),
    url(r'^chongqing_od', hway_views.chongqing_od),
    url(r'^faultRoad_impact/(.*)/(.*)/(.*)/$', hway_views.faultRoad_impact),
]
