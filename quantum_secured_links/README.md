# Quantum-Secured Links Simulation

This project simulates a secure communication link using Quantum Key Distribution (QKD) combined with classic symmetric-key encryption.

## Project Structure

- **`qkd_simulation/`**: Contains the logic for the quantum key distribution protocols.
  - `bb84.py`: Implements the BB84 protocol to generate a shared secret key.
- **`encryption/`**: Contains the logic for data handling and encryption.
  - `aes_encryptor.py`: Implements AES encryption using a key derived from the QKD protocol.
  - `data_simulator.py`: Generates a mock telemetry data stream for encryption.
- **`performance_analysis/`**: Contains the logic for evaluating the system's performance.
  - `evaluator.py`: Calculates metrics like Quantum Bit Error Rate (QBER) and checks data integrity.
- **`main.py`**: The main execution file that orchestrates the entire simulation process.
- **`requirements.txt`**: Lists all necessary Python libraries.

## How to Run

1.  **Clone the repository:**
    ```
    git clone [https://github.com/your-username/quantum-secured-links.git](https://github.com/your-username/quantum-secured-links.git)
    cd quantum-secured-links
    ```

2.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3.  **Run the main simulation:**
    ```
    python main.py
    ```

## Key Concepts

-   **QKD (Quantum Key Distribution)**: A method of distributing encryption keys using quantum mechanics, ensuring that any eavesdropping attempt is detected.
-   **BB84 Protocol**: One of the first and most widely known QKD protocols.
-   **AES (Advanced Encryption Standard)**: A symmetric-key encryption standard used to encrypt the actual data stream with the quantum-generated key.
-   **QBER (Quantum Bit Error Rate)**: A measure of the error rate in the shared quantum key, which indicates the security of the link. A high QBER suggests the presence of an eavesdropper.