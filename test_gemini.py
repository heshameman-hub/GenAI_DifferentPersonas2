import google.generativeai as genai


genai.configure(api_key="AIzaSyByv3nbwWfxhrpgbLAhDgvfP2S0_ayd19c")

model = genai.GenerativeModel("models/gemini-2.5-flash-preview-09-2025")


prompt = "Summarize the text: Artificial Intelligence is changing the world."

response = model.generate_content(prompt)

print(response.text)
