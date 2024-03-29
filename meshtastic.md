# UVOD

prirocnik je razdeljen na tri poglavja:
1. opis in definiranje osnovnih pojmov
1. hiter opis protokolnega sklada
1. podroben opis nastavitev 
1. Hitro in umazano navodilo za uspostaviti napravo

# Definiranje pojmov

FIRMWARE >> je koda katero zapisemo na samo napravo. V vecini je spisana v jeziku C++ in v binarni obliki jo zapecemo na napravo. Vsaka verzija naprave ima razlicne procesorje, module, ... zato je firmware za vsako napravo kompiliran v bitno kodo posebej in je zelo pomebno da izberemo pravi firmware za naso napravo

SOFTWARE >> je aplikacija na nasem mobilnem telefonu katera interacira z meshtastic napravo preko serijskega (usb kabel,..), bluetooth-a, ali wi-fija. Wi-fi ali bluetoot ne moremo uporabiti naeenkrat.

LORA >> Long range radio 
Meshtastic naprave lahko uporabljajo razlicne frekvencne pase. Najbolj primeren v EU je 868mhz band imenovan ISM (Industrial, G

MESHTATIC >> Je projekt kateri zavezema odprtokodno programsko kodo namenjeno komuniciranju s posebnimi nizkocenovnimi mikroprocesorji, kateri za oddajanje modulacije uporabljajo LoRa module. Poleg tekstovnih sporocil omogoca tudi oddajanje telemtrije (temperature, GPS koordinat, vlage, meritve razlicnih senzorjev)

ISM band >> je del radijskega spektra rezerviran za "industrial, scientific and medical" namene (868Mhz).

PROTOBUF >> protocol ki skrbi za komunikacijo med napravami. Protokol razvit s strani Google-a, ki s pomocjo sheme strukturira podatkje.Prokokol je neodvisen od jezika na "backend-u". V primerjavi z JSON zapisom, zmanjsa latency in zmanjsa velikost paketa ob istem sporocilu,

CHANNEL >> Kanal na kateremu naprave komunicirajo. Kanal ni le frekvenca na katermem naprave komunicirajo ampak je tesno povezan z nastavitvami katere so "hardcodane" v kanal. To so ime kanala, enkripcija, frekvenca, nacin, geslo. Pomebno je razumeti, da je potrebno upostevati vec nastavitev da naprave uspesno komunicirajo na istem "kanalu".

MQTT >> message query telemetry transport. Lahki omrezni protokol za preposiljanje sporocil na nacin publish/subscribe oz objavi/naroci-se. Protokol se ne uporablja preko lora omrezja , ampak za komunikacijo preko interneta.

MQTT BROKER >> je server na katerem zivi software, kateri deluje kot "posta" -- preposilja sporocila. Deluje na principu topic-ov/tem. Vsak ki je narocen na doloceno temo, dobi sporocila povezana s to temo. Skrbi za komunikacijo z vsemi klienti/meshtastici, ki so povezani z brokerjem.

# PROTOKOLNI SKLAD (Protocol stack)

## Nivo 0 LoRa radio (layer 0)

Pred samim RF signalom paketka modem odda "preamble", kateri omogoca modemom/napravam ki poslusajo da sinhronizirajo ure in zacenjo poslusati sporocilo/paket ki bo poslan. Po "preamble" sledi LoRa fizicna glava z informacijo dolzine paketka in sinhronizacjisko besedo prepoznavanje omrezja. Za meshtastic standardna `0x2B`.

## Nivo 1 (layer 1)

V glavi zero hop sporocila se nahaja:

* Prejemnik - Node ID
* Posiljatelj - Node ID
* Edinstven packed ID
* Flag - Zastava - (hop limit, wantAck, Mqtt,..)
* Dekripcijsko navodilo - 
* Padding za poravnanje podatkov

Sledi le se dejanski podatki iz paketka/sporocila.

> CSMA/CA carrieer-sense multiple access /w collision avoidance

Vsi oddajniki naredijo channel activiti detection preden karkoli posljejo. Ce je kanal zaseden bo oddajnik pocakal nakljucno stevilo casovnih slotov preden bo poskusal oddajati. Tako se zmanjsa moznost kolizij. Vecja koz je utilizacija kanala, vecje oz. daljse je okno casovnih slotov pred dejansko oddajo.


## Nivo 2 (layer2)

Z oznacitvijo zastavice `wantAck` v MeshPacket-u, bomo dobil nazaj sporocilo da je bil paket dostavljen. Ce je paketek namnjen vsem oz. broadcast-u, nasa naprava ne caka na sporocilo o dostavi, ampak poslusa ce je druga naprava v nasem dometu sporocilo preposlala naprej.

## Nivo 3 (Flooding for multi-hop)

Ce nasa naprava dobi paket z hopLimit-om vecijm od 0 bo paket preposlala naprej.

# KONFIGURACIJA / NASTAVITVE

Poglavje je razdelejno na `Radio Config` in `Module Config`. Ob razumevanju teh dveh pod-poglavji spoznamo podrobno veliko vecino vseh nastavitev naprave. Te nastavitve se nahajajo v aplikaciji, ce kliknemo v desnem kotu zgoraj na tri pikice oz. ti. nastavitveni gumb.

# KONFIGURACIJA NASTVITEV(Radio Config)

## Nastavitve kanala oz.skuping (Channel)

Nastavitve kanala so namanjene segregiranju paketkov v grupe, nastavitve enkripcije in internetnega prehoda. Le-te nastavitve so tudi unikatne za vsak kanal. Nastavitve kanal se posljejo s `Channel` protobufom kot admin paket/sporocilo.

Poznami tri vloge kanalov:

1. primarni kanal , ki je lahko samo eden
1. sekundarnih kanalov je lahko vec
1. onemogoceni kanali

> Naprave v mrezi, ki imajo nastavljen drugacen `PRIMARY CHANNEL` morajo eksplicitno nastavit frekvecni slot.

> Naprave samo na `PRIMARY CHANNEL` samodejno oddajajo boradcast telemtrije in pozicije.

### Uplink in Downlink

Skrbi za preposiljanje paketov v internet preko Mqtt Brokerja ( za dopolnit)


# Nastavitve naprave (Device)

V tem meniju nastavimo kaksno vlogo bo imela nasa naprav. ali se bo obnasla kot "klient" oz. naprava za posiljanje in sprejemanje sporocil, router ki bo posredoval sporocila v internet, ali le lokalni repater brez interneta. Obstajjo se druge vloge opisane v original dokumentaciji.

### Dolocitev vloge nase naprave

Vloga|Opis|Poraba
:--|--:|---:
CLIENT||Normalna
ROUTER||Visoka
ROUTER-CLIENT|Najvisja
REPEATER|Visoka


# Dolocitev rebroadcasting

Vrednost|Opis
---|---
ALL| rebroadcast vsa sporocila
ALL-SKIP-DECODING| samo za vlogo repeater
LOCAL-ONLY| samo za domaco mrezo/mesh
KNOWN-ONLY| ne prebroadcasta sporocila neznanih naprav v znanem omrezju

## LoRa nastavitve (LoRa)

`unset` je prenastavljen nacin modema za pasovno sirino spred facto in coding rate, kateri vplivajo na hitrost ooddajanja in domet.  Prdastavljena konfiguracija je optimalna in ni potrebnih sprememb.

`LONG_FAST` je opstimalna in prednastavljena konfiguracija vseh treh faktorjev. Daljse kombinacije zasedejo veilko casovno okno, najdaljse pa so celo nezanesljive in samo za testne namene.

###Pasovna sirina

Pasovne sirine ki so na voljo (v kHz):

Posebna st.|Interpretirana kot
:--|--:
31|31.25
62|62.25
200|203.125
400|406.25
800|812.5
1600|1625.0

## (Network) 

Nastavitve za povezavo na naprave na WI-FI/domaci router. Povezave ne uspe ce mogoce imamo WPA3 ali katero posebno rokovanje vklopljeno. Tudi na GUEST network-u iz vornoastnih razlogov ga mogoce ne bomo videli.

## (Position)

## (Power)

## (User)

// TO-DO

# KONFIGURCIJA LORA MODULA (Module Config)

## MQTT

V tem meniju vklopimo/izklopim mqtt modul. Vnesti moramo URL mqtt brokerja, uporabnisko ime, geslo, vklopit/izklopt enkrpcijo, TLS, JSON, ter obvezno vnesti `root topic`.

## Neighbour Info

Nastavimo interval posliljanja sporocil sosedom v mrezi o stanju naprave.

## Telemetry

// TO-DO

# Uporabne spletne vsebin

* (Offical)[https://meshtastic.org/]
* (Reddit)[https://www.reddit.com/r/meshtastic/]
* (Discord)[https://discord.com/invite/ktMAKGBnBs]

// YT CHANNELS TO-DO
