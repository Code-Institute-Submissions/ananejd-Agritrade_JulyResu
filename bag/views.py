from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ bag contents page rendered """

    return render(request, 'bag/bag.html')