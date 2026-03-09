import os 
from abc import ABC, abstractmethod
from typing import List , Dict , Tuple
from pathlib import path
from langchain.text_splitter import RecursiveCharacterTextSplitter

processors_lits={
    
}

class Docs_processor(ABC):

    def __init__(self,docs_path,chunking_size=800,chunking_overlap=100):
        
        self.docs_path=docs_path
        self.chunking_size=chunking_size
        self.chunking_overlap=chunking_overlap

        #splitter using langchain splitter 

        self.splitter=RecursiveCharachterTextSplitter(
            chunking_size=self.chunking_size
            chunking_overlap=self.chunking_overlap
            separators=["\n\n", "\n", ".", " ", ""]
        )
        
    def load_docs(self)->Tuple[List[str],List[Dict]]:
        docs=[]
        meta_data=[]

        for file_path in path(self.docs_path).glob("*.txt"):
            with open(file_path,"r", encoding="utf-8") as f :
                 content=f.read()

        docs.append(content)
        meta_data.append(
            "source":file_path.name,
            "path":str(file_path)
        ) 

        return docs, meta_data

    def process_docs(self , docs:list[str] , meta_data:list[dict])-> Tuple[List[str],List[Dict]]:

        processed_docs=[]
        procesed_meta=[]

        for doc,meta in zip (docs,meta_data):
            clean_doc=doc.strip()

            if clean_doc :
               processed_doc.append(clean_doc) 
               processed_meta.appen(meta)

        return processed_doc, processed_meta

    def chunk_docs(self , docs:list[str] , meta_data:list[dict])->Tuple[List[str],List[Dict]]:
        
        chunked_docs=[]
        chunked_meta=[]

        for doc , meta in zip(docs,meta_data):
            splits=self.splitter.split_text(doc)

            for idx,chunk in enumerate(splits):
                chunked_docs.append(chunk)

                chnked_meta=meta.copy()
                chunked_meta["chunk_index"]= idx
                chunked_meta.append(chunked_meta)

        return chunked_docs, chunked_meta

    def run_processor(self , processor_type:str):
        doc_processor=processors_lits.get(processor_type)
        if doc_processor:
            return doc_processor()
        else:
            raise ValueError("processor type not found")