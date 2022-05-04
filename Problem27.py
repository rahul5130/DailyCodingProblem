#Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

#For example, given the string "([])[]({})", you should return true.

#Given the string "([)]" or "((()", you should return false.
s=input()
l=[]
for i in s:
    if (len(l)>0) and ((i=='}' and l[-1]=="{") or (i==']' and l[-1]=="[") or (i==')' and l[-1]=="(")):
        l.pop()
    else:
        l.append(i)
print(True if len(l)==0 else False)

#TimeComplexity:o(n)
#SpaceComplexity:o(n)


