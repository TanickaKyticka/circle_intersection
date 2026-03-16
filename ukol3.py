# def greet_patient(name):
#     """Pozdraví pacienta jménem.
#
#     Args:
#         name (str): Jméno pacienta.
#
#     Returns:
#         None: Funkce nic nevrací.
#     """
#     print(f"Dobrý den, pane/paní {name}!")
#
# # Volání
# greet_patient("Novák")    # Dobrý den, pane/paní Novák!
# greet_patient("Svobodová") # Dobrý den, pane/paní Svobodová!
#
# def calculate_bmi(weight, height):
#     """Vypočítá hodnotu BMI (Body Mass Index) z hmotnosti a výšky.
#
#     Args:
#         weight (float): Hmotnost v kilogramech.
#         height (float): Výška v metrech.
#
#     Returns:
#         float: Vypočítaná hodnota BMI.
#     """
#     bmi = weight / (height ** 2)
#     return bmi
#
# def greet_patient(name):
#     print(f"Dobrý den, pane/paní {name}!")
# greet_patient("Jan Novák")
#
# temp = 36.1
# def has_fever(temp):
#     if temp > 38 :
#         is_fever = True
#     else :
#         is_fever = False
#     return temp > 38
# print(has_fever(39))

# blood_pressure = [120, 125, 118, 130, 135, 128, 122]
# print(max(blood_pressure))
# print(min(blood_pressure))
#
# count = 0
# for p in blood_pressure:
#     if p > 130:
#         count += 1
# print(count)
#
# days = ["Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun"]
# blood_pressure = [120, 125, 118, 130, 135, 128, 122]
# for day, bp in zip(days, blood_pressure):
#     print(f"{day}: {bp} mmHg")


# temperature_log = [
#         ["Jan Novák", 36.5, 36.7, 36.6],
#         ["Marie Svobodová", 37.2, 38.1, 38.5],
#         ["Petr Dvořák", 36.8, 36.9, 37.0]
# ]
#
# for patient in temperature_log:
#     avg = sum(patient[1:4])/3
    maximal = max(temperature_log[1:4])
    print(patient[0])

def classify_pressure(systolic, diastolic)
    measurements = [
        ["Jan", 118, 78],
        ["Marie", 135, 88],
        ["Petr", 125, 82],
        ["Anna", 145, 95],
        ["Tomáš", 119, 79],
        ["Eva", 142, 91]
    ]
    if systolic < 120 and diastolic < 80:
        cat = "Normal"
