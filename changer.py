import string
import random

aznum=list(string.ascii_letters+string.digits+string.punctuation)
sh_aznum=aznum.copy()
random.shuffle(sh_aznum)




def password_creat(password):    
    data1=dict(zip(aznum,sh_aznum))
    pas = ""
    for i in password:
        if i in data1:
            pas+=data1[i]
        elif i==' ':
            pas+=' '
        
    return pas



def sentene_creat(sentence): 
    data2=dict(zip(sh_aznum,aznum))   
    sen=''
    for i in sentence:
        if i in data2:
            sen+=data2[i]
        elif i==' ':
            sen+=' '
    return sen