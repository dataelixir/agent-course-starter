import os
from anthropic import Anthropic

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("No API key found. Set it first (step 4 of the checklist):")
    print('  export ANTHROPIC_API_KEY="your-key-here"')
    raise SystemExit(1)

client = Anthropic()  # reads ANTHROPIC_API_KEY automatically

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[{
        "role": "user",
        "content": "In one sentence, congratulate someone who just ran "
                   "their first AI API call from Python, and mention one "
                   "chore an agent could take off a data person's plate."
    }]
)

print()
print("It works. The model says:")
print()
print(message.content[0].text)
