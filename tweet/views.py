from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm ,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# View for the home page 
def index(request):
    return render(request, 'index.html')

# View to list all tweets, ordered by creation date
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-create_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

# View to create a new tweet
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # Associate the tweet with the logged-in user
            tweet.save()  # Save to the database
            return redirect('tweet_list')  # Redirect to the tweet list view
    else:
        form = TweetForm()  # Create a blank form for GET request
    return render(request, 'tweet_form.html', {'form': form})

# View to edit an existing tweet
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Ensure the tweet belongs to the logged-in user
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()  # Save the edited tweet
            return redirect('tweet_list')  # Redirect to tweet list after successful edit
    else:
        form = TweetForm(instance=tweet)  # Pre-populate the form with the existing tweet data
    return render(request, 'tweet_form.html', {'form': form})

# View to delete a tweet
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Ensure the tweet belongs to the logged-in user
    if request.method == 'POST':
        tweet.delete()  # Delete the tweet
        return redirect('tweet_list')  # Redirect to tweet list after deletion
    return render(request, 'tweet_conform_delete.html', {'tweet': tweet})  # Render delete confirmation page

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
            
    else:
        form=UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})  # Render delete confirmation page

    
    