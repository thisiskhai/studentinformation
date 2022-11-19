from django.shortcuts import render, redirect
from .models import Forming
from .forms import ListingForm

# Create your views here.

#Add new information
def create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "addNew.html", context)
# Show information
def show(request):
    formings = Forming.objects.all()
    context = {
        'formings': formings
    }
    return render(request, 'show.html', context)
# Show details
def detail(request, pk):
    forming = Forming.objects.get(id = pk)
    context = {
        'forming': forming
    }
    return render(request, 'showDetail.html', context)
# Delete object
def deleteInfo(request, pk):
    forming = Forming.objects.get(id=pk)
    forming.delete()
    return redirect("/")

#Update information
def update(request, pk):
    forming = Forming.objects.get(id=pk)
    form = ListingForm(instance=forming)


    if request.method == "POST":
        form = ListingForm(request.POST, instance=forming)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "update.html", context) 