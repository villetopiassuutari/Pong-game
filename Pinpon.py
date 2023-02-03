#Käytän apunani pythonin turtle-kirjastoa, kutsutaan sitä alussa
import turtle

#Luodaan ensin alusta/ikkuna, johon aletaan lisäämään tavaraa
#Annetaan ikkunalle myös nimi
wn = turtle.Screen()
wn.title("Pong-peli")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Annetaan pistetilanteeksi alussa 0-0
score_a = 0
score_b = 0
avot = []
bvot = []
voitot = {}
p = 0
m = 0


#Luodaan näytölle vasemmanpuoleinen "maila"
maila_a = turtle.Turtle()
maila_a.speed(0)
maila_a.shape("square")
maila_a.color("white")
maila_a.shapesize(stretch_wid=5, stretch_len=1)
maila_a.penup()
maila_a.goto(-350, 0)

#Vastaavasti luodaan oikeanpuoleinen "maila"
maila_b = turtle.Turtle()
maila_b.speed(0)
maila_b.shape("square")
maila_b.color("red")
maila_b.shapesize(stretch_wid=5, stretch_len=1)
maila_b.penup()
maila_b.goto(350, 0)

#Luodaan näytön keskelle pallo, jolla peliä pelataan
#Annetaan pallolle myös nopeus x- ja y-koordinaatin suhteen, jolla se tulee liikkumaan
pallo = turtle.Turtle()
pallo.speed(0)
pallo.shape("circle")
pallo.color("white")
pallo.penup()
pallo.goto(0, 0)
pallo.dx = 0.13
pallo.dy = 0.13

#Luodaan teksti, joka näyttää pelitilanteen kahden pelaajan välillä
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pelaaja A: 0 Pelaaja B: 0", align="center", font=("Arial", 24, "bold"))


#Kirjoitetaan funktiot, joilla voidaan liikuttaa molempia mailoja y-akselilla
def maila_a_ylos():
    y = maila_a.ycor()
    y += 30
    maila_a.sety(y)


def maila_a_alas():
    y = maila_a.ycor()
    y -= 30
    maila_a.sety(y)


def maila_b_ylos():
    y = maila_b.ycor()
    y += 30
    maila_b.sety(y)


def maila_b_alas():
    y = maila_b.ycor()
    y -= 30
    maila_b.sety(y)


#Kun pelaaja A saavuttaa tarvitun pistemäärän, toinen pelaaja katoaa kentältä ja vain voittaja jää jäljelle!
#Ruudulle ilmestyy teksti, joka kertoo kumpi pelaaja voitti
def juhla():
    j = turtle.Turtle()
    j.speed(0)
    j.color("white")
    j.penup()
    j.hideturtle()
    j.goto(-150, 150)
    j.write("Pelaaja A voitti pelin!", align="left", font=("Arial", 33, "bold", "underline"))
    pen.clear()
    pallo.clear()
    pallo.color("black")
    maila_b.color("black")
    


#Sama juttu pelaajalle B
def juhla2():
    j2 = turtle.Turtle()
    j2.speed(0)
    j2.color("red")
    j2.penup()
    j2.hideturtle()
    j2.goto(150, 150)
    j2.write("Pelaaja B voitti pelin!", align="right", font=("Arial", 33, "bold", "underline"))
    pen.clear()
    pallo.color("black")
    maila_a.color("black")
    

    



#Määritetään näppäimet, joilla peliä voidaan pelata
#Tarvitaan ylös- ja alas näppäimet kahdelle pelaajalle, joten luodaan neljä näppäinohjainta

wn.listen()
wn.onkeypress(maila_a_ylos, "w")
wn.onkeypress(maila_a_alas, "s")
wn.onkeypress(maila_b_ylos, "Up")
wn.onkeypress(maila_b_alas, "Down")

#Pääohjelma
#Toistaa itseään niin kauan, että pelaaja sulkee pelin painamalla rastia

#Peli ilmoittaa kuitenkin kun se loppuu, toisen pelaajan saavuttaessa tarpeeksi pisteitä
#Pelin loppuessa voittaja voi jäädä tuulettelemaan kentälle
while True:
    wn.update()

    #Pallon liike saadaan muuttamalla pallon x- ja y-koordinaattia aijemmin määritetyn nopeuden verran
    pallo.setx(pallo.xcor() + pallo.dx)
    pallo.sety(pallo.ycor() + pallo.dy)

    #Luodaan pelille reunat ja määritellään mitä tapahtuu, kun pallo osuu kuhunkin reunaan
    #Jos pallo osuu ylä- tai alareunaan, pallo vaihtaa suuntaansa y-akselilla, joka saa pallon pomppaamaan pois kyseisestä reunasta
    if pallo.ycor() > 290:
        pallo.sety(290)
        pallo.dy *= -1
        

    if pallo.ycor() < -290:
        pallo.sety(-290)
        pallo.dy *= -1
        
        

#Jos pallo osuu ruudun päätyihin, pallo ei enää pomppaa takaisin, vaan palaa ruudun keskelle ja vaihtaa taas suuntaa
#Riippuen siitä kumpaan päähän pallo osuu, lisätään vastapuolen pelaajalle yksi piste
#Tässä käsitellään mitä tehdään, jos pallo osuu ruudun oikeaan reunaan
    if pallo.xcor() > 390:
        pallo.goto(0, 0)
        pallo.dx *= -1
        score_a += 1
        #Kun pistetilanne päivittyy, pitää vanha tilanne poistaa alta, ettei tekstistä tule yhtä mössöä
        #Tämä onnistuu pen.clear() komennolla, jota en tajunnut ensin käyttää ja kesti hetken aikaa ennenkuin tajusin tämän
        pen.clear()
        pen.write("Pelaaja A: {} Pelaaja B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "bold"))

#Tässä käsitellään mitä tehdään, jos pallo osuu ruudun vasempaan reunaan
    if pallo.xcor() < -390:
        pallo.goto(0, 0)
        pallo.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Pelaaja A: {} Pelaaja B: {}".format(score_a, score_b), align="center", font=("Arial", 24, "bold"))

    #Tässä kohdassa luodaan mailoille "pinta", että saadaan pallo pomppaamaan mailasta poispäin jos pallo siihen osuu
    #Pallo siis periaatteessa hetkellisesti asetetaan mailan pinnalle uudestaan ja samalla vaihdetaan pallon x-akselin suuntaa, jos pallo määritelmän mukaan osuu mailaan
    if pallo.xcor() > 340 and pallo.xcor() < 350 and (
            pallo.ycor() < maila_b.ycor() + 40 and pallo.ycor() > maila_b.ycor() - 50):
        pallo.setx(340)
        bvot.append(p)
        p += 1
        pallo.dx *= -1
        
        


    if pallo.xcor() < -340 and pallo.xcor() > -350 and (
            pallo.ycor() < maila_a.ycor() + 40 and pallo.ycor() > maila_a.ycor() - 50):
        pallo.setx(-340)
        avot.append(m)
        m += 1
        pallo.dx *= -1
        

    #Pelaajan saavuttaessa 10 pistettä, peli päättyy ja juhla-funktio kutsutaan riippuen kumpi pelaaja voitti
    #Näytölle ilmestyy tieto siitä, kuinka monta kosketusta voittajan maila teki pallon kanssa
    #Ohjelma myös lukee pelitilanne-tiedostoa ja luo uuden tiedoston, jossa näkyy kuka viimeisimmän pelin on voittanut
    #A voittaa
    if score_a == 10:
        voitot["Viime pelin voittaja"] = "Pelaaja A"
        ja = turtle.Turtle()
        ja.speed(0)
        ja.color("white")
        ja.penup()
        ja.hideturtle()
        ja.goto(0,0)
        ja.write(f"Pelaajan A kosketukset: {len(avot)}", align="center", font=("Arial", 33, "bold"))
        pallo.goto(-200,-200)
        
    
        #Luodaan pelaajan tiedostoihin tekstitiedosto, josta pystyy tarkistamaan, kuka on voittanut viimeisimmän pelin
        #Ohjelma avaa ja lukee ensin pohjatiedoston, jota se muokkaa siten, että se näyttää lukijalle halutun tiedon
        with open("Pelitilanne.txt" , "r") as tiedosto:
            lines = tiedosto.readlines()

        with open("ViimePelinVoittaja.txt", "w") as tiedosto2:
                for line in lines:
                    line = line.replace("{'Viime pelin voittaja': 'Pelaaja B'}", "")
                    tiedosto2.write(line)
        juhla()
        
        
    #B voittaa
    if score_b == 10:
        voitot["Viime pelin voittaja"] = "Pelaaja B"
        jb = turtle.Turtle()
        jb.speed(0)
        jb.color("red")
        jb.penup()
        jb.hideturtle()
        jb.goto(0,0)
        jb.write(f"Pelaajan B kosketukset: {len(bvot)}", align="center", font=("Arial", 33, "bold"))
        pallo.goto(-200,-200)
        

        with open("Pelitilanne.txt" , "r") as tiedosto:
                lines = tiedosto.readlines()
        with open("ViimePelinVoittaja.txt", "w") as tiedosto2:
            for line in lines:
                line = line.replace("{'Viime pelin voittaja': 'Pelaaja A'}", "")
                tiedosto2.write(line)
        juhla2()

    #Ohjelma päättyy, kun pelaaja päättää painaa rastia ikkunan oikeasta yläkulmasta
    #Ruudulle jää tiedot siitä kumpi voitti ja kuinka monta kosketusta voittajan mailalla oli pallon kanssa