from django.shortcuts import render, redirect
from settings.models import Settings
# Create your views here.

def index(request):
    try:
        setting = Settings.objects.latest("id")
    except:
        return redirect("no_settings")
    context = {
        "setting": setting,
    }
    return render(request, "index.html", context)

