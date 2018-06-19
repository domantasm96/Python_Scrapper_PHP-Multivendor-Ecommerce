# Domantas Meidus, VU MIF IT 3 kursas, 1 gr - Kursinis darbas.

## Python Scrapper PHP Multivendor Ecommerce

Pagrindinis implementacijos kodas yra pavadintas __ns.py__ vardu.

Programos paleidimas turi būti įvykdytas specialiai kursinio implementacijai sukurtoje virtualios mašinos aplinkoje.

### Komandos norint sėkmingai paleisti programą:

1. Terminale suvedamas ssh adresas, kuris prijungs prie sistemos:
	-- ssh -p 1822 kursinis@193.219.91.103
2. Įvedami VM prisijungimo duomenys
3. cd Python_Scrapper_PHP-Multivendor-Ecommerce
4. python3 ns.py

Kai ns.py kodas sėkmingai įvykdomas, programos išeities rezultatai yra išsaugoti __MySql__ duomenų bazėje. Ją galima pasiekti tokiu būdu:

1. mysql -u root -p'root' -D kursinis (ši komanda prijungs vartotoją prie duomenų bazės)
2. show tables; (parodys duomenų bazėje egzistuojančias lenteles)
3. Komandos išeities rezultatų atvaizdavimui: 	
	-- a) select * from Cart;
	-- b) select * from Seller;
	-- c) select * Whishlist;

### Virtualios mašinos paskirtis 

Virutali mašina sukurta siekiant sėkmingai įvykdyti kursinio implementacijos kodo dalį, kurio tikslas yra  prisijungiat prie pažeidžiamos DEMO versijos internetinio puslapio bei naudojantis SQL injekcijos atakų vektoriais, atsiųsti jautrią informaciją iš puslapio apie visus prisiregistravusius vartotojus bei tą informaciją importuoti į MySql duomenų bazę.


### Prisijungimo duomenys prie sistemos:
- VM adresa1(jungiantis per Linux): ssh -p 1822 kursinis@193.219.91.103
- VM adresas2(jungiantis per Windows): putty.exe -ssh -P 1822 kursinis@193.219.91.103
- Vartotojo vardas: kursinis
- Slaptažodis: Kursini5

### Sistemos duomenų bazės prisijungimo duomenys:
- Vartotojo vardas: root
- Slaptažodis: root

### Prisijungimo duomenys prie svetainės, kurioje yra naudojama SQL injekcija:
- Vartotojo vardas: tesotest22@gmail.com
- Prisijungimo vardas: super1234
- Prisijungimo URL: http://www.fxwebsolution.com//demo/arthi/multivendor/sign-in.php

Pagrindinis implementacijos kodas yra pavadintas __ns.py__ vardu.

### Norint paleisti programą, reikia per terminalą įvykdyti šią komandinę eilutę: 

- __python3 ns.py__

### Prieš paleidžiant programą, reikia įsitikinti ar sistema atitinka reikalavimus:

1. Vartotojas turi būti "__Python_Scrapper_PHP-Multivendor-Ecommerce__" direktorijoje
2. Sistemos duomenų bazė turi būti sukonfiguruota taip, kad vartotojo vardas būtų "root", o slaptažodis: "root"

Visi reikiami įrankiai jau yra įrašyti į sistemą, bet jeigu atsitiktų taip, kad reiktų sistemą kurti iš naujo, tam yra parašytas bash scenarijus 'setup.sh'. Norint šį scenarijų paleisti, vartotojas turi turėti administratoriaus teises: sudo ./setup.shd

### Nuorodos susijusios su kursiniu darbu:

1. Overleaf internetinė platforma, per kurią buvo rašomas kursinis darbas: https://www.overleaf.com/read/vnwxbxdscqjd
2. GitLab kursinio darbo repositorijos nuoroda: https://git.mif.vu.lt/dome3235/Python_Scrapper_PHP-Multivendor-Ecommerce (ši repozitorija yra pasiekiama tik įgaliotams asmenims, dėl privatumo nustatymų).

