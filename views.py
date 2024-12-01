from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def game(request, pk):
    URL = 'https://www.mufcinfo.com/manupag/100_club/100_club.html'
    
    # class list set 
    class_list = set() 
    
    # Page content from Website URL 
    page = requests.get( URL ) 
    
    # parse html content 
    soup = BeautifulSoup( page.content , 'html.parser') 

    nameclass = soup.find_all(class_="data_fields_left")
    allclass = soup.find_all(class_="data_fields")

    all_name = []
    all_class = []

    i = 0 
    j = 0

    everything = []

    for x in range(len(nameclass)):
        all_name.append(nameclass[x].text.strip())

    for y in allclass:
        all_class.append(y.text.strip())

    for z in range(round(len(all_class)/7)):
        mylist = []
        mylist.append(all_name[j])
        mylist.append(all_class[i+3])
        mylist.append(all_class[i+4])
        goals = str(round(eval(all_class[i+5]) * eval(all_class[i+6])))
        mylist.append(goals)
        everything.append(mylist)
        j+=1
        i+=7

    context = {'a':everything[pk][0],
                'b':everything[pk][1],
                'c':everything[pk][2],
                'd':everything[pk][3],
                'e':pk+1}

    return render(request, 'myapp/game.html', context)

def index(request):
    return render(request, 'myapp/index.html')