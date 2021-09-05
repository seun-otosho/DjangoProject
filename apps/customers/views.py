from django.shortcuts import render

# Create your views here.


def display_customers(request):
    # institutions = Institution.objects.all()

    if request.META.get("HTTP_HX_REQUEST") != 'true':
        return render(request, 'display_customers_full.html')

    return render(
        request, 'display_customers.html',
        # {'institutions': institutions},
    )
