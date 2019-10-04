# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room
    self.items = []

  def add_item(self, item):
    self.items.append(item)
  
  def remove_item(self, item):
    for element in self.items:
      if element.name == item.name:
        self.items.remove(item)

  def check_items(self, name):
    item_exists = False
    for element in self.items:
      if(element.name == name):
        item_exists = True
    return item_exists

  def __str__(self):
    return f"name {self.name}, location: {self.room}"

