from random import randint

def encrypt(msg, number):
    
    encrypted_msg = ""
    
    for char in msg:
        
        # Check if char is a letter
        if char.isalpha():
            
            is_upper = char.isupper()
            char = char.lower()
            
            # ord() returns the ASCII value of a character
            # 97 is the ASCII value of 'a'
            # % 26 to wrap around the alphabet
            encrypted_char = chr(((ord(char) - 97 + number) % 26) + 97)
            
            if is_upper:
                
                encrypted_char = encrypted_char.upper()
                
            encrypted_msg += encrypted_char
            
        else:
            
            encrypted_msg += char
    
    return encrypted_msg

def deciphering(msg, number):
    
    decrypted_msg = ""
    
    for char in msg:
        
        if char.isalpha():
            
            is_upper = char.isupper()
            char = char.lower()
            
            decrypted_char = chr(((ord(char) - 97 - number) % 26) + 97)
            
            if is_upper:
                
                decrypted_char = decrypted_char.upper()
                
            decrypted_msg += decrypted_char
            
        else:
            
            decrypted_msg += char
    
    return decrypted_msg

def encrypt_random(msg):
    
    # 25 is the maximum value possible (26 letters in the alphabet)
    encrypted_msg = encrypt(msg, randint(1, 25))
    
    return encrypted_msg
        
def deciphering_bruteforce(msg):
    
    for key in range(1, 26):
        
        decrypted_msg = ""
        
        for char in msg:
            
            if char.isalpha():
                
                is_upper = char.isupper()
                char = char.lower()
                decrypted_char = chr(((ord(char) - 97 - key) % 26) + 97)
                
                if is_upper:
                    
                    decrypted_char = decrypted_char.upper()
                    
                decrypted_msg += decrypted_char
                
            else:
                
                decrypted_msg += char
                
        print(f"Clé {key}: {decrypted_msg}")

#message = ""
#encrypted_message = encrypt(message, 1)
#print(encrypted_message)
#deciphering_message = deciphering(encrypted_message, 1)
#print(deciphering_message)