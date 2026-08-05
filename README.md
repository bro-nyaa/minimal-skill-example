# Minimal Skill Example

This repository is a tiny, runnable example of a Codex skill.

It is intentionally small:

- `skill/SKILL.md` contains the skill metadata and instructions.
- `scripts/validate_skill.py` checks that the example skill has the required shape.
- `.gitignore` ignores local cache files.

## Run

```powershell
python scripts/validate_skill.py
```

Expected output:

```text
Skill validation passed: skill/SKILL.md
```

## What this demonstrates

A minimal skill needs a folder with a required `SKILL.md` file. The file starts
with YAML frontmatter that includes `name` and `description`, followed by concise
instructions for the agent.

