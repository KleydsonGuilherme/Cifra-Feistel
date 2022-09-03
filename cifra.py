import binascii
import sys


def info_key(): #Coleta a chave do usuario e tranforma em Binario
    key1 = input('Insira a Chave: ')
    key1_Ascii = [ord(x) for x in key1] 
    key1_Bin = [format(y,'08b') for y in key1_Ascii] 
    key1_Bin = "".join(key1_Bin) 
    print('Chave em binario: ',Serializar_Binario(key1_Bin))
    return(key1_Bin) 

def BinaryToDecimal(binary): #Tranforma o binario para decimal
    string = int(binary, 2)  
    return string 

def Serializar_Binario(stringBin): #Transforma o Binario separado em byte para fácil leitura
    if(len(stringBin)%8 == 0):
        stringBin_serializada = ' '.join([stringBin[i:i+8] for i in range(0, len(stringBin), 8)])
        return stringBin_serializada
    else:
        return stringBin
   
def exor(a,b): #Executa o XOR
    temp = ""  
    for i in range(n): 
        try:
            if (a[i] == b[i]):
                temp += "0"
            else:  
                temp += "1"
        except IndexError:
            temp += "0"
        except:
            print('Error: inputs invalidos \n')
            sys.exit(1)
    return temp    

def Shift_Left(stringBin,n): #Realizar o SHIFT LEFT ciclico X vezes em cada Byte
    num = 0
    stringBin_cript = ''
    Array_stringBin = str(Serializar_Binario(stringBin)).split()

    while num < int(len(stringBin)//8):
        Quant_String = Array_stringBin[num]

        for i in range(n):
            start = Quant_String[0]

            Quant_String = Quant_String + start
            Quant_String = Quant_String[1:]
            i += 1  
        stringBin_cript = stringBin_cript + Quant_String
        num += 1
    return stringBin_cript

def Shift_Right(stringBin,n): #Realizar o SHIFT RIGHT ciclico X vezes em cada Byte
    num = 0
    stringBin_cript = ''
    Array_stringBin = str(Serializar_Binario(stringBin)).split()

    while num < int(len(stringBin)//8):
        Quant_String = Array_stringBin[num]

        for i in range(n):
            end = Quant_String[-1]

            Quant_String = end + Quant_String 
            Quant_String = Quant_String[:-1]
            i += 1
        stringBin_cript = stringBin_cript + Quant_String
        num += 1
    return stringBin_cript


texto_plano = input('Digite o Texto plano: ')
#Faz a conversão do Texto informado para o Binario
texto_plano_Ascii = [ord(x) for x in texto_plano] 
texto_plano_Bin = [format(y,'08b') for y in texto_plano_Ascii] 
texto_plano_Bin = "".join(texto_plano_Bin)
print('Texto plano em binario: ', Serializar_Binario(texto_plano_Bin))

#Realiza a separação do texto plano em binario e realizar a criptografia de o shift left
n = int(len(texto_plano_Bin)//2) 
L1 = texto_plano_Bin[0:n] 
R1 = texto_plano_Bin[n::] 
K1 = info_key() 
   
f1 = exor(R1,K1) 
R2 = exor(f1,L1) 
L2 = R1 
   
f2 = exor(R2,K1) 
R3 = exor(f2,L2) 
L3 = R2 
   
bin_data = L3 + R3 
str_data = ' '

#Imprime antes do Shift Left e Após
n_shift = int(input('Informar quantidade de Shift Left: '))
print('\nCriptografado em binario: ', Serializar_Binario(bin_data), end='')
bin_data = Shift_Left(bin_data, n_shift)
print('\nCriptografado em shift:   ', Serializar_Binario(bin_data))

for i in range(0, len(bin_data), 7): #Transforma o Binario criptografado em Texto 
    temp_data = bin_data[i:i + 7]  
    decimal_data = BinaryToDecimal(temp_data)  
    str_data = str_data + chr(decimal_data)  

print('Texto Criptografado Final: ')
print(str_data)

#Realizar a descriptografia fazendo o Shift Right e realiza a descriptografia da cifra. 
bin_data = Shift_Right(bin_data, n_shift)

n = int(len(bin_data)//2)
L2 = bin_data[0:n]
R2 = bin_data[n::]
   
f3 = exor(L2,K1) 
L1 = exor(R2,f3) 
R1 = L2 
   
f4 = exor(L1,K1) 
L0 = exor(R1,f4) 
R0 = L1 
texto_plano_final = L0+R0 

#Retornar o Binario para Texto de origem
print('\nTexto Descriptografado em binario: ', Serializar_Binario(texto_plano_final))
texto_plano_final = int(texto_plano_final, 2) 
texto_plano_descriptografado = binascii.unhexlify( '%x'% texto_plano_final).decode('utf-8')
print('Texto Descriptografado: ', texto_plano_descriptografado)