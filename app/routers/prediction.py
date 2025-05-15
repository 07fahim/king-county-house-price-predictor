from fastapi import APIRouter, Depends, HTTPException, Request, Form # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from app.schemas.house import HouseFeatures, PredictionResponse
from app.models.ml_model import get_model, predict_price

router = APIRouter(
    prefix="/prediction",
    tags=["prediction"],
)

templates = Jinja2Templates(directory="app/templates")

@router.post("/predict", response_model=PredictionResponse)
async def predict_house_price_api(features: HouseFeatures):
    """
    API endpoint to predict house price based on the provided features
    """
    try:
        # Get the loaded model
        model = get_model()
        
        # Make prediction
        prediction = predict_price(model, features)
        
        # Return prediction
        return PredictionResponse(
            predicted_price=prediction,
            features=features
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@router.get("/form", response_class=HTMLResponse)
async def prediction_form(request: Request):
    """
    Render the prediction form
    """
    return templates.TemplateResponse("prediction_form.html", {"request": request})

@router.post("/form", response_class=HTMLResponse)
async def handle_form(
    request: Request,
    sqft_living: float = Form(...),
    grade: float = Form(...),
    bathrooms: float = Form(...),
    bedrooms: float = Form(...),
    waterfront: int = Form(...),
    view: int = Form(...),
    sqft_basement: float = Form(...),
    yr_built: int = Form(...),
    lat: float = Form(...),
    long: float = Form(...)
):
    """
    Handle form submission and display prediction result
    """
    try:
        # Create feature object
        features = HouseFeatures(
            sqft_living=sqft_living,
            grade=grade,
            bathrooms=bathrooms,
            bedrooms=bedrooms,
            waterfront=waterfront,
            view=view,
            sqft_basement=sqft_basement,
            yr_built=yr_built,
            lat=lat,
            long=long
        )
        
        # Get the loaded model
        model = get_model()
        
        # Make prediction
        prediction = predict_price(model, features)
        
        # Format for display
        formatted_prediction = f"${prediction:,.2f}"
        
        # Return result
        return templates.TemplateResponse(
            "prediction_result.html", 
            {
                "request": request, 
                "prediction": formatted_prediction,
                "features": features
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "error.html", 
            {"request": request, "error": str(e)}
        )