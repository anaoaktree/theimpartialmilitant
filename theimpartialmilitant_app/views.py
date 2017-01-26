from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'project_name_app/index.html', {})
