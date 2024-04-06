from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Customer
from django.contrib.auth.password_validation import validate_password

# Create your views here.
# Create your views here.
def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords Do Not Match!')
            return render(request, 'register.html')
        
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, '\n'.join(e.messages))
            return render(request, 'register.html')

        try:
            user = User.objects.create_user(username=email, 
                                            first_name=first_name, 
                                            last_name=last_name, 
                                            email=email, 
                                            password=password)
            customer = Customer.objects.create(user = user,
                                               first_name=first_name,
                                               last_name=last_name,
                                               email=email,
                                               phone_no=phone_no,
                                               password=password)
            user = authenticate(username=email, password=password)
            login(request, user)
            messages.success(request, 'Your Account Has Been Registered Successfully!')
            return redi
        except Exception as e:
            messages.error(request, 'Account Was Not Created! Try Again')
            return render(request, 'register.html')
    return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('index')  # Change 'index' to your desired redirect URL after login
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
            return render(request, 'login.html')  # Change 'login.html' to your login template path
    return render(request, 'login.html')  # Change 'login.html' to your login template path