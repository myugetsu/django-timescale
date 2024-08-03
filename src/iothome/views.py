from django.shortcuts import render

def home_view(request):
  return render(request, "home.html", {})

def nodes_view(request):
  return render(request, "nodes.html", {})
