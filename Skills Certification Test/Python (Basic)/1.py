def transformSentence(sentence):
    # Write your code here
    st = sentence[0]
    for i in range(1, len(sentence)):
        # print(sentence[i])
        if sentence[i] == ' ':
            st=st+ sentence[i]
        elif sentence[i-1] == ' ':
            st=st+sentence[i]
        elif ord(sentence[i-1].lower()) < ord(sentence[i].lower()):
            st=st+sentence[i].upper()
        elif ord(sentence[i-1].lower()) > ord(sentence[i].lower()):
            st=st+sentence[i].lower()
        elif ord(sentence[i-1].lower()) == ord(sentence[i].lower()):
            st=st+sentence[i]
        
    return st

sentence=input()
result=transformSentence(sentence)
print(result)
