from django.shortcuts import render

# Create your views here.

def professors(request):
    return render(request, 'members/professors.html')