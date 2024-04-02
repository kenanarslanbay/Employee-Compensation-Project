variable "project" {
  description = "Project"
  default     = "snappy-catcher-418306"

}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "europe-west3"
  type        = string
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "de-project-data-lake"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

# variable "BQ_DATASET" {
#   description = "BigQuery Dataset the data (from GCS) will be written to"
#   type        = string
#   default     = "employee_data"
# }

## Creating table by mage pipeline