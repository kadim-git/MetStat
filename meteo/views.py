from datetime import datetime
from django.utils import timezone

from django.shortcuts import render

# Create your views here.
from .models import MeteoRecord
from .models import WindRecord

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def post_meteo(request):

    if request.method == 'POST':
        pd=request.POST
        record = MeteoRecord(DATE=pd['DATE'],
                             TA=pd['TA'],
                             DP=pd['DP'],
                             WC=pd['WC'],
                             RH=pd['RH'],
                             PA=pd['PA'],
                             PR=pd['PR'],
                             PR1H=pd['PR1H'],
                             PR24h=pd['PR24h'],
                             SR_1M=pd['SR_1M'],
                             SR_1D=pd['SR_1D'],
                             SR_45_1M=pd['SR_45_1M'],
                             SR_45_1D=pd['SR_45_1D'],
                             SD_1H=pd['SD_1H'],
                             SD_1D=pd['SD_1D'],
                             SD_45_1H=pd['SD_45_1H'],
                             SD_45_1D=pd['SD_45_1D']
                             )
        record.save()

        ob1 = MeteoRecord.objects.filter(pk=20)
        count1=MeteoRecord.objects.filter(pk__lt= record.pk-20).count()
        MeteoRecord.objects.filter(pk__lt=record.pk - 20).delete()
        count2=MeteoRecord.objects.filter(pk__lt= record.pk-20).count()

        res='<h1>Ok POST Meteo</h1>'
        return HttpResponse(res, status=200)

    else:
        res = '<h1>Ok GET</h1>'
        return HttpResponse(res, status=204)

@csrf_exempt
def post_wind(request):

    if request.method == 'POST':
        pd=request.POST
        record = WindRecord(DATE=pd['DATE'],
                             WS1AVG=pd['WS1AVG'],
                             WD1AVG=pd['WD1AVG'],
                             WS1MIN2=pd['WS1MIN2'],
                             WS1AVG2=pd['WS1AVG2'],
                             WS1MAX2=pd['WS1MAX2'],
                             WD1MIN2=pd['WD1MIN2'],
                             WD1AVG2=pd['WD1AVG2'],
                             WD1MAX2=pd['WD1MAX2'],
                             WS1MIN10=pd['WS1MIN10'],
                             WS1AVG10=pd['WS1AVG10'],
                             WS1MAX10=pd['WS1MAX10'],
                             WD1MIN10=pd['WD1MIN10'],
                             WD1AVG10=pd['WD1AVG10'],
                             WD1MAX10=pd['WD1MAX10'],
                             )
        record.save()

        ob1 = WindRecord.objects.filter(pk=20)
        count1=WindRecord.objects.filter(pk__lt= record.pk-20).count()
        WindRecord.objects.filter(pk__lt=record.pk - 20).delete()
        count2=WindRecord.objects.filter(pk__lt= record.pk-20).count()

        res='<h1>Ok POST Wind</h1>'
        return HttpResponse(res, status=200)

    else:
        res = '<h1>Ok GET</h1>'
        return HttpResponse(res, status=204)

def index_test(request):
    """View function for home page of site."""
    #record = MeteoRecord(DATE = datetime.now(),
    record = MeteoRecord(DATE =timezone.now(),
    TA = -3.2,
    DP = -3.5,
    WC = 0,
    RH = 98,
    PA = 753.6,
    PR = 0,
    PR1H = 0,
    PR24h = 0,
    SR_1M = 24,
    SR_1D = 6,
    SR_45_1M = 22,
    SR_45_1D = 5,
    SD_1H = 18660,
    SD_1D = 106621,
    SD_45_1H = 15723,
    SD_45_1D = 88713
)

    # Save the object into the database.
    record.save()

    # Generate counts of some of the main objects
    records = MeteoRecord.objects.all().values()
    num_instances = MeteoRecord.objects.all().count()


    context = {
        'records': records[0],
        'num_instances': num_instances,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def meteost(request):
    records = MeteoRecord.objects.all().order_by('id')
    num_instances = MeteoRecord.objects.all().count()

    context = {
        'records': records,
        'num_instances': num_instances,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'meteost.html', context=context)

def windmod(request):
    records = WindRecord.objects.all().order_by('id')
    num_instances = WindRecord.objects.all().count()

    context = {
        'records': records,
        'num_instances': num_instances,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'windmod.html', context=context)

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    rec_meteo = MeteoRecord.objects.all().values()
    rec_wind = WindRecord.objects.all().values()

    context = {
        'records': rec_meteo[0],

        'rec_meteo': rec_meteo[0],
        'rec_wind': rec_wind[0],
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
