## 🌟 Week 1 — Prompting Labs (Gemini Version)

This project contains Python scripts that demonstrate **17 prompt engineering patterns** using **Google Gemini API** instead of OpenAI.
It’s part of the **GenAI course Week 1 labs**.

---

### 🧠 What’s Inside

Each prompt pattern shows how to design effective prompts for different use cases:

1. Zero-Shot Prompting
2. One-Shot Prompting
3. Few-Shot Prompting
4. Role Prompting
5. Style Prompting
6. Emotion Prompting
7. Contextual Prompting
8. Rephrase-and-Respond
9. Re-Reading (RE2)
10. System Prompting
11. Self-Ask
12. Chain-of-Thought (CoT)
13. Step-Back Prompting
14. Self-Consistency
15. Thread-of-Thought (ThoT)
16. Tree-of-Thought (ToT)
17. ReAct (Reason + Act)

Each pattern runs, prints the model’s output, and logs both the **prompt** and **response** into the `week1_runs` folder.

---

### ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/heshameman-hub/GenAI_DifferentPersonas1.git
   cd GenAI_DifferentPersonas1
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Gemini API key**
   Create a `.env` file in the project folder and add:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

   > ⚠️ Do not upload your `.env` file to GitHub.

5. **Run the script**

   ```bash
   python Week1_Prompting_Labs_Gemini.py
   ```

---

### 📂 Output

All runs will be saved automatically in:

```
/week1_runs/
```

Each file includes the prompt text and model response.

---

### 💬 Notes

* This version uses the Gemini model:
  `models/gemini-2.5-flash-preview-09-2025`
* You can adjust temperature or model name at the top of the script.
* Safe for beginners — easy to modify and explore.

---
