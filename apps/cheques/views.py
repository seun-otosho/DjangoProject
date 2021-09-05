from django.shortcuts import render


# Create your views here.

def display_cheques(request):
    # institutions = Institution.objects.all()
    return render(
        request, 'display_cheques.html',
        # {'institutions': institutions},
    )
