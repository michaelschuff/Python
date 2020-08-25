t=0
num=int(input())
decimal=int(input())
for x in range(num):
    t+=round(float(input()),decimal)
print(round(t,decimal))