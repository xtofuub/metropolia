# Projekti 4 - Kalareissu

## Idea

Tämä on tekstipohjainen kalastuspeli.

Alussa pelaaja syöttää nimen ja iän. Sen jälkeen voi kalastaa eri paikoissa. Kun kala tulee, pelaaja päättää pitääkö sen vai vapauttaako sen.

Pelin tavoitteena on saada kolme kalaa.

## Toiminnot

Päävalikossa on:

1. Kalasta
2. Vaihda paikkaa
3. Näytä saalis
4. Tallenna peli
5. Lataa peli
6. Lopeta

Kalastaessa peli arpoo kalan senhetkisestä paikasta. Kalan nimi ja paino näytetään ennen kuin pelaaja tekee päätöksen.

Pelissä on kolme kalastuspaikkaa: Lampi, Joki ja Meri. Näistä voi valita oman reitin pelin aikana.

## Luokat

Pelissä on kolme luokkaa:

- Pelaaja
- Huone
- Esine

Pelaajalla on nimi, ikä, sijainti ja saalis. Huone tarkoittaa tässä kalastuspaikkaa ja sisältää siellä olevat kalat. Esine sisältää kalan nimen ja painon.

## Tiedostot

Projektin rakenne on jaettu eri Python-moduuleihin:

```text
projekti4/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── pelaaja.py
│   ├── huone.py
│   └── esine.py
└── readme.md
```

`main.py` sisältää pelin käynnistyksen, päävalikon ja pelin toiminnot.

`modules/pelaaja.py` sisältää Pelaaja-luokan.

`modules/huone.py` sisältää Huone-luokan.

`modules/esine.py` sisältää Esine-luokan.

Pelissä käytetään myös `tallennus.json`-tiedostoa, kun peli tallennetaan.

## Kestävä kehitys

Aihe liittyy YK:n tavoitteeseen 14, Vedenalainen elämä.

Pelissä kalan voi vapauttaa takaisin veteen. Tarkoituksena on tuoda esiin vastuullista kalastamista.

## Tällä hetkellä

- pelaajan nimi ja ikä
- Pelaaja-, Huone- ja Esine-luokat
- Lampi, Joki ja Meri
- kalan arpominen
- kalan pitäminen tai vapauttaminen
- saaliin näyttäminen
- kolmen kalan tavoite
- pelin tallentaminen
- tallennetun pelin lataaminen
- kolme eri kalastusreittiä

Pelissä on useita funktioita, joilla eri toimintoja on jaettu omiin osiin.

## Käynnistys

```bash
python main.py
```
