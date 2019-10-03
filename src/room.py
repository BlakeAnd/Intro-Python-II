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

  def directions(self):
    dir = "("
    if self.n_to:
      dir = dir + " n "
    if self.s_to:
      dir = dir + " s "
    if self.e_to:
      dir = dir + " e "
    if self.w_to:
      dir = dir + " w "
    dir = dir + ")"
    return dir

  def __repr__(self):
    return f"{repr(self.name)}"
