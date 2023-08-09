from django.shortcuts import render

context = {"text": "Home Page Ok !", "title": "Home 💡"}


# Create your views here.
def home(request):
    return render(request, "home/index.html", context)
