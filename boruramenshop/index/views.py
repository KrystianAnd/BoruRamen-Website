from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def menu(request):
    return render(request, 'menu.html')

def PolitykaStrony(request):
    return render(request, 'polityka_strony.html')