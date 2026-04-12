from .BaseController import BaseController
from .ProjectControllers import ProjectController
import os
from langchain_community.document_loaders import TextLoader,PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from models import ProcessingEnum
class ProcessController(BaseController):
    def __init__(self,project_id:str):
        super().__init__()
        self.project_id=project_id
        self.project_path=ProjectController().get_project_path(project_id=project_id)
    def get_file_extension(self,file_id:str):
         return os.path.splitext(file_id)[-1]
    
    def get_file_loader(self,file_id:str):
        file_extension=self.get_file_extension(file_id=file_id)
        file_path=os.path.join(self.project_path,file_id)
        if file_extension ==ProcessingEnum.TXT.value:
            return TextLoader(file_path,encoding="utf-8")
        elif file_extension ==ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        else:
           return None
    
    def get_file_content(self,file_id:str):
        loader=self.get_file_loader(file_id=file_id)
        if loader is None:
            return None
        documents=loader.load()
        return documents
    
    def process_file_content(self,file_content:list,file_id:str,chunck_size:int=100,overlap_size:int=20):
        text_splitter=RecursiveCharacterTextSplitter( chunk_size=chunck_size,chunk_overlap=overlap_size,
            length_function=len
            )
        file_content_texts=[doc.page_content for doc in file_content]
        file_content_metadata=[doc.metadata for doc in file_content]
        documents = []
        for text, meta in zip(file_content_texts, file_content_metadata):
            doc = Document(
                page_content=str(text),   # تأكدي إنه string
                metadata=dict(meta)       # تأكدي إنه dict
            )
            documents.append(doc)

        chunks = text_splitter.split_documents(documents)  
        return chunks
    

