import random as r
x='i love sweets'
print(r.sample(x,2))

#everytime it gives different output
a=[1,2,3,4]


r.shuffle(a)
print(a)

a=[1,2,3,4,5,6]
print(r.choice(a))

b="welcome back"
print(r.choice(b))

a=r.random()
print(a)
#will  return random under number  between 0.0 to 1.0
#0.0 includes 1.0 execludes

print(r.randint(20,30))

a=[10,20,30,40,50]
print(r.choices(a,k=10))

s="hello ggood day"
print(r.choices(s,k=30))

print(r.uniform(5,10))


