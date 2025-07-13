import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
order_items = pd.read_csv("C:/Users/DELL/Documents/olist_order_items_dataset.csv")
orders = pd.read_csv("C:/Users/DELL/Documents/olist_orders_dataset.csv")
order_payments = pd.read_csv("C:/Users/DELL/Documents/olist_order_payments_dataset.csv")
products = pd.read_csv("C:/Users/DELL/Documents/olist_products_dataset.csv")
customers = pd.read_csv("C:/Users/DELL/Documents/olist_customers_dataset.csv")
sellers = pd.read_csv("C:/Users/DELL/Documents/olist_sellers_dataset.csv")
product_category_translation = pd.read_csv("C:/Users/DELL/Documents/product_category_name_translation.csv")
merged = order_items.merge(orders, on='order_id') \
                    .merge(order_payments, on=['order_id']) \
                    .merge(products, on='product_id') \
                    .merge(customers, on='customer_id') \
                    .merge(sellers, on='seller_id') \
                    .merge(product_category_translation, on='product_category_name')
merged.to_csv('C:/Users/DELL/Documents/brazilian_ecommerce_dataset.csv', index=False)
df = pd.read_csv('C:/Users/DELL/Documents/brazilian_ecommerce_dataset.csv')
df = df.drop(['seller_id', 'freight_value'], axis=1)
df = df[df['customer_state'].isin(["SP", "RJ", "MG"])]
df = df[['product_category_name', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm', 'customer_state', 'price']]
df = df.dropna()
df = df[(df['price'] >= df['price'].quantile(0.05)) & (df['price'] <= df['price'].quantile(0.95))]
df = pd.get_dummies(df, columns=['product_category_name', 'customer_state'])
X_train, X_test, y_train, y_test = train_test_split(df.drop('price', axis=1), df['price'], test_size=0.2, random_state=42)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("Mean absolute error:", mae)
