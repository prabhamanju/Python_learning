'''
The format() method takes the passed arguments, formats them, and places them in the string where 
the placeholders {} are
'''

quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want to pay {} dollars for {} pieces of item {}."
print(myOrder.format(quantity, itemNo, price)) 

#use index numbers {0} to be sure the arguments are placed in the correct placeholders:
myOrder = "I want to pay {2} dollars for {1} pieces of item {0}."
print(myOrder.format(quantity, itemNo, price)) 
