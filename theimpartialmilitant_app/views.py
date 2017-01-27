from django.shortcuts import render
from scripts import parliament_data as p

# Create your views here.
def index(request):
    context = {
    "issues":p.get_data()
    }
    return render(request, 'theimpartialmilitant_app/index.html', context)
