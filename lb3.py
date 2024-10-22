orbital_radii = {}

def add_planet(planet_name, radius):
    orbital_radii[planet_name] = radius
    print(f"Додано: {planet_name} з радіусом орбіти {radius}")

def search_planet(planet_name):
    radius = orbital_radii.get(planet_name)
    if radius:
        print(f"Радіус орбіти планети {planet_name}: {radius}")
    else:
        print(f"Планету {planet_name} не знайдено")

while True:
    print("\nМеню:")
    print("1. Додати планету")
    print("2. Знайти планету")

    choice = input("Виберіть опцію (1/2): ")

    if choice == "1":
        planet_name = input("Введіть назву планети: ")
        radius = float(input("Введіть радіус орбіти: "))
        add_planet(planet_name, radius)
    elif choice == "2":
        planet_name = input("Введіть назву планети для пошуку: ")
        search_planet(planet_name)
    elif choice == "3":
        print("Програма завершена.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
