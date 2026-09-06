# The Agent Course — Starter Repo

Starter files for **The Agent Course**, a 4-week cohort from the publisher of [Data Elixir](https://dataelixir.com) that teaches data practitioners to build small, practical AI agents for their own work, organized as plain folders you can read, run, and grow. The pattern is called **directory-as-agent**: an agent is a directory containing a markdown instructions file, a small script, and an output folder. No frameworks, nothing hidden.

Curious what that looks like in production? Two write-ups of the systems behind this course: [Investing with Agents](https://lonriesberg.com/posts/investing-with-agents/) and [Teaching an AI My Taste](https://lonriesberg.com/posts/teaching-an-ai-my-taste/).

## Quick start

You'll need Python 3.10+, a terminal, and an [Anthropic API key](https://console.anthropic.com) with a few dollars of credit behind it.

**1. Check Python** (3.10 or newer):

```bash
python3 --version
```

**2. Clone this repo and step inside:**

```bash
git clone https://github.com/dataelixir/agent-course-starter.git
cd agent-course-starter
```

**3. Get an API key** Go to [console.anthropic.com](https://console.anthropic.com), create an account, add $10 of credits under Billing, then create an API key under API Keys. Copy it somewhere safe; you only get to see it once.

**4. Put the key where Python can find it** (current terminal window only):

Mac/Linux:
```bash
export ANTHROPIC_API_KEY="paste-your-key-here"
```

Windows (PowerShell):
```powershell
$env:ANTHROPIC_API_KEY="paste-your-key-here"
```

**4. Install the one dependency:**

```bash
pip install -r requirements.txt
```

**5. Run the hello agent:**

```bash
python3 hello_agent.py
```

If a congratulations prints in your terminal, you just called an AI model from your own code, on your own machine. Every agent in this course starts exactly like this, with about forty more lines around it.

Hit a snag? The two usual suspects: the key isn't set in *this* terminal window (re-run step 3), or `pip` needs to be `pip3` or `python3 -m pip`.

## What's in here

| Path | What it is |
|---|---|
| `hello_agent.py` | A ~20-line script proving your setup works — the course's opening exercise |
| `template/` | The empty directory-as-agent convention: copy it to start any new agent |
| `starter-prompt.md` | A prompt for building an agent *with* an AI coding assistant, the sanctioned fast path |
| `data/` | Sample data used in the live sessions: weekly metrics CSV, a curated feed list, synthetic invoices |

The `template/` folder is deliberately tiny — an instructions file, a run script stub, an output directory, and a `.gitignore` that keeps secrets out of your commits. It grows week by week during the course (memory, evals, logs, a schedule), and that growth is the curriculum.

## Course members

Full setup instructions, troubleshooting, week 0, and all course materials live in the community: **[Start Here: Your Week 0 Checklist](https://community.dataelixir.com/c/course-hub/start-here-your-week-0-checklist)** (member login required).

## Not a member?

The founding cohort is running in fall 2026; the next cohort opens in January. For info, send a note to [lon@dataelixir.com](mailto:lon@dataelixir.com?subject=The%20Agent%20Course%20inquiry) or subscribe to [Data Elixir](https://dataelixir.com) to hear when doors open.

## License

MIT — see [LICENSE](LICENSE). Copy the template, build your company's agents with it, make it yours. That's what it's for.
