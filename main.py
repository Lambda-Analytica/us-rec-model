#---------------------------------------#
#----------------IMPORTS----------------#
#---------------------------------------#

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder


#---------------------------------------#
#---------------LOAD DATA---------------#
#---------------------------------------#

equipment_df = pd.read_csv('merged_equipment.csv', dtype={'ENT_PHY_ZIP': 'str'})
product_data = pd.read_csv('Clean Dinex Catalogue.csv', low_memory=False)


#---------------------------------------#
#---------------FUNCTIONS---------------#
#---------------------------------------#

# Helper function to clean engine series codes
def clean_engine_series(engine_series):
    replacements = {
        'ISX/SIGNATURE': 'Cummins ISX', 'ISX': 'Cummins ISX', 'ISX 15L': 'Cummins ISX',
        'MX13': 'MX-13', 'VE D16': 'VE-D16', 'VE D7': 'VE-D7', 'VE D12': 'VE-D12',
        'ISB': 'Cummins ISB', 'ISB 260': 'Cummins ISB', 'A26': 'International A26',
        'ISB 3.9': 'Cummins ISB', 'ISB 175': 'Cummins ISB', 'D13': 'VE-D13',
        'B6.7': 'Cummins B6.7', 'MP7-355E':'MP7'
    }
    return replacements.get(engine_series, engine_series)

def recommend_top_products(zipcode):
    products = pd.DataFrame(all_products[['Dinex Product', 'Dinex Number']].drop_duplicates())
    products['Zipcode'] = zipcode
    products['Dinex Product Encoded'] = label_encoder.transform(products['Dinex Product'])

    predicted_fleet_sizes = model.predict(products[['Zipcode', 'Dinex Product Encoded']])
    products['2024 Compatible VIOs'] = np.ceil(predicted_fleet_sizes)
    
    top_products = products.sort_values(by='2024 Compatible VIOs', ascending=False).head(10)
    return top_products[['Dinex Product', 'Dinex Number', '2024 Compatible VIOs']]


#---------------------------------------#
#---------------CLEAN DATA--------------#
#---------------------------------------#

# Manually add leading zero if Zipcode is exactly 4 characters long
equipment_df['Zipcode'] = equipment_df['Zipcode'].apply(lambda x: '0' + x if len(x) == 4 else x)

# Apply cleaning function
equipment_df['Engine'] = equipment_df['Engine'].apply(clean_engine_series)
product_data['Engine'] = product_data['Engine'].replace('MP7-355E', 'MP7')

# Convert data types to 'category' where applicable
equipment_df['Engine'] = equipment_df['Engine'].astype('category')
product_data['Engine'] = product_data['Engine'].astype('category')


#---------------------------------------# many computers may not have enough RAM to filter
#---------------FILTER DATA-------------# for all engines via a loop. So, it is done 'piecemeal'
#---------------------------------------# here for each engine.

# Filter the equipment dataframe for 'MP8' engine
mp8_equipment = equipment_df[equipment_df['Engine'] == 'MP8']
# Filter the product dataframe for 'MP8' engine
mp8_products = product_data[product_data['Engine'] == 'MP8']
# Merge the two dataframes on the 'Engine' column
merged_data_mp8 = pd.merge(mp8_equipment, mp8_products, on='Engine')
# Group by product details and sum the 'Fleet Size'
product_compatibility_count_mp8 = merged_data_mp8.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
# check the results for the 'MP8' engine for sanity
#print(product_compatibility_count_mp8)

# Filter the equipment dataframe for 'MP7' engine
mp7_equipment = equipment_df[equipment_df['Engine'] == 'MP7']
mp7_products = product_data[product_data['Engine'] == 'MP7']
merged_data_mp7 = pd.merge(mp7_equipment, mp7_products, on='Engine')
product_compatibility_count_mp7 = merged_data_mp7.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_mp7)

# Filter the equipment dataframe for 'VE-D13' engine
ved13_equipment = equipment_df[equipment_df['Engine'] == 'VE-D13']
ved13_products = product_data[product_data['Engine'] == 'VE-D13']
merged_data_ved13 = pd.merge(ved13_equipment, ved13_products, on='Engine')
product_compatibility_count_ved13 = merged_data_ved13.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_ved13)

# Filter the equipment dataframe for 'Cummins ISX' engine
isx_equipment = equipment_df[equipment_df['Engine'] == 'Cummins ISX']
isx_products = product_data[product_data['Engine'] == 'Cummins ISX']
merged_data_isx = pd.merge(isx_equipment, isx_products, on='Engine')
product_compatibility_count_isx = merged_data_isx.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_isx)

# Filter the equipment dataframe for 'Cummins ISB' engine
isb_equipment = equipment_df[equipment_df['Engine'] == 'Cummins ISB']
isb_products = product_data[product_data['Engine'] == 'Cummins ISB']
merged_data_isb = pd.merge(isb_equipment, isb_products, on='Engine')
product_compatibility_count_isb = merged_data_isb.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_isb)

# Filter the equipment dataframe for 'International A26' engine
a26_equipment = equipment_df[equipment_df['Engine'] == 'International A26']
a26_products = product_data[product_data['Engine'] == 'International A26']
merged_data_a26 = pd.merge(a26_equipment, a26_products, on='Engine')
product_compatibility_count_a26 = merged_data_a26.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_a26)

# Filter the equipment dataframe for 'DD15' engine
dd15_equipment = equipment_df[equipment_df['Engine'] == 'DD15']
dd15_products = product_data[product_data['Engine'] == 'DD15']
merged_data_dd15 = pd.merge(dd15_equipment, dd15_products, on='Engine')
product_compatibility_count_dd15= merged_data_dd15.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_dd15)

# Filter the equipment dataframe for 'DD13' engine
dd13_equipment = equipment_df[equipment_df['Engine'] == 'DD13']
dd13_products = product_data[product_data['Engine'] == 'DD13']
merged_data_dd13 = pd.merge(dd13_equipment, dd13_products, on='Engine')
product_compatibility_count_dd13= merged_data_dd13.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_dd13)

# Filter the equipment dataframe for 'MX-13' engine
mx13_equipment = equipment_df[equipment_df['Engine'] == 'MX-13']
mx13_products = product_data[product_data['Engine'] == 'MX-13']
merged_data_mx13 = pd.merge(mx13_equipment, mx13_products, on='Engine')
product_compatibility_count_mx13 = merged_data_mx13.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_mx13)

# Filter the equipment dataframe for 'PX-7' engine
px7_equipment = equipment_df[equipment_df['Engine'] == 'PX-7']
px7_products = product_data[product_data['Engine'] == 'PX-7']
merged_data_px7 = pd.merge(px7_equipment, px7_products, on='Engine')
product_compatibility_count_px7 = merged_data_px7.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_px7)

# Filter the equipment dataframe for 'PX-9' engine
px9_equipment = equipment_df[equipment_df['Engine'] == 'PX-9']
px9_products = product_data[product_data['Engine'] == 'PX-9']
merged_data_px9 = pd.merge(px9_equipment, px9_products, on='Engine')
product_compatibility_count_px9 = merged_data_px9.groupby(['Dinex Number', 'Dinex Product', 'Engine', 'Zipcode'])['Fleet Size'].sum().reset_index()
#print(product_compatibility_count_px9)

# Concatenate all DataFrames into a single DataFrame. this will be computationally expensive
# List of product compatibility counts for different engines
product_counts = [
    product_compatibility_count_mp8, product_compatibility_count_mp7,
    product_compatibility_count_ved13, product_compatibility_count_isx,
    product_compatibility_count_isb, product_compatibility_count_a26,
    product_compatibility_count_dd15, product_compatibility_count_b67,
    product_compatibility_count_dd13, product_compatibility_count_mx13,
    product_compatibility_count_px7, product_compatibility_count_px9
]
all_products = pd.concat(product_counts, ignore_index=True)

# Save the concatenated DataFrame to a single CSV file
all_products.to_csv('All_Product_Compatibilities.csv', index=False)


#---------------------------------------#
#--------------TRAIN MODEL--------------#
#---------------------------------------#

# Encode categorical variables
label_encoder = LabelEncoder()
all_products['Dinex Product Encoded'] = label_encoder.fit_transform(all_products['Dinex Product'])

# Select features and target
# Note that future iterations should include "Year" IOT predict stock recommendation
# for future years but different training method (e.g., time-series analysis) may be needed
X = all_products[['Zipcode', 'Dinex Product Encoded']]
y = all_products['Fleet Size']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# prompt user to input desired zip code
zipcode_input = input("Enter a zip code to find the top 10 products: ")
top_products = recommend_top_products(int(zipcode_input))
print("Top 10 Recommended Products:")
# display top products by Dinex number, product and zipcode
print(top_products)

# example output:
#Enter a zipcode to find the top 10 products:  33435
#
#Top 10 Recommended Products:
#        Dinex Product Dinex Number  2024 Compatible VIOs
#194348      PM sensor       8CL009                 130.0
#692466       Injector       2AT002                  64.0
#660945       Injector       8CL010                  64.0
#5618320      Injector       5EL088                  64.0
#3739916      Injector       3FL021                  64.0
#201289       Injector       8CL012                  64.0
#2483154      Injector       5EL061                  64.0
#3148652    NOX Sensor       5EL004                  61.0
#166584     NOX Sensor       8CL001                  61.0
#4491402    NOX Sensor        22025                  61.0

