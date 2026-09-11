from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parent

# Only scan HTML files in the project.
HTML_FILES = PROJECT_ROOT.rglob("*.html")

# Matches lines such as:
# body.page-home .
# body.page-about .
# body.page-skills .
BROKEN_SELECTOR = re.compile(
    r"^\s*body\.page-[a-z0-9-]+\s*\.\s*$",
    re.MULTILINE,
)


def main():
    fixed_files = []

    for path in HTML_FILES:
        # Skip backup files.
        if ".before-" in path.name:
            continue

        content = path.read_text(encoding="utf-8")

        updated = BROKEN_SELECTOR.sub("", content)

        if updated != content:
            path.write_text(updated, encoding="utf-8")
            fixed_files.append(path.relative_to(PROJECT_ROOT))

    print()
    print("========================================")
    print("          CSS SELECTOR FIXER")
    print("========================================")
    print()

    if not fixed_files:
        print("✓ No broken CSS selectors found.")
        return

    print("✓ Fixed files:")

    for path in fixed_files:
        print(f"  - {path}")

    print()
    print(f"✓ Total files fixed: {len(fixed_files)}")


if __name__ == "__main__":
    main()
