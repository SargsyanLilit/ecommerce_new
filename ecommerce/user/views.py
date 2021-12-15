from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from orders.models import Orders
from .forms import UserRegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


#@login_required
def profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    orders = Orders.objects.filter(user_id=request.user.id)
    context = {
        'profile': profile,
        'orders_list': orders,

    }
    return render(request, 'user/profile.html', context=context)

