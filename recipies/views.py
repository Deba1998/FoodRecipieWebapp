from django.shortcuts import render, HttpResponse,redirect
from matplotlib.style import context
from numpy import require
from .models import Recipedetails
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from random import randint
from django.db.models import Q
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm
# from .filters import OrderFilter
# Create your views here.
def index(request):
	allrecipies=Recipedetails.objects.all()
	context={'recipies':allrecipies}
	return render(request,'index.html',context)

def registerUser(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			print(request.POST)
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
		context = {'form':form}
		return render(request, 'register.html', context)

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				print("logged in invoked")
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'login.html', context)
def logoutUser(request):  
	logout(request)
	return redirect('login')
	
def viewdetails(request,pk):
	recipie=Recipedetails.objects.get(pk=pk)
	context={'recipie':recipie}
	return render(request,'viewdetails.html',context)
@login_required(login_url='login')
def editdetails(request,pk):
	recipie=Recipedetails.objects.get(pk=pk)
	context={'recipie':recipie}
	if request.method=="POST":
		recipie.name=request.POST.get('name')
		recipie.desc=request.POST.get('desc')
		recipie.ingredients=request.POST.get('ingredients')
		recipie.instructions=request.POST.get('instructions')
		recipie.save()
		messages.success(request, 'Recipie details updated successfully!')
	return render(request,'editdetails.html',context)
@login_required(login_url='login')
def adddetails(request):
	folder='static/'
	recipie=Recipedetails()
	if request.method=="POST":
		recipie.name=request.POST.get('name')
		recipie.desc=request.POST.get('desc')
		recipie.ingredients=request.POST.get('ingredients')
		recipie.instructions=request.POST.get('instructions')
		stri=""
		for i in range(10):
			val=randint(0, 9)
			stri=stri+str(val)
		recipie.prikey=stri
		recipie.save()
		myfile = request.FILES['upload']
		myfile.name=stri+".jpg"
		fs = FileSystemStorage(location=folder)   
		filename = fs.save(myfile.name, myfile)
		messages.success(request, 'Recipie details updated successfully!')
	return render(request,'adddetails.html')
def searchBar(request):
	if request.method == 'GET':
		query = request.GET.get('query')
		if query:
			products = Recipedetails.objects.filter(Q(name__contains=query)|Q(ingredients__contains=query))
			return render(request, 'searchbar.html', {'products':products})
		else:
			print("No information to show")
			return render(request, 'searchbar.html', {})
@login_required(login_url='login')
def deldetails(request,pk):
	recipie=Recipedetails.objects.get(pk=pk)
	recipie.delete()
	return redirect('index')