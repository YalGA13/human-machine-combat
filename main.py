import time

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Терминатор")

    def start(self):
        print("Битва начинается!")
        print(f"Игрок: {self.player}")
        print(f"Противник: {self.computer}\n")

        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f" Раунд {round_number}")
            self.player.attack(self.computer)
            print(f"Осталось у {self.computer.name}: {self.computer.health} HP\n")
            if not self.computer.is_alive():
                print("Победа! Терминатор is dead!")
                break

            time.sleep(1)

            self.computer.attack(self.player)
            print(f"Осталось у {self.player.name}: {self.player.health} HP\n")
            if not self.player.is_alive():
                print("Поражение! Терминатор победил.")
                break

            time.sleep(1)
            round_number += 1

        print("\nИгра окончена.")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
