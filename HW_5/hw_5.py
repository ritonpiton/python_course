import random


class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


class Individual:
    def __init__(self, age, satiation, gender, last_ate_at):
        self.age = int(age)
        self.satiation = int(satiation)
        self.gender = gender
        self.last_ate_at = last_ate_at


class Animal:
    def __init__(self, name, size, diet, habitat, lifespan):
        self.name = name
        self.size = size
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.individuals = []

    def add_individual(self, age, satiation, gender, last_ate_at):
        self.individuals.append(Individual(age, satiation, gender, last_ate_at))

    def get_individual_age(self, age):
        if age.isdigit() and int(age) <= self.lifespan:
            return True
        return False

    def reproduce(self, move_num):
        males = [individual for individual in self.individuals if individual.gender == 'M']
        females = [individual for individual in self.individuals if individual.gender == 'F']

        pairs = min(len(males), len(females))

        for i in range(pairs):
            male = males[i]
            female = females[i]

            if self.habitat == 'Water' and male.satiation > 50 and female.satiation > 50:
                for _ in range(10):
                    self.add_individual(0, 23, random.choice(['M', 'F']), move_num)
            elif self.habitat == 'Air' and male.satiation > 42 and female.satiation > 42 and male.age > 3 and female.age > 3:
                for _ in range(4):
                    self.add_individual(0, 64, random.choice(['M', 'F']), move_num)
            elif self.habitat == 'Land' and male.satiation > 20 and female.satiation > 20 and male.age > 5 and female.age > 5:
                for _ in range(2):
                    self.add_individual(0, 73, random.choice(['M', 'F']), move_num)

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Size: {self.size}')
        print(f'Diet: {self.diet}')
        print(f'Habitat: {self.habitat}')
        print(f'Lifespan: {self.lifespan} years')
        print(f'Individuals: {len(self.individuals)}')
        for idx, individual in enumerate(self.individuals, start=1):
            print(
                f'  Individual {idx}: Age {individual.age} years, Satiation {individual.satiation}, Gender {individual.gender}, Last ate at: {individual.last_ate_at}')
        print()


class Planet:
    def __init__(self):
        self.animals = []
        self.plant_food_supply = 1000
        self.SIZE_CONVERT = {'XS': 1, 'S': 2, 'M': 3, 'L': 4, 'XL': 5}

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_all_animals(self):
        for animal in self.animals:
            animal.display_info()

    def find_animal_by_name(self, animal_name):
        for animal in self.animals:
            if animal.name.lower() == animal_name.lower():
                return animal
        return None

    def increase_plant_food_supply(self, amount):
        if str(amount).isdigit():
            self.plant_food_supply += int(amount)
            print(
                colors.GREEN + f'Plant food supply increased by {amount}. Current supply: {self.plant_food_supply}' + colors.END)
        else:
            print(colors.RED + 'Invalid amount.' + colors.END)

    def decrease_plant_food_supply(self, amount):
        if str(amount).isdigit():
            if (self.plant_food_supply-int(amount)) <= 0:
                self.plant_food_supply=0
            else:
                self.plant_food_supply -= int(amount)

    def _manage_ages_of_animals(self):
        for animal in self.animals:
            for individual in animal.individuals[:]:
                individual.age += 1
                if individual.age >= animal.lifespan:
                    self.increase_plant_food_supply(self.SIZE_CONVERT[animal.size])
                    animal.individuals.remove(individual)

    def _manage_plant_animals_satiation(self, plant_animals, move_num):
        for animal in plant_animals:
            for individual in animal.individuals:
                if self.plant_food_supply > 0:
                    self.decrease_plant_food_supply(1)
                    if individual.satiation <= 74:
                        individual.satiation += 26
                    else:
                        individual.satiation = 100
                    individual.last_ate_at = move_num

    def _manage_meat_animals_satiation(self, meat_animals, move_num):
        potential_preys = self.animals

        for predator in meat_animals:
            for individual in predator.individuals[:]:
                if random.choice([1, 1]):
                    if potential_preys:
                        random_prey_animal = random.choice(potential_preys)
                        if random_prey_animal.individuals:
                            random_prey_individual = random.choice(random_prey_animal.individuals)
                            if (random_prey_animal.name is not predator.name and
                                    random_prey_animal.habitat == predator.habitat and
                                    self.SIZE_CONVERT[random_prey_animal.size] <= self.SIZE_CONVERT[predator.size]):
                                random_prey_animal.individuals.remove(random_prey_individual)
                                if individual.satiation <= 47:
                                    individual.satiation += 53
                                else:
                                    individual.satiation = 100
                                individual.last_ate_at = move_num
                else:
                    individual.satiation -= 16

    def _manage_not_ate_animals(self, move_num):
        for animal in self.animals:
            for individual in animal.individuals:
                if individual.last_ate_at is not move_num:
                    individual.satiation -= 9

    def _manage_hungry_animals_population(self):
        for animal in self.animals:
            for individual in animal.individuals[:]:
                if individual.satiation < 10:
                    self.increase_plant_food_supply(self.SIZE_CONVERT[animal.size])
                    animal.individuals.remove(individual)

    def make_alive(self, move_num):
        print(colors.GREEN + f'Current plant supply: {self.plant_food_supply}' + colors.END)

        plant_animals = [animal for animal in self.animals if animal.diet == 'Plant']
        meat_animals = [animal for animal in self.animals if animal.diet == 'Meat']

        for animal in self.animals:
            animal.reproduce(move_num)

        self._manage_ages_of_animals()
        self._manage_plant_animals_satiation(plant_animals, move_num)
        self._manage_meat_animals_satiation(meat_animals, move_num)
        self._manage_not_ate_animals(move_num)
        self._manage_hungry_animals_population()

        self.display_all_animals()


def main_menu(planet, animals_details):
    move_num = 1

    while True:
        print('\n1. Add individual to a animal')
        print('2. Increase plant food supply')
        print('3. Display current characteristics of all animal')
        print('4. Generate random filling of the planet')
        print(colors.YELLOW + '5. Make 1 move' + colors.END)
        print('6. Exit')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                animal_name = input('Enter animal name: ')
                animal: Animal = planet.find_animal_by_name(animal_name)

                if animal:
                    age = input('Enter age: ')
                    valid_age = animal.get_individual_age(age)

                    if valid_age:
                        satiation = input('Enter satiation level (x/100): ')

                        if satiation.isdigit() and 0 <= int(satiation) <= 100:
                            gender = input('Enter gender (M/F): ').upper()

                            if gender == 'M' or gender == 'F':
                                animal.add_individual(age, satiation, gender, move_num)
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
                initialize_random_animals(planet, animals_details)
            case '5':
                planet.make_alive(move_num)
                move_num += 1
            case '6':
                exit()
            case _:
                print(colors.RED + 'Invalid choice. Please try again.' + colors.END)


def initialize_animals(planet, animals_details):
    for details in animals_details:
        animal = Animal(details.name, details.size, details.diet, details.habitat, details.lifespan)
        animal.individuals = []
        planet.add_animal(animal)
    planet.display_all_animals()


def initialize_random_animals(planet, animals_details):
    print(colors.BLUE + 'Generating...' + colors.END)

    planet.animals = []

    for details in animals_details:
        animal = Animal(details.name, details.size, details.diet, details.habitat, details.lifespan)
        num_individuals = random.randint(0, 5)
        for _ in range(num_individuals):
            age = random.randint(0, details.lifespan)
            satiation = random.randint(0, 100)
            gender = random.choice(['M', 'F'])
            last_ate_at = 0
            animal.add_individual(age, satiation, gender, last_ate_at)
        planet.add_animal(animal)

    planet.display_all_animals()


def main():
    animals_details = [
        Animal('Lion', 'L', 'Meat', 'Land', 14),
        Animal('Snake', 'S', 'Meat', 'Land', 10),
        Animal('Bear', 'L', 'Meat', 'Land', 25),
        Animal('Gazelle', 'M', 'Plant', 'Land', 15),
        Animal('Deer', 'M', 'Plant', 'Land', 20),
        Animal('Eagle', 'M', 'Meat', 'Air', 20),
        Animal('Parrot', 'S', 'Plant', 'Air', 50),
        Animal('Falcon', 'S', 'Meat', 'Air', 15),
        Animal('Whale', 'XL', 'Meat', 'Water', 90),
        Animal('Shark', 'L', 'Meat', 'Water', 30),
        Animal('Dolphin', 'M', 'Meat', 'Water', 50),
        Animal('Fish', 'S', 'Plant', 'Water', 10)
    ]

    planet = Planet()
    initialize_animals(planet, animals_details)
    main_menu(planet, animals_details)


main()
