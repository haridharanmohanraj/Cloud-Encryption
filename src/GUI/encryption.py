from cryptography.fernet import Fernet
import eel
import io



#Function which generates our key (AES)
@eel.expose
def keyGen():
    key = Fernet.generate_key()
    file = open('src\Keys\key.key', 'wb')
    file.write(key)
    file.close()
    print("\nKey Created.\n")

#Function which reads the key 
def keyRead():
    try:
        file = open('src\Keys\key.key', 'rb')
        key = file.read()
        file.close()
        return key
    except FileNotFoundError:
        #If key does not exists a new one is created.
        print("No Key exists, a new one has just been created.")
        keyGen()
        keyRead()



#Function to encrypt files using the key
@eel.expose
def encrypt(fileName):
    Key = keyRead()
    with open("src/Files/"+ fileName, "rb") as f:
        data = f.read()
    fernet = Fernet(Key)
    encrypted = fernet.encrypt(data)
    with open("src/Files/"+ fileName, "wb") as f:
        f.write(encrypted)

#Function to decrypt files using the key
@eel.expose
def decrypt(fileName):
    Key = keyRead()
    with open("src/Downloads/"+ fileName, "rb") as f:
        data1 = f.read()
    fernet = Fernet(Key)
    decrypted = fernet.decrypt(data1)
    with open("src/Downloads/"+ fileName, "wb") as f:
        f.write(decrypted)
        print("File decrypted successfully") 