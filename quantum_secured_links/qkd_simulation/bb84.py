import numpy as np

# QKD BB84 Protocol Logic
class BB84:
    def __init__(self, key_length):
        self.key_length = key_length

    def generate_random_bits(self):
        return np.random.randint(2, size=self.key_length)

    def generate_random_bases(self):
        return np.random.randint(2, size=self.key_length)

    def measure_photons(self, bits, bases):
        measured_bits = []
        for i in range(self.key_length):
            if bits[i] == bases[i]:
                measured_bits.append(bits[i])
            else:
                measured_bits.append(np.random.randint(2))
        return np.array(measured_bits)

    def sieve_key(self, alice_bases, bob_bases, alice_bits, bob_bits):
        sieved_key = []
        for i in range(self.key_length):
            if alice_bases[i] == bob_bases[i]:
                sieved_key.append(bob_bits[i])
        return np.array(sieved_key)

    def run_protocol(self):
        # Alice's actions
        alice_bits = self.generate_random_bits()
        alice_bases = self.generate_random_bases()

        # Bob's actions
        bob_bases = self.generate_random_bases()
        bob_bits = self.measure_photons(alice_bits, bob_bases)

        # Public discussion
        shared_key = self.sieve_key(alice_bases, bob_bases, alice_bits, bob_bits)

        print(f"Alice's bits: {alice_bits}")
        print(f"Alice's bases: {alice_bases}")
        print(f"Bob's bases: {bob_bases}")
        print(f"Bob's measured bits: {bob_bits}")
        print(f"Shared raw key: {shared_key}")
        return shared_key

if __name__ == '__main__':
    bb84 = BB84(key_length=20)
    bb84.run_protocol()