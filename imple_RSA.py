from charm.core.math.integer import integer,isPrime,gcd,random,randomPrime,toInt
from charm.toolbox.PKEnc import PKEnc
from charm.toolbox.PKSig import PKSig
from charm.toolbox.paddingschemes import OAEPEncryptionPadding,PSSPadding
from charm.toolbox.conversion import Conversion
from math import ceil

'''
the purpose of adding random padding to the clear text before encrypting it is to prevent a successful chosen plaintext attack
'''

class RSA():
    def __init__(self,padding=OAEPEncryptionPadding()):
        self.padding_scheme = padding
    
    def generate_key(self, bits=1024):
        while True:
            p, q = randomPrime(bits), randomPrime(bits)
            if isPrime(p) and isPrime(q) and p != q:
                N = p * q
                phi_N = (p - 1) * (q - 1)
                break
        
        while True:
            b = random(phi_N)
            if not gcd(b, phi_N) == 1:
                continue
            a = b ** -1
            break
        
        public_key = { 'N':N, 'b':toInt(b) } 
        private_key = { 'p':p, 'q':q, 'a':a }
        print(public_key)
        print(private_key)
        return (public_key, private_key)
    
    def encrypt(self, message, public_key,salt=None):
        octet_length = int(ceil(int(public_key['N']).bit_length() / 8.0))
        EM = self.padding_scheme.encode(message, octet_length,"",salt)
        i = Conversion.OS2IP(EM)
        ip = integer(i) % public_key['N'] 
        return (ip ** public_key['b']) % public_key['N']
        
    
    def decrypt(self, encrypted_msg, private_key):
        
        p = private_key['p']
        q = private_key['q']
        a = private_key['a']
        N = p*q
        phi_N = (p-1)*(q-1)
        
        octet_length = int(ceil(int(N).bit_length() / 8.0))
        M = (encrypted_msg ** (private_key['a'] % phi_N)) % N
        os = Conversion.IP2OS(int(M), octet_length)
        return self.padding_scheme.decode(os)
    
my_rsa = RSA()
public_key , private_key =my_rsa.generate_key()
message = input("enter the message to encrypt:")
message = str.encode(message) # to bytes
encrypted_msg = my_rsa.encrypt(message,public_key)
decrypted_msg = my_rsa.decrypt(encrypted_msg,private_key)

print("message:{0}\nencrpted message:{1}\ndecrypted message:{2}".format(message,encrypted_msg,decrypted_msg))

if message==decrypted_msg:
    print('enc. and dec. successful')
else:
    print('invalid enc. or dec.')

