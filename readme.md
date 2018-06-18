
# Prisijungimo duomenys prie sistemos:
VM adresa1(jungiantis per Linux): ssh -p 1822 kursinis@193.219.91.103
VM adresas2(jungiantis per Windows): putty.exe -ssh -P 1822 kursinis@193.219.91.103
Vartotojo vardas: kursinis
Slaptažodis: Kursini5

# istemos duomenų bazės prisijungimo duomenys:
Vartotojo vardas: root
Slaptažodis: root

# Prisijungimo duomenys prie svetainės, kurioje yra naudojama SQL injekcija:
Vartotojo vardas: tesotest22@gmail.com
Prisijungimo vardas: super1234
Prisijungimo URL: http://www.fxwebsolution.com//demo/arthi/multivendor/sign-in.php

Pagrindinis implementacijos kodas yra pavadintas __ns.py__ vardu.

# Norint paleisti programą, reikia per terminalą įvykdyti šią komandinę eilutę: 

__python3 ns.py__

### Prieš paleidžiant programą, reikia įsitikinti ar sistema atitinka reikalavimus:

1. Vartotojas turi būti "__Python_Scrapper_PHP-Multivendor-Ecommerce__" direktorijoje
2. Sistemos duomenų bazė turi būti sukonfiguruota taip, kad vartotojo vardas būtų "root", o slaptažodis: "root"

Visi reikiami įrankiai jau yra įrašyti į sistemą, bet jeigu atsitiktų taip, kad reiktų sistemą kurti iš naujo, tam yra parašytas bash scenarijus 'setup.sh'. Norint šį scenarijų paleisti, vartotojas turi turėti administratoriaus teises: sudo ./setup.shd
