from django.shortcuts import render


# Create your views here.

def display_facilities(request):
    # institutions = Institution.objects.all()
    return render(
        request, 'display_facilities.html',
        # {'institutions': institutions},
    )
