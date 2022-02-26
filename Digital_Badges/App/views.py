from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
	return render(request,'index.html')

def upload_badge(request):
	if request.method=="POST" and request.FILES['file']:
		badge_details=Badge_Details()
		badge_details.Name=request.POST.get('Name')
		badge_details.Description=request.POST.get('Description')
		badge_details.Image=request.FILES['file']

		students=request.POST.get('students')
		eligible_students=students.split(",")
		badge_details.Eligible_students=eligible_students
		
		badge_details.save()
		return redirect('index')
	return render(request,'upload_badge.html')