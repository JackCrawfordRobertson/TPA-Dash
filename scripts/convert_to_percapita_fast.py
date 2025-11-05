#!/usr/bin/env python3
"""
Fast version: Convert payment transaction values to per capita.
Downloads population data once in bulk, then performs calculations.
"""

import pandas as pd
import requests
import io
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

# Configuration
INPUT_FILE = "Payments Trends Report 2025 - with coordinates.csv"
OUTPUT_FILE = "Payments Trends Report 2025 - Per Capita.csv"
YEARS = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

# Country name mapping to World Bank country codes
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


def download_population_data():
    """
    Download World Bank population data for all countries and years.
    Uses the bulk CSV download API which is much faster.
    """
    print("Downloading population data from World Bank...")

    # World Bank API bulk download for total population indicator
    url = "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # The API returns a zip file, so we need to extract it
        import zipfile
        import io as io_module

        zip_file = zipfile.ZipFile(io_module.BytesIO(response.content))
        csv_file = [f for f in zip_file.namelist() if f.endswith('.csv') and 'API_SP.POP.TOTL' in f][0]

        df = pd.read_csv(zip_file.open(csv_file))
        print(f"✅ Downloaded population data with {len(df)} countries")
        return df

    except Exception as e:
        print(f"❌ Error downloading data: {e}")
        return None


def parse_population_data(df_pop):
    """
    Parse World Bank population data into a dictionary.
    Returns: {country_code: {year: population}}
    """
    # World Bank CSV has format: Country Name, Country Code, Indicator Name, Indicator Code, then years as columns
    pop_dict = {}

    for idx, row in df_pop.iterrows():
        country_code = row['Country Code']
        if pd.isna(country_code):
            continue

        pop_dict[country_code] = {}

        for year in YEARS:
            year_col = str(year)
            if year_col in row:
                try:
                    pop = float(row[year_col])
                    if not pd.isna(pop):
                        pop_dict[country_code][year] = pop
                except (ValueError, TypeError):
                    pass

    return pop_dict


def main():
    """
    Main execution function.
    """
    try:
        # Check if input file exists
        if not Path(INPUT_FILE).exists():
            print(f"❌ Error: {INPUT_FILE} not found in current directory")
            return

        print(f"Loading {INPUT_FILE}...")
        df = pd.read_csv(INPUT_FILE)
        print(f"✅ Loaded {len(df)} countries")

        # Download population data
        df_pop = download_population_data()
        if df_pop is None:
            return

        # Parse population data
        print("Parsing population data...")
        pop_dict = parse_population_data(df_pop)
        print(f"✅ Parsed population for {len(pop_dict)} country codes")

        # Create per capita version
        df_percapita = df.copy()

        # Process each country
        print(f"\nCalculating per capita values...")
        success_count = 0
        missing_pop = []

        for idx, row in df.iterrows():
            country = row["Country"]
            country_code = COUNTRY_CODES.get(country)

            if not country_code:
                continue

            country_pop = pop_dict.get(country_code, {})

            if not country_pop:
                missing_pop.append(country)
                continue

            success_count += 1

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

            # Progress indicator
            if (idx + 1) % 20 == 0:
                print(f"  Processed {idx + 1}/{len(df)} countries...")

        # Save to CSV
        print(f"\nSaving to {OUTPUT_FILE}...")
        df_percapita.to_csv(OUTPUT_FILE, index=False)

        print(f"\n✅ Done! Per capita data saved to {OUTPUT_FILE}")
        print(f"\nSummary:")
        print(f"- Countries with population data: {success_count}")
        print(f"- Years processed: {', '.join(map(str, YEARS))}")
        print(f"- Values: Per capita transaction amounts (in USD)")

        if missing_pop:
            print(f"\n⚠️  Countries without population data ({len(missing_pop)}):")
            for country in missing_pop[:10]:
                print(f"   - {country}")
            if len(missing_pop) > 10:
                print(f"   ... and {len(missing_pop) - 10} more")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
