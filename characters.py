class Character:
  def __init__(self, name, health, damage):
    self.name = name
    self.health = health
    self.damage = damage

  def attack(self, other):
    other.health -= self.damage
    print(f"{self.name} attacks {other.name} for {self.damage} damage!")

  def is_alive(self):
    return self.health > 0

player = Character("Player", 100, 20)