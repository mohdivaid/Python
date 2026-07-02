#Write a program to calculate profit or loss.
cost_price=2000
selling_price=1200 
if(selling_price>cost_price):
    profit=selling_price-cost_price
    print("profit gets:",profit)
elif(cost_price>selling_price):    
    loss=cost_price-selling_price
    print("loss:",loss)