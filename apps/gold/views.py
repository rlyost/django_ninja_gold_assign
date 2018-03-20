from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'your_gold' not in request.session:
        request.session['your_gold'] = 0
        request.session['activities'] = []
        request.session['temp'] = 0
        request.session['newline'] = -1
    return render(request, 'gold/index.html')

def process_money(request):
    if request.method == "POST":
        request.session['newline'] += 1
        if request.POST['building'] == 'farm':
            request.session['temp'] = random.randrange(10, 21)
            request.session['your_gold'] += request.session['temp'] 
            temp2 = "<div class='green'>Earned ", str(request.session['temp']), " golds from the farm!    ", strftime("%Y-%m-%d %H:%M:%S", gmtime()), "</div>"
            temp3 = "".join(temp2)
            request.session['activities'].append(temp3)
        elif request.POST['building'] == 'cave':
            request.session['temp'] = random.randrange(5, 11)
            request.session['your_gold'] += request.session['temp']
            temp2 = "<div class='green'>Earned ",str(request.session['temp'])," golds from the cave!   ", strftime("%Y-%m-%d %H:%M:%S", gmtime()), "</div>"
            temp3 = "".join(temp2)
            request.session['activities'].append(temp3)
        elif request.POST['building'] == 'house':
            request.session['temp'] = random.randrange(2, 6)
            request.session['your_gold'] += request.session['temp']
            temp2 = "<div class='green'>Earned ",str(request.session['temp'])," golds from the house!   ", strftime("%Y-%m-%d %H:%M:%S", gmtime()), "</div>"
            temp3 = "".join(temp2)
            request.session['activities'].append(temp3)
        elif request.POST['building'] == 'casino':
            request.session['temp'] = random.randrange(0, 101)-50
            request.session['your_gold'] += request.session['temp']
            if request.session['temp'] > 0:
                temp2 = "<div class='green'>Earned ",str(request.session['temp'])," golds from the casino!   ", strftime("%Y-%m-%d %H:%M:%S", gmtime()), "</div>"
                temp3 = "".join(temp2)
                request.session['activities'].append(temp3)
            else:
                temp2 = "<div class='red'>Entered a casino and lost ",str(-request.session['temp']),".....Ouch! ", strftime("%Y-%m-%d %H:%M:%S", gmtime()), "</div>"
                temp3 = "".join(temp2)
                request.session['activities'].append(temp3)    
    return redirect("/")

def reset(request):
    # reset the gold and activities redirect to the home page
    request.session['your_gold'] = 0
    request.session['activities'] = []
    request.session['newline'] = -1
    return redirect('/')