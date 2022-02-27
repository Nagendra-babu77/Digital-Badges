from django.shortcuts import render,redirect
from .models import *
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework import status
import json
import os
from rest_framework.permissions import AllowAny
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import MultipleObjectsReturned,ObjectDoesNotExist
# Create your views here.

def index(request):
	return render(request,'index.html')

@api_view()
@permission_classes([AllowAny])
def check_student_eligibilty(request):
	try:
		Name=request.query_params['name']
		Email=request.query_params['email']
		badge=Badge_Details.objects.get(Name=Name)
		eligible_students=badge.Eligible_students
		for s in eligible_students:
			if s==Email:
				img=badge.Image
				return JsonResponse({'status_code':200,'image':img.url})
		return JsonResponse({"status_code":403,"message":"Not Eligible!"})
	except MultiValueDictKeyError:
		return JsonResponse({"status_code":403,"message":"Key Parameter is Wrong!"})
	except MultipleObjectsReturned:
		return JsonResponse({"status_code":403,"message":"Duplicate Badge Name Presented!"})
	except ObjectDoesNotExist:
		return JsonResponse({"status_code":403,"message":"Badge Name doesn't exist!"})
	

	

def upload_badge(request):
	if request.method=="POST" and request.FILES['file']:
		#save badge
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

def badges_list(request):
	badges=list(Badge_Details.objects.values())
	#Update badge
	if request.method=="POST":
		badge_id=request.POST.get('badge_id')
		badge_details=Badge_Details.objects.get(id=badge_id)
		badge_details.Name=request.POST.get('Name')
		badge_details.Description=request.POST.get('Description')
		try:
			if request.FILES['file']:
				new_img=request.FILES['file']

				# deleting old uploaded image.
				oldimage_path = badge_details.Image.path
				if os.path.exists(oldimage_path):
					os.remove(oldimage_path)

				badge_details.Image=new_img
		except:
			pass
		students=request.POST.get('students')
		eligible_students=students.split(",")
		badge_details.Eligible_students=eligible_students
		
		badge_details.save()
		return redirect('badges_list')
	return render(request,'badges_list.html',{'badges':badges})

@api_view(['GET'])
def get_badge(request,pk):
	try:
		badge=Badge_Details.objects.get(id=pk)
		d={}
		data=[]
		d['id']=badge.id
		d['Name']=badge.Name
		d['Description']=badge.Description
		Eligible_students=badge.Eligible_students
		students=""
		for s in Eligible_students:
			students+=s+","
		d['students']=students[:-1]
		d['Image_url']=badge.Image.url
		data.append(d)
		return JsonResponse({"status":200, "message": "success", "data": data}, status=status.HTTP_200_OK)
   
	except Exception as e:
		return JsonResponse({"status":500, "message": json.dumps({
			"error": str(e)
		})}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def delete_badge(request,pk):
	badge=Badge_Details.objects.get(id=pk)
	badge.delete()
	return redirect("badges_list")