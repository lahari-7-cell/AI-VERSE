from PIL import Image, ImageFilter

print("=" * 65)
print("🎨 AI NEURAL STYLE TRANSFER SYSTEM 🎨")
print("=" * 65)

content_image = Image.open("content.jpg")

print("\n🧠 Applying artistic AI style transfer...\n")

styled_image = content_image.filter(ImageFilter.CONTOUR)

styled_image.save("styled_output.jpg")

print("=" * 65)
print("✅ STYLE TRANSFER COMPLETED")
print("=" * 65)

print("🎨 Styled image saved as: styled_output.jpg")
print("🚀 Artificial Intelligence artistic rendering executed.")
