from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILE = ROOT / "skill" / "SKILL.md"


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
        values[key.strip()] = value.strip()
    return values


def main():
    if not SKILL_FILE.exists():
        raise SystemExit(f"Missing required file: {SKILL_FILE}")

    frontmatter = parse_frontmatter(SKILL_FILE.read_text(encoding="utf-8"))
    missing = [key for key in ("name", "description") if not frontmatter.get(key)]
    if missing:
        raise SystemExit(f"Missing required frontmatter fields: {', '.join(missing)}")

    name = frontmatter["name"]
    if not all(char.islower() or char.isdigit() or char == "-" for char in name):
        raise SystemExit("Skill name must use lowercase letters, digits, and hyphens")

    print("Skill validation passed: skill/SKILL.md")


if __name__ == "__main__":
    main()

