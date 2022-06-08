from django.shortcuts import render

def SinglePage(request):
    return render(
        request,
        'SinglePage/SinglePage.html'
    )

def SinglePage2(request):
    return render(
        request,
        'SinglePage/SinglePage2.html'
    )


def SinglePage3(request):
    return render(
        request,
        'SinglePage/SinglePage3.html'
    )


# Create your views here.
