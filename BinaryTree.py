class Nodes:
  def __init__(self, data):
    self.data = data
    self.left_child = None
    self.right_child = None


  def get_children(self):
    children = []
    if self.left_child is not None:
      children.append(self.left_child.data)
    if self.right_child is not None:
      children.append(self.right_child.data)
    return children


  def visualization(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left_child:
                next_level.append(n.left_child)
            if n.right_child:
                next_level.append(n.right_child)
        current_level = next_level
       

  def __repr__(self):
    return str(self.data)
    #return str(self.data) + "\n" + str(self.get_children()) + "\n"




class BinarySearchTree:
  def __init__(self):
    self.root = None


  def insert(self, root, value):
    if root is None:
      self.root = Nodes(value)
      return

    if root.data > value:
      if root.left_child is None:
        root.left_child = Nodes(value)
        return
      else:
        self.insert(root.left_child, value)
    
    if root.data < value:
      if root.right_child is None:
        root.right_child = Nodes(value)
        return
      else:
        self.insert(root.right_child, value)

    
  
  def search(self, root, key):
    if root is None:
      return "not a team in this championship"

    if root.data == key:
      return root
    
    if root.data > key:
      return self.search(root.left_child, key)
    
    if root.data < key: 
      return self.search(root.right_child, key)

  