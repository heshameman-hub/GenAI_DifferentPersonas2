# Week 1 — Prompt Patterns Lab (Gemini Version)
# Run and log experiments for 17 prompt patterns using Google Gemini

import os, datetime, pathlib
import google.generativeai as genai

# --- Setup ---
PROVIDER = "gemini"
MODEL = "models/gemini-2.5-flash-preview-09-2025"  # latest stable version
GEN_ARGS = dict(temperature=0.2)

# Configure Gemini API Key (make sure GOOGLE_API_KEY is set)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Output directory
OUT_DIR = pathlib.Path("week1_runs_gemini")
OUT_DIR.mkdir(exist_ok=True)

summary = []  # 👈 هنا هنخزن كل النتائج

# --- Helper functions ---
def log_result(kind, name, prompt, output):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    (OUT_DIR / f"{kind}_{name}_{ts}.prompt.txt").write_text(prompt, encoding="utf-8")
    (OUT_DIR / f"{kind}_{name}_{ts}.output.txt").write_text(output, encoding="utf-8")
    print(f"✅ Saved results for {name} → {OUT_DIR}")

def llm_gemini(prompt, model=MODEL, **gen_args):
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt, generation_config=gen_args)
    return response.text

def run(prompt, name="test", provider=PROVIDER, **gen_args):
    print(f"\n🧠 Running pattern: {name}")
    if provider == "gemini":
        output = llm_gemini(prompt, **gen_args)
        log_result("pattern", name, prompt, output)
        summary.append(f"## {name}\n\n**Prompt:**\n{prompt}\n\n**Output:**\n{output}\n\n---\n")
        print(output)
    else:
        raise NotImplementedError("Only Gemini supported in this version.")

# --- Prompting Patterns ---
patterns = [
    ("zero_shot", "Explain how rainbows are formed."),
    ("few_shot", """Translate English to French.
English: Good morning → French: Bonjour
English: Thank you → French: Merci
English: How are you? →"""),
    ("chain_of_thought", """Solve step by step:
If a train travels 60 km/h for 2 hours, then 90 km/h for 1 hour, what is the average speed?"""),
    ("role_prompting", """You are an experienced career coach.
Give advice for someone switching from marketing to data analysis."""),
    ("instruction", """Write a short paragraph about teamwork in 3 sentences."""),
    ("template", """Generate a template email for requesting feedback after a job interview."""),
    ("persona", """Answer as if you are a witty comedian: Why did the AI cross the road?"""),
    ("context", """Context: You are writing for a tech newsletter.
Write 2 sentences about AI in healthcare."""),
    ("style_transfer", """Rewrite this in Shakespearean English:
'AI helps doctors diagnose diseases faster.'"""),
        ("delimiters", """Summarize the text below between triple quotes:

\"\"\" 
AI is revolutionizing education by personalizing learning experiences.
\"\"\"
"""),
    ("step_by_step", """Let's reason step by step:
What happens to water when it’s heated to 100°C at sea level?"""),
    ("self_consistency", """Give three different creative uses for paperclips."""),
    ("reframing", """Explain why electric cars are important, but from the point of view of an oil company executive."""),
    ("analogy", """Explain machine learning to a 10-year-old using an analogy."""),
    ("socratic", """Ask me 3 questions to help me think deeply about the impact of AI on society."""),
    ("multimodal", """Imagine a picture showing a cat chasing a robot mouse.
Describe the scene in a fun and detailed way."""),
    ("react", """You are solving this logically:
What number comes next in the sequence: 2, 4, 8, 16, ?"""),
]

# --- Run All ---
for name, prompt in patterns:
    run(prompt, name=name)

# --- Save Summary ---
summary_file = OUT_DIR / "week1_summary_report.txt"
summary_file.write_text("\n".join(summary), encoding="utf-8")

print(f"\n📄 All results saved in summary file: {summary_file}")
