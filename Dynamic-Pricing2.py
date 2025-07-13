import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("C:/Users/DELL/Documents/brazilian_ecommerce_dataset.csv")

# Print available columns to check the correct date column
print(data.columns)

# Rename the correct column (replace with actual column name)
data = data.rename(columns={"order_purchase_timestamp": "date"})  # Change if needed

# Ensure 'date' column exists before proceeding
if "date" in data.columns:
    data["day_of_week"] = pd.to_datetime(data["date"]).dt.dayofweek
else:
    raise KeyError("The 'date' column does not exist. Please check the column name in your dataset.")

# Define features and target variable
X = data[["previous_sales", "competitor_price", "day_of_week"]]  # Ensure these columns exist
y = data["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict new data
new_data = {"previous_sales": 100, "competitor_price": 50, "day_of_week": 2}
predicted_price = model.predict([list(new_data.values())])
print("Predicted optimal price:", predicted_price)
