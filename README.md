# Data Engineering Zoomcamp Project

## Problem

Project goal is to develop end to end data engineering solution focused on ETL processes. This involves extracting data from diverse source, transforming it into a consistent format, and loading it into a central repository. By achieving this, I aim to facilitate efficient data management and analysis for informed decision-making process.

## Dataset
The dataset maintained by the San Francisco Controller's Office encompasses detailed records of salaries and benefits disbursed to City employees starting from fiscal year 2013. It comprises comprehensive information on compensation packages provided to employees across various departments, positions, and pay grades within the city administration.

Data can be accessed via following link [[Employee Compensation data](https://data.sfgov.org/City-Management-and-Ethics/Employee-Compensation/88g8-5mnd/about_data)]

## Architecture
![flow](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/45802d75-8757-4eb2-bc88-48a15bb77df7)

## Technologies
1. Cloud: **GCP**
2. Infrastructure as code (IaC): **Terraform**
3. Datalake: **GCP Bucket**
4. Workflow orchestration: **Mage** 
5. Data Warehouse: **BigQuery** 
6. Transformations: **Mage & Pandas**
7. Dashboard: **Looker Studio**

### Cloud: GCP
The Google Cloud Platform is used for deploying the end to end pipeline withing Google Cloud Storage (GCS) as a data lake, and BigQuery as a data warehouse.

### Infrastructure as code (IaC): Terraform
Terraform is an open source tool which has been used for provisioning infrastructure resources. In this case, it was used to create GCP resources by creating the following: https://github.com/kenanarslanbay/Employee-Compensation-Project/tree/main/01-Infrastructure 

### Workflow Orchestration: Mage
The mage orchestrates two pipelines:

The first pipeline extracts data from an API, applies cleaning and transformation steps, then writes the transformed data to Google Cloud Storage.

![first_api](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/89ac280c-2a3f-47b4-aa66-d40bb447f3ab)![trigger_1PNG]



The second pipeline retrieves data from Google Cloud Storage, applies further transformations, and then writes the processed data to BigQuery for in-depth analysis.

![API2](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/3b2aed29-8789-43b8-ae8a-42e130ed73d8)


### Looker Studio
By connecting our final data to Looker studio following dashboard has been created.
![dashboard](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/4e432f1e-2a3e-4155-97d0-2cf3ff0e206f)

You can also access interactive dashboard via following link: [dashboard](https://datastudio.google.com/s/kJWMinVHqMw)](https://lookerstudio.google.com/u/0/reporting/70c4d6ad-bd73-4df2-9f95-5a6f17477cc6/page/gw7uD )


### Reproduce the Project

 
## Prerequisities
    - docker
    - docker-compose
    - terraform
    - git
    - GCP account
    - gcloud (if not working on a GCP VM)
    - make
    
## Google Cloud Platform
For the project you will need access to a free trial of GCP or you can use your existing one via [here](https://cloud.google.com/free). 

## Service Account
In gcp go to menu on the left then choose "IAM & Admin" then select  "**Service accounts**",
Click on "Create Service Account" and create a new account with any name that you want to use
Then add the following roles: ![API](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/bfcbb30c-9b5c-4e53-9ae3-da9d53f003af)

## Service Account Key
We need the authorization key for the created service account. First, go to service account details.Then on **"KEYS"** Tab select **"Add Key"** section **"Create new key"**. Choose Json and save the file in your local.
Install the [Gcloud SDK](https://cloud.google.com/sdk/docs/install-sdk) and set your environment variable pointing to your key:
```
export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"

gcloud auth application-default login
```

## Setting up environment in VM:
Creating ssh key on your local machine to make ssh connection to your vm.
go to directory **~/.ssh** on your terminal
Run following command to create ssh key:
```
ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
```
Put public key to Google Cloud. Below the section Compute Engine go to Metadata. Select SSH tab, and add SSH key. Then enter the key found within the public key file and save.

## Create VM on compute engine section
- choose region that close to you
- create 30-40 gb standard disk
- Choose 4 cpu 16gb Memory as standart
- For operating system you may choose ubuntu 20.04

## Accessing Your VM via SSH

### Initial SSH Connection
1. Copy the External IP address of your VM.
2. Open your command line interface.
3. Enter the following command:

```bash
ssh -i ~/.ssh/gpc <yourname>@<externalip>
```

# Configuring ssh file to connect automatically whenever we exits:

- Create a file under **~/.ssh** called config. We will be using this for configuring SSH.

Host de-project
	HostName <externalip>
    User <your_user_name>
    IdentityFile ~/.ssh/gpc
	
After you saved you can connect with following or you can set this configs on vs code.
-**ssh de-project**

**Note**: When you shutdown vm and intiliaze the VM IP may change time ti time.Thus, you may need to change external ip in your configs!

# Installing Docker

To install Docker on your system, follow these steps:

1. Update package lists:
    ```bash
    sudo apt-get update
    ```

2. Install necessary dependencies:
    ```bash
    sudo apt-get install ca-certificates curl
    ```

3. Set up Docker's official GPG key:
    ```bash
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    ```

4. Install Docker packages:
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

## Reproducing the Pipeline

Follow these steps to reproduce the pipeline:

1. Clone the repository:
    ```bash
    git clone https://github.com/kenanarslanbay/Employee-Compensation-Project.git
    cd Employee-Compensation-Project/
    ```

2. Navigate to the infrastructure directory:
    ```bash
    cd $HOME/Employee-Compensation-Project/01-Infrastructure
    ```

3. Initialize Terraform:
    ```bash
    terraform init
    ```

4. Plan the changes:
    ```bash
    terraform plan
    ```

5. Apply the changes:
    ```bash
    terraform apply
    ```

**Important Note:** Remember to destroy all remote objects managed by our Terraform configuration after completing your project to avoid unnecessary charges to your GCP account:
```bash
terraform destroy

  



