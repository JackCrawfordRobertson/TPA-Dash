#!/usr/bin/env python3
"""
Update the HTML file with new Payment Penetration (% of GDP) data
"""

import csv
import os
import re

def load_gdp_percentage_data(filepath):
    """Load the % of GDP data from CSV"""
    data = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row['Country']
            data[country] = {
                '2021': float(row['2021']),
                '2022': float(row['2022']),
                '2023': float(row['2023']),
                '2024': float(row['2024']),
                '2025': float(row['2025'])
            }
    return data

def generate_js_object(data):
    """Generate JavaScript object string from data"""
    js_lines = []
    for country, values in sorted(data.items()):
        js_line = f'        "{country}": {{ "2021": {values["2021"]}, "2022": {values["2022"]}, "2023": {values["2023"]}, "2024": {values["2024"]}, "2025": {values["2025"]} }},'
        js_lines.append(js_line)

    # Remove trailing comma from last line
    if js_lines:
        js_lines[-1] = js_lines[-1].rstrip(',')

    return '\n'.join(js_lines)

def main():
    # File paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'data')
    pages_dir = os.path.join(project_root, 'pages')

    csv_file = os.path.join(data_dir, 'Payments Trends Report 2025 - Per Capita.csv')
    html_file = os.path.join(pages_dir, 'global-reach-growth.html')

    print("Loading % of GDP data from CSV...")
    gdp_data = load_gdp_percentage_data(csv_file)
    print(f"Loaded {len(gdp_data)} countries")

    print("Generating JavaScript object...")
    js_object_content = generate_js_object(gdp_data)

    print("Reading HTML file...")
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("Replacing paymentDataPerCapita object...")
    # Pattern to match the entire paymentDataPerCapita object
    pattern = r'(const paymentDataPerCapita = \{)\s*[\s\S]*?\n(\s*\};)'

    replacement = r'\1\n' + js_object_content + '\n    \\2'

    updated_html = re.sub(pattern, replacement, html_content)

    if updated_html == html_content:
        print("ERROR: No replacement made. Pattern might not match.")
        return False

    print("Writing updated HTML file...")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("✓ Successfully updated HTML file with % of GDP data!")
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
