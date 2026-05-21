from transformers import pipeline

print("=" * 65)
print("🤖 AI GENERATIVE TEXT MODEL 🤖")
print("=" * 65)

generator = pipeline(
    "text-generation",
    model="gpt2"
)

topic = input("\n📝 Enter a topic for AI text generation:\n\n")

print("\n🧠 Generating intelligent AI content...\n")

prompt = f"Write a professional paragraph about {topic}:"

result = generator(
    prompt,
    max_new_tokens=80,
    temperature=0.7,
    num_return_sequences=1
)

generated_text = result[0]['generated_text']

print("=" * 65)
print("📌 GENERATED TEXT")
print("=" * 65)

print(generated_text)

print("\n" + "=" * 65)
print("✅ Text generation completed successfully.")
print("🚀 Artificial Intelligence language model executed.")