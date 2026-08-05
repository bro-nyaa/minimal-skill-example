# Minimal Skill Example

[![Validate Skill](https://github.com/bro-nyaa/minimal-skill-example/actions/workflows/validate.yml/badge.svg)](https://github.com/bro-nyaa/minimal-skill-example/actions/workflows/validate.yml)

This repository is a tiny, runnable Codex skill. It turns a small project idea
into one goal, exactly three implementation steps, and one verification check.

It is intentionally small:

- `minimal-skill-example/SKILL.md` contains the metadata and instructions.
- `minimal-skill-example/agents/openai.yaml` contains UI metadata.
- `scripts/validate_skill.py` checks that the example skill has the required shape.
- `.github/workflows/validate.yml` runs the same check on GitHub.

## Validate

```powershell
python scripts/validate_skill.py
```

Expected output:

```text
Skill validation passed: minimal-skill-example/SKILL.md
```

## Install locally

Copy the `minimal-skill-example` folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\minimal-skill-example "$env:USERPROFILE\.codex\skills\minimal-skill-example"
```

Then invoke it with a prompt such as:

```text
Use $minimal-skill-example to turn a command-line todo app into the smallest runnable plan.
```

## Structure

```text
minimal-skill-example/
|-- minimal-skill-example/
|   |-- SKILL.md
|   `-- agents/openai.yaml
|-- scripts/validate_skill.py
`-- README.md
```

## What it demonstrates

A skill folder matches the skill name and contains a required `SKILL.md`. The
file starts with YAML frontmatter containing `name` and `description`, followed
by concise instructions for the agent.
