from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406425804',
        'name': 'Mohammad Aly Haidarulloh',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)