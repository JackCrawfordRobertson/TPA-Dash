#!/usr/bin/env python3
"""
Calculate Payment Transaction Intensity (Transaction Value as % of GDP)
Shows total payment flows relative to economic output. Values can exceed 100%
due to money velocity (same money used multiple times) and B2B transaction chains.

Data sources:
- Transaction values: Payments Trends Report 2025 (Statista)
- GDP data: IMF 2025 projections from StatisticsTimes.com
"""

import csv
import os

# GDP data for 2025 (in billions USD) - Source: IMF projections via StatisticsTimes.com
GDP_DATA = {
    "United States": 30615.74,
    "China": 19398.58,
    "Japan": 4279.83,
    "Germany": 5013.57,
    "India": 4125.21,
    "United Kingdom": 3958.78,
    "France": 3361.56,
    "Italy": 2543.68,
    "Canada": 2283.60,
    "Brazil": 2256.91,
    "Russia": 2540.66,
    "Mexico": 1862.74,
    "South Korea": 1858.57,
    "Australia": 1829.51,
    "Spain": 1891.37,
    "Indonesia": 1443.26,
    "Turkey": 1565.47,
    "Saudi Arabia": 1268.54,
    "Netherlands": 1320.64,
    "Poland": 1039.62,
    "Switzerland": 1002.67,
    "Taiwan": 884.39,
    "Argentina": 683.37,
    "Belgium": 716.98,
    "Sweden": 662.32,
    "Austria": 566.46,
    "Singapore": 574.19,
    "Israel": 610.75,
    "Thailand": 558.57,
    "United Arab Emirates": 569.10,
    "Malaysia": 470.57,
    "Philippines": 494.16,
    "Vietnam": 484.73,
    "Bangladesh": 475.01,
    "Pakistan": 410.50,
    "Romania": 422.51,
    "Colombia": 438.12,
    "Iran": 356.51,
    "South Africa": 426.38,
    "Egypt": 349.26,
    "Peru": 318.48,
    "Chile": 347.17,
    "Greece": 282.02,
    "Nigeria": 285.00,
    "Iraq": 265.46,
    "Kenya": 136.01,
    "Ghana": 111.96,
    "Ethiopia": 109.49,
    "Algeria": 288.01,
    "Kazakhstan": 300.05,
    "Ukraine": 209.71,
    "Uzbekistan": 137.48,
    "Czechia": 383.38,
    "Hungary": 247.76,
    "Slovakia": 154.59,
    "Bulgaria": 127.92,
    "Lithuania": 95.27,
    "Latvia": 47.88,
    "Estonia": 46.76,
    "Slovenia": 79.22,
    "Croatia": 103.90,
    "Serbia": 100.05,
    "Bosnia and Herzegovina": 33.24,
    "Montenegro": 9.35,
    "North Macedonia": 18.78,
    "Armenia": 27.86,
    "Azerbaijan": 76.39,
    "Tajikistan": 17.03,
    "Kyrgyzstan": 20.16,
    "Turkmenistan": 72.12,
    "Belarus": 85.74,
    "Moldova": 19.62,
    "Norway": 517.10,
    "Denmark": 459.61,
    "Finland": 314.72,
    "Iceland": 38.39,
    "Ireland": 708.77,
    "Portugal": 337.94,
    "Luxembourg": 100.64,
    "Costa Rica": 102.64,
    "Panama": 90.41,
    "Uruguay": 84.99,
    "Paraguay": 47.40,
    "Bolivia": 57.09,
    "Ecuador": 130.53,
    "Dominican Republic": 129.75,
    "Guatemala": 120.85,
    "Honduras": 39.45,
    "El Salvador": 36.59,
    "Nicaragua": 20.69,
    "Jamaica": 23.14,
    "Puerto Rico": 126.55,
    "Haiti": 30.91,
    "Morocco": 179.61,
    "Tunisia": 59.07,
    "Botswana": 19.19,
    "Namibia": 14.69,
    "Mozambique": 24.73,
    "Tanzania": 87.44,
    "Uganda": 64.99,
    "Rwanda": 14.77,
    "Zambia": 29.37,
    "Zimbabwe": 53.31,
    "Senegal": 36.84,
    "Burkina Faso": 26.87,
    "Niger": 22.97,
    "Chad": 21.59,
    "Benin": 24.40,
    "Ivory Coast": 99.21,
    "Guinea": 27.52,
    "Togo": 10.95,
    "Madagascar": 19.38,
    "Cameroon": 60.58,
    "Gabon": 21.46,
    "Republic of the Congo": 15.70,
    "Mauritius": 15.73,
    "Seychelles": 2.23,
    "Sudan": 35.90,
    "Oman": 105.19,
    "Bahrain": 47.39,
    "Jordan": 56.16,
    "Cyprus": 39.94,
    "Lebanon": 28.28,
    "Nepal": 45.51,
    "Bhutan": 3.41,
    "Sri Lanka": 98.96,
    "Brunei Darussalam": 15.57,
    "Cambodia": 48.80,
    "Laos": 16.93,
    "Myanmar": 60.56,
    "Timor-Leste": 2.13,
    "Papua New Guinea": 32.71,
    "Fiji": 6.34,
    "New Zealand": 280.45,  # Adding from separate source
    "Kuwait": 172.67,  # Adding from separate source
    "Malta": 21.77,  # Adding from separate source
    "Guyana": 25.06,
    "Suriname": 4.50,
    "Belize": 3.30,
    "Cuba": 107.35,  # Adding estimate
    "Malawi": 15.21,  # Adding estimate
    "Burundi": 3.58,  # Adding estimate
    "Lesotho": 2.48,  # Adding estimate
    "Gambia": 2.55,  # Adding estimate
    "Equatorial Guinea": 11.58,  # Adding estimate
    "Sierra Leone": 5.77,  # Adding estimate
    "Mongolia": 22.84,  # Adding estimate
}

def load_transaction_data(filepath):
    """Load transaction data from CSV"""
    data = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            country = row['Country']
            data[country] = {
                '2018': float(row['2018'].replace(',', '')),
                '2019': float(row['2019'].replace(',', '')),
                '2020': float(row['2020'].replace(',', '')),
                '2021': float(row['2021'].replace(',', '')),
                '2022': float(row['2022'].replace(',', '')),
                '2023': float(row['2023'].replace(',', '')),
                '2024': float(row['2024'].replace(',', '')),
                '2025': float(row['2025'].replace(',', '')),
                'Latitude': row['Latitude'],
                'Longitude': row['Longitude']
            }
    return data

def calculate_gdp_percentage(transaction_value_billions, gdp_billions):
    """Calculate transaction value as percentage of GDP"""
    if gdp_billions == 0:
        return 0
    return (transaction_value_billions / gdp_billions) * 100

def main():
    # File paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_dir = os.path.join(project_root, 'data')

    input_file = os.path.join(data_dir, 'Payments Trends Report 2025 - with coordinates.csv')
    output_file = os.path.join(data_dir, 'Payments Trends Report 2025 - Per Capita.csv')

    print("Loading transaction data...")
    transaction_data = load_transaction_data(input_file)

    print("Calculating Transaction Value as % of GDP...")
    results = []
    missing_gdp = []

    for country, data in transaction_data.items():
        if country in GDP_DATA:
            gdp = GDP_DATA[country]

            # Calculate percentage of GDP for each year
            result = {
                'Country': country,
                '2018': round(calculate_gdp_percentage(data['2018'], gdp), 2),
                '2019': round(calculate_gdp_percentage(data['2019'], gdp), 2),
                '2020': round(calculate_gdp_percentage(data['2020'], gdp), 2),
                '2021': round(calculate_gdp_percentage(data['2021'], gdp), 2),
                '2022': round(calculate_gdp_percentage(data['2022'], gdp), 2),
                '2023': round(calculate_gdp_percentage(data['2023'], gdp), 2),
                '2024': round(calculate_gdp_percentage(data['2024'], gdp), 2),
                '2025': round(calculate_gdp_percentage(data['2025'], gdp), 2),
                'Latitude': data['Latitude'],
                'Longitude': data['Longitude']
            }
            results.append(result)
            print(f"  {country}: {result['2025']}% of GDP")
        else:
            missing_gdp.append(country)
            print(f"  WARNING: No GDP data for {country}")

    # Write results to CSV
    print(f"\nWriting results to {output_file}...")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Country', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', 'Latitude', 'Longitude']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✓ Successfully processed {len(results)} countries")

    if missing_gdp:
        print(f"\n⚠ Warning: {len(missing_gdp)} countries missing GDP data:")
        for country in missing_gdp:
            print(f"  - {country}")

    print("\n" + "="*60)
    print("Summary Statistics (2025):")
    print("="*60)

    # Calculate some interesting stats
    gdp_percentages = [r['2025'] for r in results]
    avg_pct = sum(gdp_percentages) / len(gdp_percentages)
    max_pct = max(gdp_percentages)
    min_pct = min(gdp_percentages)

    max_country = next(r['Country'] for r in results if r['2025'] == max_pct)
    min_country = next(r['Country'] for r in results if r['2025'] == min_pct)

    print(f"Average Transaction Value as % of GDP: {avg_pct:.2f}%")
    print(f"Highest: {max_country} at {max_pct:.2f}%")
    print(f"Lowest: {min_country} at {min_pct:.2f}%")
    print("="*60)

if __name__ == "__main__":
    main()
