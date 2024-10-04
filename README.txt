# Engine Fleet Size and Product Compatibility Prediction

This project is designed to analyze equipment data and product catalog information to predict 
the compatibility of products with engine fleets based on ZIP codes. The system identifies 
fleet sizes and suggests the top 10 products for a given ZIP code based on a random forest 
regression model that predicts fleet size compatibility with Dinex products.

## Project Overview

The project uses two datasets:
- **`merged_equipment.csv`**: Contains equipment data including city, state, country, ZIP code, engine series code, fleet size, and other attributes.
- **`Clean Dinex Catalogue.csv`**: Contains product information including Dinex product names, product numbers, and the engine types they are compatible with.

The goal is to predict and recommend Dinex products based on ZIP code fleet sizes, with specific focus on various engine types (e.g., MP7, MP8, Cummins ISX, etc.).

## Features

- Cleans and processes equipment and product data.
- Standardizes and categorizes engine types for consistency in analysis.
- Filters and merges datasets by engine type.
- Predicts the fleet size based on ZIP code and engine compatibility.
- Recommends the top 10 Dinex products for a given ZIP code using a trained Random Forest Regressor model.

## Data Processing Steps

1. **Load and Clean Data**:
   - Read and clean `merged_equipment.csv` and `Clean Dinex Catalogue.csv`.
   - Standardize engine series codes to ensure consistency.
   - Add missing leading zeroes to ZIP codes that are only 4 characters long.

2. **Engine Data Preparation**:
   - Filter the equipment and product data for each specific engine type (e.g., MP7, MP8, Cummins ISX).
   - Merge the equipment and product data on the engine type.
   - Group the merged data by product details and ZIP code to sum fleet sizes.

3. **Model Training**:
   - Encode categorical variables, such as the Dinex product name.
   - Train a RandomForest Regressor model to predict fleet sizes based on ZIP code and product compatibility.

4. **Product Recommendations**:
   - For a given ZIP code, the model predicts the fleet sizes of different products.
   - The system then returns the top 10 recommended Dinex products based on predicted fleet sizes.

## Technologies Used

- **Python 3**: The programming language used to build the project.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **scikit-learn**: For machine learning (RandomForest Regressor).
- **CSV**: Data files in CSV format are used for analysis.

## Installation

To run this project locally, follow the steps below:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Linux or MacOS
venv\Scripts\activate  # For Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Prepare the datasets
Make sure you have the following CSV files in the root directory:
    merged_equipment.csv
    Clean Dinex Catalogue.csv

### 5. Run the application
python main.py

### 6. Predict Product Compatibility
You will be prompted to enter a ZIP code. The system will then display the
top 10 recommended products based on fleet size predictions for that ZIP code.

## Project Structure

├── main.py                            # Main Python script that runs the program
├── merged_equipment.csv              # Dataset with equipment information (not included in repo)
├── Clean Dinex Catalogue.csv         # Dataset with product catalog information (not included in repo)
├── All_Product_Compatibilities.csv   # Output CSV file with merged product compatibilities
├── requirements.txt                  # Dependencies for the project
├── Procfile                          # optional Configuration file for deployment (e.g., Heroku)
└── .gitignore                        # Git ignore file

## Sample Input/Output

Input
Enter a zipcode to find the top 10 products:

Output
Enter a zipcode to find the top 10 products:  33435

Top 10 Recommended Products:
        Dinex Product Dinex Number  2024 Compatible VIOs
194348      PM sensor       8CL009                 130.0
692466       Injector       2AT002                  64.0
660945       Injector       8CL010                  64.0
5618320      Injector       5EL088                  64.0
3739916      Injector       3FL021                  64.0
201289       Injector       8CL012                  64.0
2483154      Injector       5EL061                  64.0
3148652    NOX Sensor       5EL004                  61.0
166584     NOX Sensor       8CL001                  61.0
4491402    NOX Sensor        22025                  61.0



