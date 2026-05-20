from transformers import pipeline

print("=" * 65)
print("✨ SMARTSUMMARIZER - AI ARTICLE CONDENSER ✨")
print("=" * 65)

# Loading text generation model
generator = pipeline(
    task="text-generation",
    model="gpt2"
)

article_content = input("\n📄 Paste your article below:\n\n")

original_word_count = len(article_content.split())

print("\n🧠 Processing article intelligently...\n")

prompt = f"""
Create a concise professional summary for the following article.

Focus on:
- key historical facts
- cultural importance
- spiritual significance

Article:
{article_content}

Professional Summary:
"""

result = generator(
    prompt,
    max_new_tokens=80,
    temperature=0.5,
    num_return_sequences=1
)

generated_text = result[0]['generated_text']

# Extract only summary part
summary = generated_text.split("Professional Summary:")[-1].strip()

summary_word_count = len(summary.split())

compression_ratio = round(
    ((original_word_count - summary_word_count)
    / original_word_count) * 100,
    2
)

print("=" * 65)
print("📌 GENERATED SUMMARY")
print("=" * 65)

formatted_summary = summary.replace("-", "\n🔹")

print(formatted_summary)

print("\n" + "=" * 65)
print("📊 SUMMARY ANALYTICS")
print("=" * 65)

print(f"📝 Original Word Count   : {original_word_count}")
print(f"✨ Summary Word Count    : {summary_word_count}")
print(f"⚡ Compression Efficiency : {compression_ratio}%")

print("\n✅ AI summarization completed successfully.")
print("🚀 Transformer-based NLP engine executed.")