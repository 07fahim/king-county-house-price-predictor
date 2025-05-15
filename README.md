## Deployment

For detailed deployment instructions, see the [Deployment Guide](deployment-guide.md).

### Quick Deployment Options

#### Docker
```bash
docker build -t king-county-house-predictor .
docker run -p 8000:8000 king-county-house-predictor
```

#### Render
This project includes a `render.yaml` file for easy deployment to Render.com.

#### GitHub Actions
Automated CI/CD pipeline is configured via GitHub Actions workflow file.# King County House Price Predictor

A machine learning web application that predicts house prices in King County, Washington based on property features. Built with FastAPI, scikit-learn, and XGBoost.

## Features

- **ML-Powered Price Prediction**: Uses a trained machine learning model to estimate house prices based on property characteristics
- **User-Friendly Web Interface**: Simple form for entering property details
- **RESTful API**: Programmatic access via JSON endpoints
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: HTML, CSS, Jinja2 templates
- **Machine Learning**: scikit-learn, XGBoost
- **Data Processing**: pandas, NumPy

## Installation

### Prerequisites

- Python 3.8+
- pip
- Docker (optional for containerized deployment)

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/king_county_house_price_predictor.git
   cd king_county_house_price_predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the application at http://127.0.0.1:8000

### Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t king-county-house-predictor .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 king-county-house-predictor
   ```

3. Access the application at http://localhost:8000

## Usage

### Web Interface

1. Navigate to http://127.0.0.1:8000
2. Click on "Start Prediction"
3. Fill in the property details
4. Submit the form to get the predicted house price

### API

#### Predict House Price

**Endpoint**: `POST /prediction/predict`

**Request Body**:
```json
{
  "sqft_living": 2000,
  "grade": 8,
  "bathrooms": 2.5,
  "bedrooms": 3,
  "waterfront": 0,
  "view": 0,
  "sqft_basement": 0,
  "yr_built": 1990,
  "lat": 47.6062,
  "long": -122.3321
}
```

**Response**:
```json
{
  "predicted_price": 525000.0,
  "features": {
    "sqft_living": 2000,
    "grade": 8,
    "bathrooms": 2.5,
    "bedrooms": 3,
    "waterfront": 0,
    "view": 0,
    "sqft_basement": 0,
    "yr_built": 1990,
    "lat": 47.6062,
    "long": -122.3321
  }
}
```

## Model Information

The prediction model was trained on King County housing data from May 2014 to May 2015, covering 21,613 house sales.

### Features Used
- Square footage of living space
- Overall grade of the house
- Number of bathrooms
- Number of bedrooms
- Waterfront status
- View quality
- Square footage of basement
- Year built
- Latitude & longitude coordinates

### Model Selection
Multiple regression models were evaluated, including:
- Random Forest
- Gradient Boosting
- XGBoost
- Linear Regression
- Ridge & Lasso Regression
- Support Vector Regression
- K-Nearest Neighbors

The best performing model is automatically selected and saved based on R2 score.

## Development

### Project Structure
```
king_county_house_price_predictor/
├── app/
│   ├── __init__.py
│   ├── main.py                      # FastAPI application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── ml_model.py              # Model loading and prediction logic
│   ├── routers/
│   │   ├── __init__.py
│   │   └── prediction.py            # API endpoints and form handling
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── house.py                 # Pydantic schemas for validation
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css           # Application styling
│   │   ├── images/
│   │   │   └── house.svg            # Image assets
│   │   └── js/                      # Optional JavaScript files
│   └── templates/
│       ├── error.html               # Error page
│       ├── index.html               # Home page
│       ├── prediction_form.html     # Input form
│       └── prediction_result.html   # Results page
├── data/
│   ├── feature_columns.txt          # List of model features
│   ├── model.pkl                    # Trained model file
│   ├── scaler.pkl                   # Scaler for SVR (if needed)
│   └── use_scaler.txt               # Flag file for scaler usage
├── .github/
│   └── workflows/
│       └── ci-cd.yml                # GitHub Actions workflow
├── Dockerfile                       # Docker container configuration
├── .dockerignore                    # Files to exclude from Docker builds
├── .gitignore                       # Git ignore patterns
├── render.yaml                      # Render deployment configuration
├── model_evaluation.py              # Script to evaluate and save best model
├── requirements.txt                 # Dependencies
├── test_api.py                      # Script to test API
├── deployment-guide.md              # Detailed deployment instructions
└── README.md                        # Project documentation
```

### Training a New Model
To evaluate and train a new model:

1. Ensure the dataset is available
2. Run the model evaluation script:
   ```bash
   python model_evaluation.py
   ```
3. The best model will be automatically saved to `data/model.pkl`

### Testing the API
To test the API independently:

```bash
python test_api.py
```

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributors

- Your Name - Gazi Mohammad Fahim Faiyaz
  

## Acknowledgments

- King County for providing the housing dataset
- FastAPI for the excellent web framework
- scikit-learn and XGBoost for machine learning tools
