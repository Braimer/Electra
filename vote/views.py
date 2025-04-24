from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import RegisterForm, LoginForm
from .models import Candidate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy

# Register View
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('vote')  # Redirect to voting page after registration
        return render(request, 'register.html', {'form': form})

# Custom Login View
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('vote')  # Redirect to vote page after login

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out

# Voting View
'''@login_required
def vote_view(request):
    # Check if the user has already voted
    if request.user.has_voted:
        return redirect('results')  # Redirect to results if user has voted already

    candidates = Candidate.objects.all()

    if request.method == 'POST':
        selected_candidate_id = request.POST.get('candidate')
        selected_candidate = Candidate.objects.get(id=selected_candidate_id)

        # Update the vote count
        selected_candidate.votes += 1
        selected_candidate.save()

        # Mark user as voted
        request.user.has_voted = True
        request.user.save()

        return redirect('results')  # Redirect to results after voting

    return render(request, 'vote.html', {'candidates': candidates})'''

# Results View
@login_required
def results_view(request):
    candidates = Candidate.objects.all().order_by('-votes')  # Optional: order by highest votes
    return render(request, 'results.html', {'candidates': candidates})


@login_required
def vote_view(request):
    user = request.user

    if user.has_voted:
        return render(request, 'vote.html', {
            'has_voted': True,
            'candidates': [],  # or you can skip it
        })

    candidates = Candidate.objects.all()

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        try:
            candidate = Candidate.objects.get(id=candidate_id)
            candidate.votes += 1
            candidate.save()

            user.has_voted = True
            user.save()

            return redirect('results')  # make sure results page exists
        except Candidate.DoesNotExist:
            pass  # optionally show error

    return render(request, 'vote.html', {
        'candidates': candidates,
        'has_voted': False,
    })
