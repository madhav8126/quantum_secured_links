import numpy as np
from qkd_simulation.bb84 import BB84
from encryption.aes_encryptor import AESEncryptor
from encryption.data_simulator import DataSimulator
from performance_analysis.evaluator import Evaluator

def main():
    print("Starting Quantum-Secured Links Simulation...")
    print("\n--- Running BB84 QKD Protocol to Generate a Key ---")
    key_bit_length = 128
    qkd_protocol = BB84(key_length=key_bit_length)
    sieved_key_bits = qkd_protocol.run_protocol()

    if len(sieved_key_bits) < 16:
        print("Warning: The sieved key is too short for AES. Exiting.")
        return

    shared_key_bytes = np.packbits(sieved_key_bits)[:16].tobytes()
    print(f"\nGenerated shared key (bytes): {shared_key_bytes.hex()}")

    print("\n--- Encrypting Simulated Telemetry Data ---")
    aes_encryptor = AESEncryptor(shared_key_bytes)
    data_simulator = DataSimulator()
    
    original_data = data_simulator.generate_telemetry_data()
    print(f"Original data: {original_data}")

    encrypted_data = aes_encryptor.encrypt(original_data)
    print(f"Encrypted data (in hex): {encrypted_data.hex()}")
    print("\n--- Decrypting and Verifying Data ---")
    decrypted_data = aes_encryptor.decrypt(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")
    print("\n--- Evaluating System Performance ---")
    evaluator = Evaluator()

    is_match = evaluator.evaluate_encryption_performance(original_data, decrypted_data)
    print(f"Data integrity check: {'Success' if is_match else 'Failed'}")
    
    qber = evaluator.calculate_qber(sieved_key_bits, sieved_key_bits)
    print(f"Simulated QBER (Quantum Bit Error Rate): {qber:.2f}%")
    if qber > 5.0:
        print("ALERT: QBER is high! The key may be compromised.")
    else:
        print("QBER is within acceptable limits. The key is likely secure.")

if __name__ == '__main__':
    main()