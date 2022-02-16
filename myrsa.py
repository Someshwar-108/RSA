import rsa

publicKey, privateKey = rsa.newkeys(512)
#pip install rsa
msg = input('Enter the message')
encMsg = rsa.encrypt(msg.encode(), publicKey)
print('Original msg', msg)
print('encrypted msg', encMsg)

decMsg = rsa.decrypt(encMsg, privateKey).decode()
print('decrypted msg', decMsg)
