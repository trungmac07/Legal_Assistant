

##### APP CONFIG #####
KEY_PATH = "./data/.key"
LAW_DOCS_PATH = "./data/preprocessed_laws"
TOP_K = 3
# For online model we keep truncate dim for existing vectordb compatibility
TRUNCATE_DIM = 768
MODEL_PATH = "truro7/vn-law-embedding"
VECTORDB_PATH = "./data/vectordb_128.pt"
OPENAI_MODEL = "gpt-4o-mini"
DEVICE = "cuda"  # cuda or cpu