from django.shortcuts import render

# Create your views here.


def landing_view(request):
    return render(request, "landing-page.html")
