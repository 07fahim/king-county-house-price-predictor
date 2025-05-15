# Deployment Guide: King County House Price Predictor

## GitHub Repository Setup
1. Create a new GitHub repository
2. Initialize with your project files
3. Add the following configuration files:
   - `Dockerfile`
   - `.github/workflows/ci-cd.yml`
   - `render.yaml`

## GitHub Actions Setup
1. Go to your GitHub repository settings
2. Navigate to "Secrets and variables" → "Actions"
3. Add the following secret:
   - `RENDER_DEPLOY_HOOK`: The Render deploy hook URL (you'll get this from Render)

## Docker Hub Setup (Optional)
If you want to push Docker images to Docker Hub, create an account and repository. This is optional if you deploy directly via Render's Dockerfile.

## Render Deployment Setup
1. Create a Render account: https://render.com/
2. Link your GitHub account in Render
3. Create a new Web Service:
   - Choose "Deploy from GitHub"
   - Select your repository
   - Choose "Docker" as the environment
   - Configure the service:
     - Name: `king-county-house-predictor`
     - Environment Variables: Add `PORT=8000`
     - Create a deploy webhook and copy the URL
4. Save the deploy webhook URL as `RENDER_DEPLOY_HOOK` in your GitHub repo secrets

## Continuous Deployment Workflow
The workflow file `.github/workflows/ci-cd.yml` will:
- Run automatically on every push to the main branch
- Checkout your code
- Trigger the Render deploy webhook
- This will cause Render to redeploy your app automatically with the latest changes

### Example GitHub Actions Workflow (`.github/workflows/ci-cd.yml`):
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Trigger Render Deploy Hook
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

## Testing the Deployment
1. Make a change to your repository
2. Push the change to the `main` branch
3. GitHub Actions will run the CI/CD pipeline
4. Render will redeploy the updated app automatically
5. Check your Render dashboard for deployment status and logs
6. Access your app at the Render URL provided

## Monitoring and Logs
* Check GitHub Actions for CI/CD logs
* Use Render dashboard for app logs, metrics, and alerts

## Scaling
Render lets you scale easily:
* Change instance count or type from the Render dashboard