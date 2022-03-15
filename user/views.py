from django.shortcuts import render
from .forms import UserForm
from .models import Contact
# Create your views here.
def index(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST or None)
        if form.is_valid():
           form.save()
           print(form)
    ctx = {
        'forms':form

    }
    return render(request,'index.html',ctx)