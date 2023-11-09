N = int(input())
M = int(input())
summa = 0
number = []
k = 1
if (N*(N+1))/2 >= M:
   while summa < N:
      for a in range(k, N):
         summa += a
         number.append(a)
         if summa > N:
            summa = 0
            number.clear()
         if summa == M:
            for i in number:
               print(i)
            break
      k += 1
else:
   print(0)





