from django.shortcuts import render

def SinglePage(request):
    return render(
        request,
        'SinglePage/SinglePage.html'
    )


# Create your views here.
