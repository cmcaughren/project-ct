#terraform set up of providers, set up of storage bucket

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
    
    google-beta = {
      source = "hashicorp/google-beta"
      version = "4.68.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

provider "google-beta" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

data "google_storage_bucket" "storage_bucket" {
  name          = local.storage_bucket
}

#for first terraform provision run: comment this out
#run "terraform init -backend-config=config.gcs.tfbackend
#in this file provide the storage bucket name and the prefix
#run "terraform apply". terraform will provision the bucket.
#Once provisioned, uncomment and run "terraform apply" again,
#so terraform will move the statefiles into the bucket.
#See operations/README
terraform {
 backend "gcs" {
 }
}
