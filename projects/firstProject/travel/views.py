from django.shortcuts import render
from django.http import HttpResponse
from .models import destinations

dests = []

# Create your views here.
def index(request):

    # destManali = destinations()
    # destManali.name = 'Manali'
    # destManali.image = 'DestManali.JPG'
    # destManali.price = 6000
    # destManali.desc = 'Honeymoon Destination'
    # destManali.offer = False
    #
    # destSikkim = destinations()
    # destSikkim.name = 'Sikkim'
    # destSikkim.image = 'destSikkim.JPG'
    # destSikkim.price = 7000
    # destSikkim.desc = 'Explore Incredible North East India'
    # destSikkim.offer = True
    #
    # destShillong = destinations()
    # destShillong.name = 'Shillong'
    # destShillong.image = 'destShillong.JPG'
    # destShillong.price = 10000
    # destShillong.desc = 'Explore Cleanest Village, cleanest lakes in the country'
    # destShillong.offer = False

    # dests = [destManali,destSikkim,destShillong]

    globals()['dests'] = destinations.objects.all()

    return render(request,'index.html',{'dests': dests})

def Jaipur(request):
    return render(request,'Jaipur.html')