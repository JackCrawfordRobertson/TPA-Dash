#!/usr/bin/env python3
"""
Convert the Per Capita CSV (now % of GDP) to JavaScript object format
for inclusion in the HTML file
"""

import csv
import os

def main():
    # File paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'data')

    input_file = os.path.join(data_dir, 'Payments Trends Report 2025 - Per Capita.csv')
    output_file = os.path.join(project_root, 'payment_data_percapita_js.txt')

    print("Converting CSV to JavaScript format...")

    js_lines = []

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row['Country']
            # Format the JavaScript object entry
            js_line = f'        "{country}": {{ "2021": {row["2021"]}, "2022": {row["2022"]}, "2023": {row["2023"]}, "2024": {row["2024"]}, "2025": {row["2025"]} }},'
            js_lines.append(js_line)

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(js_lines))

    print(f"✓ JavaScript object written to {output_file}")
    print(f"✓ Total countries: {len(js_lines)}")
    print("\nYou can now copy this content and paste it into the HTML file")
    print("to replace the paymentDataPerCapita object values.")

if __name__ == "__main__":
    main()
