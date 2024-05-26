PROJECT_ID="${PROJECT_ID:-$(gcloud config get-value project)}"

gcloud builds submit --tag us-docker.pkg.dev/$PROJECT_ID/cooking-images/recipe-web-app:latest .

gcloud run deploy recipe-web-app --image=us-docker.pkg.dev/$PROJECT_ID/cooking-images/recipe-web-app:latest --region=us-central1 --port=8501