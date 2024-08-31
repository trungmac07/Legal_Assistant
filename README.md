# Law Assistant Using RAG and LLM

## Overview
This project provides a Django-based backend that integrates Retrieval-Augmented Generation (RAG) with a Language Model (LLM) for answering legal questions. It uses precomputed embeddings of legal documents stored in a PyTorch tensor and OpenAI's GPT-4 API to generate contextually relevant responses based on the user's queries.

## Features

**Embedding Similarity:** Use my custom embedding model to compute embeddings for legal questions and documents, then determine the similarity between them to retrieve the most relevant documents for RAG. For more information about my embedding model, please visit my repository [here](https://github.com/trungmac07/VN_Law_Embedding)

**Legal Question Answering:** Leverages RAG to retrieve relevant legal documents and generate responses using GPT-4.

**Django Backend:** Provides RESTFUL API for sending questions and receiving responses by clients.

**Streaming Responses:** Streams answers from the LLM to provide real-time feedback.

**Efficient Document Management:** Manages and retrieves document embeddings (vector database) with PyTorch.

## Prerequisites

Python 3.8 or higher

Django 4.x

PyTorch

OpenAI API Key

## Install

### Clone the Repository
```sh
git clone https://github.com/trungmac07/Law_Assistant
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Data and Set Up
Download the data directory from [here.](https://drive.google.com/drive/folders/1Th0Cy7XbfjKMbIjmA5R-qII4IZLugJnb?usp=sharing)

Extract the `preprocessed_laws.zip` and `embedding_model` inside - These are legal documents and a pre-trained embedding model.

Open the file .key and paste your OpenAI organization (first line) and API key (second line).

Then paste `data` directory into the `Law_Assistant/Django_Server/`.


### Apply Migrations

```sh
python manage.py migrate
```

### Run Server
```sh
python manage.py runserver
```

## Usage

### API Endpoints

POST /chat/
Submit a legal question to the backend, which retrieves relevant documents and returns a streamed response from the LLM.

### Request Body:
```sh
{
  "question": "Các hành vi nào phải chịu trách nhiệm hình sự?"
}
```

### Response:

The response is streamed back as plain text. The content is generated based on the top retrieved legal documents.

