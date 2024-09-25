'''
 n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a + b) 
'''
n = int(input())
peppers = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 40000,
    "Habanero": 125000
    }
t = 0
for i in range(n):
    pepper = input()
    t += peppers[pepper]
print(t)