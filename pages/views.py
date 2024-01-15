from django.shortcuts import render
from members.models import Bio

# Create your views here.


def index(request):
    profs = Bio.objects.filter(position=1)
    context = {
        'profs': profs,
        'total': len(profs)
        }
    return render(request, 'pages/index.html', context)

def serendipity(request):

    context = {}
    return render(request, 'pages/serendipity.html', context)