from django.shortcuts import render,get_object_or_404,redirect
from .models import Meeting,Room
from .forms import MeetingForm

# Create your views here.
def detail(request, id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request,"meetings/detail.html",{"meeting": meeting})

def room(request):
    rooms = Room.objects.all()
    return render(request,"meetings/rooms_list.html",{"rooms":rooms}) 

#MeetingForm is a class based on modelform provided by django
#in this method we have to pass the model Meeting and 
# exclude will continue the list of attributes we do not want to show 
# in the form while creating a new meeting
#MeetingForm = modelform_factory(Meeting,exclude=[])
def add_meetings(request):
    if request.method == "POST":
        #form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else :
        form = MeetingForm()

    return render(request,"meetings/add_meetings.html",{"form" : form})
