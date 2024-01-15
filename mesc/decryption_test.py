import base64
from cryptography.fernet import Fernet 

# key is generated 
f = Fernet(b"2GMyCOCeG8G3zoj_Cg7-lZ8XWFJt8D7f1FYZMcpztJU=")

token = b"gAAAAABljqJpj_uGnCCnRIQLWvJdOAYysVBPm_gx6Fr4k75QHo3ET1KK2fjoEDys3UFvmERcATVL_JtPbDCOoQj5MxzmgluNQXz8xgH9yuztQulzV_P8QBs="
# display the ciphertext 
print(token.decode()) 
  
# decrypting the ciphertext 
d = f.decrypt(token) 
  
# display the plaintext and the decode() method  
# converts it from byte to string 
print(d.decode()) 