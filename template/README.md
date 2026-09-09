# The Agent Template

An agent is a folder. This one contains:

- **instructions.md** — what the agent is told. Judgment lives here, in plain English. (Rename it `taste.md` if your agent's job is judging or curating.)
- **run.py** — the plumbing. It reads instructions.md, gathers input, makes one model call, writes the result to output/.
- **output/** — where results land, one dated file per run.
- **.gitignore** — keeps secrets out of your commits.

To start a new agent: copy this whole folder, give it a name (`content_scout/`, `report_drafter/`), rewrite instructions.md for the job, and point run.py at your input. Keep your agent folders **next to** this repo, never inside it — every agent is its own house on the street.

As an agent evolves, the folder grows: `memory/` (what it knows), `evals/` (how you check it), `logs/` (what it did), a schedule (so it runs without you). The growth is the curriculum.

Open the folder and you're looking at the whole agent. Nothing is hidden. That's the point.
