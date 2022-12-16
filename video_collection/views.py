from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm, SearchForm
from django.contrib import messages 
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models.functions import Lower

# Home page view function
def home(request):
    app_name = 'Exercise Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

# View function for adding a new video
def add(request):
    if request.method == 'POST':   # adding a new video
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                # Save the new Video object to the database
                new_video_form.save()   
                return redirect('video_list')
            except IntegrityError:
                # Display a warning message if the video already exists
                messages.warning(request, 'You already added that video')
            except ValidationError:
                # Display a warning message if the URL is invalid
                messages.warning(request, 'Invalid YouTube URL')
        
        # Invalid form 
        messages.warning(request, 'Check the data entered')
        # Render the form with the invalid data
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form}) 
            
    # GET request, render an empty form    
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form}) 
    
# View function for displaying a list of videos
def video_list(request):

    # Create a form instance from GET data
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        # Filter the videos by the search term and order the list by name
        search_term = search_form.cleaned_data['search_term']
        videos = Video.objects.filter(name__icontains=search_term).order_by(Lower('name'))

    else:
        # Invalid form, create an empty form
        search_form = SearchForm()
        # Get all videos ordered by name
        videos = Video.objects.order_by(Lower('name'))

    return render(request, 'video_collection/video_list.html', {'videos': videos, 'search_form': search_form})

