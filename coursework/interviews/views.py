from django.shortcuts import render

# Create your views here.

def interview(request):
    return render(request, 'interviews/interview.html')

def cakeboy(request):
    return render(request, 'interviews/CAKEBOYinterview.html')

def jeembo(request):
    return render(request, 'interviews/JEEMBOinterview.html')