from django.shortcuts import redirect, render, HttpResponseRedirect
from Join.forms import Form
from Join.models import Join

# Create your views here.
import time


def success(request):
    if(time.sleep(5)):
        return HttpResponseRedirect("/home/")
    return render(request, 'success.html')


def JoinNow(request):
    my_form = Form()
    if request.method == 'POST':
        my_form = Form(request.POST)
        if my_form.is_valid():
            my_form.cleaned_data
            Join.objects.create(**my_form.cleaned_data)
            my_form = Form(request.GET)
            return redirect('/success/')
    context = {
        "form": my_form
    }
    return render(request, 'join.html', context)
