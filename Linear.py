products=["Pen","Pencil","Eraser","Scale","Pencil","pen"]
def Linear_Search_product(targetProduct):
  indices=[]
  for index,items in enumerate(products):
    if(targetProduct==items):
      indices.append(index)
  return indices

target="pencil"
print(Linear_Search_product(target))