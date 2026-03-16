# age_text = "25"
# age = int(age_text)
# print(type(age_text))  # <class 'str'>
# print(type(age))       # <class 'int'>
# print(age + 5)  # 30
#
# price_text = "19.99"
# price = float(price_text)
# print(type(price_text))  # <class 'str'>
# print(type(price))       # <class 'float'>
# print(price * 2)  # 39.98

# score = 100
# print(type(score))  # <class 'int'>
# message = "Skóre: " + str(score)
# print(type(message))  # <class 'str'>
# print(message)  # "Skóre: 100"
#
# jmeno = input("Zadej své jméno: ")
# print(f"Ahoj, {jmeno}!")


# print("=== Registrace pacienta ===")
# name = input("Jméno: ")
# age = input("Věk: ")  # ⚠️ Vrací STRING, ne číslo!
# allergies = input("Alergie (oddělené čárkou): ")
#
# print(f"\nPacient: {name}")
# print(f"Věk: {age} let")
# print(f"Alergie: {allergies}")
#
# #fahrenheit_text = "67"
# fahrenheit_text = input("Zadej: F:")
#
# fahrenheit = float(fahrenheit_text)
# celsius = (fahrenheit - 32) * 5/9
# print(f"{fahrenheit} °F je {celsius} °C")

#heslo = "xdd"
#heslo = "hahahahah"

# heslo = input("Zadej heslo: ")
#
# delka = len(heslo)
# print(f"Tvoje heslo má {delka} znaků.")
#
# if delka < 8 :
#     print(f"Heslo je příliš krátké!")

# nemocnice = input("Zadej název nemocnice: ")
# oddeleni = input("Zadej název oddělení: ")
#
# cara = "=" * 30
#
# print(cara)
# print(nemocnice + " - " + oddeleni)
# print(cara)
#
# bmi_weight = 75  # kg
# bmi_height = 1.80  # m
#
# # Výpočet přímo v f-stringu:
# print(f"BMI: {bmi_weight / (bmi_height ** 2):.1f}")
# # "BMI: 23.1"

# systolic = int(input("systolic:"))
# diastolic = int(input("diastolic:"))
# MAP = (systolic + 2 * diastolic) / 3
# print(f"{MAP:.1f}")

# print("abcdefgh"[2:6])       # "cdef"
# print("abcdefgh"[::3])        # "adg"
# print("Python"[::-1])         # "nohtyP" (otočení)
# print("Programming"[1:10:2])  # "rgamn" (od 1 do 10, každý druhý)
#
# # Praktické použití - kontrola DNA sekvence
# dna = "ACGTTAGCTA"
# first_codon = dna[0:3]    # První kodon: "ACG"
# print(f"První kodon: {first_codon}")
#
# # Otočení řetězce (reverzní sekvence)
# reversed_dna = dna[::-1]
# print(f"Reverzní sekvence: {reversed_dna}")
#
# rodne_cislo = input("Zadejte rodne cislo: ")
# rok = rodne_cislo[0:2]
# mesic = rodne_cislo[2:4]
# den = rodne_cislo[4:6]
#
# print(f"datum narozeni: {den} . {mesic} . 20{rok}")

# word = "Python"
#
# for character in word:
#     print(character)
#


# dna = "ACGTTAGCTA"
#
# gc_count = 0
#
# for znak in dna:
#     if znak == "G" or znak == "C":
#         gc_count += 1
#
# print("GC obsah:", gc_count, "znaků")

temperature = float(input("Teplota: "))  # Uživatel zadal "37.5"
if temperature > 38:  # 🔴 Breakpoint
    print("Horečka!")