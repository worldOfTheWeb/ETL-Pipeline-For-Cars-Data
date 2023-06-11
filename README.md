
# ETL Pipeline For Cars Data

## Overview

The goal of this project is to build an ETL (Extract, Transform, Load) pipeline for processing and analyzing cars info data. The project involves loading data using API or from files, transforming the data using Python and Pandas, and then loading the transformed data into a new database or generating reports.




## Installation

Install Python3 via Ubuntu terminal

First, check if Python3 is already installed or not.
```bash
$ python3
```
The output displays that “python” is not installed in the system.

Now, follow bellow steps to install Python3 and Pandas.

#### Step 1: To update apt package

 ```bash
$ sudo apt update
```   

#### Step 2: Add deadsnakes PPA

 ```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
```   

#### Step 3: In this step, install python3

 ```bash
$ sudo apt install python3.10
```   

#### Step 4: Verify Python Installation

 ```bash
$ python3 -V
```   
The output will be:

 ```bash
--> Python 3.10.4
``` 
#### Step 5: Now, once python3 is installed. Install Pandas

Install  python-pip

 ```bash
$ sudo apt-get install python-pip
``` 
#### Step 6: Install Numpy

 ```bash
$ sudo pip install numpy
``` 
#### Step 7: Install Pandas

 ```bash
$ sudo pip install pandas
``` 
#### Now, both Python3 and Pandas are installed in the system.
## Project Goals

#### 1. Data Ingestion :

Connect to a database using SQL (e.g., MySQL, PostgreSQL. Write pandas queries to load data via API or from files.

#### 2. Transforming Data :

Use Python and Pandas to perform data cleaning and transformation tasks. 
Some possible transformations include:

--> Data cleaning: Handle missing values, remove duplicates, etc.

--> Data formatting: Convert data types (e.g., datetime format), standardize values, etc.

--> Feature engineering: Create new features based on existing data, such as data load_date or data update_data in case of updating data.

#### 3. Loading Data :

Schedule the ETL pipeline to run automatically at regular intervals (e.g., daily, weekly) using a task scheduling tool like cron job.

Implement data validation checks to ensure the quality and integrity of the extracted and transformed data by generating the logs everytime the pipeline triggers.
## Tech Stack

**Language:** Python

**Framework or Library:** Pandas

**Database:** MySQL

**Complier:** Visual Studio Code

## Dataset Used

This Kaggle dataset contains statistics (CSV files) on cars info over the course of many months. There are up to 400 cars parts information for many locations. The data for each region is in its own file.

