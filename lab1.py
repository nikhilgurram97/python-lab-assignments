c= open('para.txt', 'rU')
words={} # empty dictionary
for line in c: # iterate every line
    for word in line.split(): # iterate every word
        if word  in words:    # check whether the word already exists in dictionary
            words[word]=words[word]+1 # increase the frequency
        else:    # if it dosent have word
            words[word]=1 #add word
f=open('result.txt','w+')
txt=str(words)
f.write(txt)
c.close()
