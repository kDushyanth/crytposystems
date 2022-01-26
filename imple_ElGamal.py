from charm.toolbox.integergroup import IntegerGroupQ

class ElGamal:
    def __init__(self,group_obj):
        global group
        group = group_obj
        
    def generate_key(self,bits=1024):
        
        group.paramgen(bits)
        alpha = group.randomGen()
        a = group.random() 
        beta = alpha ** a
        
        public_key = {'alpha':alpha, 'beta':beta }
        private_key = {'a':a}
        return (public_key,private_key)
    
    def encrypt(self,plaintext,public_key):
        r = group.random()
        y1 = public_key['alpha']** r
        y2 = group.encode(plaintext) * (public_key['beta'] ** r)
        return (y1,y2)
    
    def decrypt(self,ciphertext,private_key):
        y1,y2 = ciphertext
        temp1 = y1 ** private_key['a']
        temp2 = y2 * (temp1 ** -1)
        plaintext = group.decode(temp2 % group.p)
        return plaintext
    
group_obj = IntegerGroupQ()

my_elgamal = ElGamal(group_obj)
public_key , private_key = my_elgamal.generate_key()
plaintext = input("enter the message to encrypt:")
plaintext = str.encode(plaintext) # to bytes
ciphertext = my_elgamal.encrypt(plaintext,public_key)
decrypted = my_elgamal.decrypt(ciphertext,private_key)

print("message:{0}\ndecrypted message:{1}".format(plaintext,decrypted))
print("encryptions(y1,y2):\ny1:{0}\ny2:{1}".format(ciphertext[0],ciphertext[1]))

if plaintext==decrypted:
    print('enc. and dec. successful')
else:
    print('invalid enc. or dec.')

