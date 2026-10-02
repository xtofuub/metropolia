# Projekti 4 - Kalareissu

## Idea

Tämä on tekstipohjainen kalastuspeli.

Alussa pelaaja syöttää nimen ja iän. Sen jälkeen voi kalastaa lammella tai joella. Kun kala tulee, pelaaja päättää pitääkö sen vai vapauttaako sen.

Pelin tavoitteena on saada kolme kalaa.

## Toiminnot

Päävalikossa on:

1. Kalasta
2. Vaihda paikkaa
3. Näytä saalis
4. Lopeta

Kalastaessa peli arpoo kalan senhetkisestä paikasta. Kalan nimi ja paino näytetään ennen kuin pelaaja tekee päätöksen.

## Luokat

Pelissä on kolme luokkaa:

- Pelaaja
- Huone
- Esine

Pelaajalla on nimi, ikä, sijainti ja saalis. Huone tarkoittaa tässä kalastuspaikkaa ja sisältää siellä olevat kalat. Esine sisältää kalan nimen ja painon.

## Tiedostot

Projekti on tällä hetkellä tässä kansiossa:

```
projekti4/
├── projekti4.py
└── readme.md
```

Peli on yhdessä Python-tiedostossa, koska siinä ei ole vielä niin paljon koodia, että sitä olisi järkevää jakaa useaan tiedostoon.

## Kestävä kehitys

Aihe liittyy YK:n tavoitteeseen 14, Vedenalainen elämä.

Pelissä kalan voi vapauttaa takaisin veteen. Tarkoituksena on tuoda esiin vastuullista kalastamista.

## Tällä hetkellä

- pelaajan nimi ja ikä
- Pelaaja-, Huone- ja Esine-luokat
- Lampi ja Joki
- kalan arpominen
- kalan pitäminen tai vapauttaminen
- saaliin näyttäminen
- kolmen kalan tavoite

Projekti on vielä kesken.

## Käynnistys

```bash
python projekti4.py
```
