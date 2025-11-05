#!/usr/bin/env python3
"""
Convert payment transaction values to per capita by fetching population data
from the World Bank API and dividing transaction values by population.
"""

import pandas as pd
import requests
import json
from pathlib import Path
import time

# Configuration
INPUT_FILE = "Payments Trends Report 2025 - with coordinates.csv"
OUTPUT_FILE = "Payments Trends Report 2025 - Per Capita.csv"
YEARS = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

# World Bank API endpoint for population data
# Using indicator SP.POP.TOTL (Total Population)
WORLD_BANK_API = "https://api.worldbank.org/v2/country/{country_code}/indicator/SP.POP.TOTL"

# Country name to World Bank country code mapping
COUNTRY_CODES = {
    "Argentina": "ARG", "Armenia": "ARM", "Australia": "AUS", "Austria": "AUT",
    "Azerbaijan": "AZE", "Bahrain": "BHR", "Bangladesh": "BGD", "Belarus": "BLR",
    "Belgium": "BEL", "Belize": "BLZ", "Benin": "BEN", "Bhutan": "BTN",
    "Bolivia": "BOL", "Bosnia and Herzegovina": "BIH", "Botswana": "BWA", "Brazil": "BRA",
    "Brunei Darussalam": "BRN", "Bulgaria": "BGR", "Burkina Faso": "BFA", "Burundi": "BDI",
    "Cambodia": "KHM", "Cameroon": "CMR", "Canada": "CAN", "Chad": "TCD",
    "Chile": "CHL", "China": "CHN", "Costa Rica": "CRI", "Croatia": "HRV",
    "Cuba": "CUB", "Cyprus": "CYP", "Czechia": "CZE", "Denmark": "DNK",
    "Dominican Republic": "DOM", "Ecuador": "ECU", "Egypt": "EGY", "El Salvador": "SLV",
    "Equatorial Guinea": "GNQ", "Estonia": "EST", "Ethiopia": "ETH", "Fiji": "FJI",
    "Finland": "FIN", "France": "FRA", "Gabon": "GAB", "Gambia": "GMB",
    "Germany": "DEU", "Ghana": "GHA", "Greece": "GRC", "Guatemala": "GTM",
    "Guinea": "GIN", "Guyana": "GUY", "Haiti": "HTI", "Honduras": "HND",
    "Hungary": "HUN", "Iceland": "ISL", "India": "IND", "Indonesia": "IDN",
    "Iran": "IRN", "Iraq": "IRQ", "Ireland": "IRL", "Israel": "ISR",
    "Italy": "ITA", "Ivory Coast": "CIV", "Jamaica": "JAM", "Japan": "JPN",
    "Jordan": "JOR", "Kazakhstan": "KAZ", "Kenya": "KEN", "Kuwait": "KWT",
    "Kyrgyzstan": "KGZ", "Laos": "LAO", "Latvia": "LVA", "Lebanon": "LBN",
    "Lesotho": "LSO", "Lithuania": "LTU", "Luxembourg": "LUX", "Madagascar": "MDG",
    "Malawi": "MWI", "Malaysia": "MYS", "Malta": "MLT", "Mauritius": "MUS",
    "Mexico": "MEX", "Moldova": "MDA", "Mongolia": "MNG", "Montenegro": "MNE",
    "Morocco": "MAR", "Mozambique": "MOZ", "Myanmar": "MMR", "Namibia": "NAM",
    "Nepal": "NPL", "Netherlands": "NLD", "New Zealand": "NZL", "Nicaragua": "NIC",
    "Niger": "NER", "Nigeria": "NGA", "North Macedonia": "MKD", "Norway": "NOR",
    "Oman": "OMN", "Pakistan": "PAK", "Panama": "PAN", "Papua New Guinea": "PNG",
    "Paraguay": "PRY", "Philippines": "PHL", "Poland": "POL", "Portugal": "PRT",
    "Puerto Rico": "PRI", "Republic of the Congo": "COG", "Romania": "ROU", "Russia": "RUS",
    "Rwanda": "RWA", "Saudi Arabia": "SAU", "Senegal": "SEN", "Serbia": "SRB",
    "Seychelles": "SYC", "Sierra Leone": "SLE", "Singapore": "SGP", "Slovakia": "SVK",
    "Slovenia": "SVN", "South Africa": "ZAF", "South Korea": "KOR", "Spain": "ESP",
    "Sri Lanka": "LKA", "Sudan": "SDN", "Suriname": "SUR", "Sweden": "SWE",
    "Switzerland": "CHE", "Taiwan": "TWN", "Tajikistan": "TJK", "Tanzania": "TZA",
    "Thailand": "THA", "Timor-Leste": "TLS", "Togo": "TGO", "Tunisia": "TUN",
    "Turkey": "TUR", "Turkmenistan": "TKM", "Uganda": "UGA", "Ukraine": "UKR",
    "United Arab Emirates": "ARE", "United Kingdom": "GBR", "United States": "USA",
    "Uruguay": "URY", "Uzbekistan": "UZB", "Vietnam": "VNM", "Zambia": "ZMB",
    "Zimbabwe": "ZWE"
}


def fetch_population_data(country_code, year):
    """
    Fetch population data from World Bank API for a specific country and year.
    """
    try:
        url = f"{WORLD_BANK_API.format(country_code=country_code)}?date={year}&format=json"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        # API returns [metadata, data] array
        if len(data) > 1 and data[1] and len(data[1]) > 0:
            population = data[1][0].get("value")
            if population:
                return float(population)
        return None

    except Exception as e:
        print(f"Error fetching data for {country_code} ({year}): {e}")
        return None


def load_and_process():
    """
    Load CSV, fetch population data, and calculate per capita values.
    """
    print(f"Loading {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)

    # Create a copy for per capita calculations
    df_percapita = df.copy()

    print(f"Fetching population data from World Bank API...")
    print(f"This may take a moment ({len(df) * len(YEARS)} requests)...\n")

    # For each country and year, fetch population and calculate per capita
    for idx, row in df.iterrows():
        country = row["Country"]
        country_code = COUNTRY_CODES.get(country)

        if not country_code:
            print(f"⚠️  Warning: No country code found for '{country}' - skipping")
            continue

        print(f"Processing {country} ({idx + 1}/{len(df)})...")

        for year in YEARS:
            year_col = str(year)

            # Get transaction value (might have commas for thousands)
            transaction_val = row[year_col]
            if isinstance(transaction_val, str):
                transaction_val = float(transaction_val.replace(",", ""))

            # Fetch population
            population = fetch_population_data(country_code, year)

            if population and transaction_val:
                # Convert transaction value from billions to actual value, then divide by population
                per_capita = (transaction_val * 1_000_000_000) / population
                df_percapita.loc[idx, year_col] = round(per_capita, 2)
            else:
                if not population:
                    print(f"   Could not fetch population for {country} ({year})")
                df_percapita.loc[idx, year_col] = None

            # Be nice to the API - add small delay
            time.sleep(0.2)

    return df_percapita


def main():
    """
    Main execution function.
    """
    try:
        # Check if input file exists
        if not Path(INPUT_FILE).exists():
            print(f"Error: {INPUT_FILE} not found in current directory")
            return

        # Process data
        df_percapita = load_and_process()

        # Save to new CSV
        print(f"\nSaving to {OUTPUT_FILE}...")
        df_percapita.to_csv(OUTPUT_FILE, index=False)

        print(f"✅ Done! Per capita data saved to {OUTPUT_FILE}")
        print(f"\nSummary:")
        print(f"- Total countries processed: {len(df_percapita)}")
        print(f"- Years: {', '.join(map(str, YEARS))}")
        print(f"- Values are per capita transaction amounts (in USD)")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
