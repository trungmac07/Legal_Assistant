from sentence_transformers import SentenceTransformer
import torch

_model_instance = None

def get_embedding_model(device: str = 'cpu', truncate_dim: int = 128) -> SentenceTransformer:
    global _model_instance
    if _model_instance is None:
        _model_instance = SentenceTransformer("truro7/vn-law-embedding", device=device, truncate_dim=truncate_dim)
    return _model_instance

def encode_texts(texts, device: str = 'cpu', truncate_dim:int = 128):
    model = get_embedding_model(device, truncate_dim=truncate_dim)
    embeddings = model.encode(texts, convert_to_numpy=False, device=device, normalize_embeddings=True, truncate_dim=truncate_dim)
    if isinstance(embeddings, torch.Tensor):
        return embeddings
    return torch.tensor(embeddings, device=device)


