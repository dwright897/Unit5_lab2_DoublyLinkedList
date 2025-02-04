#Dalton Wright
#DoublyLinkedList
#1-27-25

class DoublyLinkedList:
  class DoublyNode:
    def __init__(self, value):
      """Creates a new node with a given value"""
      self.value = value
      self.prev = None
      self.next = None

    def set_prev(self, node):
      """sets previous pointer"""
      if node != None:
        if node.next == None or node.prev == None:
          self.prev = node
        else:
          raise TypeError("Previous must be a DoublyNode Object")
      else:
        self.prev = None      
    def set_next(self, node):
      """Sets the next pointer to a new DoublyNode"""
      if node != None:
        if node.prev == None or node.next ==None:
          self.next = node

        else:
          raise TypeError("Next must be a DoublyNode Object")
      else:
        self.next = node
    # SinglyNode to-string
    def __str__(self):
      """Provided str to produce output"""
      return f"|{self.value}|"
  
  def __init__(self):
    """create an empty Doubly linked list"""
    self.head = None
    self.tail = None
    self.__size = 0
  def head_insert(self, value):
    """inserts a new node at head"""
    new_node = self.DoublyNode(value)
    if self.__is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      new_node.set_next(self.head)
      self.head.set_prev(new_node)
      self.head = new_node
    self.__size +=1
  
  def tail_insert(self, value):
    """insert a new node at the tail of the list"""
    new_node = self.DoublyNode(value)
    if self.__is_empty() == True:
      self.head = new_node
      self.tail = new_node
    else:
      if self.tail is not None:
        new_node.set_prev(self.tail)
        self.tail.set_next(new_node)
      self.tail = new_node
    self.__size +=1

  def head_remove(self):
    """removes the node at the head of the list"""
    if self.__is_empty():
      raise IndexError("Remove from empty list")
    value = self.head.value
    self.head = self.head.next
    if self.head != None:
      self.head.set_prev(None)
    else:
      self.tail = None
    self.__size -=1
    return value

  def tail_remove(self):
    """removes and returns the value of the tail node"""
    if self.__is_empty():
      raise IndexError("Remove from empty list")
    value = self.tail.value
    self.tail = self.tail.prev
    if self.tail is not None:
      self.tail.set_next(None)
    else:
      self.head = None
    self.__size -=1
    return value
  
  def __is_empty(self):
    """returns True if the list is empty"""
    return self.__size == 0
  def __len__(self):
    """returns the size of the list"""
    return self.__size
  
  def __str__(self):
    """Provided str to produce output"""
    out = "HEAD > "

    walk = self.head
    for i in range(self.__size):
        out += f"{walk} "
        walk = walk.next
        if walk != None:
            out += "<-> "

    out += "< TAIL"
    return out

   
