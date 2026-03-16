# records = [
#     ("ORD-001", 2, 499),
#     ("ORD-002", 8, 149),
#     ("ORD-003", 1, 1299),
#     ("ORD-004", 5, 89),
#     ("ORD-005", 10, 59),
# ]
#
# orders = [
#     {"id": oid, "kusy": kusy, "cena_za_kus": cena}
#     for oid, kusy, cena in records
# ]
#
# big_orders = [
#     o for o in orders
#     if o["kusy"] >= 5 or o["cena_za_kus"] >= 1000
# ]
#
# report = [
#     f'{o["id"]}: celkem {o["kusy"] * o["cena_za_kus"]} Kč'
#     for o in big_orders
# ]
#
# print("Počet všech objednávek:", len(orders))
# print("Počet větších objednávek:", len(big_orders))
#
# for r in report:
#     print(r)

# with open("data/lab_notes.txt", mode="r", encoding="utf-8") as file:
#     content = file.read()
# print(content)
#
# import json
#
# with open("data/limits.json", "r") as file:
#     limits = json.load(file)
#
# print(limits)
# print(type(limits))

git config --global user.name "Tvoje Jmeno"