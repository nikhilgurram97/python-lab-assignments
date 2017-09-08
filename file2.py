string1=input("enter the required string to be tested")
str.lower(string1)
alpha={}
alpha['q']=0          # set initial frequency of every alphabet to 0
alpha['w']=0
alpha['e']=0
alpha['r']=0
alpha['t']=0
alpha['y']=0
alpha['u']=0
alpha['i']=0
alpha['o']=0
alpha['p']=0
alpha['a']=0
alpha['s']=0
alpha['d']=0
alpha['f']=0
alpha['g']=0
alpha['h']=0
alpha['j']=0
alpha['k']=0
alpha['l']=0
alpha['z']=0
alpha['x']=0
alpha['c']=0
alpha['v']=0
alpha['b']=0
alpha['n']=0
alpha['m']=0
for letter in string1:
    if letter in alpha:
        alpha[letter]=alpha[letter]+1      #count frequency of all letters in string
count=0
for k,v in alpha.items():
    if (v==0):
        print("string doesnt contain",k)     # check string with all alphabets
        count+=1
if (count==0):
    print("string contains all alphabets")   #if it contains all alphabets
