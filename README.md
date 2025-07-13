# Mini-RAG

A Minimal Application using Rag for Question Answering

# Requirements

- python 3.8 or later

### Install python using miniconda

1) Download and install miniconda
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag-app python=3.8
```
3) Activate the environment:
```bash
$ conda activate mini-rag-app
```
### (optional) Setup your command line interface for better readability
```bash
export psl="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
4) Installation
```bash
$ pip install -r requirements.txt
```
### Setup the environment variables
```bash
$ cp .env.example .env
```
## Run the FastAPI Server
```bash
$ uvicorn main:app --reload --hosat 0.0.0.0
```
## Postman Collection
Download the postman collection from [/Assets/mini-rag-app.postman_collection.json]

