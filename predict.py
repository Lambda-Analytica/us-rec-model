import numpy as np
import joblib

# Load the trained model and label encoder
model = joblib.load('\\model\\train_model.joblib')
# Load the trained label encoder
label_encoder = joblib.load('label_encoder.joblib')

def prepare_input(zipcode, products_df):
    """Prepare input data for prediction by encoding categorical variables and aligning with the model's expectations."""
    products = products_df[['Dinex Product', 'Dinex Number']].drop_duplicates()
    products['Zipcode'] = zipcode
    products['Dinex Product Encoded'] = label_encoder.transform(products['Dinex Product'])
    return products[['Zipcode', 'Dinex Product Encoded']]

def make_prediction(zipcode, products_df):
    """Predict the fleet sizes for given products in a specified zipcode."""
    input_data = prepare_input(zipcode, products_df)
    predicted_fleet_sizes = model.predict(input_data)
    products_df['Predicted Fleet Size'] = np.ceil(predicted_fleet_sizes)  # Apply ceiling to the predictions

    # Add predicted data back to products dataframe
    result_df = products_df.copy()
    result_df['2024 Compatible VIOs'] = products_df['Predicted Fleet Size']
    
    # Sort and select top 10 products
    top_products = result_df.sort_values(by='2024 Compatible VIOs', ascending=False).head(10)
    return top_products[['Dinex Product', 'Dinex Number', '2024 Compatible VIOs']]
"E:\Dinex_US\reecommendation_project\model\train_model.py"
