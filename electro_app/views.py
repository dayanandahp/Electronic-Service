from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    #create api for contact
    #display the reviews in index page
    return render(request, 'index.html')

def bookings(request):
    #create api for booking form
    return render(request, 'bookings.html')

def appointment(request):
    #create api for displaying appointments/bookings
    return render(request, 'appointment.html')

def logins(request):
    return render(request, 'logins.html')

def regs(request):
    return render(request, 'reg.html')

def show(request, ID):
    #create api for displaying each appointment in details
    return render(request, 'show.html')

def delete_items(request, ID):
    #create api for deleting booking items
    return redirect('/appointment')

def logoutuser(request):
    return redirect('/')

def reviews(request):
    #create api for review form which is in index page
    return redirect('/')
    
def delete_reviews(request, ID):
    #create api for deleting reviews
    return redirect('/')

def subscrib(request):
    #create api for subscrib form which is in index page
    return redirect('/')