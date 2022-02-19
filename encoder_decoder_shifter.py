import string
alphabet=string.ascii_lowercase
alphabet=list(alphabet)

def crypter(text,shift_times,coding_mode):
    shift_sign=1
    result=""
    if coding_mode==2:
        shift_sign*=-1
    if shift_times<0:
        shift_sign*=-1
    shift_times=abs(shift_times)
    for char in text:
        index=alphabet.index(char) 
        while index+shift_times>25:
            shift_times-=26
        if shift_sign<0 and shift_times>0:    
            shift_times*=shift_sign
        result+=alphabet[index+shift_times]
    return(result)    

# def encoder(text,shift_times):
#     result=""
#     for chr_index in range(0,len(text)):
#         chr=text[chr_index]
#         index=alphabet.index(chr)
#         if index+shift_times>25:
#             index-=25
#         result+=alphabet[index+shift_times]
#     return(str(result))    
# def decoder(text,shift_times):
#     result=""
#     for chr_index in range(0,len(text)):
#         chr=text[chr_index]
#         index=alphabet.index(chr)
#         result+=alphabet[index-shift_times]
#     return(str(result))

# print(alphabet)
coding_mode=0
while coding_mode!=3:  
    coding_mode=int(input("Chose number of your choice From menu:\n 1 = encode\t\t2 = decode\t\t 3 = exit\n"))
    final_result=""
    if coding_mode==3:
        final_result="Thanks for using this service"
    elif coding_mode==1 or coding_mode==2:
         text=input("What is the message: ").lower()
         shift_times=int(input("How many shifting you want: "))
         result=""
         final_result=crypter(text,shift_times,coding_mode)   
    # elif coding_mode==1:
    #     text=input("What is the message: ").lower()
    #     shift_times=int(input("How many shifting you want: "))
    #     result=""
    #     final_result=encoder(text,shift_times)
    # elif coding_mode==2:
        
    #     text=input("What is the message: ").lower()
    #     shift_times=int(input("How many shifting you want: "))
    #     result=""
    #     final_result=decoder(text,shift_times) 
    else:
        print("Wrong choice")
        final_result="***"     
    print (f"The result is : {final_result}")

