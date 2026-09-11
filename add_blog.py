from pathlib import Path
from datetime import date
import html
import re
import sys
import markdown


PROJECT_ROOT = Path(__file__).resolve().parent
PORTFOLIO_FILE = PROJECT_ROOT / "index.html"
BLOG_DIR = PROJECT_ROOT / "blog"
BLOG_INDEX = BLOG_DIR / "index.html"

BLOG_START = "<!-- BLOG:START -->"
BLOG_END = "<!-- BLOG:END -->"


def check_file(path):
    """Check that a required file exists."""
    if path.exists():
        print(f"✓ {path.relative_to(PROJECT_ROOT)}")
        return True

    print(f"✗ Missing: {path.relative_to(PROJECT_ROOT)}")
    return False


def check_blog_markers():
    """Verify that blog/index.html contains our automation markers."""

    if not BLOG_INDEX.exists():
        print("✗ blog/index.html is missing")
        return False

    html_content = BLOG_INDEX.read_text(encoding="utf-8")

    if BLOG_START not in html_content:
        print("✗ BLOG:START marker is missing from blog/index.html")
        return False

    if BLOG_END not in html_content:
        print("✗ BLOG:END marker is missing from blog/index.html")
        return False

    if html_content.index(BLOG_START) >= html_content.index(BLOG_END):
        print("✗ Blog markers are in the wrong order")
        return False

    print("✓ Blog markers found in blog/index.html")
    return True


def slugify(text):
    """Convert a title into a safe URL/file name."""

    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)

    return text.strip("-")


def ask(question):
    """Ask the user for a required value."""

    while True:
        value = input(f"{question}: ").strip()

        if value:
            return value

        print("Please enter a value.")


def create_article():
    """Create a new DevSecOps journal article."""

    print()
    print("========================================")
    print("         NEW DEVSECOPS ARTICLE")
    print("========================================")
    print()

    title = ask("Article title")
    category = ask("Category")
    summary = ask("Short summary")
    learned = ask("What did you learn today")
    activities = ask("What did you do")
    problem = ask("What problem did you encounter")
    solution = ask("How did you solve it")
    takeaways = ask("Key takeaways")

    article_date = date.today()
    display_date = article_date.strftime("%B %d, %Y")

    slug = slugify(title)

    if not slug:
        print("✗ Could not create a filename from the title.")
        return 1

    # Store published articles inside blog/posts/.
    POSTS_DIR = BLOG_DIR / "posts"
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    article_file = POSTS_DIR / f"{slug}.html"

    if article_file.exists():
        print()
        print("✗ Article already exists:")
        print(f"  {article_file.relative_to(PROJECT_ROOT)}")
        return 1

    # Escape user input before placing it inside HTML.
    title = html.escape(title)
    category = html.escape(category)
    summary = html.escape(summary)
    learned = html.escape(learned)
    activities = html.escape(activities)
    problem = html.escape(problem)
    solution = html.escape(solution)
    takeaways = html.escape(takeaways)

    article_html = f"""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <meta
        name="description"
        content="{summary}"
    >

    <title>{title} | Felix Amoah</title>

</head>


<body>

    <header>

        <a href="../index.html">
            ← Back to Portfolio
        </a>

        <p>
            DEVSECOPS ENGINEERING JOURNAL
        </p>

    </header>


    <main>

        <article>

            <header>

                <p>
                    {display_date}
                </p>

                <p>
                    {category}
                </p>

                <h1>
                    {title}
                </h1>

                <p>
                    {summary}
                </p>

            </header>


            <section>

                <h2>
                    What I Learned
                </h2>

                <p>
                    {learned}
                </p>

            </section>


            <section>

                <h2>
                    What I Did
                </h2>

                <p>
                    {activities}
                </p>

            </section>


            <section>

                <h2>
                    The Problem
                </h2>

                <p>
                    {problem}
                </p>

            </section>


            <section>

                <h2>
                    How I Solved It
                </h2>

                <p>
                    {solution}
                </p>

            </section>


            <section>

                <h2>
                    Key Takeaways
                </h2>

                <p>
                    {takeaways}
                </p>

            </section>

        </article>

    </main>


    <footer>

        <p>
            © {article_date.year} Felix Amoah
        </p>

        <a href="../index.html">
            Back to Portfolio
        </a>

    </footer>

</body>

</html>
"""

    article_file.write_text(article_html, encoding="utf-8")

    # ---------------------------------------------------------
    # Add the new article card to blog/index.html
    # ---------------------------------------------------------

    blog_index = BLOG_INDEX.read_text(encoding="utf-8")

    if BLOG_START not in blog_index or BLOG_END not in blog_index:
        print("✗ Blog markers are missing from blog/index.html")
        print("  Article was created, but the index was not updated.")
        return 1

    article_card = f"""
                <article class="note">
                    <div class="note-number">NEW</div>

                    <div class="article-meta">
                        <span class="tag">{category}</span>
                        <span class="tag">{display_date}</span>
                    </div>

                    <h3>{title}</h3>

                    <p>
                        {summary}
                    </p>

                    <a class="read-button" href="/blog/posts/{slug}.html">
                        Read Article →
                    </a>
                </article>
"""

    # Insert newest article immediately after BLOG:START.
    insertion_point = blog_index.index(BLOG_START) + len(BLOG_START)

    blog_index = (
        blog_index[:insertion_point]
        + article_card
        + blog_index[insertion_point:]
    )

    BLOG_INDEX.write_text(blog_index, encoding="utf-8")

    print()
    print("✓ Article created successfully")
    print()
    print(f"Title:   {title}")
    print(f"Category: {category}")
    print(f"Date:     {display_date}")
    print(f"File:     {article_file.relative_to(PROJECT_ROOT)}")
    print()

    return 0


def validate_project():
    """Validate the current project structure."""

    print()
    print("========================================")
    print("       DEVSECOPS BLOG MANAGER")
    print("========================================")
    print()

    print("Checking project...")
    print()

    files_ok = all([
        check_file(PORTFOLIO_FILE),
        check_file(BLOG_INDEX),
        check_file(BLOG_DIR),
    ])

    print()

    if not files_ok:
        print("✗ Project validation failed")
        return 1

    if not check_blog_markers():
        print("✗ Blog validation failed")
        return 1

    print()
    print("✓ Project is ready for blog automation")
    print()

    return 0


def main():
    """Handle command-line commands."""

    if len(sys.argv) == 1:
        return validate_project()

    command = sys.argv[1].lower()

    if command == "new":
        return create_article()

    if command == "validate":
        return validate_project()

    print(f"Unknown command: {command}")
    print()
    print("Available commands:")
    print("  python3 add_blog.py")
    print("  python3 add_blog.py validate")
    print("  python3 add_blog.py new")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
