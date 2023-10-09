import numpy as np
import pandas as pd
import re
from datetime import datetime, timedelta


# Load Transform and clean the energy data as per the given instructions
energy_data = pd.read_excel(
    r"task2/Data/Energy_Indicators.xls", skiprows=17, skipfooter=38
)
energy_data = energy_data[["Unnamed: 2", "Petajoules", "Gigajoules", "%"]]

previous_names = energy_data.columns
new_names = ["Country", "Energy Supply", "Energy Supply per Capita", "% Renewable's"]

renaming = dict(zip(previous_names, new_names))
energy_data.rename(columns=renaming, inplace=True)
energy_data.replace("...", np.nan, inplace=True)
energy_data["Energy Supply"] = energy_data["Energy Supply"].transform(
    lambda x: x * 1000000
)
dict_country_replace = {
    "Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong",
}
energy_data["Country"] = energy_data["Country"].replace(dict_country_replace)
energy_data["Country"] = energy_data["Country"].transform(
    lambda x: re.sub(r"\([^)]*\)", "", x)
)

# Load Transform and clean world bank data

GDP = pd.read_csv("task2\Data\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5871885.csv", skiprows=4)

GDP.rename(columns={"Country Name": "Country"}, inplace=True)

GDP["Country"] = GDP["Country"].replace(
    {
        "Korea, Rep.": "South Korea",
        "Iran, Islamic Rep.": "Iran",
        "Hong Kong SAR, China": "Hong Kong",
    }
)

# LOAD Transform and clean

ScimEn = pd.read_excel(r"task2\Data\scimagojr country rank 1996-2022.xlsx")

# Merging the datasets
ScimEn = ScimEn.drop(["Region"], axis=1)

energy_data.set_index("Country", inplace=True)
GDP.set_index("Country", inplace=True)
ScimEn.set_index("Country", inplace=True)

ScimEn = ScimEn[ScimEn["Rank"] <= 15]

energy_ScimEn = ScimEn.merge(energy_data, how="left", on="Country")

# current_year = datetime.now().year
current_year = datetime(2015, 1, 1).year

# Create a list of string values for the last 10 years
last_ten_years = [str(year) for year in range(current_year - 9, current_year + 1, 1)]
GDP = GDP[last_ten_years]

final_data = energy_ScimEn.merge(GDP, how="left", on="Country")
print(final_data)
final_data.to_csv("task2/output/final.csv")
