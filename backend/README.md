# Jethro Backend
The backend application for Jethro - Church Service Scheduling Application

# Setup
1. [install gcloud](https://cloud.google.com/sdk/docs/install)
2. init gcloud: `gcloud init`

# Development
1. setup dependencies for project: `just install`
2. getting service account credential:
   1. visit google cloud console
   2. go to application project -> Security -> Secret Manager -> `app-engine-sa-json`
   3. action -> view secret value
   4. store the value in `src/service-account.json`
3. deploy locally: `just deploy`
4. format code: `just lint`

# Deployment
1. manual: `gcloud app deploy`
2. When pushed to master, github workflow will deploy to GAE.
