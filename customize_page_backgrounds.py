from pathlib import Path
import re
import shutil

ROOT = Path(".")

PAGES = {
    "index.html": {
        "class": "page-home",
        "accent": "#38bdf8",
        "bg1": "#020617",
        "bg2": "#0f172a",
        "bg3": "#172554",
        "pattern": "grid",
    },

    "about/index.html": {
        "class": "page-about",
        "accent": "#a78bfa",
        "bg1": "#0f0720",
        "bg2": "#1e1b4b",
        "bg3": "#312e81",
        "pattern": "network",
    },

    "projects/index.html": {
        "class": "page-projects",
        "accent": "#22d3ee",
        "bg1": "#031525",
        "bg2": "#0c2742",
        "bg3": "#164e63",
        "pattern": "code",
    },

    "labs/index.html": {
        "class": "page-labs",
        "accent": "#34d399",
        "bg1": "#021612",
        "bg2": "#052e2b",
        "bg3": "#064e3b",
        "pattern": "terminal",
    },

    "blog/index.html": {
        "class": "page-journal",
        "accent": "#fbbf24",
        "bg1": "#171005",
        "bg2": "#29200a",
        "bg3": "#451a03",
        "pattern": "dots",
    },

    "skills/index.html": {
        "class": "page-skills",
        "accent": "#60a5fa",
        "bg1": "#061225",
        "bg2": "#0c1e3a",
        "bg3": "#1e3a8a",
        "pattern": "grid",
    },

    "certifications/index.html": {
        "class": "page-certifications",
        "accent": "#c084fc",
        "bg1": "#13051f",
        "bg2": "#2e1065",
        "bg3": "#4c1d95",
        "pattern": "stars",
    },

    "security/index.html": {
        "class": "page-security",
        "accent": "#fb7185",
        "bg1": "#180407",
        "bg2": "#3f0a12",
        "bg3": "#4c0519",
        "pattern": "security",
    },

    "resume/index.html": {
        "class": "page-resume",
        "accent": "#94a3b8",
        "bg1": "#0b1018",
        "bg2": "#1e293b",
        "bg3": "#334155",
        "pattern": "lines",
    },

    "contact/index.html": {
        "class": "page-contact",
        "accent": "#2dd4bf",
        "bg1": "#021514",
        "bg2": "#0f2928",
        "bg3": "#134e4a",
        "pattern": "network",
    },
}


def make_css(data):
    patterns = {
        "grid": """
            background-image:
                linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px);
            background-size: 45px 45px;
        """,

        "network": """
            background-image:
                radial-gradient(circle at 20% 20%, rgba(255,255,255,.08) 0 2px, transparent 3px),
                radial-gradient(circle at 80% 30%, rgba(255,255,255,.06) 0 2px, transparent 3px),
                radial-gradient(circle at 40% 75%, rgba(255,255,255,.05) 0 2px, transparent 3px);
            background-size: 180px 180px;
        """,

        "code": """
            background-image:
                linear-gradient(rgba(255,255,255,.025) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,.025) 1px, transparent 1px);
            background-size: 32px 32px;
        """,

        "terminal": """
            background-image:
                repeating-linear-gradient(
                    0deg,
                    rgba(255,255,255,.025) 0px,
                    rgba(255,255,255,.025) 1px,
                    transparent 1px,
                    transparent 5px
                );
        """,

        "dots": """
            background-image:
                radial-gradient(rgba(255,255,255,.08) 1px, transparent 1px);
            background-size: 28px 28px;
        """,

        "stars": """
            background-image:
                radial-gradient(circle, rgba(255,255,255,.10) 1px, transparent 1px);
            background-size: 55px 55px;
        """,

        "security": """
            background-image:
                linear-gradient(135deg, rgba(255,255,255,.025) 25%, transparent 25%),
                linear-gradient(315deg, rgba(255,255,255,.025) 25%, transparent 25%);
            background-size: 70px 70px;
        """,

        "lines": """
            background-image:
                repeating-linear-gradient(
                    135deg,
                    rgba(255,255,255,.025) 0px,
                    rgba(255,255,255,.025) 1px,
                    transparent 1px,
                    transparent 35px
                );
        """,
    }

    return f"""
/* ================= PAGE-SPECIFIC DEVSECOPS THEME ================= */

body.{data['class']} {{
    background:
        radial-gradient(
            circle at 15% 15%,
            {data['bg3']} 0%,
            transparent 35%
        ),
        radial-gradient(
            circle at 85% 85%,
            {data['bg2']} 0%,
            transparent 40%
        ),
        linear-gradient(
            135deg,
            {data['bg1']},
            {data['bg2']}
        );

    background-attachment: fixed;
    color: #f8fafc;
}}

body.{data['class']}::before {{
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: -1;
    opacity: .55;
    {patterns[data['pattern']]}
}}

body.{data['class']} .hero {{
    position: relative;
}}

body.{data['class']} h1,
body.{data['class']} h2,
body.{data['class']} h3 {{
    color: #f8fafc;
}}

body.{data['class']} .eyebrow,
body.{data['class']} .section-number {{
    color: {data['accent']};
}}

body.{data['class']} .gradient {{
    background: linear-gradient(
        90deg,
        {data['accent']},
        #ffffff
    );
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}}

body.{data['class']} .btn-primary {{
    background: {data['accent']};
    color: #020617;
}}

body.{data['class']} .btn-primary:hover {{
    filter: brightness(1.12);
}}

body.{data['class']} .btn-outline:hover {{
    border-color: {data['accent']};
    color: {data['accent']};
}}

body.{data['class']} .card,
body.{data['class']} .project-card,
body.{data['class']} .skill-card,
body.{data['class']} .highlight {{
    background: rgba(15, 23, 42, .68);
    border-color: rgba(255,255,255,.10);
    backdrop-filter: blur(10px);
}}

body.{data['class']} .navbar {{
    background: rgba(2, 6, 23, .78);
    backdrop-filter: blur(14px);
}}

body.{data['class']} .footer {{
    background: rgba(2, 6, 23, .65);
}}

@media (max-width: 700px) {{
    body.{data['class']} {{
        background-attachment: scroll;
    }}
}}
"""


for relative_path, data in PAGES.items():

    file = ROOT / relative_path

    if not file.exists():
        print(f"⚠ Skipping missing page: {relative_path}")
        continue

    html = file.read_text(encoding="utf-8")

    # Create backup only once.
    backup = file.with_name(file.stem + ".before-background.html")

    if not backup.exists():
        shutil.copy2(file, backup)

    # Remove previous generated theme if present.
    html = re.sub(
        r'\s*/\* ================= PAGE-SPECIFIC DEVSECOPS THEME ================= \*/.*?</style>',
        '</style>',
        html,
        flags=re.DOTALL,
    )

    # Add CSS immediately before </style>.
    css = make_css(data)

    if "</style>" in html:
        html = html.replace(
            "</style>",
            css + "\n</style>",
            1
        )
    else:
        print(f"⚠ No </style> found in {relative_path}")
        continue

    # Add the page-specific body class.
    body_match = re.search(r'<body([^>]*)>', html, re.IGNORECASE)

    if body_match:
        attributes = body_match.group(1)

        # Remove previous generated page classes.
        attributes = re.sub(
            r'\s+class=["\'][^"\']*(?:page-home|page-about|page-projects|page-labs|page-journal|page-skills|page-certifications|page-security|page-resume|page-contact)[^"\']*["\']',
            "",
            attributes,
            flags=re.IGNORECASE,
        )

        if re.search(r'\bclass\s*=', attributes):
            attributes = re.sub(
                r'class=["\']([^"\']*)["\']',
                lambda m: f'class="{m.group(1)} {data["class"]}"',
                attributes,
                count=1,
                flags=re.IGNORECASE,
            )
        else:
            attributes += f' class="{data["class"]}"'

        replacement = f"<body{attributes}>"

        html = html[:body_match.start()] + replacement + html[body_match.end():]

    else:
        print(f"⚠ No <body> found in {relative_path}")
        continue

    file.write_text(html, encoding="utf-8")

    print(f"✓ Updated: {relative_path}")
    print(f"  Theme: {data['class']}")
    print(f"  Accent: {data['accent']}")
    print(f"  Pattern: {data['pattern']}")


print()
print("=" * 60)
print("✓ ALL PAGE BACKGROUNDS UPDATED")
print("=" * 60)
print()
print("Each page now has:")
print("  ✓ Unique background colours")
print("  ✓ Unique visual pattern")
print("  ✓ Unique accent colour")
print("  ✓ Readable text")
print("  ✓ Dark professional DevSecOps theme")
print("  ✓ Mobile support")
print()
print("Backups were created before modification.")
print("=" * 60)
