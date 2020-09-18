

class Node:
  def __init__(self, load=None, next=None):
    """
    Set node with two params:
    load: data inside node
    next: the node to each this node points to

    If they are not setted, they are equal to None
    """
    self.load = load
    self.next = next

  def __str__(self):
    """
    Return node's load
    """
    return str(self.load)