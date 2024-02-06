import json
import numpy as np
import pandas as pd

EMBEDDING_MODEL = "text-embedding-ada-002"  # dimension number 1536

def get_embedding(client, text: str, model: str=EMBEDDING_MODEL) -> list[float]:
    result = client.embeddings.create(
      model=model,
      input=text
    )
    list_result = result.model_dump_json(indent=2)
    dict_result = json.loads(list_result)
    return dict_result["data"][0]["embedding"] 

def compute_doc_embeddings(client, df: pd.DataFrame) -> dict[tuple[int, int], list[float]]:
    return {
        (r.skill_id, r.skill_name): get_embedding(client, r.skill_name) for idx, r in df.iterrows() # need to change based on specified dataframe
    }

def vector_similarity(x: list[float], y: list[float]) -> float:

    # return np.dot(np.array(x), np.array(y))
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

def order_document_sections_by_query_similarity(client, query: str, contexts: dict[(int, str), np.array]) -> list[(float, (int, str))]:

    query_embedding = get_embedding(client, query)
    
    document_similarities = sorted([
        (vector_similarity(query_embedding, doc_embedding), doc_index) for doc_index, doc_embedding in contexts.items()
    ], reverse=True)
    
    return document_similarities
