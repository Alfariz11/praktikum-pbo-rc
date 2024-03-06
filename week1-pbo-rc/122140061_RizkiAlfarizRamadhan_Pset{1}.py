import time
import random

class Character:
    def __init__(self, name, health, attack_min, attack_max, defense):
        self.name = name
        self.health = health
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_opponent(self, opponent):
        damage = random.randint(self.attack_min, self.attack_max) - opponent.defense
        if damage > 0:
            opponent.take_damage(damage)
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {opponent.name}, but the attack is blocked!")

class Action:
    def __init__(self, character):
        self.character = character

    def execute(self, opponent):
        pass

class AttackAction(Action):
    def execute(self, opponent):
        self.character.attack_opponent(opponent)

class DefenseAction(Action):
    def execute(self, opponent):
        self.character.defense += 1
        print(f"{self.character.name} goes into defense mode! Defense increased by 1!")

class GiveUpAction(Action):
    def execute(self, opponent):
        print(f"{self.character.name} gives up!")
        opponent.wins = True

class Game:
    def __init__(self):
        self.atreus = Character("Atreus", 500, 5, 15, 10)
        self.daedalus = Character("Daedalus", 750, 8, 12, 8)
        self.current_round = 1
        self.winner = None

    def start(self):
        while not self.winner:
            print(f"\nRound-{self.current_round}")
            print(f"{self.atreus.name} | {self.atreus.health}|{self.atreus.defense}|")
            print(f"{self.daedalus.name} | {self.daedalus.health}|{self.daedalus.defense}|")
            self.current_round += 1

            if not self.atreus.is_alive():
                self.winner = self.daedalus
                print(f"{self.daedalus.name} wins!")
                break

            if not self.daedalus.is_alive():
                self.winner = self.atreus
                print(f"{self.atreus.name} wins!")
                break

            print(f"{self.atreus.name}, Select the action: 1. Attack, 2. Defense")
            action_input = int(input())
            if action_input == 1:
                AttackAction(self.atreus).execute(self.daedalus)
            elif action_input == 2:
                DefenseAction(self.atreus).execute(self.atreus)

            print(f"{self.daedalus.name}, Select the action: 1. Attack, 2. Defense, 3. Give up")
            action_input = int(input())
            if action_input == 1:
                AttackAction(self.daedalus).execute(self.atreus)
            elif action_input == 2:
                DefenseAction(self.daedalus).execute(self.daedalus)
            elif action_input == 3:
                GiveUpAction(self.daedalus).execute(self.atreus)
                self.winner = self.atreus
                break

            time.sleep(1)

if __name__ == "__main__":
    game = Game()
    game.start()