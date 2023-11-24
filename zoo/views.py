from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from zoo.forms import *
from zoo.models import *
from django.contrib import messages
from pyexpat.errors import messages


# Create your views here.

#base function
def home(request):
    return render(request, 'home.html')

def home_login(request):
    return render(request, 'login/home_login.html')

def login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            return redirect('home_login')   
        else:
            return render(request, 'login/login.html', {'error': 'Invalid username or password'})

    return render(request, 'login/login.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'login/registration.html', {'form': form})




#building's function
def building(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = BuildingForm(request.POST)
        # Check whether it's valid:
        if form.is_valid(): 
            return HttpResponseRedirect('/success/')
    else:
        form = BuildingForm()
    context = {
        'form': form,
    }
    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'building/building.html', context)

def insert_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_building') 
        else:
            # If the form is not valid, re-render the page with the form
            return render(request, 'building/insert_building.html', {'form': form})
    else:
        form = BuildingForm()
        return render(request, 'building/insert_building.html', {'form': form})

def select_building(request):
    buildings = Building.objects.all()
    context = {
        'buildings': buildings
    }
    return render(request, 'building/select_building.html', context)

def view_building(request):
    buildings = Building.objects.all()
    context = {'buildings': buildings}
    return render(request, 'building/view_building.html', context)

def update_building(request, building_id):
    building_obj = get_object_or_404(Building, id=building_id)

    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=building_obj)

        print("Form valid status:", form.is_valid())  # Check if the form is valid
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Building updated successfully.")
                return redirect('view_building')
            except Exception as e:
                # Log the error
                print("Error saving form:", e)
                messages.error(request, "Error updating building.")
        else:
            # Form is not valid, print errors and render form with errors
            print("Form errors:", form.errors)
            return render(request, 'building/update_building.html', {'form': form})

    else:
        # For a GET request, show the form with the building's current data
        form = BuildingForm(instance=building_obj)
        return render(request, 'building/update_building.html', {'form': form})

def building_action(request):
    building_id = request.POST.get('building_id')
    action = request.POST.get('action')

    if action == 'delete':
       building = get_object_or_404(Building, pk=building_id)
       building.delete()
       return redirect('view_building')
       
    elif action == 'update':
        return redirect(update_building)





#enclosure's function
def enclosure(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = EnclosureForm(request.POST)
        # Check whether it's valid:
        if form.is_valid(): 
            return HttpResponseRedirect('/success/')
    else:
        form = EnclosureForm()
    context = {
        'form': form,
    }
    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'enclosure/enclosure.html', context)


def select_enclosure(request):
    enclosure = Enclosure.objects.all()
    context = {'enclosure': enclosure}
    return render(request, 'enclosure/select_enclosure.html', context)

def view_enclosure(request):
    enclosure = Enclosure.objects.all()
    context = {'enclosure': enclosure}
    return render(request, 'enclosure/view_enclosure.html', context)

def insert_enclosure(request):
    # If the form is submitted
    if request.method == 'POST':
        # Retrieve form data
        square_foot = request.POST.get('square_foot')
        building_id = request.POST.get('building_id')
        
        if square_foot and building_id:
            try:
                building = Building.objects.get(id=building_id)
                new_enclosure = Enclosure(square_foot=square_foot, building_id=building)
                new_enclosure.save()
                # Redirect to a new URL after saving
                return redirect(reverse('view_enclosure'))
            except Building.DoesNotExist:
                # Handle the error if Building with building_id does not exist
                pass 
        else:
            # If the form is not valid, re-render the page with the form
            return render(request, 'enclosure/insert_enclosure.html', {'buildings': buildings})  
   
    buildings = Building.objects.all()  
    return render(request, 'enclosure/insert_enclosure.html', {'buildings': buildings})

def update_enclosure(request, enclosure_id):
    enclosure_obj = get_object_or_404(Enclosure, id=enclosure_id)

    if request.method == 'POST':
        form = EnclosureForm(request.POST, instance=enclosure_obj)

        print("Form valid status:", form.is_valid())  # Check if the form is valid
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Enclosure updated successfully.")
                return redirect('view_enclosure')
            except Exception as e:
                # Log the error
                print("Error saving form:", e)
                messages.error(request, "Error updating enclosure.")
        else:
            # Form is not valid, print errors and render form with errors
            print("Form errors:", form.errors)
            return render(request, 'enclosure/update_enclosure.html', {'form': form})

    else:
        # For a GET request, show the form with the enclosure's current data
        form = EnclosureForm(instance=enclosure_obj)
        return render(request, 'enclosure/update_enclosure.html', {'form': form})
    
def enclosure_action(request):
    enclosure_id = request.POST.get('enclosure_id')
    action = request.POST.get('action')

    if action == 'delete':
       enclosure = get_object_or_404(Enclosure, pk=enclosure_id)
       enclosure.delete()
       return redirect('view_enclosure')
       
    elif action == 'update':
        return redirect(update_enclosure)
    
    


    
    
def zoo_action(request):
    action = request.POST.get('action')
    
    if action == 'building':
        return building(request)
    
    elif action == 'enclosure':
        return enclosure(request)