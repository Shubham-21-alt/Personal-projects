#!/usr/bin/env python
# coding: utf-8

# In[10]:


import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load sentence transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def load_trap_clauses(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [trap["text"] for trap in data["trap_clauses"]]

def get_embeddings(sentences):
    return model.encode(sentences, convert_to_tensor=False)

def match_sentences_to_traps(input_sentences, trap_clauses, threshold=0.75):
    input_embeddings = get_embeddings(input_sentences)
    trap_embeddings = get_embeddings(trap_clauses)

    results = []

    for i, input_vec in enumerate(input_embeddings):
        max_sim = 0
        best_trap = None
        for j, trap_vec in enumerate(trap_embeddings):
            sim = cosine_similarity([input_vec], [trap_vec])[0][0]
            if sim > max_sim:
                max_sim = sim
                best_trap = trap_clauses[j]

        results.append({
            "sentence": input_sentences[i],
            "matched_trap": best_trap if max_sim >= threshold else None,
            "similarity": round(float(max_sim), 3),
            "is_match": max_sim >= threshold
        })

    return results



# In[18]:


if __name__ == "__main__":
    from preprocessing import preprocess_text

    # Step 1: Load and preprocess the input text
    sample_file = "C:\\Users\\Dell\\Desktop\\legal-trap-detector\\data\\sample_input.txt"
    input_sentences = preprocess_text(sample_file)

    # Step 2: Load trap clauses
    trap_clauses = load_trap_clauses("C:\\Users\\Dell\\Desktop\\legal-trap-detector\\traps\\trap_clauses.json")

    # Step 3: Match sentences
    matches = match_sentences_to_traps(input_sentences, trap_clauses, threshold=0.5)

    # Step 4: Show results
    print("\n🔐 Matched Sentences:\n")
    for match in matches:
        if match["matched_trap"] is not None:
            print("📌 Sentence     :", match["sentence"])
            print("⚠️  Matched Trap :", match["matched_trap"])
            print("🧮 Similarity   :", match["similarity"])
            print("-" * 60)

    print("\n🚫 Unmatched Sentences:\n")
    for match in matches:
        if match["matched_trap"] is None:
            print("📌 Sentence     :", match["sentence"])
            print("🧮 Similarity   :", match["similarity"])
            print("-" * 60)

 

