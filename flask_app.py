from flask import Flask, render_template, request
from random import choice

#STATISTICS.TXT SPIS TREŚCI
#0 - KLIKNIĘĆ (GENERUJ)/UŻYĆ SZMITEKFY()

app = Flask(__name__)

obj,cel=[],[]
count1,count2=0,0
generations=0

try:
    f=open("wyrazy_a.txt","r",encoding="utf-8")
    lines=f.read().splitlines()
    for i in lines:
        obj.append(i)
        count1+=1
    f.close()
except:
    print("Błąd w odczytywaniu wyrazów z grupy A. Sprawdź stan pliku wyrazy_a.txt")
    exit()

try:
    f=open("wyrazy_b.txt","r",encoding="utf-8")
    lines=f.read().splitlines()
    for i in lines:
        cel.append(i)
        count2+=1
    f.close()
except:
    print("Błąd w odczytywaniu wyrazów z grupy B. Sprawdź stan pliku wyrazy_b.txt")
    exit()

def getstats():
    try:
        f=open("statistics.txt","r",encoding="utf-8")
        lines=f.read().splitlines()
        generations=int(lines[0])
        f.close()
    except:
        print("Błąd w odczytywaniu statystyk. Sprawdź stan pliku statistics.txt")
        exit()
    
    return generations

def szmitekfy(arr1,arr2,generations):
    try:
        generations+=1
        f=open("statistics.txt","w",encoding="utf-8")
        f.write(str(generations))
        f.close()
    except:
        print("Błąd w odczytywaniu statystyk. Sprawdź stan pliku statistics.txt")
        exit()

    return str(choice(arr1)+str(" w ")+choice(arr2))

print("Załadowano",(count1+count2),"wyrazów")
print("A:",count1)
print("B:",count2)

@app.route('/', methods=["GET","POST"])
def hello_world():
    return render_template("home.html", test="Naciśnij przycisk poniżej, aby wygenerować tekst.", wyrazy=count1+count2, wyr1=count1, wyr2=count2, komb=count1*count2, total=getstats())

@app.route('/generate', methods=["GET","POST"])
def generate():
    if request.method=="POST":
        if request.form["submit_button"]=="Generuj":
            pass
        return render_template("home.html", test=szmitekfy(obj,cel,getstats()), wyrazy=count1+count2, wyr1=count1, wyr2=count2, komb=count1*count2, total=getstats())

@app.route('/about')
def about():
    return render_template("about.html", wyrazy=count1+count2, wyr1=count1, wyr2=count2, komb=count1*count2)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__=="__main__":
    app.run(debug=False)