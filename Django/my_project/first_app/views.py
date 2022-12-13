from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    my_dict = {'insert_me': "now this is ok"}
    return render(request,'author-polls/index.html', context =my_dict)
