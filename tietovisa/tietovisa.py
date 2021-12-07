
# Kommentit on luotu itseäni ja kurssin opettajaa varten, joten niissä on ääkkösiä. Jos ohjelma julkastaisiin tulisi kommentit muuttaa.

# Tuodaan moduuleita sitä myötä kun niille on tarvetta
# Moduuli 'os' on tarpeellisia kansioitten luomiseen ja niistä tiedostojen lukemiseen.
# Moduuli 'json' on tarpeellisia dictionary muodon tallentamiseen ja siitä lukemiseen.
# Moduuli 'pprint' helpottaa dictionary muodon ulosantia ja on näin ollen vain kosmeettisista syistä mukana.
import os.path
import os
import json
from os import listdir
from os.path import isfile, join
import pprint
# Ensin on lyhyt opastus, jotta käyttäjä ei syöttäisi liian pitkiä kysymyksiä käyttökokemuksen helpottamiseksi.
# Varsinkin vastaukset täytyy tässä versiossa kirjoittaa kokonaisuudessaan oikein.
print("")
print("Tervetuloa visailupeligeneraattoriin.")
print("")
print("""Ohjelmalla voit luoda ja pelata visailupelejä.
Ohjelmaa voidaan hyödyntää esimerkiksi ulkomaisen kielen opiskelussa.
Kirjoitathan lyhyitä vastauksia, koska tehtävien suorittaja joutuu kirjoittamaan vastauksen. Esim.""")
print("")
print("""Mikä on auto englanniksi?
a) ball b) carrot c) car""")
print("")
DUMP = input("Enteriä painamalla pääset päävalikkoon")
# 'while loop' on syötetty alkuun, jotta ohjelma palautuisi alkuvalikkoon
while True:
    # Luetaan kansiota tehtäväsarjojen tallennusta ja lukua varten käyttäjän omaan kansioon
    hakemisto = os.path.expanduser("~")
    hakemisto = os.path.expanduser("~\\peligeneraattori_tiedostot\\")
    print("Tallennuskansiosi on, ", hakemisto)
    # Jos kansiota ei ole olemassa se luodaan.
    if not os.path.exists(hakemisto):
        os.makedirs(hakemisto)
    # Käyttäjälle ilmoitetaan mitä valintoja ohjelmassa on mahdollista suorittaa
    print("")
    print("""Päävalikko:
    1. Luo uusi tehtäväsarja
    2. Vastaa kysymyksiin
    3. Poistu ohjelmasta""")
    # Käyttäjä valitsee luvun jonka perusteella ohjelma suorittaa tehtävän
    print("")

    try:
        aloitusluku = int(input("Valitse jokin numero aloitustaulusta: "))
    except ValueError:
        print("")
        print("Syötä jokin numeroista 1, 2 tai 3")
        print("")
        continue
    if aloitusluku == 1:
        lkm = 1
        # 'while loop' on käytössä, jotta ohjelma palauttaisi käyttäjän jos hän yrittää kirjoittaa olemassa olevaan tiedostoon
        # Tässä ohjelma versiossa ei muokata olemassa olevaa tiedostoa vaan kirjoitetaan aina uusi
        while True:
            try:
                hak = hakemisto
                # Seuraava kooodi näyttää kyseisessä hakemistossa olevat tiedostot
                onlyfiles = [f for f in listdir(hak) if isfile(join(hak, f))]
                print("")
                print("Tiedostot hakemistossa ovat: ")
                print(onlyfiles)
                print("")
                # Kysymyksessä varoitetaan syöttämästä olemassa olevaa tiedostoa, mutta näin käydessä käyttäjä palautetaan
                print("""Anna kysymyssarjalle nimi yhdellä sanalla 
(älä syötä jo olemassa olevaa tiedostoa)
(kirjoita kysymyssarjan nimi yhtenä sanana ilman erikoismerkkejä tai ääkkösiä)""")
                print("")
                tiedosto_nimi = input("Kirjoita kysymyssarjan nimi: ")
                # Tiedostot tulee tallentaa '.json' muotoon jotta 'dictionary' olisi uudelleen avattavissa
                tiedosto = tiedosto_nimi + '.json'
                # Seuraavaksi testataan vain onko tiedosto olemassa palautusta varten
                txt = (hakemisto + tiedosto)
                print(txt)
                file = open(txt, "x")
                # Tässä tallennetaan kysymys, vastaukset ja oikea vastaus. Koska oikea vastaus on tässä versiossa erillisenä
                # on käytettävä 'nested dictionary' muotoa, jotta kysymyksen vastaus voidaan tarkastaa.
                # Aluksi oli tarkoituksena tehdä sama asia 'class' ominaisuutta käyttäen, mutta päädyin 'nested dictionary' muotoon.
                # Suunnitteilla on, että ohjelman tulevissa versioissa vaihduttaisiin 'class' muotoon,
                # jotta ohjelmasta saataisiin monipuolisempi
                print("")
                print("(Kysymyssarjassa tulee olla vähintään kaksi kysymystä!)")
                print("")
                k_num = ('kysymys'+str(lkm))
                c = input(f"Kysymys {lkm}: ")
                d = input("Vastaus vaihtoehto 1: ")
                e = input("Vastaus vaihtoehto 2: ")
                f = input("Vastaus vaihtoehto 3: ")
                a = input("Oikea vastaus: ")
                # Luodaan 'dicionary' nimeltä 'kv'
                kv = {}
                # Jokainen kysymys yksilöidään omalla joka muodostetaan alkamaan numerosta '1'
                # Ja tämän jälkeen lisäytymään omillaan aina seuraavaan numeroon 'auto increment'
                kv[k_num] = []
                # Sen sisälle tulee 'nested dictionary', joka mahdollistaa vastauksien eri määrän esim. 'while loop':lla
                # Tässä versiossa kuitenkin rajattu automaattisesti kolmeen.
                kv[k_num].append({
                    'k': c,
                    'v1': d,
                    'v2': e,
                    'v3': f

                })
                # Oikea vastaus kirjataan erilliseksi kysymyksestä
                # Vastauksen numero lisääntyy samoin kuin kysymyksessä, jotta ne pystytään liittämään toisiinsa.
                # Vastaus on oltava erillisenä kysymyksestä ja määrittää onko tehtävään vastattu oikein.
                kv['vastaus'+str(lkm)] = []
                kv['vastaus'+str(lkm)].append(a)
                lista = {"kysymyssarja": [kv]}
            # Tässä vaiheessa palautetaan ohjelma, jos tiedosto on jo olemassa
            except FileExistsError:
                print("Kyseinen tiedosto on jo olemassa")
                print("")
                continue
            except OSError:
                print("Nyt oli kyllä liian monimutkainen nimi, kokeilepa uudestaan")
                print("")
                continue
            else:
                # Tästä alkaa oma looppi, joka suoriuduttuaan palautuu päävalikkoon

                while True:
                    jatko = input(
                        "Jos haluat jatkaa kysymysten tekoa paina k, jos et paina e: ")
                    # Aina kun käyttäjä syöttää 'k' kysymyssarjaan lisätään uusi kysymys.
                    # Kysymyksiä voi lisätä niin paljon kuin haluaa
                    # Huomioitavaa vielä uudelleen on että koko kysymyssarja tulee syöttää kerralla.
                    if jatko == "k":
                        lkm += 1
                        k_num = ('kysymys'+str(lkm))
                        c = input(f"Kysymys {lkm}: ")
                        d = input("Vastaus vaihtoehto 1: ")
                        e = input("Vastaus vaihtoehto 2: ")
                        f = input("Vastaus vaihtoehto 3: ")
                        a = input("Oikea vastaus: ")
                        kv = kv
                        kv[k_num] = []
                        kv[k_num].append({
                            'k': c,
                            'v1': d,
                            'v2': e,
                            'v3': f

                        })
                        kv['vastaus'+str(lkm)] = []
                        kv['vastaus'+str(lkm)].append(a)
                        lista = {"kysymyssarja": kv}

                    if jatko == "e":
                        # Vastatatessa 'e' käyttäjä lopettaa tehtäväsarjan ja siirtyy tallennukseen.
                        # Tallennus on suoritettava '.json' muodossa, jotta 'nested dictionary':ä voidaan myöhemmin käsitellä
                        # Ennen tätä ohjelma kuitenkin näyttää kysymykset
                        print("")
                        print("Kysymykset ja vastauksesi ovat:")
                        pprint.pprint(kv)
                        print("")
                        with open(txt, 'w') as f:
                            json.dump(lista, f)
                        break
                        # Break komennot on sijoitettava oikein, jotta ohjelma palautuisi alku valikkoon
            break
    if aloitusluku == 2:

        # Jos valitaan aloitus luku '2' siirrytään tiedoston lukuun ja suoritukseen
        hak = hakemisto
        # Tiedostot näytetetään, jotta niistä voisi valita haluamansa tehtäväsarjan
        print("")
        onlyfiles = [f for f in listdir(hak) if isfile(join(hak, f))]
        print("Tiedostot hakemistossa ovat: ")
        print(onlyfiles)
        print("")
        # Käyttäjä syöttää haluamnsa kysymyssarjan.
        tiedosto_nimi = input(
            "Minkä kysymyssarjan haluat suorittaa, (päätettä ei tarvitse kirjoittaa): ")
        tiedosto = tiedosto_nimi + '.json'
        txt = (hakemisto + tiedosto)
        # Kysymyssarja ladataan '.json' tiedostosta ja niiden sisältä avataan kysymykset
        with open(txt) as json_file:
            lista = json.load(json_file)
            kv = lista['kysymyssarja']
        # Luvulle oikein ja lkm on määritelty aloitus numerona '0', jotta niiden lukumäärä saadaan tallennettua.
        k_lkm = 0
        oikein = 0
        # Suoritukseen on lisätty 'try' lohko
        try:
            while True:
                k_lkm += 1
                kys = "kysymys" + str(k_lkm)
                vas = "vastaus"+str(k_lkm)
                # 'for loop' suorittaa kysymyksen ja vastaukset luettavammassa muodossa
                for p in kv[kys]:
                    print('Kysymys: ' + p['k'])
                    print('Vastaus1: ' + p['v1'])
                    print('Vastaus2: ' + p['v2'])
                    print('Vastaus3: ' + p['v3'])
                v = input("Anna vastaus ")
                # Kysymykseen syötetty vastaus haetaan ja verrataan antaamaasi vastaukseen
                if v in kv.get(vas):
                    oikein += 1
                    print("Vastasit oikein")
                    print("")
                else:
                    print("Vastasit väärin")
                    print("")

        except TypeError:
            print("")
            print("""Kysymyssarjassa tulee olla vähintään kaksi kysymystä.
Poista kyseinen kysymyssarja ja tee kysymyssarja uudelleen.""")
            print("")
        # 'KeyError' lopettaa tehtävä sarjan
        except KeyError:
            print("Tehtävät loppuivat")
            print("")
            # Poistetaan 'tyhjä' kysymys joka päättää sarjan
            k_lkm1 = k_lkm - 1
            print(
                f"Tehtäviä oli {k_lkm1}, joista vastasit oikein {oikein} tehtävään")
            print("")
            dump = input("Paina Enter palataksesi päävalikkoon")
        pass
    # Jos aloitusvalikosta syötetään luku '3' ohjelma lopettaa.
    if aloitusluku == 3:
        print("")
        print("Moro!")
        print("")
        break
