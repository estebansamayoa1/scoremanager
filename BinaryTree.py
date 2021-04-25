class Node:
    def __init__(self, equipo1, equipo2):
        self.data = None
        self.left_child = equipo1
        self.right_child = equipo2


    def get_children(self):
        children = []
        if self.left_child is not None:
            children.append(self.left_child.data)
        if self.right_child is not None:
            children.append(self.right_child.data)
        return children

    def getdata(self, equipo1, equipo2):
        if equipo1==True:
            self.data=equipo1
        if equipo2==True:
            self.data=equipo2
        return self.data

  
    def __repr__(self):
        return "Data: " + str(self.getdata(True, False)) + ", Children: " + str(self.get_children())


class BinaryTree:
  def __init__(self):
    self.root = None
    self.left_child=None
    self.right_child=None


  def insert(self, root, equipo1, equipo2):
    if root is None:
      self.root = Node(equipo1, equipo2)
      return

    if equipo1.winner == True:
      if root.left_child is None:
        root.left_child = Node(equipo1, equipo2)
        return
      else:
        self.insert(root.left_child, equipo1, equipo2)
    
    if equipo2.winner == True:
      if root.right_child is None:
        root.right_child = Node(equipo1, equipo2)
        return
      else:
        self.insert(root.right_child, equipo1, equipo2)


  def inorder_traverse(self, root):
    if root is not None:
      self.inorder_traverse(root.left_child)
      print(root.data)
      self.inorder_traverse(root.right_child)
    
  
  def search(self, root, key):
    if root is None:
      return "Key not found in tree :("

    if root.data == key:
      return root
    
    if root.data > key:
      return self.search(root.left_child, key)
    
    if root.data < key: 
      return self.search(root.right_child, key)


  def find_min(self, root):
    current_node = root

    while current_node.left_child is not None:
      current_node = current_node.left_child

    return current_node


  def find_max(self, root):
    current_node = root

    while current_node.right_child is not None:
      current_node = current_node.right_child

    return current_node