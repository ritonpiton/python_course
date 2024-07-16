class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


class Individual:
    def __init__(self, age, satiation, gender):
        self.age = age
        self.satiation = satiation
        self.gender = gender


class Animal:
    def __init__(self, name, size, diet, habitat, lifespan):
        self.name = name
        self.size = size
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.individuals = []

    def add_individual(self, age, satiation, gender):
        self.individuals.append(Individual(age, satiation, gender))

    def get_individual_age(self, age):
        if age.isdigit() and int(age) <= self.lifespan:
            return True
        return False

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Size: {self.size}')
        print(f'Diet: {self.diet}')
        print(f'Habitat: {self.habitat}')
        print(f'Lifespan: {self.lifespan} years')
        print(f'Individuals: {len(self.individuals)}')
        for idx, individual in enumerate(self.individuals, start=1):
            print(
                f'  Individual {idx}: Age {individual.age} years, Satiation {individual.satiation}, Gender {individual.gender}')
        print()


class Planet:
    def __init__(self):
        self.animals = []
        self.plant_food_supply = 1000

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_all_animals(self):
        for animal in self.animals:
            animal.display_info()

    def find_animal_by_name(self, species_name):
        for animal in self.animals:
            if animal.name.lower() == species_name.lower():
                return animal
        return None

    def increase_plant_food_supply(self, amount):
        if amount.isdigit():
            self.plant_food_supply += int(amount)
            print(colors.GREEN + f'Plant food supply increased by {amount}. Current supply: {self.plant_food_supply}' + colors.END)
        else:
            print(colors.RED + 'Invalid amount.' + colors.END)

def main_menu(planet):
    while True:
        print('\n1. Add individual to a species')
        print('2. Increase plant food supply')
        print('3. Display current characteristics of all species')
        print('4. Exit')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                species_name = input('Enter species name: ')
                animal: Animal = planet.find_animal_by_name(species_name)

                if animal:
                    age = input('Enter age: ')
                    valid_age = animal.get_individual_age(age)

                    if valid_age:
                        satiation = input('Enter satiation level (x/100): ')

                        if satiation.isdigit() and 0 <= int(satiation) <= 100:
                            gender = input('Enter gender (M/F): ')

                            if gender == 'M' or gender == 'F':
                                animal.add_individual(age, satiation, gender)
                                print(colors.GREEN + 'Individual added.' + colors.END)
                            else:
                                print(colors.RED + 'Incorrect gender.' + colors.END)
                        else:
                            print(colors.RED + 'Incorrect satiation.' + colors.END)
                    else:
                        print(colors.RED + 'Invalid age.' + colors.END)
                else:
                    print(colors.RED + 'Species not found.' + colors.END)
            case '2':
                amount = input('Enter amount to increase plant food supply: ')
                planet.increase_plant_food_supply(amount)
            case '3':
                planet.display_all_animals()
            case '4':
                exit()
            case _:
                print(colors.RED + 'Invalid choice. Please try again.' + colors.END)


def initialize_animals(planet):
    animal_species = [
        Animal('Lion', 'L', 'Meat', 'Land', 14),
        # Animal('Elephant', 'XL', 'Plant', 'Land', 60),
        # Animal('Eagle', 'M', 'Meat', 'Air', 20),
        # Animal('Shark', 'L', 'Meat', 'Water', 30),
        # Animal('Penguin', 'M', 'Meat', 'Water', 20),
        # Animal('Giraffe', 'L', 'Plant', 'Land', 25),
        # Animal('Snake', 'S', 'Meat', 'Land', 10),
        # Animal('Butterfly', 'XS', 'Plant', 'Air', 1),
        # Animal('Bear', 'L', 'Meat', 'Land', 25),
        # Animal('Whale', 'XL', 'Meat', 'Water', 90),
        # Animal('Parrot', 'S', 'Plant', 'Air', 80),
        # Animal('Dolphin', 'M', 'Meat', 'Water', 50)
    ]

    for species in animal_species:
        planet.add_animal(species)

    planet.display_all_animals()


def main():
    planet = Planet()
    initialize_animals(planet)
    main_menu(planet)


main()
