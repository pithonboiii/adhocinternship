#take a list say  adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
#write the program that will do
#  i)  print only those numbers greater than 5
#  ii)  also print those numbers those are less than or  equals to 2  ( <= 2 )
#  iii)  store these answers in in two different list also
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
print(adhoc)

first= [i for i in adhoc if i>5]	
print(first)
second=[j for j in adhoc if j<=2]
print(second)	
