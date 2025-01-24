# Sorting the list based on first item of each inner list
items = [[2, 7], [7, 3], [3, 8], [8, 7], [9, 7], [4, 9]]
sort_first_item = sorted(items,key=lambda item:[0])
print(sort_first_item)

#Sorting the list based on last item of each inner list
sort_last_item=sorted(items,key=lambda item:item[-1])
print(sort_last_item)

# Sorting Dictionary based on values
my_dict={'a':4,'b':3,'c':2,'d':1}
sort_dict=sorted(my_dict.items(),key=lambda item:item[1])
print(sort_dict)

# Sorting Dictionary based on share prices
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB':10.34}

ss_prices=sorted(prices.items(),key=lambda d:d[-1] )
print(ss_prices)  #Based on value
s_prices=sorted(prices.items(),key=lambda d:d[1])
print(s_prices)   #Based on value

s_prices=sorted(prices.items(),key=lambda d:d[0])
print(s_prices)  #Based on key

#max and minimum prices
max_price=max(ss_prices,key=lambda item:item[-1])
min_price=min(ss_prices,key=lambda item:item[-1])
#print both the values
print(max_price)
print(min_price)
