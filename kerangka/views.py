from django.shortcuts import render, redirect
from kerangka.forms import CreateUserForm
import logging
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, CustomPasswordChangeForm

logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    logger.info("Home view accessed")
    return render(request, 'Home.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {form.cleaned_data["username"]}')

            return redirect('home')

    context = {'form' :form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'home.html', context)

def profilePage(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to log in to view your profile.")
        return redirect('login')

    # Ambil profil pengguna yang sedang login (dari UserProfile)
    profile = UserProfile.objects.filter(user=request.user).first()

    context = {
        'user': request.user,
        'profile': profile  # Tambahkan profil pengguna ke context
    }
    return render(request, 'accounts/profile.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def edit_profile_view(request):
    # Ambil profil pengguna terkait
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def update_user_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect('update_profile')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'accounts/update_profile.html', {
        'user_form': user_form,
        'password_form': password_form,
    })

