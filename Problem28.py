"""Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


l=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
#size of the window
k=16
#prev and curr indicates length of string previously and current
prev=0
curr=0
# to store strings of length k we use list s
s=[]
# indicates the index of starting word in the string
start=0
#shows word length in string used for providing padding spaces easily
#wl is initialised as -1 as for single word we dont require as space
wl=-1
for i in range(len(l)):
    prev=curr
    curr+=len(l[i])
    wl+=1
    if curr+wl==k:
        s.append((start,i,curr))
        curr=0
        start=i+1
        wl=-1
    elif curr+wl>k:
        s.append((start,i-1,prev))
        curr=len(l[i])
        start=i
        wl=0
if start!=len(l):
    s.append((start,len(l)-1,curr))
new=""
cc=[]
for i in range(len(s)):
    stringlength=s[i][2]
    first=s[i][0]
    last=s[i][1]
    if last-first>0:
        rem=(k-stringlength)%(last-first)
    else:
        rem=0
    if last==first:
        j=last-1
    for j in range(first,last):
        new+=l[j]+" "*((k-stringlength)//(last-first))
        if rem>0:
            new+=" "
            rem-=1
    new+=l[j+1]
    if first==last:
        new+=" "*(k-stringlength)
    cc.append(new)
    new=""

print(cc)

#m indicates max length of a word in list l

#TimeComplexity:o(n*m)
#SpaceComplexity:o(n)



