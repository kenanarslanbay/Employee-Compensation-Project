# Data Engineering Zoomcamp Project

## Problem Statement

Project goal is to develop end to end data engineering solution. This involves extracting data from data source, transforming it into a consistent format, and loading it into a central repository. By achieving this, I aim to facilitate efficient data management and analysis for informed decision-making process.

## Dataset
The [data](https://data.sfgov.org/City-Management-and-Ethics/Employee-Compensation/88g8-5mnd/about_data) maintained by the San Francisco Controller's Office encompasses detailed records of salaries and benefits disbursed to City employees starting from fiscal year 2013. It comprises comprehensive information on compensation packages provided to employees across various departments, positions, and pay grades within the city administration.

## Architecture
![flow](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/45802d75-8757-4eb2-bc88-48a15bb77df7)

## Technologies Used

1. **Cloud Platform:** Google Cloud Platform (GCP)
2. **Infrastructure as Code (IaC):** Terraform
3. **Data Lake:** Google Cloud Storage (GCS)
4. **Workflow Orchestration:** Mage
5. **Data Warehouse:** BigQuery
6. **Data Transformation:** Mage & Pandas
7. **Dashboard:** Looker Studio

### Cloud: GCP
Google Cloud Platform is utilized for deploying the end-to-end pipeline with Google Cloud Storage (GCS) as a data lake and BigQuery as a data warehouse.

### Infrastructure as code (IaC): Terraform
Terraform is an open-source tool used for provisioning infrastructure resources. It was employed to create GCP resources by defining infrastructure as code [here](https://github.com/kenanarslanbay/Employee-Compensation-Project/tree/main/01-Infrastructure).

### Workflow Orchestration: Mage

Mage used to orchestrate the following pipelines:

1. The first pipeline extracts data from an API, applies cleaning and transformation steps, then writes the transformed data to Google Cloud Storage.

   ![API Pipeline](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/89ac280c-2a3f-47b4-aa66-d40bb447f3ab)

2. The second pipeline retrieves data from Google Cloud Storage, applies further transformations, and then writes the processed data to BigQuery for in-depth analysis.

   ![BigQuery Pipeline](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/3b2aed29-8789-43b8-ae8a-42e130ed73d8)


### Looker Studio

A dashboard has been created by connecting the final data to Looker Studio.

![looker_dashboard](https://github.com/kenanarslanbay/Employee-Compensation-Project/assets/66200735/b6b37262-0336-4c3c-99ca-8fae71aa4ea8)

An interactive version of the dashboard is available [here](https://lookerstudio.google.com/u/0/reporting/70c4d6ad-bd73-4df2-9f95-5a6f17477cc6/page/gw7uD).


## Reproduce the Project

 
### Prerequisities
    - docker
    - docker-compose
    - terraform
    - git
    - GCP account
    - gcloud (if not working on a GCP VM)
    - make
    
### Google Cloud Platform
Access to a free trial of GCP or an existing account is required. [Click here](https://cloud.google.com/free) to sign up for the free trial.

### Service Account

1. Go to the "IAM & Admin" section in the GCP console.
2. Select "Service accounts" and click on "Create Service Account".
3. Assign the following roles:
   - Viewer
   - Artifact Registry Reader
   - Artifact Registry Writer
   - BigQuery Admin
   - Cloud SQL Admin
   - Service Account Admin
   - Storage Admin
   - Storage Object Admin
 
### Service Account Key

To access the authorization key for the created service account, follow these steps:

1. Navigate to the service account details.
2. In the "KEYS" tab, select the "Add Key" section.
3. Choose the JSON format and create a new key.
4. Save the JSON file.

Later on, we will save this file in our home folder `$HOME/.google/` on the VM.

### Setting up Environment in VM

### Create VM on Compute Engine

Follow these steps to create a VM instance on Google Compute Engine:

- Choose a region that close to you.
- Create a standard disk with a size of 30-40 GB.
- Choose 4 CPUs and 16 GB memory as standard.
- For the operating system we will proceed with any linux distribution. For example, you may choose Ubuntu 20.04.

### Setting up Environment in VM

To set up your environment in the VM:

1. Create an SSH key on your local machine to make an SSH connection to your VM.
   - Navigate to the directory `~/.ssh` on your terminal.
   - Run the following command to create an SSH key:
     ```bash
     ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
     ```
2. Put the public key to Google Cloud. Under Compute Engine, go to Metadata, select the SSH tab, and add the SSH key. Then, enter the key found within the public key file and save.

### Accessing Your VM via SSH

### Initial SSH Connection

To access your VM via SSH for the first time:

1. Copy the External IP address of your VM.
2. Open your command-line interface.
3. Enter the following command:

   ```bash
   ssh -i ~/.ssh/gcp <yourname>@<externalip>

### Configuring ssh file to connect automatically whenever we exits:
Create a file under **~/.ssh** called config. We will be using this for configuring SSH connection.
```
Host de-project
    HostName <your_external_ip>
    User username
    IdentityFile ~/.ssh/<de-project>
```
	
After you saved you can connect with following or you can set this configs on vs code.
**ssh de-project**

**Note**: When you shutdown vm and intiliaze the VM IP may change time ti time.Thus, you may need to change external ip in your configs!

### Installing Docker

To install Docker on your system, follow [here](https://docs.docker.com/engine/install/ubuntu/)

### Running docker without sudo:
```
sudo groupadd docker
sudo usermod -aG docker $USER
sudo service docker restart
```

## Reproducing the Pipeline

Follow these steps to reproduce the pipeline:

1. Clone the repository:
    ```bash
    git clone https://github.com/kenanarslanbay/Employee-Compensation-Project.git
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
    terraform plan -var="project=<your-gcp-project-id>"
    ```

5. Apply the changes:
    ```bash
    terraform apply -var="project=<your-gcp-project-id>"
    ```

**Important:** Remember to destroy all remote objects managed by our Terraform configuration after completing your project to avoid unnecessary charges to your GCP account:
```
terraform destroy
```

### Configuring GCP with Mage

To upload your data (or GCS Bucket) using Mage, you first need to configure it to authenticate with GCP. Follow these steps:

1. Navigate to your `io_config.yaml` file.

2. Update the section under Google to include your service account credentials:

    ```yaml
    GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/{creds}.json"
    GOOGLE_LOCATION: EU # Optional
    ```

    Replace `{your_credentials}.json` with the filepath of your service account credentials JSON file. Optionally, specify the desired location in `GOOGLE_LOCATION`.

3. When you are running mage make you sure you have your creds.json in your mage directory.

4. Run the make file in make directory to run everything then you can observe runs of pipeline via mage ui.


### Extra

Setting Up Git Pre-commit Hooks

1. Creating a hook for the repo run **pre-commit install** in your shell

2. Run **git add .pre-commit-config.yaml**

3. Run a **git commit git commit -m "testing"**


  



