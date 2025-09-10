import openai
from sentence_transformers import SentenceTransformer
import datasets, accelerate
import torch
import torch.nn.functional as F
import os
from Django_Server.config import *
from Law_Assistant.embedding.loader import get_embedding_model
from types import SimpleNamespace

class RAGService:
    def __init__(self, 
                 key_path : str, 
                 law_docs_path : str, 
                 model_path : str, 
                 vectordb_path : str, 
                 truncate_dim = 128, 
                 top_k = 3,
                 openai_model = "gpt-4o-mini",
                 device = 'cpu'):
        
        self.law_docs_path = law_docs_path
        self.truncate_dim = truncate_dim
        self.top_k = top_k
        self.device = device if torch.cuda.is_available() else "cpu"
        self.openai_model = openai_model

        self.model = get_embedding_model(self.device, self.truncate_dim)
        self.embedding_docs = torch.stack(torch.load(vectordb_path, weights_only=False), dim=0).to(self.device)

        if(self.embedding_docs.shape[-1] != truncate_dim):
            raise ValueError(f"The embedding database shape does not match the model's truncate dimension. {self.embedding_docs.shape[-1]} and {truncate_dim}")

        self.embedding_docs = self.embedding_docs.view(self.embedding_docs.shape[0], 1, truncate_dim)
       
        with open(key_path) as f:
            self.org = f.readline().strip()
            self.api_key = f.readline().strip()

        self.client = openai.OpenAI(
            organization = self.org,
            api_key = self.api_key
        )

        self.all_laws = []

        files = sorted(os.listdir(law_docs_path))
        self.law_doc_files = files
        self.all_laws = dict()

    def embed_query(self, query):
        embedding = self.model.encode(query, convert_to_numpy=False, device=self.device, normalize_embeddings=True)
        if not isinstance(embedding, torch.Tensor):
            embedding = torch.tensor(embedding, device=self.device)
        return embedding.unsqueeze(0)

    def get_top_documents(self, question, k = 3):
        embedding = self.embed_query(question)
        cosine_similarities = F.cosine_similarity(embedding.unsqueeze(0).expand(self.embedding_docs.shape[0], 1, self.truncate_dim), self.embedding_docs, dim = -1).view(-1)
        top_k = cosine_similarities.topk(k)
        top_k_indices = top_k.indices
        top_k_values = top_k.values
        if(top_k_values[0] < 0.6):
            return None
        else:
            return top_k_indices
    
    def retrieve_doc(self, index):
        if(index not in self.all_laws):
            with open(os.path.join(self.law_docs_path,self.law_doc_files[index]), 'r', encoding="utf-8") as f:
                l = f.read()
                self.all_laws[index] = l

        return self.all_laws[index]
    
    def generate_prompt(self, question, top_k_indices):
        if(top_k_indices == None):
            return question
        else:
            prompt = "Tôi cung cấp cho bạn một số văn bản pháp luật có liên quan như sau: \n\n"
            
            for k in top_k_indices:
                prompt += self.retrieve_doc(k) + "\n\n"

            prompt += f"Từ những văn bản pháp luật trên, hãy giúp tôi trả lời cụ thể cho câu hỏi sau: \n\n{question}\n\n"
            prompt += """
CHÚ Ý:
- Cần câu trả lời cụ thể đầy đủ từ những thông tin vừa cung cấp.
- Trích dẫn rõ ràng các tên luật và điều, khoản.
- Nếu các văn bản không liên quan đến văn bản hoặc không cung cấp đủ thông tin thì hãy từ chối trả lời câu hỏi, không tự trả lời theo ý kiến riêng.
- Không nhắc gì về việc được cung cấp tài liệu.      

                """
            return prompt

    def stimulate_stream(self, text):
        
        chunk = [SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content=i+" "))]) for i in text.split(" ")]
        return chunk
    
    def generate_response(self, prompt):
        stream = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": f"Bạn là người trợ lý pháp luật."}, {"role": "user", "content": f"{prompt}"}],
            stream=True,
        )

        return stream

        #return self.stimulate_stream(prompt)
        
    def send_message(self, text):
        top_k_indices = self.get_top_documents(text, self.top_k)
        prompt = self.generate_prompt(text, top_k_indices)
        response_stream = self.generate_response(prompt)
        return response_stream


