import os
import sys
import json
import urllib.request
import urllib.error
import argparse

# --- Configuration ---
# Model IDs go stale. Update these when a newer model ships; nothing else in
# the script depends on the specific ID.
#
# These are deliberately capable models rather than cheap ones. The point of
# the ensemble is an independent second opinion on analytical judgment —
# convergence between three models only means something if all three are
# actually capable of the reasoning. Volume is two calls per run, so cost is
# not the constraint here.
#
# Verified against provider docs 2026-08-14:
#   gpt-5.6-sol      OpenAI frontier tier, for complex professional work.
#                    Cheaper alternatives in the same generation if needed:
#                    gpt-5.6-terra (balanced), gpt-5.6-luna (high volume).
#   gemini-3.7-flash Latest GA Flash. Chosen over gemini-3.1-pro-preview
#                    because that one is still preview — not something to pin
#                    a shared skill to. Supports tunable thinking levels if
#                    you later want to raise reasoning depth.
MODELS = {
    "openai": {"model": "gpt-5.6-sol", "name": "ChatGPT"},
    "gemini": {"model": "gemini-3.7-flash", "name": "Gemini"},
}

# Long analyses on a slow connection can exceed the default socket timeout.
REQUEST_TIMEOUT = 180


def send(req, provider_label):
    """Send a request and return the parsed JSON, with readable failures."""
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:500]
        print(f"Error: {provider_label} returned HTTP {e.code}.\n{body}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error: could not reach {provider_label} ({e.reason}).")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: {provider_label} returned a response that was not JSON.")
        sys.exit(1)


def call_openai(prompt, content):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: Set OPENAI_API_KEY in your ~/.zshrc")
        sys.exit(1)

    model = MODELS["openai"]["model"]
    url = "https://api.openai.com/v1/chat/completions"
    data = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    }).encode()
    req = urllib.request.Request(url, data=data, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    })
    result = send(req, "OpenAI")
    try:
        return result["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        print(f"Error: unexpected OpenAI response shape:\n{json.dumps(result)[:500]}")
        sys.exit(1)


def call_gemini(prompt, content):
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: Set GEMINI_API_KEY or GOOGLE_API_KEY in your ~/.zshrc")
        sys.exit(1)

    model = MODELS["gemini"]["model"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    full_prompt = f"{prompt}\n\n---\n\n{content}"
    data = json.dumps({
        "contents": [{"parts": [{"text": full_prompt}]}]
    }).encode()
    req = urllib.request.Request(url, data=data, headers={
        "Content-Type": "application/json"
    })
    result = send(req, "Gemini")
    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        print(f"Error: unexpected Gemini response shape:\n{json.dumps(result)[:500]}")
        sys.exit(1)


# --- Main ---
parser = argparse.ArgumentParser(description="Ensemble risk assessment")
parser.add_argument("input_file", help="Path to assumptions markdown file")
parser.add_argument("--provider", choices=["openai", "gemini"], required=True,
                    help="Which model provider to use")
args = parser.parse_args()

try:
    with open(args.input_file, "r") as f:
        assumptions_text = f.read()
except FileNotFoundError:
    print(f"Error: no file at {args.input_file}")
    sys.exit(1)

if not assumptions_text.strip():
    print(f"Error: {args.input_file} is empty — nothing to assess.")
    sys.exit(1)

prompt = """You are independently analyzing research assumptions extracted
from a qualitative analysis. Your task is the same task another model has
already completed — but you must do it independently, from scratch.

You have been given:
- A completed qualitative analysis with findings and evidence
- OR a list of assumptions already extracted from such an analysis

YOUR JOB: Independently assess each assumption for risk.

For each assumption:

1. State your risk level: Critical / High / Moderate / Low

2. Explain your reasoning — specifically:
   - Impact if wrong: does the recommendation change fundamentally?
   - Reversibility: if the team acts on this and it's wrong, how hard
     to course-correct?
   - Likelihood of being wrong: given evidence quality, sample size,
     and evidence type (behavioral vs stated, spontaneous vs prompted)

3. Surface any assumptions you see that may not have been extracted —
   claims embedded in the analysis that should be questioned but weren't.

4. For the top 3 riskiest assumptions, briefly suggest what validation
   approach would test them most effectively.

Be specific and analytical. Reference particular assumptions by number.
"Assumption 3 should be Critical because the entire recommendation
depends on it and the evidence is from a single segment" is useful.
"This needs more research" is not.

Output as a structured risk assessment with clear rankings and reasoning."""

provider_name = MODELS[args.provider]["name"]
model_name = MODELS[args.provider]["model"]

print(f"Sending to {provider_name} ({model_name})...")
print(f"Input: {len(assumptions_text)} chars")
print("Waiting for response...\n")

if args.provider == "openai":
    result = call_openai(prompt, assumptions_text)
elif args.provider == "gemini":
    result = call_gemini(prompt, assumptions_text)

# Save the response
output_path = args.input_file.replace(".md", f"-{args.provider}-assessment.md")
with open(output_path, "w") as f:
    f.write(f"# Ensemble risk assessment: {provider_name}\n\n")
    f.write(f"**Model:** {model_name}\n")
    f.write(f"**Input:** {args.input_file}\n\n")
    f.write(f"---\n\n{result}\n")

print(f"Assessment saved to: {output_path}")
print(f"\n--- Response ---\n")
print(result)
