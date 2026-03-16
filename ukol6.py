# function_design.py

def analyze_password(
    password,
    min_length=8,
    require_digit=True,
    require_upper=True,
    require_symbol=False,
    banned_words=None
):
    # výchozí zakázaná slova
    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']

    symbols = "!@#$%^&*()-_=+[]{};:,.?"

    missing_rules = []
    total_rules = 0
    passed_rules = 0

    # 1) minimální délka
    total_rules += 1
    if len(password) >= min_length:
        passed_rules += 1
    else:
        missing_rules.append("min_length")

    # 2) číslice
    if require_digit:
        total_rules += 1
        if any(c.isdigit() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("digit")

    # 3) velké písmeno
    if require_upper:
        total_rules += 1
        if any(c.isupper() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("upper")

    # 4) symbol
    if require_symbol:
        total_rules += 1
        if any(c in symbols for c in password):
            passed_rules += 1
        else:
            missing_rules.append("symbol")

    # 5) zakázaná slova
    total_rules += 1
    password_lower = password.lower()
    if any(word.lower() in password_lower for word in banned_words):
        missing_rules.append("banned_word")
    else:
        passed_rules += 1

    score_percent = int((passed_rules / total_rules) * 100)
    is_strong = len(missing_rules) == 0

    return is_strong, score_percent, missing_rules


# -------------------------
# TESTOVACÍ VOLÁNÍ FUNKCE
# -------------------------

# 1) čistě poziční argumenty
print(analyze_password("Tanicka1501", 8, True, True, True, None))
print("Komentář: Použití pouze pozičních argumentů je krátké, ale hůře čitelné. "
      "Není na první pohled jasné, co jednotlivé hodnoty znamenají, "
      "zejména u více parametrů.\n")


# 2) mix pozičních a pojmenovaných argumentů
print(analyze_password("Tanicka1501*", 10, require_symbol=True))
print("Komentář: Kombinace pozičních a pojmenovaných argumentů zlepšuje čitelnost. "
      "Základní parametry mohou být poziční a méně časté lze pojmenovat.\n")


# 3) volání s vypnutým pravidlem pro symbol
print(analyze_password("Test1234", require_symbol=False))
print("Komentář: Použití pojmenovaného argumentu zde jasně říká, "
      "že pravidlo pro symbol je vypnuté. Je to přehlednější než spoléhat "
      "na pořadí parametrů.\n")


# 4) vlastní seznam banned_words
print(analyze_password(
    "Admin123!",
    require_symbol=True,
    banned_words=["admin", "root", "test"]
))
print("Komentář: Pojmenované argumenty jsou zde nejčitelnější, protože "
      "je okamžitě jasné, že měníme seznam zakázaných slov. "
      "U složitějších funkcí je tento styl nejbezpečnější.")