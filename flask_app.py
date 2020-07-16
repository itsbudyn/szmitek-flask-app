
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
from random import choice

app = Flask(__name__)

#####
obj,cel=[],[]
count1,count2=0,0

try:
    f=open("wyrazy_a.txt","r",encoding="utf-8")
    lines=f.read().splitlines()
    for i in lines:
        obj.append(i)
        count1+=1 # a czemu nie, pochwalmy się ile mamy słówek
    f.close()
except:
    print("Błąd w odczytywaniu wyrazów z grupy A. Sprawdź stan pliku wyrazy_a.txt")
    exit()

# Tutaj wczytujemy plik wyrazy_b.txt
try:
    f=open("wyrazy_b.txt","r",encoding="utf-8")
    lines=f.read().splitlines()
    for i in lines:
        cel.append(i)
        count2+=1 # tu to samo, potem to dodamy do siebie i będzie jedna super liczba
    f.close()
except:
    print("Błąd w odczytywaniu wyrazów z grupy B. Sprawdź stan pliku wyrazy_b.txt")
    exit()

def szmitekfy(arr1,arr2):
    return str(choice(arr1)+str(" w ")+choice(arr2))

print("Załadowano",(count1+count2),"wyrazów")
print("A:",count1)
print("B:",count2)
#####

@app.route('/', methods=["GET","POST"])
def hello_world():
    return render_template("home.html", test="Naciśnij przycisk poniżej, aby wygenerować tekst.", wyrazy=count1+count2, wyr1=count1, wyr2=count2)

@app.route('/generate', methods=["GET","POST"])
def generate():
    if request.method=="POST":
        if request.form["submit_button"]=="Generuj":
            pass
        return render_template("home.html", test=szmitekfy(obj,cel), wyrazy=count1+count2, wyr1=count1, wyr2=count2)

@app.route('/about')
def about():
    return render_template("about.html", wyrazy=count1+count2, wyr1=count1, wyr2=count2)
    

if __name__=="__main__":
    app.run(debug=True)