#Dalton Wright
#SinglyLinkedList
#1-27-25

class SinglyLinkedList:
  class SinglyNode:
    def __init__(self, value):
      """Creates a new node with a given value"""
      self.value = value
      self.next = None

    def set_next(self, node):
      """Sets the next pointer to a new SinglyNode"""
      try:
        node.next
      except:
        raise TypeError("Next must be a SinglyNode Object")
      self.next = node
    # SinglyNode to-string
    def __str__(self):
      """Provided str to produce output"""
      return f"|{self.value}|"
  
  def __init__(self):
    """create an empty Singly linked list"""
    self.head = None
    self.tail = None
    self.__size = 0
  def head_insert(self, value):
    """inserts a new node at head"""
    new_node = self.SinglyNode(value)
    if self.__is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node
    self.__size +=1
  
  def tail_insert(self, value):
    """insert a new node at the tail of the list"""
    new_node = self.SinglyNode(value)
    if self.__is_empty() == True:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
    self.__size +=1

  def head_remove(self):
    """removes the node at the head of the list"""
    if self.__is_empty():
      raise IndexError("Remove from empty list")
    value = self.head.value
    self.head = self.head.next
    if self.head is None:
      self.tail = None
    self.__size -=1
    return value
  def __is_empty(self):
    """returns True if the list is empty"""
    return self.__size == 0
  def __len__(self):
    """returns the size of the list"""
    return self.__size
  # SinglyLinkedList to-string
  def __str__(self):
    """Provided str to produce output"""
    out = "HEAD > "

    walk = self.head
    for i in range(self.__size):
        out += f"{walk} "
        walk = walk.next
        if walk != None:
            out += "-> "

    out += "< TAIL"
    return out

