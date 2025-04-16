strana_stol = {
    "Россия": "Москва",
    "Беларусь": "Минск",
    "Испания": "Барселона",
    "Италия": "Рим"
}

print ("Все пары стран и столиц:")
for strana, stol in strana_stol.items():
    print(f"{strana}: {stol}")


spec_strana =input(("\nВведите страну:"))
spec_strana=spec_strana.capitalize()

if spec_strana in strana_stol:
    print(f"Страна {spec_strana}, столица {strana_stol[spec_strana]}")
else:
    print(f"Страна {spec_strana} не найдена в перечне" )


sorted_strana=sorted(strana_stol.keys())
print("\nСписок стран и столиц в алфавитном порядке:")
for strana in sorted_strana:
    print(f"{strana}: {strana_stol[strana]}")