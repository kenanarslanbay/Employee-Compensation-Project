# Data Engineering Zoomcamp Project

## Problem

Project goal is to develop end to end data engineering solution focused on ETL processes. This involves extracting data from diverse source, transforming it into a consistent format, and loading it into a central repository. By achieving this, I aim to facilitate efficient data management and analysis for informed decision-making process.


## Dataset
The dataset maintained by the San Francisco Controller's Office encompasses detailed records of salaries and benefits disbursed to City employees starting from fiscal year 2013. It comprises comprehensive information on compensation packages provided to employees across various departments, positions, and pay grades within the city administration.

Data can be accessed via following link [[Employee Compensation data](https://data.sfgov.org/City-Management-and-Ethics/Employee-Compensation/88g8-5mnd/about_data)]

## Data Pipeline
[flow](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/5862226d-2eda-4511-8e63-68b8564d98ec)


## Technologies
1. Cloud: **GCP**
2. Infrastructure as code (IaC): **Terraform**
3. Datalake: **GCP Bucket**
4. Workflow orchestration: **Mage** 
5. Data Warehouse: **BigQuery** 
6. Transformations: **Pandas**
7. Dashboard: **Looker Studio****

### Cloud: GCP
The Google Cloud Platform is used for deploying the end to end pipeline withing Google Cloud Storage (GCS) as a data lake, and BigQuery as a data warehouse.

### Infrastructure as code (IaC): Terraform
Terraform is an open source tool which has been used for provisioning infrastructure resources. In this case, it was used to create GCP resources by creating the following [Terraform files](./terraform).

### Workflow orchestration: Mage
Mage is an open source orchestration tool that provides data extraction, integration and transformation by building real-time and batch pipelines.
![mageaads](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/8742c356-5877-45c5-be25-572b8d0c0474)



### Dashboard
The [dashboard](https://datastudio.google.com/s/kJWMinVHqMw)](https://lookerstudio.google.com/u/0/reporting/70c4d6ad-bd73-4df2-9f95-5a6f17477cc6/page/gw7uD ) was built on Google Data Studio. 
<img src="images/dashboard.png">

### Prerequisities

    - docker
    - docker-compose
    - terraform
    - git
    - GCP account
    - gcloud (if not working on a GCP VM)

### Reproduce the Project
The steps to reproduce this pipeline is as follows:
1. Clone the repo
    ```
        git clone https://github.com/kenanarslanbay/Employee-Compensation-Project.git

        cd Employee-Compensation-Project/
    ```
2. Setup Terraform for IaC [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp)<br>
Then run the scripts in the following order [here](./terraform/README.md)


