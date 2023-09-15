from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('login_view')
        else:
            # Handle authentication failure, e.g., show an error message
            return render(request, 'auth_social/login.html', {'error_message': 'Invalid login credentials'})

    else:
        # Display the login form
        return render(request, 'auth_social/login.html')


@login_required
def home(request):
    return render(request, 'auth_social/home.html')
