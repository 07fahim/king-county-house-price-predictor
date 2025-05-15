#!/bin/bash

# Create project root directory
mkdir -p king_county_house_price_predictor
cd king_county_house_price_predictor

# Create directory structure
mkdir -p app/models app/routers app/schemas app/templates app/static/css app/static/images app/static/js data

# Create empty Python package files
touch app/__init__.py
touch app/models/__init__.py
touch app/routers/__init__.py
touch app/schemas/__init__.py

# Create empty placeholder files
touch app/main.py
touch app/models/ml_model.py
touch app/routers/prediction.py
touch app/schemas/house.py
touch app/templates/index.html
touch app/templates/prediction_form.html
touch app/templates/prediction_result.html
touch app/templates/error.html
touch app/static/css/styles.css
touch app/static/images/house.svg
touch model_evaluation.py
touch test_api.py
touch requirements.txt
touch README.md

echo "Project structure created successfully!"