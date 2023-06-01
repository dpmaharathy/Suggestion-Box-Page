from django.shortcuts import render,redirect
from .models import Suggestion
# Create your views here.
 
def suggestion_form(request):
    if request.method=='POST':
        employee_id = request.POST['employee_id']
        suggestion = request.POST['suggestion']
        resolution = request.POST['resolution']
        Suggestion.objects.create(employee_id=employee_id,suggestion=suggestion,resolution=resolution)
        return redirect('thank_you')
    
    return render(request,'suggestion_form.html')


def suggestion_table(request):
    suggestions = Suggestion.objects.all()
    print(suggestions)
    return render(request,'suggestion_table.html',{'suggestion':suggestions})

def thank_you(request):
    return render(request,'thank_you.html')
