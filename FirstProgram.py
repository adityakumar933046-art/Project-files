salary = int(input("enter salary: "))
if salary <=100000:
   tax =0
   print("your tax is",tax)
elif 100000 <salary <=500000:
   tax=(salary-100000)*0.1
   print("your tax is",tax)
elif salary>500000:
   tax=(salary-500000)*0.2+50000
   print("your tax is" ,tax)
 

