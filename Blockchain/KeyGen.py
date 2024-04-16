# Script per a generar números C random per a utilitzar posteriorment en l’encriptació dels fitxers


import os
import secrets


class KeyGenerator:
    def __init__(self, storage_file="generated_numbers.txt"):
        self.storage_file = storage_file
        self.generated_numbers = self.load_generated_numbers()


    def load_generated_numbers(self):
        generated_numbers = set()
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                for line in f:
                    number = int(line.strip())
                    generated_numbers.add(number)
        return generated_numbers


    def save_generated_numbers(self):
        with open(self.storage_file, 'w') as f:
            for number in self.generated_numbers:
                f.write(str(number) + '\n')


    def generate_unique_number(self, min_value, max_value):
        number = None
        while True:
            number = secrets.randbelow(max_value - min_value) + min_value
            if number not in self.generated_numbers:
                self.generated_numbers.add(number)
                self.save_generated_numbers()
                print("Número aleatori generat:", number)
                break
        return number


# Exemple d'ús
key_generator = KeyGenerator(storage_file="C:\\Users\\ensierrar\\Desktop\\R\\generated_numbers.txt")
numero_aleatori = key_generator.generate_unique_number(1000, 9999)  # Genera un número aleatori entre 1000 i 9999
print("Número aleatori generat:", numero_aleatori)
