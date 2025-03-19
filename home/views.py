from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # ✅ Use a LIST of dictionaries instead of a SET
    peoples = [
        {'name': 'Anees', 'age': 26},
        {'name': 'Ali', 'age': 24},
        {'name': 'Ahmad', 'age': 29},
        {'name': 'Saboor', 'age': 52},
        {'name': 'Sameen', 'age': 58},
    ]
    
    for people in peoples:
        print(peoples)
    
    # ✅ Correct context dictionary
    return render(request, "home/index.html", context={'peoples': peoples})

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> This is a success page</h1>")
