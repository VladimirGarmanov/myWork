for a in range(1,1000):
   for b in range(1,1000):
      for c in range(1,1000):
         if (a*b)/c + (a*c)/b + (b*c)/a == 3:
            print(a,b,c)