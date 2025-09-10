import torch 

a = torch.load("/home/trungmac/code/projects/Law_Assistant/Django_Server/data/vectordb_128.pt", weights_only=False)

a = [ i.to('cpu') for i in a]

torch.save(a,"/home/trungmac/code/projects/Law_Assistant/Django_Server/data/new_vectordb_128.pt")
