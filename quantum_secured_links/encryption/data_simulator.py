import json
import random

class DataSimulator:
    def __init__(self):
        self.counter = 0

    def generate_telemetry_data(self):
        self.counter += 1
        data = {
            "timestamp": f"2025-09-17T10:23:25.{self.counter:03}Z",
            "sensor_id": f"SENSOR-{random.randint(100, 999)}",
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "pressure": round(random.uniform(900.0, 1100.0), 2),
            "status": random.choice(["OK", "WARNING", "CRITICAL"])
        }
        return json.dumps(data)

if __name__ == '__main__':
    simulator = DataSimulator()
    for _ in range(3):
        print(simulator.generate_telemetry_data())