[![CI/CD](https://github.com/nogibjj/xushanqing_project4/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/nogibjj/xushanqing_project4/actions/workflows/docker-image.yml)


## xushanqing_project4
Continuous Delivery of Flask/FastAPI Data Engineering API on AWS

## To Do
* Create a Microservice that returns a JSON payload and performs a Data Engineering related task in FastAPI
* Push source code to Github
* Configure Build System to Deploy changes
* Use IaC (Infrastructure as Code) to deploy code
* Configure Build Server to Deploy Changes on build (Continuous Delivery: Use AWS ECR, AWS App Runner to deploy the service)
* Push tested source code to Github and perform Continuous Integration with Github Actions (or similar SaaS Build service)

## Details
I create a mircroservice in FastAPI, which could help us decide what to eat in Duke. I use Docker and deployed it on GCP.

## How to use
Add parameters after the link: 
category include:  category: burger, snack,chicken,sandwich,pizza,global
* well-come page list all category that could search: welcome to the top 50 fast food in US dataset, lets's begin to using sql to query fast food chain company in US. (https://bepmpbmtbd.us-east-1.awsapprunner.com/)
https://bepmpbmtbd.us-east-1.awsapprunner.com/{category}
* select top 3 sellers in this category (burger). (https://bepmpbmtbd.us-east-1.awsapprunner.com/burger)
