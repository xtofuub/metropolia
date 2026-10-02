# Projekti 4 - Kalareissu

## Idea

Tässä projektissa tehdään yksinkertainen tekstipohjainen kalastuspeli. Pelaaja luo oman hahmonsa ja voi kalastaa eri paikoissa. Kaloja voi joko pitää tai vapauttaa.

Pelin tavoitteena on saada kolme kalaa saaliiksi.

## Pelin toiminta

Pelin alussa pelaaja antaa nimensä ja ikänsä. Pelaaja aloittaa lammelta.

Päävalikosta voi:

1. Kalastaa
2. Vaihtaa kalastuspaikkaa
3. Näyttää saaliin
4. Lopettaa pelin

Kalastettaessa peli arpoo nykyisen kalastuspaikan kaloista yhden kalan. Pelaaja näkee kalan nimen ja painon ja voi päättää, pitääkö kalan vai vapauttaako sen.

## Luokat

Projektissa käytetään kolmea luokkaa:

- **Pelaaja** sisältää pelaajan nimen, iän, nykyisen sijainnin ja saaliin.
- **Huone** kuvaa kalastuspaikkaa ja sen kaloja.
- **Esine** kuvaa kalastettavaa kalaa. Sillä on nimi ja paino.

## Tiedostorakenne

Projekti 4 on omassa kansiossaan.

```
projekti4/
├── projekti4.py
└── readme.md
```

Peli on tällä hetkellä toteutettu yhdessä Python-tiedostossa, koska projekti on vielä pieni. Jos peli kasvaa kehityksen aikana, toimintoja voidaan jakaa erillisiin moduuleihin.

## Kestävä kehitys

Peli liittyy YK:n kestävän kehityksen tavoitteisiin, erityisesti tavoitteeseen 14: **Vedenalainen elämä**.

Pelissä pelaaja voi vapauttaa kalan takaisin veteen sen sijaan, että pitäisi kaikki saadut kalat. Pelin tarkoituksena on tuoda esille vastuullista kalastamista ja vesistöjen huomioimista.

## Nykyinen tila

Peli on vielä kesken ja sitä kehitetään vaiheittain.

Tällä hetkellä pelissä on:

- pelaajan nimi ja ikä
- kolme luokkaa
- kaksi kalastuspaikkaa: Lampi ja Joki
- kalojen arpominen
- saaliin näyttäminen
- kalan pitäminen tai vapauttaminen
- pelin tavoite saada kolme kalaa

Myöhemmin peliin lisätään tarvittavia toimintoja ja ominaisuuksia projektin edetessä.

## Käynnistäminen

Peli käynnistetään suorittamalla tiedosto:

```bash
python projekti4.py
```
