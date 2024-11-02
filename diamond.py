x = int(input("Please enter a number:"))
text = "*"
s = int(x+x)
row = int(x + 10) 
print (f"For Rows = {x}, " )
for n in range (1,x+1) :
    m = text.center(row)
    print (f"{m}")
    text += "**"
for n in range(x):
    text +="**"
for n in range(x,s):
  text = text[:-2]
  m  = text.center(row)
  print (f"{m}")
       



         