import binascii
from re import T
import sys


def info_key(): 
    key1 = input('Insira a frase chave: ')
    key1_Ascii = [ord(x) for x in key1] 
    key1_Bin = [format(y,'08b') for y in key1_Ascii] 
    key1_Bin = "".join(key1_Bin) 
    print(Serializar_Binario(key1_Bin))
    return(key1_Bin) 
   
def exor(a,b):
    temp = ""  
    for i in range(n):  
        try:
            if (a[i] == b[i]): 
                temp += "0"
            else:  
                temp += "1"   
        except:
            print('Frase chave muito curta, tente novamente com uma nova frase chave. \n')
            sys.exit(1)
    return temp 
      
def BinaryToDecimal(binary):
    string = int(binary, 2)  
    return string 

def Serializar_Binario(stringBin):
    if(len(stringBin)%8 == 0):
        stringBin_serializada = ' '.join([stringBin[i:i+8] for i in range(0, len(stringBin), 8)])
        return stringBin_serializada
    else:
        return stringBin

texto_plano = input('Digite o Texto plano: ')
texto_plano_Ascii = [ord(x) for x in texto_plano] 
texto_plano_Bin = [format(y,'08b') for y in texto_plano_Ascii] 
texto_plano_Bin = "".join(texto_plano_Bin)
print(Serializar_Binario(texto_plano_Bin))

n = int(len(texto_plano_Bin)//2) 
L1 = texto_plano_Bin[0:n] 
R1 = texto_plano_Bin[n::] 
   
K1= info_key() 
   
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
      
print('\nTexto Criptografado em binario:', Serializar_Binario(bin_data))
print('Texto Criptografado:', str_data,"\n") 
L2 = L3 
R2 = R3 
   
f3 = exor(L2,K1) 
L1 = exor(R2,f3) 
R1 = L2 
   
f4 = exor(L1,K1) 
L0 = exor(R1,f4) 
R0 = L1 
texto_plano_final = L0+R0 

print('Texto Descripografado em binario: ', Serializar_Binario(texto_plano_final))
texto_plano_final = int(texto_plano_final, 2) 
texto_plano_descriptografado = binascii.unhexlify( '%x'% texto_plano_final).decode('utf-8')
print('Texto Descripografado: ', texto_plano_descriptografado)