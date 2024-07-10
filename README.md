# Serverless Movies API on Azure

## Introduction
This project provides a serverless API for retrieving movie information using Azure services.

## Architecture
- Azure Functions
- Azure Cosmos DB
- Azure Blob Storage
- Azure API Management

## Setup
1. Configure Azure CLI and login.
2. Create a resource group.
3. Create a Cosmos DB account and a database.
4. Create a storage account and a blob container.
5. Load movie data into Cosmos DB.
6. Create and deploy Azure Functions.
7. Set up API Management service.

## Endpoints
- `/movies`: Get a list of all movies.
- `/movies/year?year={year}`: Get movies by year.
- `/movie/summary?movie_id={id}`: Get a summary of a movie.

## Deployment
Deploy the API using Azure CLI or Azure Portal.

## Testing
Test the API endpoints using Postman or any other API testing tool.
