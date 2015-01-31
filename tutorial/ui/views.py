from django.shortcuts import render

def index(request):
    return render(request, 'ui/index.html')
def results(request):
    return render(request, 'ui/results.html')
