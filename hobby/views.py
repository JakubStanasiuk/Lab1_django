from django.shortcuts import render

def home(request):
    context = {
        'hobby_name': 'Programowanie',
        'description': 'Moim hobby jest programowanie. Lubię tworzyć strony internetowe, aplikacje i poznawać nowe technologie.'
    }
    return render(request, 'hobby/home.html', context)

def about(request):
    return render(request, 'hobby/about.html')

def gallery(request):
    return render(request, 'hobby/gallery.html')
