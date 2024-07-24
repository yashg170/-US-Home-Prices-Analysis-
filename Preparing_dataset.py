**Objective**: Develop a data science model using publicly available data to examine the relationship between selected variables and home prices, using the S&P Case-Shiller Index as a proxy for home prices.

The features selected for analysis are:


*   Construction Price Index
*   Consumer Price Index (CPI)
*   GDP per Capita
*   House Price
*   Household Median Income
*   Interest Rate
*   Monthly House Supply
*   Subsidies
*   Total Households
*   Urban Population
*   Working Population

The data is collected from (FRED)[https://fred.stlouisfed.org/].

Datasets of these features are processed and combined to give the final processed dataset without any null or absurd data values.
"""

import pandas as pd
import numpy as np

# Reading CASE-SHILLER Price Index into a dataframe
df_price = pd.read_csv("house_price.csv")

# Changing data type of date col
df_price["DATE"] = pd.to_datetime(df_price["DATE"])

# Limiting to last 20 years
temp = df_price["DATE"] >= "2000-01-01"
df_price = df_price[temp]

df_price.reset_index(inplace = True)
df_price.drop(columns=["index"], inplace = True)

df_price["Year"] = df_price["DATE"].dt.year
df_price["Month"] = df_price["DATE"].dt.month

df_price
df_price.shape

# Loading the Per Capita GDP data into a DataFrame

df_gdpc = pd.read_csv("GDP_per_capita.csv", header =None, skiprows=1, names=["DATE","A939RX0Q048SBEA"])
df_gdpc.rename(columns={"A939RX0Q048SBEA":"Per_Capita_GDP"}, inplace = True)

temp = df_gdpc["DATE"] >= "2000-01-01"
df_gdpc = df_gdpc[temp]

df_gdpc.reset_index(inplace = True)
df_gdpc.drop(columns=["index"], inplace = True)
df_gdpc
df_gdpc.shape

# Loading the Working Population data into a DataFrame
df_wp = pd.read_csv("working_population.csv")
df_wp = df_wp.rename(columns={'LFWA64TTUSM647S': 'Working_Population'})

temp = df_wp["DATE"] >= "2000-01-01"
df_wp = df_wp[temp]

df_wp.reset_index(inplace = True)
df_wp.drop(columns=["index"], inplace = True)
df_wp
df_wp.shape

# Loading the Interest Rate data into a DataFrame
df_Fed_rate = pd.read_csv("Interest_rate.csv")
df_Fed_rate = df_Fed_rate.rename(columns={'FEDFUNDS': 'Interest_Rate'})

temp = df_Fed_rate["DATE"] >= "2000-01-01"
df_Fed_rate = df_Fed_rate[temp]

df_Fed_rate.reset_index(inplace = True)
df_Fed_rate.drop(columns=["index"], inplace = True)
df_Fed_rate
# df_Fed_rate.shape

# Loading Construction Price Data into a dataframe

df_cp = pd.read_csv("Construction_price_index.csv",header=None, skiprows=1, names=["DATE", "WPUSI012011"])

# Renaming cols
df_cp.rename(columns={"WPUSI012011" : "Construction Price"}, inplace =True)

temp = df_cp["DATE"] >= "2000-01-01"
df_cp = df_cp[temp]

df_cp.reset_index(inplace = True)
df_cp.drop(columns=["index"], inplace = True)
df_cp

#Consumer Price Index Data

df_CPI = pd.read_csv("CPI.csv", header=None, skiprows=1, names=["DATE","CPIAUCSL"])

df_CPI.rename(columns={"CPIAUCSL": "CPI"}, inplace=True)

temp = df_CPI["DATE"] >= "2000-01-01"
df_CPI = df_CPI[temp]

df_CPI.reset_index(inplace = True)
df_CPI.drop(columns=["index"], inplace = True)
df_CPI

#Loading Monthly house supply Data
df_house = pd.read_csv("Monthly_HouseSupply.csv", header=None, skiprows=1, names=["DATE", "MSACSR"])

df_house.rename(columns={"MSACSR": "New_House_Supply"}, inplace=True)

temp = df_house["DATE"] >= "2000-01-01"
df_house = df_house[temp]

df_house.reset_index(inplace = True)
df_house.drop(columns=["index"], inplace = True)
df_house

#Loading Urban Population Data
df_urban = pd.read_csv("Urban_Population.csv")
# Converting Year to Date Format
df_urban.rename(columns={"Urban population (% of total population)": "Urban", "Year": "DATE"}, inplace=True)
df_urban["DATE"]=pd.to_datetime(df_urban['DATE'].astype(str) + '-01-01')

temp = df_urban["DATE"] >= "2000-01-01"
df_urban = df_urban[temp]

df_urban.reset_index(inplace = True)
df_urban.drop(columns=["index"], inplace = True)

df_urban.columns

#Housing Subsidies

df_subsidy=pd.read_csv("Subsidies.csv",header=None, skiprows=1, names=["DATE", "Subsidies"])

temp = df_subsidy["DATE"] >= "2000-01-01"
df_subsidy = df_subsidy[temp]

df_subsidy.reset_index(inplace = True)
df_subsidy.drop(columns=["index"], inplace = True)

df_subsidy.tail()
df_subsidy.columns

# Loading the Real Median Household Income data into a DataFrame
df_income = pd.read_csv("Household_median_income.csv", header=None, skiprows=1, names=["DATE", "MEHOINUSA672N"])

df_income.rename(columns={"MEHOINUSA672N": "median_income"}, inplace=True)

temp = df_income["DATE"] >= "2000-01-01"
df_income = df_income[temp]

df_income.reset_index(inplace = True)
df_income.drop(columns=["index"], inplace = True)
df_income.columns

# Total number of households Data
df_household = pd.read_csv("TotalHouseholds.csv",header=None,skiprows=1, names=["DATE", "TTLHH"])
df_household =df_household.rename(columns={"TTLHH": "Total_Households"})

temp = df_household["DATE"] >= "2000-01-01"
df_household = df_household[temp]

df_household.reset_index(inplace = True)
df_household.drop(columns=["index"], inplace = True)
df_household.columns

#Merging

# Converting the 'DATE' column in df_pcgdp to datetime format
df_gdpc["DATE"]= pd.to_datetime(df_gdpc["DATE"])

# Merging df_CS with df_pcgdp on the 'DATE' column using a left join
df_price=pd.merge(df_price,df_gdpc,how="left")

df_price
df_price.columns
#We need to interpolate the data

# Create empty Data Frame to store combined df
df = pd.DataFrame()
monthly_dataframes = [df_price, df_wp, df_Fed_rate, df_cp, df_house, df_CPI]
for dfi in monthly_dataframes:
    # Remove leading and trailing whitespaces from column names
    dfi.columns = dfi.columns.str.strip()
    if 'DATE' in dfi.columns:
       dfi['DATE'] = pd.to_datetime(dfi['DATE'])
       dfi.set_index('DATE', inplace=True)

       df= pd.concat([df,dfi], axis =1)
    else:
        print(f"Warning: 'DATE' column not found in DataFrame. Skipping this DataFrame.")

df.reset_index(inplace=True)

#Merging other datatframes

left= [df_urban,df_subsidy,df_income,df_household]
for df_temp in left:
    if 'Year' not in df_temp.columns:
        # print(df_temp['DATE'])
        df_temp['Year'] = pd.DatetimeIndex(df_temp['DATE']).year
        df_temp.set_index('DATE', inplace=True)
        # print(df.columns)
        # print(df_temp.columns)
        df = pd.merge(df, df_temp,how="left", on='Year')
    else:
        df_temp.set_index('Year', inplace=True)
        # df_temp.columns
        df = pd.merge(df, df_temp, how="left", on='Year')
df

df.set_index("DATE", inplace=True)
df.columns

print(df.shape)

df.isna().sum()

# Filling missing values in the Per_Capita_GDP column using interpolation
df["Per_Capita_GDP"] = df["Per_Capita_GDP"].interpolate()

df.dropna(inplace=True)

df.isna().sum()

df

print("Shape of dataset: ", df.shape)

df.to_csv("processed_dataset.csv")
