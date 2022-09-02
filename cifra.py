import binascii 
def rand_key(p): 
    key1 = "01010110 01101001 01100100 01100001 00100000 11000011 10101001 00100000 01100010 01100101 01101100 01100001" #Key = Vida é bela
    return(key1) 
   
def exor(a,b):  
    temp = ""  
    for i in range(n):  
        if (a[i] == b[i]): 
            temp += "0"
        else:  
            temp += "1"   
    print('temp:', temp)
    return temp 
     
def BinaryToDecimal(binary):      
    string = int(binary, 2)  
    print('string:', string)
    return string 
texto_plano = "Kley"
print("Texto plano é:", texto_plano) 
texto_plano_Ascii = [ord(x) for x in texto_plano] 
texto_plano_Bin = [format(y,'08b') for y in texto_plano_Ascii] 
texto_plano_Bin = "".join(texto_plano_Bin) 
  
n = int(len(texto_plano_Bin)//2) 
L1 = texto_plano_Bin[0:n] 
R1 = texto_plano_Bin[n::] 
m = len(R1) 
   
K1= rand_key(m) 
   
f1 = exor(R1,K1) 
R2 = exor(f1,L1) 
L2 = R1 
   
f2 = exor(R2,K1) 
R3 = exor(f2,L2) 
L3 = R2 
   
bin_data = L3 + R3 
str_data =' '
  
for i in range(0, len(bin_data), 7):  
    temp_data = bin_data[i:i + 7]  
    decimal_data = BinaryToDecimal(temp_data)  
    str_data = str_data + chr(decimal_data)  
      
print("Texto Criptografado:", str_data) 
L4 = L3 
R4 = R3 
   
f3 = exor(L4,K2) 
L5 = exor(R4,f3) 
R5 = L4 
   
f4 = exor(L5,K1) 
L6 = exor(R5,f4) 
R6 = L5 
PT1 = L6+R6 
   
  
PT1 = int(PT1, 2) 
RPT = binascii.unhexlify( '%x'% PT1) 
print("Texto Descripografado: ", RPT)