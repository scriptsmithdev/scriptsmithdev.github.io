from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
BLOG_INDEX = PROJECT_ROOT / "blog" / "index.html"

BLOG_START = "<!-- BLOG:START -->"
BLOG_END = "<!-- BLOG:END -->"

JOURNAL_SECTION = f"""
    <section>
        <div class="container">

            <div class="section-label">
                JOURNAL ENTRIES
            </div>

            <h2>Latest Articles</h2>

            <div class="notes-grid">

{BLOG_START}
{BLOG_END}

            </div>

        </div>
    </section>

"""


def main():
    if not BLOG_INDEX.exists():
        print("✗ blog/index.html not found")
        return 1

    content = BLOG_INDEX.read_text(encoding="utf-8")

    if BLOG_START in content or BLOG_END in content:
        print("✗ Blog markers already exist")
        return 1

    # Find the Engineering Notes section.
    marker = """    <section>
        <div class="container">

            <div class="section-label">
                ENGINEERING NOTES
            </div>
"""

    if marker not in content:
        print("✗ Could not find ENGINEERING NOTES section")
        return 1

    # Insert the dynamic journal section immediately before
    # the Engineering Notes section.
    content = content.replace(
        marker,
        JOURNAL_SECTION + marker,
        1,
    )

    BLOG_INDEX.write_text(content, encoding="utf-8")

    print("✓ Blog automation section added")
    print("✓ BLOG:START marker added")
    print("✓ BLOG:END marker added")
    print("✓ Existing journal design preserved")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
