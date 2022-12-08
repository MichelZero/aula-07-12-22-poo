###
# autores:
# michel silva

# data: 30/11/2022
#
# Composição 
# .

# classe A
class A: 
  def __init__(self, a, b, c) -> None:
    self.a = a
    self.b = b
    self.c = c
    

# classe B
class B:
  def __init__(self, d, e) -> None:
    self.d = d
    self.e = e
    self.A = A("soma = ", 2, 4)
    
  def somaTodosNum(self):
    x = self.d + self.e + self.A.b + self.A.c
    return x
  
  
##############################################################
b1 = B(6, 8)
print(b1.somaTodosNum())