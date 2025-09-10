from django.apps import AppConfig
from .services import RAGService
from Django_Server.config import *
from pathlib import Path
import sys
class LawAssistantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Law_Assistant'

    def ready(self):
        if any(cmd in sys.argv for cmd in ['migrate', 'makemigrations', 'collectstatic']):
            self.rag_service = None
            return
        if not Path(VECTORDB_PATH).exists():
            self.rag_service = None
            return
        try:
            self.rag_service = RAGService(key_path=KEY_PATH,
                                          law_docs_path=LAW_DOCS_PATH,
                                          model_path=MODEL_PATH,
                                          vectordb_path=VECTORDB_PATH,
                                          truncate_dim=TRUNCATE_DIM,
                                          top_k=TOP_K,
                                          openai_model=OPENAI_MODEL,
                                          device=DEVICE)
        except Exception:
            self.rag_service = None
          
