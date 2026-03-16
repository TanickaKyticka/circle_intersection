#course = "Algoritmizace"
#print (f"Vítejte v kurzu {course}")
#print (2+3)
# print(10 - 20)    # -10
# print(2 * 5)      # 10
# print(10 / 3)     # 3.333...
# print(10 // 3)    # 3 (celočíselné dělení)
# print(10 % 3)     # 1 (zbytek)
# print(2 ** 6)     # 64 (dvě na šestou)
from Tools.scripts.generate_global_objects import Printer

# number_1 = 2
# number_2 = 5
# print(number_1 + number_2)

# Výpočet BMI (Body Mass Index)
# weight = 50  # kg
# height = 1.63  # m
#
# bmi = weight / (height ** 2)
# print(f"Vaše BMI: {bmi}")  # Vypíše na 1 des. místo

# number = 14
# divisor = 3
#
# remainder = number % divisor
# print(f"Číslo {number} děleno {divisor} má zbytek {remainder}")

# MONTHS = 12
# TAX_RATE_PCT = 15
# monthly_income = 25000
# yearly_before_tax = MONTHS * monthly_income
# tax_rate = (TAX_RATE_PCT / 100)
# tax_whole = yearly_before_tax * tax_rate
# print(f"celkova dan = {tax_whole}")

# temperature = 38.5
#
# has_fever = temperature >= 38.0
# print(f"Horečka: {has_fever}")  # Vypíše True nebo False

# Seznam teplot pacientů
temperatures = [36.6, 37.2, 38.1, 36.9, 37.5]

# Přístup k jednotlivým prvkům pomocí indexu (začíná od 0!)
# print(temperatures[0])  # 36.6 (první prvek)
# print(temperatures[1])  # 37.2 (druhý prvek)
# print(temperatures[4])  # 37.5 (pátý prvek)

# # Délka seznamu
# temperatures = [36.6, 37.2, 38.1, 36.9, 37.5]
# count = len(temperatures)
# print(f"Máme {count} měření teploty")  # Máme 5 měření teploty
#
# # Délka textu (počet znaků včetně mezer)
# name = "Jan Novák"
# length = len(name)
# print(f"Jméno má {length} znaků")  # Jméno má 9 znaků

# patients = ["Jan Novák", "Marie Svobodová", "Petr Dvořák"]
#
# first_patient = patients[0]
# second_patient = patients[1]
#
# print(f"První pacient: {first_patient}")
# print(f"Druhý pacient: {second_patient}")

# number = 10
# if number > 5:
#     print("cislo je vetsi nez 5")
# else:
#     print("cislo je mensi nebo rovno 5")

# heart_rate = 105
# TACHYCARDIA_LIMIT = 100
# if heart_rate > TACHYCARDIA_LIMIT :
#     print("zrychleny tep")
# else :
#     print("srdecni frekvence v norme")

# Vypíše "Ahoj" 5x pod sebou a pak se rozloučí
# for i in range(5):
#     print(f"Ahoj {i}")
#     print("...další řádek v cyklu (taky odsazený)")
#
# print("Toto se vypíše až po skončení cyklu (už není odsazené).")

# Seznam oblíbených ovoce
# fruits = ["jablko", "hruška", "banán", "pomeranč"]
#
# # Projdeme všechny položky a vypíšeme je
# for fruit in fruits:
#     print(f"Mám rád {fruit}")

# for i in range(10) :
#     print(f" luzko c. {i}")

# temperatures = [36.6, 37.2, 38.1, 36.9, 37.5]
# for temp in temperatures :
#         print(f"Teplota: {temp}")

# heart_rate = 72
# if heart_rate > 100:
#     print("Tachykardie!")
#
# patient_name = "Jan Novák"
# print(f"Pacient: {patient_name}")
#
# temperature = 37.5
# if temperature > 38.0:
#     print("Horečka!")
#
# temperatures = [36.6, 37.2, 38.1]
# first_temp = temperatures[0]
# last_temp = temperatures[2]
# print(last_temp)

# Seznam teplot pacientů
# temperatures = [36.6, 38.5, 37.2, 39.1, 36.9]
#
# # Projdeme všechny teploty
# for temp in temperatures:
#     if temp >= 38.0:
#         print(f"Horečka: {temp} °C")
#     else:
#         print(f"V normě: {temp} °C")

# Seznam teplot
temperatures = [36.6, 38.5, 37.2, 39.1, 36.9, 38.2]

# Počítadlo pacientů s horečkou
fever_count = 0

for temp in temperatures:
    if temp >= 38.0:
        fever_count += 1  # Zkrácený zápis pro: fever_count = fever_count + 1

print(f"Celkem pacientů: {len(temperatures)}")
print(f"Pacientů s horečkou: {fever_count}")


