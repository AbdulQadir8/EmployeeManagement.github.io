from django.http import HttpResponse
import datetime
from django.shortcuts import render
def home(request):
    isActive=True
    if request.method=="POST":
        check=request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True

   
    date = datetime.datetime.now()
    isActive=True
    name="Abdul Qadar"
    list_of_programs=["wac to program calculator",
                      "wac to program game",
                      "wac to program website",]
    student_data={"student_name":"Usama Khan",
             "student_city":"Lahore",
             "university":"UOL",
             "Program":"Bs Physics"}
    # return HttpResponse("<h1>Hellow this is index page</h2>"+str(date))
    data={
        'date':date,
        "name":name,
        'isActive':isActive,
        'list_of_programs':list_of_programs,
        'student_data':student_data
    }
    return render(request,"home.html",data)

def about(request):
    print("about function is called from view")
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html",{}) 

def services(request):
    print("This is Services page")
    # return HttpResponse("<h1>This is Services page</h1>")
    return render(request,"services.html")