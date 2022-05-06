""" Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid."""
#input string
st=input()
#a is a variable to check whether previous and current elements are same are not
a=st[0]
count=1
#encoded string to be stored in encodedstr
encodedstr=""
for i in st[1:]:
    if i==a:
        count+=1
    else:
        encodedstr+=str(count)+a
        a=i
        count=1
encodedstr+=str(count)+a
print(encodedstr)
#decoding the encodedstring
decodedstr=""
for i in range(0,len(encodedstr),2):
    decodedstr+=int(encodedstr[i])*encodedstr[i+1]
print(decodedstr)


#TimeComplexity:o(n)
#SpaceComplexity:o(n)



