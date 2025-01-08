# apigateway-lambda-integration
API Gateway - Lambda Proxy vs Non-Proxy integration

## Table of Contents
1. [About](#about)
2. [Getting Started](#getting-started)
3. [Contact](#contact)

## About
This project intends to explain about AWS API Gateway Lambda integration types Proxy and Non-Proxy
This repository contains the reference material for the below tutorial video: 
 - [AWS API Gateway – Lambda Proxy vs Non-Proxy Integration with Python]
 - https://youtu.be/HrszWYar65M
   
## Getting Started
### Prerequisites
### 1.0
- AWS Account
  - Free tier account
- IAM User & Permissions
   - Assign required privileges to IAM user
   - 
### Lambda Integration
### Proxy Integration
- python code 
  - apigateway-lambda-proxy.py
- JSON data
  - apigateway-lambda-proxy.json

### Non-Proxy Integration    
- python code 
  - apigateway-lambda-nonproxy.py
- JSON data
  - apigateway-lambda-nonproxy.json

### Steps
### 1.0
- Create Lambda Function
  - From AWS console create a lambda function using python language
  - Copy the Python Program from below files based on integration types:
    - apigateway-lambda-proxy.py
    - apigateway-lambda-nonproxy.py
   - Please watch the video from below link for detailed explanation on Lambda:
     - https://youtu.be/La8uu9CHRIA 
 #### 2.1 
 - Create API
   - Create REST API in AWS Console
   - Create Method  Type “POST”
 ### 2.2
 - Test AWS API in Postman
   - For proxy integration pass the below JSON data:
     - apigateway-lambda-proxy.json  
  - For non-proxy integration pass the below JSON data:        
    - apigateway-lambda-nonproxy.json
    
## Contact
- Name: Arockiadoss Jesudoss
- GitHub: https://github.com/noelaanzi
- Linkedin: www.linkedin.com/in/arockiadoss-4756a4145
- YouTube: https://www.youtube.com/@IT-SkilL-MasteR
- Facebook: https://www.facebook.com/Arockiadoss.sna/
- Instagram : https://www.instagram.com/arockiadoss_sna/?hl=en
