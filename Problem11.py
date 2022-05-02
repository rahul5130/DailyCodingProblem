#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

#Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

st=input()
l=list(map(str,input().split()))
l=set(l)
d={}
out=[]
def autocompete(st,l):
    for i in l:
        if st in i:
                out.append(i)

    return out


print(autocompete(st,l))
