word='banana'
letter_list=list('_ _ _ _ _ _'.split())
print (letter_list)

def find_letter(haystack,needle,start=0,end=-1):
    for index,letter in enumerate(haystack[start:]):
        if letter==needle:
            return index+start
    return -1

def put_letter(letter_list,word,letter):
    start=0
    while(1):
        pos=find_letter(word,letter,start)

        if pos!=-1:
            letter_list[pos]=letter
            start=pos+1
            #print(pos,start)
        else:
            break


for _ in range(9):
    letter=input('put ur letter:' )
    put_letter(letter_list,word,letter)
    print(' '.join(letter_list))
