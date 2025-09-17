class Evaluator:
    def __init__(self):
        pass

    def calculate_qber(self, key_alice, key_bob):
        if len(key_alice) != len(key_bob):
            raise ValueError("Keys must have the same length to calculate QBER.")

        differences = sum(1 for a, b in zip(key_alice, key_bob) if a != b)
        qber = (differences / len(key_alice)) * 100
        return qber

    def evaluate_encryption_performance(self, original_data, decrypted_data):
        return original_data == decrypted_data

if __name__ == '__main__':
    evaluator = Evaluator()

    # Example QBER calculation
    key_a = [0, 1, 0, 1, 1, 0]
    key_b = [0, 1, 1, 1, 1, 0]  # One bit difference
    qber = evaluator.calculate_qber(key_a, key_b)
    print(f"Calculated QBER: {qber:.2f}%")

    # Example encryption performance check
    original = "Hello World"
    decrypted = "Hello World"
    is_match = evaluator.evaluate_encryption_performance(original, decrypted)
    print(f"Encryption check successful: {is_match}")