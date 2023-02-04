q1="""do you have brain?
a.naaku ledu
b.neek vundi
c.neeku ledu
d.naku vundi """


q2="""who invented engineering?
a.Imhotep
b.ainstene
c.viswesaraya
d.Ayyalasomayajula Lalitha"""


q3="""who makes yo happy?
a.your friend
b.your family
c.your lover
d.your mobile"""


q4="""will let you know other peoples know about your secretes?
a.yes i will
b.no i wont """


questions={q1:"a",q2:"a",q3:"d",q4:"b"}
name=input("Hi Whats ur name")
print("Hello",name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this questions (yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("wow! you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer, u lost 1 mark")
        score=score-1
        print ("ur current score is",score)
    flag2=input("Do you want to Quit? type (Yes/No)")
    if flag2=="yes":
        break
print("Your total score is", score)    
