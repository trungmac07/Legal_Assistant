from django.core.management.base import BaseCommand
from django.apps import apps
import os
import torch
from Law_Assistant.embedding.loader import get_embedding_model
from Django_Server.config import LAW_DOCS_PATH, VECTORDB_PATH, TRUNCATE_DIM


class Command(BaseCommand):
    help = 'Recompute embeddings for all documents in data folder and save to vectordb file.'

    def add_arguments(self, parser):
        parser.add_argument('--docs', type=str, default=LAW_DOCS_PATH, help='Path to folder containing documents')
        parser.add_argument('--out', type=str, default=VECTORDB_PATH, help='Output path for embedding tensor (.pt)')
        parser.add_argument('--device', type=str, default='cpu', help='Device to run model on')

    def handle(self, *args, **options):
        docs_path = options['docs']
        out_path = options['out']
        device = options['device']

        model = get_embedding_model(device)

        files = sorted(os.listdir(docs_path))
        texts = []
        for file in files:
            file_path = os.path.join(docs_path, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    texts.append(f.read())

        self.stdout.write(self.style.NOTICE(f'Encoding {len(texts)} documents ...'))
        embeddings = model.encode(texts, convert_to_numpy=False, device=device, normalize_embeddings=True, truncate_dim=TRUNCATE_DIM)
        embeddings = [i.to('cpu') for i in embeddings]
        torch.save(embeddings, out_path)
        self.stdout.write(self.style.SUCCESS(f'Embeddings saved to {out_path}'))


