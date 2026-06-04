import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

resume_texts = []

folder = "resumes"

for file in os.listdir(folder):

    if file.endswith(".txt"):

        path = os.path.join(folder, file)

        with open(path,
                  "r",
                  encoding="utf-8") as f:

            resume_texts.append(
                f.read()
            )

embeddings = model.encode(
    resume_texts,
    convert_to_numpy=True
)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    embeddings.astype(np.float32)
)


def retrieve_resume(query):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    D, I = index.search(
        query_embedding.astype(np.float32),
        1
    )

    return resume_texts[I[0][0]]