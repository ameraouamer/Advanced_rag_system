Advanced RAG System with Query Decomposition & Cross-Encoder Reranking

📌 Overview

This project implements an advanced Retrieval-Augmented Generation (RAG) system designed to improve information retrieval from large document collections.

Unlike basic RAG pipelines that rely solely on vector similarity, this system introduces:

Query decomposition (multi-query retrieval)
Document chunking with metadata tracking
Cross-encoder reranking for precision

The result is a more accurate and robust retrieval pipeline, especially for complex and multi-intent queries.

Key Components :

1. Query Processing Agent
Built using LangChain
Decomposes complex queries into structured sub-queries
Improves retrieval recall

3. Document Processor
Loads raw documents from disk
Cleans and normalizes text
Splits documents into chunks using recursive chunking
Preserves metadata for 

4. Vector Store
Powered by ChromaDB
Stores document embeddings
Performs fast similarity search to retrieve top M candidates

6. Cross-Encoder Reranker
Scores (query, document) pairs jointly
Improves precision over standard embedding-based retrieval
Filters out semantically similar but irrelevant documents

Clone the repo : 

git clone https://github.com/your-username/advanced-rag-system.git
cd advanced-rag-system
