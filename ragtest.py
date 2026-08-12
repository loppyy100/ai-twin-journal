
import ollama

def embed(text):
    return ollama.embed(model="nomic-embed-text", input=text)["embeddings"][0]

def similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    size_a = sum(x * x for x in a) ** 0.5
    size_b = sum(x * x for x in b) ** 0.5
    return dot / (size_a * size_b)

memories = [
    "I went for a run this morning",
    "I ate pizza for dinner",
    "I felt stressed about my exam",
]
memory_vectors = [embed(m) for m in memories]

question = "did I do any exercise?"
q_vector = embed(question)

# STEP 3 — find the BEST memory (your found-flag pattern, but tracking the top score)
best_score = -1
best_memory = ""
for i in range(len(memories)):
    score = similarity(q_vector, memory_vectors[i])
    if score > best_score:
        best_score = score
        best_memory = memories[i]

print("Retrieved memory:", best_memory)

# STEP 4 — hand it to Qwen to answer like a human (the "G" = Generate)
response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {"role": "system", "content": "Answer using only this memory: " + best_memory},
        {"role": "user", "content": question},
    ],
)
print("Twin says:", response["message"]["content"])
