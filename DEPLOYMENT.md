# Cloud Run Deployment Guide

## Prerequisites

1. **Google Cloud Account** with billing enabled
2. **gcloud CLI** installed ([Download](https://cloud.google.com/sdk/docs/install))
3. **GitHub repository** (already done ✅)

## Quick Deployment Steps

### 1. Login to Google Cloud

```bash
gcloud auth login
```

### 2. Set Your Project

```bash
# Create new project (if needed)
gcloud projects create cldrun-first-project --name="CLDRUN First"

# Set the project
gcloud config set project cldrun-first-project
```

### 3. Enable Required APIs

```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### 4. Deploy to Cloud Run (Using Buildpacks - No Dockerfile!)

```bash
gcloud run deploy cldrun-first \
  --source . \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars DEBUG=False
```

**That's it!** 🚀 Buildpacks will automatically:
- Detect it's a Python/Django app
- Install dependencies from requirements.txt
- Use Procfile to start the app
- Build and deploy everything

### 5. Get Your Service URL

After deployment, you'll get a URL like:
```
https://cldrun-first-xxxxxxxx-el.a.run.app
```

## Continuous Deployment from GitHub (Optional)

### Connect GitHub to Cloud Run

1. Go to [Cloud Run Console](https://console.cloud.google.com/run)
2. Click "Create Service"
3. Select "Continuously deploy from a repository"
4. Connect your GitHub account
5. Select repository: `DipanshuMetricVibes/cldrun-first`
6. Select branch: `main`
7. Build configuration:
   - **Build type**: Buildpacks (No Dockerfile required!)
   - Region: `asia-south1`
8. Configure:
   - Allow unauthenticated invocations
   - Add environment variable: `DEBUG=False`
9. Click "Deploy"

Now every push to `main` branch will auto-deploy! 🎉

## Environment Variables (Production)

For production, you can set these via Cloud Run:

```bash
gcloud run services update cldrun-first \
  --region asia-south1 \
  --set-env-vars DEBUG=False \
  --set-env-vars SECRET_KEY=your-production-secret-key-here
```

## Verify Deployment

Visit your Cloud Run URL and check:
- ✅ Home page: `/`
- ✅ About page: `/about/`
- ✅ Contact page: `/contact/`

## View Logs

```bash
gcloud run logs read cldrun-first --region asia-south1
```

## Update Deployment

Just run the deploy command again or push to GitHub (if continuous deployment is set up):

```bash
git add .
git commit -m "update"
git push origin main
```

## Troubleshooting

### Static files not loading?
- Check that WhiteNoise is in requirements.txt ✅
- Verify STATIC_ROOT is set in settings.py ✅
- Run `python manage.py collectstatic` before deploying ✅

### Permission denied?
```bash
gcloud auth login
gcloud config set project cldrun-first-project
```

### Want to change region?
Available regions: `asia-south1` (Mumbai), `asia-southeast1` (Singapore), `us-central1` (Iowa)

## Cost Estimate

Cloud Run free tier includes:
- 2 million requests/month
- 360,000 GB-seconds/month
- 180,000 vCPU-seconds/month

Your small Django app will likely stay within free tier! 💰

## Next Steps

1. Set up custom domain
2. Enable Cloud SQL for production database
3. Set up Cloud Storage for media files
4. Configure error monitoring with Cloud Logging
