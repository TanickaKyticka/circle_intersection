# Circle Intersection Project

## Popis projektu

Tento program zjišťuje, zda se dvě kružnice protínají, a pokud ano, kolik mají průniků.

Program:

* spočítá vzdálenost mezi středy kružnic
* porovná vzdálenost se součtem a rozdílem poloměrů
* určí počet průniků (0, 1 nebo 2)
* vrátí výsledek jako slovník
* vypíše výsledek do terminálu
* vykreslí obě kružnice pomocí knihovny matplotlib

---

## Struktura projektu

```
cviceni1/
│
├── main.py
├── circle_stats.py
├── circles_intersection_draw.py
└── README.md
```

### main.py

Hlavní skript programu.
Definuje dvě kružnice, zavolá funkci pro výpočet průniku a zobrazí výsledek.

### circle_stats.py

Modul obsahující matematické funkce:

* `radius_sum()` – součet poloměrů
* `euclid_distance()` – Euklidovská vzdálenost mezi body
* `has_intersection()` – rozhodne o průniku kružnic

### circles_intersection_draw.py

Modul pro vykreslení kružnic pomocí knihovny **matplotlib**.

---

## Instalace knihoven

Program používá knihovnu `matplotlib`.

Instalace:

```
pip install matplotlib
```

nebo

```
uv add matplotlib
```

---

## Spuštění programu

Program spustíš příkazem:

```
python main.py
```

Po spuštění program:

1. vypíše informaci o průniku kružnic
2. zobrazí graf s vykreslenými kružnicemi

---

## Příklad výstupu

```
Kružnice se protínají a mají 2 průniky.
```

Zároveň se otevře okno s grafem, kde jsou obě kružnice vykreslené.

---

## Reprezentace kružnice

Kružnice je v programu reprezentována jako slovník:

```python
circle = {"x": 0, "y": 0, "r": 2}
```

* `x` – souřadnice středu na ose X
* `y` – souřadnice středu na ose Y
* `r` – poloměr kružnice
