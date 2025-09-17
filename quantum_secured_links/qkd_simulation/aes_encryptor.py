from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AESEncryptor:
    def __init__(self, key):
        self.key = key
        # Pad the key if necessary to be 16, 24, or 32 bytes long
        self.key = pad(self.key, AES.block_size)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        return cipher.iv + ciphered_data

    def decrypt(self, data):
        iv = data[:AES.block_size]
        ciphered_data = data[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        decrypted_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        return decrypted_data.decode('utf-8')

if __name__ == '__main__':
    # Example usage
    key = b'mysecretkey12345'
    aes_encryptor = AESEncryptor(key)

    message = "This is a test telemetry data stream."
    print(f"Original message: {message}")

    encrypted_data = aes_encryptor.encrypt(message)
    print(f"Encrypted data: {encrypted_data}")

    decrypted_data = aes_encryptor.decrypt(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")