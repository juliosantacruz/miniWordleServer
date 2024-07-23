from django.shortcuts import render
 
 
 

 

def HomeView(request):
    context={}
    return render(request, 'home.html', context)