import speech_recognition as sr

print("=" * 65)
print("🎤 AI SPEECH RECOGNITION SYSTEM 🎤")
print("=" * 65)

audio_file = input("\n📁 Enter audio file name (example: sample.wav): ")

recognizer = sr.Recognizer()

try:
    with sr.AudioFile(audio_file) as source:
        print("\n🎧 Listening to audio...")
        
        audio_data = recognizer.record(source)

        print("🧠 Processing speech intelligently...\n")

        text = recognizer.recognize_google(audio_data)

        print("=" * 65)
        print("📝 TRANSCRIBED TEXT")
        print("=" * 65)

        print(text)

        print("\n" + "=" * 65)
        print("✅ Speech recognition completed successfully.")
        print("🚀 Artificial Intelligence transcription engine executed.")

except FileNotFoundError:
    print("\n❌ Audio file not found.")
    
except sr.UnknownValueError:
    print("\n❌ Could not understand the audio.")

except sr.RequestError:
    print("\n❌ API request failed.")