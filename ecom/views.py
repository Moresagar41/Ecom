from django.http import HttpResponse
from django.shortcuts import render
import datetime 

def about_page(request):
  msg = "We are a training institute for data science"
  return render(request,"home_page.html",{'msg':msg})

def contact_page(request):
  
  return render(request,"contact_us.html")

def home_page(request):
  data={}
  currentTime = datetime.datetime.now().hour
  if 4 < currentTime < 12:
    data['msg'] = "Good Morning"
  elif 12 <= currentTime < 16:
    data['msg'] = "Good Afternoon"
  elif 16 <= currentTime < 20:
    data['msg'] = "Good Evening"
  else:
    data['msg']="Time to sleep Good Night"
  print(data['msg'])

  data['lst']=['Corona','plauge','xyz']


   
   
  return render(request,"home_page.html",data)

def helloworld(request): 
    return HttpResponse("Hello Class")

def home(request):

    _html = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1 class=text-center>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>"""

    return HttpResponse(_html)