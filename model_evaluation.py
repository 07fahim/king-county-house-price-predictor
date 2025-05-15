import pandas as pd # type: ignore
import numpy as np
from time import time
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor # type: ignore
from sklearn.tree import DecisionTreeRegressor # type: ignore
from sklearn.linear_model import LinearRegression, Ridge, Lasso # type: ignore
from sklearn.svm import SVR # type: ignore
from sklearn.neighbors import KNeighborsRegressor # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error # type: ignore
from xgboost import XGBRegressor # type: ignore
import joblib # type: ignore
import os

# Create data directory
os.makedirs('data', exist_ok=True)

# Load the dataset
df = pd.read_csv(r"D:\KING_PRICE_PREDICTION\king_county_house_price_predictor\kc_house_data.csv")  # Update path if needed

# Feature selection
X = df[['sqft_living', 'grade', 'bathrooms', 'bedrooms', 'waterfront', 'view', 'sqft_basement', 'yr_built', 'lat', 'long']]
y = df['price']  # Target variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define evaluation function
def evaluate(name, model, X_train, X_test, y_train, y_test, results):
    start = time()
    model.fit(X_train, y_train)
    end = time()
    train_time = end - start
    preds = model.predict(X_test)
    r2 = model.score(X_test, y_test)
    evs = explained_variance_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)
    # Append results to the list
    results.append({
        "Model": name,
        "R2 Score": r2,
        "Explained Variance": evs,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "Training Time (seconds)": train_time
    })

# Create results list
results = []

# Standardize features for SVR
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Models list
models = [
    ("Random Forest", RandomForestRegressor(n_estimators=400, random_state=0)),
    ("Gradient Boosting", GradientBoostingRegressor(n_estimators=400, max_depth=5, learning_rate=0.1)),
    ("AdaBoost", AdaBoostRegressor(n_estimators=50, learning_rate=0.2, loss='exponential')),
    ("Decision Tree", DecisionTreeRegressor()),
    ("Linear Regression", LinearRegression()),
    ("Ridge Regression", Ridge(alpha=1.0)),
    ("Lasso Regression", Lasso(alpha=0.1)),
    ("Support Vector Regressor", SVR(kernel='rbf')),
    ("KNN Regressor", KNeighborsRegressor(n_neighbors=5)),
    ("XGBoost Regressor", XGBRegressor(n_estimators=400, learning_rate=0.1, max_depth=5, random_state=42))
]

# Evaluate all models
for name, model in models:
    print(f"Training {name}...")
    if name == "Support Vector Regressor":
        evaluate(name, model, X_train_scaled, X_test_scaled, y_train, y_test, results)
    else:
        evaluate(name, model, X_train, X_test, y_train, y_test, results)

# Convert results to DataFrame
results_df = pd.DataFrame(results)
results_df.sort_values(by="R2 Score", ascending=False, inplace=True)

# Display results
print("\nModel Performance Comparison:")
print(results_df)

# Save best model
best_model_name = results_df.iloc[0]['Model']
best_model_idx = next(i for i, (name, _) in enumerate(models) if name == best_model_name)
best_model = models[best_model_idx][1]

# If best model is already trained, get it from models list
if best_model_name == "Support Vector Regressor":
    print(f"\nSaving best model ({best_model_name}) and scaler...")
    best_model.fit(X_train_scaled, y_train)  # Refit to ensure it's trained
    joblib.dump(best_model, 'data/model.pkl')
    joblib.dump(scaler, 'data/scaler.pkl')
    # Save a flag file to indicate we need to use the scaler
    with open('data/use_scaler.txt', 'w') as f:
        f.write("True")
else:
    print(f"\nSaving best model ({best_model_name})...")
    best_model.fit(X_train, y_train)  # Refit to ensure it's trained
    joblib.dump(best_model, 'data/model.pkl')
    # If previous best model was SVR but this one isn't, remove scaler flag
    if os.path.exists('data/use_scaler.txt'):
        os.remove('data/use_scaler.txt')

print(f"Best model ({best_model_name}) saved to data/model.pkl")

# Save feature columns for reference
with open('data/feature_columns.txt', 'w') as f:
    f.write(','.join(X.columns))