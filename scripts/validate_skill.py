from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "minimal-skill-example"
SKILL_FILE = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md must close YAML frontmatter with ---")

    values = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        if key in values:
            raise ValueError(f"Duplicate frontmatter field: {key}")
        values[key] = value.strip()

    body = text[end + len("\n---\n") :].strip()
    return values, body


def main():
    if not SKILL_FILE.exists():
        raise SystemExit(f"Missing required file: {SKILL_FILE}")

    frontmatter, body = parse_frontmatter(SKILL_FILE.read_text(encoding="utf-8"))
    missing = [key for key in ("name", "description") if not frontmatter.get(key)]
    if missing:
        raise SystemExit(f"Missing required frontmatter fields: {', '.join(missing)}")

    extra = sorted(set(frontmatter) - {"name", "description"})
    if extra:
        raise SystemExit(f"Unsupported frontmatter fields: {', '.join(extra)}")

    name = frontmatter["name"]
    if not NAME_PATTERN.fullmatch(name):
        raise SystemExit("Skill name must use lowercase letters, digits, and hyphens")
    if name != SKILL_DIR.name:
        raise SystemExit("Skill folder name must match the frontmatter name")
    if not body:
        raise SystemExit("SKILL.md must contain instructions after the frontmatter")

    if not OPENAI_YAML.exists():
        raise SystemExit(f"Missing recommended file: {OPENAI_YAML}")
    interface = OPENAI_YAML.read_text(encoding="utf-8")
    for field in ("display_name:", "short_description:", "default_prompt:"):
        if field not in interface:
            raise SystemExit(f"Missing agents/openai.yaml field: {field[:-1]}")
    if f"${name}" not in interface:
        raise SystemExit("default_prompt must mention the skill with $skill-name")

    relative_skill = SKILL_FILE.relative_to(ROOT).as_posix()
    print(f"Skill validation passed: {relative_skill}")


if __name__ == "__main__":
    main()
