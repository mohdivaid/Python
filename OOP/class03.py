class mobile:
  def __init__ (self, brand, model, price):
      self.brand =  brand
      self.model = model
      self.price = price
m1 = mobile("Iphone","17 pro","1 lakh")
m2 = mobile("Samsung","S21","50 thousand")

print(m1.brand, m1.model, m1.price)
print(m2.brand, m2.model, m2.price)