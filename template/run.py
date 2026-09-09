import os
from datetime import date
from pathlib import Path
from anthropic import Anthropic

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("No API key found. Set it first (step 4 of the checklist):")
    print('  export ANTHROPIC_API_KEY="your-key-here"')
    raise SystemExit(1)

# 1. The instructions: your judgment, read fresh from disk every run
instructions = Path("instructions.md").read_text()

# 2. The input: REPLACE this with your real input
#    (a feed, a CSV, a folder of documents, a pasted transcript...)
agent_input = "There is no input yet. Say so, briefly, and suggest one kind of input this agent's instructions seem built for."

# 3. One model call: instructions + input in, result out
client = Anthropic()
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[{
        "role": "user",
        "content": f"{instructions}\n\n---\n\nToday's input:\n\n{agent_input}",
    }],
)
result = message.content[0].text

# 4. The output: one dated file per run
out_path = Path("output") / f"{date.today().isoformat()}.md"
out_path.write_text(result)

print(f"Done. Result written to {out_path}")
print()
print(result)
