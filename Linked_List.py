from Team import Team

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)

class LinkedList:
  def __init__(self):
    self.head = None

  def __str__(self): 
    node = self.head
    nodes = []
    while node is not None:
      nodes.append(node.data)
      node = node.next
    return nodes
  
  def traverse(self):
    node = self.head
    while node is not None:
      print(node.data)
      node = node.next

  def rank_teams(self):
    node = self.head
    count=1
    while node is not None:
      node.data.setRank(count)
      node = node.next
      count+=1
    return count
  
  def last_team(self):
    node = self.head
    count=1
    while node is not None:
      node.data.setRank(count)
      node = node.next
      count+=1
    return count

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  def insert_first(self, node):
    node.next = self.head
    self.head = node

  def index(self):
    node = self.head
    count = 0
    while node is not None:
      count+=1
      node = node.next
    return count

  def insert_last(self, node):
    if self.head is None:
      self.head = node
    else:
      for current_node in self:
        pass
      current_node.next = node
  
  def get_lastRank(self):
    for current_node in self:
      pass
    return current_node.data.rank
      

    
  def remove(self, node_data):
    if self.head is None:
      raise Exception("No hay ningun equipo registrado")
  
    if self.head.data == node_data:
      self.head = self.head.next
      return

    previous_node = self.head

    for node in self:
      if node.data == node_data:
        previous_node.next = node.next
        return

      previous_node = node
    
    raise Exception("El equipo no existe")
  
  def insert_after(self, node_data, new_node):
    if self.head is None:
      raise Exception("No hay ningun equipo registrado")

    for node in self:
      if node_data == node.data:
        new_node.next = node.next
        node.next = new_node
        return

    raise Exception("El equipo no existe")


  def getElement(self, node_name):
    for node in self:
      if node_name.upper() == node.data.getName().upper():
        return node.data

  def ElementConfirmation(self, node_name):
    for node in self: 
      if node_name.upper() == node.data.getName().upper():
        return True

  def turnDict(self):
    node = self.head
    info = {}
    while node is not None:
      info[node.data.getName()] = node.data.getScore()
      node = node.next
    return info

  def getScores(self):
    lista3 = []
    for node in self:
      lista3.append(node.data.getScore())
    return lista3

  def finalScores(self, lista):
    lista.sort(reverse=True)
    print(lista)
    return(lista)

  def teamNames(self, lista):
    lista2 = []
    for score in lista:
      for node in self:
        if score == node.data.getScore():
          lista2.append(node.data.getName())
    info = {}
    counter = 0
    for x in range(len(lista2)):
      info[counter + 1] = lista2[counter]
      counter += 1
    return info
