Ohjelmoinnin perusteet TTC2030-3011 5op

HARJOITUSTYÖ

Tekijänä Matti Olavi Kastelli
AB5132
2107097

Harjoitustyöhön käytetty aika: 21h


SUUNNITELMA:


		Ohjelma toimii peligeneraattorina, jonka avulla on mahdollista luoda yksinkertainen tietovisailu
		ja tallentaa se tiedostoon uudelleen avaamista varten.
		Käyttäjä voi luoda, lisätä, pelata tai lukea tiedostoa. Tiedostoon hän voi lisätä kysymyksiä juoksevassa järjestyksessä
		ja antaa niille 3 vaihtoehtoa joista yksi on oikein. Kysymyksiä on mahdollista lisätä niin monta kuin haluaa,
		mutta niiden ja vastauksien tulee mahtua yhdelle riville.
		Käyttäjällä on mahdollisuus nähdä aiemmin luodut tiedostot, sekä jatkaa aiemmin luomaansa kysymyssarjaa.
		Pelaajalla on mahdollisuus nähdä tiedostot, joista hän voi valita pelattavan pelin. Hän voi valita vastaako kysymyksiin
		sekoitettuna vai järjestyksessä. Hänellä on myös mahdollisuus valita haluaako hän pelata kaikki kysymykset vai osan niistä,
		sekä saako hän kysymyksistä pisteitä vai tippuuko hän vastattuaan väärin takaisin päävalikkoon.
		Päävalikossa on mahdollisuus poistua sovellutuksesta.

		RAJOITTEET JA VAATIMUKSET
		1 Tiedosto tulee pystyä luomaan ja kirjoittamaan
		2 Tiedostot tulee pystyä hakemaan kansiosta ja niistä tulee olla mahdollista liittää tietoa ohjelmaan
		3 Tiedostossa tulee olla kysymykset ja vastaukset erillään ja niitä tulee pystyä tuomaan ohjelmaan siten,
		että niitä voidaan käyttää tarkoituksensa mukaisesti.
		4 Kysymysten ja vastausten tulisi sijoittua yhdelle riville(RAJOITE!)
		5 Syötettäessä väärää tietoa tulisi palautuksen tulla mahdollissimman lähelle.
		6 Ohjelmassa tulisi olla automaattinen tallennus ja jos kysymys-vastaus sarjaa ei saada suoritettua loppuun asti koko
		sarja tulee jäädä tallentumatta.

		Harjoitustyöstä on lisäksi kaavio, joka helpottaa harjotustyön kohtien ymmärtämistä, sekä havannoillistaa että harjoitustyössä
		käytettäisiin laajalti kurssilla opittuja asioita.

		Tehtävässä on haettu apua useilta eri keskustelu kanavilta ja hyödynnetty niiden käyttäjien antamia ohjeita
		Sivustot on esim. 'stackoverflow', 'Stack Abuse', 'w3schools', 'GeekforGeeks' jne.
		Ohjelman luontia varten on käyty ilmaisia netti luentoja koulun omien luentojen lisäksi.
		Luennot on vapaasti katsottavissa 'Youtube':ssa. Näistä mainittakoon ' Python - Accessing Nested Dictionary Keys'
		jota ilman dictionary muodossa tallentaminen olisi ollut paljon vaikeampaa.
		Tehtävässä ei ole kopioitu koodia vaan mallia ottaakseen ja se on aina käyttötarkoituksen mukaisesti sovellettu.


		
POHDINTA:



		Suunnitelman kaikki osa-alueet eivät täyttyneet tai olleet tarpeellisia, mutta ovat lisättävissä. 
		Keskeisimmät osa alueet ovat kuitenkin harjoitustyössä ja niiden sulavuus on saatu testattua toimivaksi.
		
		Koodi on kirjoitettu yhteen tiedostoon, jotta sen koodin kommentit olisi luettavissa. Näin ollen se e tarvitse
		muita tiedostoja toimiakseen. Ohjelma kirjoittaa itse kansion tiedostoilleen ja lisää omatoimisesti tiedostot.
		
		Koodin kommenteissa olen koettanut olla tarkkana, ei pelkästään opettajan vaan oman ja muitten oppimista edistääkseni.
		
		Harjotustyön aiheen keksittyäni ohjelmointi lähti hyvin käyntiin. Ongelmat tulivat vastaan kun aloin tallentamaan 
		tietoja tiedostoon. Työssäni tarvittavat vastaukset kysymyksiin ja kysymysten ja vastausten määrä, kuten niiden 
		löytäminen ja käyttäminen tiedostosta osoittautui hankalaksi. 
		Ensin aloin luomaan näitä 'class' muodossa ja tallentamaan 'pickle' toiminnon avulla. Tämä ei kuitenkaan onnistunut 
		odotettavasti ja 'pickle' ominaisuuden käyttäminen ei myöskään ollut tietoturva syistä tässä vaiheessa suotavaa,
		koska tiedostot olisivat olleet bitteinä. Joten päätin käyttämään 'json'
		menetelmää, joka myös mahdollistaa tiedoston muokkauksen ilman ohjelman avaamista. Samalla jäi myös 'class' menetelmän
		käyttö ja siirryin tutkimaan 'nested dictionary' menetelmää.
		Ohjelman testaukseen ja pieniin muutoksiin on kulunut odotettua enemmän aikaa. Testatessani mahdollisia virheitä nousi
		esille virheitä, joita en ollut osannut odottaa ja jotka veivät aikaa tutkia. Kuten TypeError, joka nousi esiin, 
		jos kysymyssarjaan lisäsi vain yhden kysymyksen.
		
		Seuraavaksi vielä esimerkki ohjelman toimivuudesta, sekä nostatettuja virheitä ja niiden käsittelyä.
		


ESIMERKKI TOIMINNASTA:



	PS C:\Users\okast> & C:/Users/okast/AppData/Local/Programs/Python/Python39/python.exe c:/Users/okast/OneDrive/Tiedostot/Ohjelmistoalan_osaaja/Ohjelmoinnin_perusteet/Harjoitustyö/kokonaisuus/kokonaisuus14.py

				Tervetuloa visailupeligeneraattoriin.

				Ohjelmalla voit luoda ja pelata visailupelejä.
				Ohjelmaa voidaan hyödyntää esimerkiksi ulkomaisen kielen opiskelussa.
				Kirjoitathan lyhyitä vastauksia, koska tehtävien suorittaja joutuu kirjoittamaan vastauksen. Esim.

				Mikä on auto englanniksi?
				a) ball b) carrot c) car

				Enteriä painamalla pääset päävalikkoon
	Tallennuskansiosi on,  C:\Users\okast\peligeneraattori_tiedostot\

	Päävalikko:
		1. Luo uusi tehtäväsarja
		2. Vastaa kysymyksiin
		3. Poistu ohjelmasta

				Valitse jokin numero aloitustaulusta: 1

				Tiedostot hakemistossa ovat:
				['.json', 'kysymykset.json', 'kysymyssarja.json', 'väärä muoto.json']

				Anna kysymyssarjalle nimi yhdellä sanalla
				(älä syötä jo olemassa olevaa tiedostoa)
				(kirjoita kysymyssarjan nimi yhtenä sanana ilman erikoismerkkejä tai ääkkösiä)

				Kirjoita kysymyssarjan nimi: kysymykset
				C:\Users\okast\peligeneraattori_tiedostot\kysymykset.json
				Kysymys 1: Mikä on talo englanniksi?
				Vastaus vaihtoehto 1: house
				Vastaus vaihtoehto 2: floor
				Vastaus vaihtoehto 3: road
				Oikea vastaus: house
				Jos haluat jatkaa kysymysten tekoa paina k, jos et paina e: k
				Kysymys 2: Mikä on lattia englanniksi?
				Vastaus vaihtoehto 1: road
				Vastaus vaihtoehto 2: house
				Vastaus vaihtoehto 3: floor
				Oikea vastaus: floor
				Jos haluat jatkaa kysymysten tekoa paina k, jos et paina e: k
				Kysymys 3: Mikä on tie englanniksi?
				Vastaus vaihtoehto 1: floor
				Vastaus vaihtoehto 2: road
				Vastaus vaihtoehto 3: house
				Oikea vastaus: road
				Jos haluat jatkaa kysymysten tekoa paina k, jos et paina e: e

				Kysymykset ja vastauksesi ovat:
				{'kysymys1': [{'k': 'Mikä on talo englanniksi?',
							   'v1': 'house',
							   'v2': 'floor',
							   'v3': 'road'}],
				 'kysymys2': [{'k': 'Mikä on lattia englanniksi?',
							   'v1': 'road',
							   'v2': 'house',
							   'v3': 'floor'}],
				 'kysymys3': [{'k': 'Mikä on tie englanniksi?',
							   'v1': 'floor',
							   'v2': 'road',
							   'v3': 'house'}],
				 'vastaus1': ['house'],
				 'vastaus2': ['floor'],
				 'vastaus3': ['road']}

	Tallennuskansiosi on,  C:\Users\okast\peligeneraattori_tiedostot\

	Päävalikko:
		1. Luo uusi tehtäväsarja
		2. Vastaa kysymyksiin
		3. Poistu ohjelmasta

				Valitse jokin numero aloitustaulusta: 2

				Tiedostot hakemistossa ovat:
				['.json', 'kysymykset.json', 'kysymyssarja.json', 'väärä muoto.json']

				Minkä kysymyssarjan haluat suorittaa, (päätettä ei tarvitse kirjoittaa): kysymykset
				Kysymys: Mikä on talo englanniksi?
				Vastaus1: house
				Vastaus2: floor
				Vastaus3: road
				Anna vastaus floor
				Vastasit väärin

				Kysymys: Mikä on lattia englanniksi?
				Vastaus1: road
				Vastaus2: house
				Vastaus3: floor
				Anna vastaus floor
				Vastasit oikein

				Kysymys: Mikä on tie englanniksi?
				Vastaus1: floor
				Vastaus2: road
				Vastaus3: house
				Anna vastaus road
				Vastasit oikein

				Tehtävät loppuivat

				Tehtäviä oli 3, joista vastasit oikein 2 tehtävään

				Paina Enter palataksesi päävalikkoon
	Tallennuskansiosi on,  C:\Users\okast\peligeneraattori_tiedostot\

	Päävalikko:
		1. Luo uusi tehtäväsarja
		2. Vastaa kysymyksiin
		3. Poistu ohjelmasta

				Valitse jokin numero aloitustaulusta: 3

				Moro!

	PS C:\Users\okast> 
	

NOSTATETUT VIRHEET JA NIIDEN KÄSITTELY:


	Ohjelma palautuu päävalikkoon ilman virhettä:
		
		Päävalikko:
			1. Luo uusi tehtäväsarja
			2. Vastaa kysymyksiin
			3. Poistu ohjelmasta

		Valitse jokin numero aloitustaulusta: 4
		Tallennuskansiosi on,  C:\Users\okast\peligeneraattori_tiedostot\

	ValueError:
	(Ohjelma neuvoo ja palautuu päävalikkoon)
		
		Päävalikko:
			1. Luo uusi tehtäväsarja
			2. Vastaa kysymyksiin
			3. Poistu ohjelmasta

		Valitse jokin numero aloitustaulusta: hdhteyj

		Syötä jokin numeroista 1, 2 tai 3

		Tallennuskansiosi on,  C:\Users\okast\peligeneraattori_tiedostot\

		Päävalikko:
			1. Luo uusi tehtäväsarja
			2. Vastaa kysymyksiin
			3. Poistu ohjelmasta

		Valitse jokin numero aloitustaulusta:

	FileExistsError:
	(Ohjelma neuvoo ja palautuu kysymykseen)
		
		Kirjoita kysymyssarjan nimi: kysymykset
		C:\Users\okast\peligeneraattori_tiedostot\kysymykset.json
		Kyseinen tiedosto on jo olemassa


		Tiedostot hakemistossa ovat:
		['.json', 'kysymykset.json', 'kysymyssarja.json', 'väärä muoto.json']

		Anna kysymyssarjalle nimi yhdellä sanalla
		(älä syötä jo olemassa olevaa tiedostoa)
		(kirjoita kysymyssarjan nimi yhtenä sanana ilman erikoismerkkejä tai ääkkösiä)

		Kirjoita kysymyssarjan nimi:
		
	OSError:
	(Ohjelma neuvoo ja palautuu kysymykseen)

		Kirjoita kysymyssarjan nimi: hyh\ ? äö
		C:\Users\okast\peligeneraattori_tiedostot\hyh\ ? äö.json
		Nyt oli kyllä liian monimutkainen nimi, kokeilepa uudestaan


		Tiedostot hakemistossa ovat:
		['.json', 'kysymykset.json', 'kysymyssarja.json', 'väärä muoto.json']

		Anna kysymyssarjalle nimi yhdellä sanalla
		(älä syötä jo olemassa olevaa tiedostoa)
		(kirjoita kysymyssarjan nimi yhtenä sanana ilman erikoismerkkejä tai ääkkösiä)

		Kirjoita kysymyssarjan nimi:
		
	Ohjelma palautuu kysymykseen ilman virhettä:
		
		Jos haluat jatkaa kysymysten tekoa paina k, jos et paina e: hdythyh
		Jos haluat jatkaa kysymysten tekoa paina k, jos et paina e: 
		Jos haluat jatkaa kysymysten tekoa paina k, jos et paina e:
		
	TypeError:
	(Ohjelma neuvoo ja palautuu päävalikkoon)
		
		Tiedostot hakemistossa ovat:
		['1.json', '123.json', '2.json', '3.json', '4.json', '5.json', 'abc.json', 'abcd.json', 'kys.json']

		Minkä kysymyssarjan haluat suorittaa, (päätettä ei tarvitse kirjoittaa): 1
		(Kysymyssarjassa tulee olla vähintään kaksi kysymystä!)

		Kysymyssarjassa tulee olla vähintään kaksi kysymystä.
		Poista kyseinen kysymyssarja ja tee kysymyssarja uudelleen.

		Tallennuskansiosi on,  C:\Users\okast\peligeneraattori_tiedostot\

		Päävalikko:
			1. Luo uusi tehtäväsarja
			2. Vastaa kysymyksiin
			3. Poistu ohjelmasta

	Valitse jokin numero aloitustaulusta:
		
	KeyError:
	(Tarkotuksen mukaisesti katkaisee kysymysketjun niiden loputtua)
		
		
		