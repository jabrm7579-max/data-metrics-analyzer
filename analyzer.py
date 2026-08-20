"""
Automated Data Metrics & Statistical Analyzer
A lightweight CLI utility for statistical summaries, CSV dataset parsing, and automated reporting.
Author: Mazen
"""

import csv
import math

class DataAnalyzer:
    def __init__(self, data=None):
        self.data = data or []

    def load_from_list(self, numbers):
        """Loads a list of numerical values."""
        self.data = [float(x) for x in numbers]

    def calculate_mean(self):
        if not self.data:
            return 0.0
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        if not self.data:
            return 0.0
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        return sorted_data[mid]

    def calculate_variance(self):
        if len(self.data) < 2:
            return 0.0
        mean = self.calculate_mean()
        return sum((x - mean) ** 2 for x in self.data) / (len(self.data) - 1)

    def calculate_std_dev(self):
        return math.sqrt(self.calculate_variance())

    def get_summary(self):
        if not self.data:
            return {"Error": "Dataset is empty."}
        
        return {
            "Count": len(self.data),
            "Min": min(self.data),
            "Max": max(self.data),
            "Mean": round(self.calculate_mean(), 3),
            "Median": round(self.calculate_median(), 3),
            "Variance": round(self.calculate_variance(), 3),
            "Std Deviation": round(self.calculate_std_dev(), 3),
            "Range": round(max(self.data) - min(self.data), 3)
        }

    def generate_report(self):
        metrics = self.get_summary()
        print("\n" + "=" * 45)
        print("        STATISTICAL METRICS SUMMARY         ")
        print("=" * 45)
        for key, value in metrics.items():
            print(f"  {key:<18} : {value:>15}")
        print("=" * 45 + "\n")


def main():
    print("[*] Initializing Data Metrics Analyzer...")

    # Sample engineering/sensor experiment readings
    sample_readings = [24.5, 25.1, 23.8, 26.2, 24.9, 25.4, 23.5, 27.0, 24.8, 25.0]
    
    print(f"[+] Loaded {len(sample_readings)} numerical observations.")
    
    analyzer = DataAnalyzer()
    analyzer.load_from_list(sample_readings)
    analyzer.generate_report()


if __name__ == "__main__":
    main()
