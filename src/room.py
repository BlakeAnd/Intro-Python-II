# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.w_to = None
    self.e_to = None
    self.items = []

  def add_item(self, item):
    self.items.append(item)
  
  def remove_item(self, item):
    for element in self.items:
      if(element.name == item.name):
        self.items.remove(item)

  def check_items(self, name):
    item_exists = False
    for element in self.items:
      if(element.name == name):
        item_exists = True
    return item_exists

  def directions(self):
    dir = "("
    if self.n_to:
      dir = dir + " north "
    if self.s_to:
      dir = dir + " south "
    if self.e_to:
      dir = dir + " east "
    if self.w_to:
      dir = dir + " west "
    dir = dir + ")"
    return dir

  def __repr__(self):
    return f"{repr(self.name)}"
