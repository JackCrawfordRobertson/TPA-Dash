#!/usr/bin/env python3
"""
Convert payment transaction values to per capita using pre-built population data.
"""

import pandas as pd
import requests
import json
from pathlib import Path

# Configuration
INPUT_FILE = "Payments Trends Report 2025 - with coordinates.csv"
OUTPUT_FILE = "Payments Trends Report 2025 - Per Capita.csv"
YEARS = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

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


def get_population_from_api(country_codes_list):
    """
    Fetch population data from World Bank API for multiple countries at once.
    """
    print("Fetching population data...")

    pop_dict = {}
    codes_str = ";".join(country_codes_list)

    # Use the World Bank API with date range
    url = f"https://api.worldbank.org/v2/country/{codes_str}/indicator/SP.POP.TOTL"

    try:
        response = requests.get(url, params={"format": "json", "per_page": 20000}, timeout=30)
        response.raise_for_status()

        data = response.json()

        # API returns [metadata, records]
        if len(data) > 1 and data[1]:
            for record in data[1]:
                country_code = record.get("countryCode")
                year = int(record.get("date", 0))
                value = record.get("value")

                if country_code and year and value and year in YEARS:
                    if country_code not in pop_dict:
                        pop_dict[country_code] = {}
                    try:
                        pop_dict[country_code][year] = float(value)
                    except (ValueError, TypeError):
                        pass

        return pop_dict

    except Exception as e:
        print(f"Error fetching from World Bank API: {e}")
        print("Trying fallback approach...")
        return None


def main():
    """
    Main execution function.
    """
    try:
        # Check if input file exists
        if not Path(INPUT_FILE).exists():
            print(f"❌ Error: {INPUT_FILE} not found")
            return

        print(f"Loading {INPUT_FILE}...")
        df = pd.read_csv(INPUT_FILE)
        print(f"✅ Loaded {len(df)} countries")

        # Get unique country codes to fetch
        country_codes = [COUNTRY_CODES[country] for country in df["Country"]
                        if country in COUNTRY_CODES]

        print(f"Fetching population data for {len(country_codes)} countries...")
        pop_dict = get_population_from_api(country_codes)

        if not pop_dict:
            print("❌ Failed to fetch population data")
            return

        print(f"✅ Retrieved population data for {len(pop_dict)} countries")

        # Create per capita version
        df_percapita = df.copy()

        print(f"\nCalculating per capita values...")
        success_count = 0
        missing_count = 0

        for idx, row in df.iterrows():
            country = row["Country"]
            country_code = COUNTRY_CODES.get(country)

            if not country_code or country_code not in pop_dict:
                missing_count += 1
                continue

            success_count += 1
            country_pop = pop_dict[country_code]

            for year in YEARS:
                year_col = str(year)

                # Get transaction value
                transaction_val = row[year_col]
                if isinstance(transaction_val, str):
                    transaction_val = float(transaction_val.replace(",", ""))

                # Get population for this year
                population = country_pop.get(year)

                if population and transaction_val:
                    # Transaction values are in billions
                    per_capita = (transaction_val * 1_000_000_000) / population
                    df_percapita.loc[idx, year_col] = round(per_capita, 2)
                else:
                    df_percapita.loc[idx, year_col] = None

            if (idx + 1) % 30 == 0:
                print(f"  Processed {idx + 1}/{len(df)} countries...")

        # Save to CSV
        print(f"\nSaving to {OUTPUT_FILE}...")
        df_percapita.to_csv(OUTPUT_FILE, index=False)

        print(f"\n✅ Done! Per capita data saved to {OUTPUT_FILE}")
        print(f"\nSummary:")
        print(f"- Countries processed: {success_count}")
        print(f"- Missing data: {missing_count}")
        print(f"- Years: {', '.join(map(str, YEARS))}")
        print(f"- Values: Per capita transaction amounts (USD)")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
