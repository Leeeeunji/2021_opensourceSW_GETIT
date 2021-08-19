from django.shortcuts import render, redirect, get_object_or_404
from .models import mentor

def main(request):
    return render(request, 'main.html')