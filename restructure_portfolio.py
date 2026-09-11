from pathlib import Path
import shutil
import re

ROOT = Path.cwd()

# ============================================================
# CONFIGURATION
# ============================================================

PAGES = {
    "index.html": {
        "title": "Felix Amoah | DevSecOps Engineer",
        "heading": "Building secure infrastructure, one system at a time.",
        "subtitle": "DevSecOps Engineer in Training",
        "intro": (
            "I am Felix Amoah, a DevSecOps Engineer in training focused on "
            "cloud infrastructure, automation, containers and security."
        ),
    },

    "about/index.html": {
        "title": "About | Felix Amoah",
        "heading": "My journey into DevSecOps.",
        "subtitle": "About Me",
        "intro": (
            "A practical transition from engineering and security operations "
            "into cloud and DevSecOps engineering."
        ),
    },

    "skills/index.html": {
        "title": "Technical Skills | Felix Amoah",
        "heading": "Technologies I work with.",
        "subtitle": "Technical Skills",
        "intro": (
            "A growing technical foundation built through hands-on labs, "
            "projects, troubleshooting and continuous learning."
        ),
    },

    "projects/index.html": {
        "title": "Projects | Felix Amoah",
        "heading": "Projects built through practice.",
        "subtitle": "Projects",
        "intro": (
            "Real projects where I apply cloud, containers, automation "
            "and security concepts."
        ),
    },

    "labs/index.html": {
        "title": "DevSecOps Labs | Felix Amoah",
        "heading": "Where I learn by doing.",
        "subtitle": "DevSecOps Labs",
        "intro": (
            "Hands-on experiments, infrastructure labs, troubleshooting "
            "sessions and technical exercises."
        ),
    },

    "certifications/index.html": {
        "title": "Certifications & Training | Felix Amoah",
        "heading": "Training and professional development.",
        "subtitle": "Certifications & Training",
        "intro": (
            "The courses, bootcamps and technical learning forming my "
            "DevSecOps foundation."
        ),
    },

    "security/index.html": {
        "title": "Security | Felix Amoah",
        "heading": "Security is part of the engineering process.",
        "subtitle": "DevSecOps Security",
        "intro": (
            "Applying security principles throughout development, "
            "infrastructure and deployment."
        ),
    },

    "resume/index.html": {
        "title": "Resume | Felix Amoah",
        "heading": "Professional profile.",
        "subtitle": "Resume",
        "intro": (
            "A summary of my professional background, technical training "
            "and developing DevSecOps capabilities."
        ),
    },

    "contact/index.html": {
        "title": "Contact | Felix Amoah",
        "heading": "Let's connect.",
        "subtitle": "Contact",
        "intro": (
            "Interested in DevSecOps, cloud engineering, automation or "
            "secure infrastructure? Get in touch."
        ),
    },
}


# ============================================================
# BACKUP
# ============================================================

print("\n==============================================")
print(" FELIX AMOAH PORTFOLIO RESTRUCTURE")
print("==============================================\n")

for relative_path in PAGES:
    source = ROOT / relative_path

    if source.exists():
        backup = source.with_name(source.stem + ".before-restructure" + source.suffix)

        if not backup.exists():
            shutil.copy2(source, backup)
            print(f"✓ Backup created: {backup}")
        else:
            print(f"✓ Backup already exists: {backup}")


# ============================================================
# COMMON CSS
# ============================================================

CSS = r"""
:root {
    --bg: #f7f9ff;
    --surface: #ffffff;
    --surface-soft: #eef2ff;
    --text: #101828;
    --muted: #667085;
    --primary: #5b4bff;
    --primary-dark: #4033d6;
    --blue: #2878ff;
    --cyan: #19b5fe;
    --border: #e4e7ec;
    --shadow: 0 20px 60px rgba(35, 45, 90, 0.10);
    --radius: 22px;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Inter, Arial, sans-serif;
    background:
        radial-gradient(circle at 10% 10%, rgba(91,75,255,.10), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(25,181,254,.10), transparent 25%),
        var(--bg);
    color: var(--text);
    line-height: 1.7;
}

a {
    color: inherit;
    text-decoration: none;
}

.container {
    width: min(1120px, calc(100% - 40px));
    margin: auto;
}

.navbar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(255,255,255,.94);
    backdrop-filter: blur(18px);
    border-bottom: 1px solid var(--border);
}

.nav-inner {
    min-height: 76px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;
}

.logo img {
    height: 42px;
    width: auto;
    max-width: 150px;
    object-fit: contain;
    display: block;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 22px;
    list-style: none;
    flex-wrap: wrap;
}

.nav-links a {
    font-size: .88rem;
    font-weight: 700;
    color: #475467;
}

.nav-links a:hover {
    color: var(--primary);
}

.nav-github {
    padding: 9px 15px;
    background: #101828;
    color: white !important;
    border-radius: 9px;
}

.hero {
    padding: 130px 0 100px;
    text-align: center;
}

.eyebrow {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 999px;
    background: #e9e7ff;
    color: var(--primary);
    font-size: .78rem;
    font-weight: 800;
    margin-bottom: 20px;
}

.hero h1 {
    font-family: "Space Grotesk", Inter, sans-serif;
    font-size: clamp(2.7rem, 6vw, 5rem);
    line-height: 1.05;
    letter-spacing: -.055em;
    max-width: 900px;
    margin: auto;
}

.gradient {
    background: linear-gradient(100deg, var(--primary), var(--blue), var(--cyan));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

.hero p {
    max-width: 720px;
    margin: 24px auto 30px;
    color: var(--muted);
    font-size: 1.05rem;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
}

.btn {
    display: inline-flex;
    padding: 12px 19px;
    border-radius: 11px;
    font-weight: 800;
}

.btn-primary {
    background: linear-gradient(135deg, var(--primary), var(--blue));
    color: white;
}

.btn-outline {
    background: white;
    border: 1px solid var(--border);
}

section {
    padding: 90px 0;
}

.section-number {
    color: var(--primary);
    font-size: .75rem;
    font-weight: 900;
    letter-spacing: .15em;
    text-transform: uppercase;
    margin-bottom: 9px;
}

.section-header {
    max-width: 760px;
    margin-bottom: 40px;
}

.section-header h2 {
    font-family: "Space Grotesk", Inter, sans-serif;
    font-size: clamp(2rem, 4vw, 3.1rem);
    line-height: 1.1;
    letter-spacing: -.045em;
    margin-bottom: 15px;
}

.section-header p {
    color: var(--muted);
}

.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.card {
    background: rgba(255,255,255,.96);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 28px;
    box-shadow: var(--shadow);
}

.card h3 {
    font-family: "Space Grotesk", Inter, sans-serif;
    margin-bottom: 8px;
}

.card p {
    color: var(--muted);
    font-size: .92rem;
}

.card ul {
    margin-top: 14px;
    padding-left: 18px;
    color: var(--muted);
}

.highlight {
    background: #101632;
    color: white;
    border-radius: 28px;
    padding: 45px;
}

.highlight p {
    color: #b7c0d9;
}

.tag {
    display: inline-block;
    padding: 6px 10px;
    border-radius: 999px;
    background: #eef0ff;
    color: var(--primary);
    font-size: .75rem;
    font-weight: 800;
    margin: 4px;
}

.timeline {
    border-left: 3px solid #d9dcff;
    padding-left: 25px;
}

.timeline-item {
    margin-bottom: 35px;
}

.timeline-item h3 {
    margin-bottom: 5px;
}

.timeline-item p {
    color: var(--muted);
}

footer {
    padding: 35px 0;
    border-top: 1px solid var(--border);
    background: white;
}

.footer-inner {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

footer p {
    color: var(--muted);
    font-size: .82rem;
}

@media (max-width: 850px) {
    .nav-links {
        display: none;
    }

    .grid {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 600px) {
    .container {
        width: min(100% - 28px, 1120px);
    }

    .grid {
        grid-template-columns: 1fr;
    }

    .hero {
        padding: 90px 0 70px;
    }

    .highlight {
        padding: 30px 24px;
    }

    .footer-inner {
        flex-direction: column;
        text-align: center;
    }
}
"""


# ============================================================
# NAVIGATION
# ============================================================

def navigation():
    return """
<header class="navbar">
    <div class="container nav-inner">

        <a href="/index.html" class="logo">
            <img src="/15121.png" alt="Felix Amoah Logo">
        </a>

        <nav>
            <ul class="nav-links">
                <li><a href="/index.html">Home</a></li>
                <li><a href="/about/index.html">About</a></li>
                <li><a href="/projects/index.html">Projects</a></li>
                <li><a href="/labs/index.html">Labs</a></li>
                <li><a href="/blog/index.html">Journal</a></li>
                <li><a href="/skills/index.html">Skills</a></li>
                <li><a href="/certifications/index.html">Certifications</a></li>
                <li><a href="/security/index.html">Security</a></li>
                <li><a href="/resume/index.html">Resume</a></li>
                <li><a href="/contact/index.html">Contact</a></li>

                <li>
                    <a class="nav-github"
                       href="https://github.com/scriptsmithdev"
                       target="_blank"
                       rel="noopener noreferrer">
                        GitHub
                    </a>
                </li>
            </ul>
        </nav>

    </div>
</header>
"""


def footer():
    return """
<footer>
    <div class="container footer-inner">
        <p>© 2026 Felix Amoah. DevSecOps Engineer in Training.</p>

        <p>
            AWS • Docker • Terraform • Kubernetes • CI/CD • Security
        </p>
    </div>
</footer>
"""


def html_document(title, body):
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="description"
          content="{title} — Felix Amoah DevSecOps Engineer in Training">

    <meta name="author" content="Felix Amoah">

    <title>{title}</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect"
          href="https://fonts.gstatic.com"
          crossorigin>

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap"
          rel="stylesheet">

    <style>
    {CSS}
    </style>
</head>

<body>

{navigation()}

<main>
{body}
</main>

{footer()}

</body>
</html>
"""


# ============================================================
# HOMEPAGE
# ============================================================

homepage = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">
            DEVSECOPS ENGINEER IN TRAINING
        </div>

        <h1>
            Felix <span class="gradient">Amoah.</span>
        </h1>

        <p>
            Building practical skills in cloud infrastructure,
            automation, containers, CI/CD and security.
        </p>

        <div class="buttons">
            <a href="/projects/index.html" class="btn btn-primary">
                View Projects →
            </a>

            <a href="/about/index.html" class="btn btn-outline">
                About Me
            </a>
        </div>

    </div>
</section>


<section>
    <div class="container">

        <div class="section-header">
            <div class="section-number">01 — What I Do</div>

            <h2>
                Learning DevSecOps through hands-on engineering.
            </h2>

            <p>
                I focus on understanding how applications move from
                development to secure cloud deployment.
            </p>
        </div>

        <div class="grid">

            <div class="card">
                <h3>Cloud</h3>
                <p>
                    Building practical AWS knowledge around compute,
                    networking, IAM and cloud infrastructure.
                </p>
            </div>

            <div class="card">
                <h3>Automation</h3>
                <p>
                    Using Terraform, CI/CD and scripting to make
                    infrastructure and deployment repeatable.
                </p>
            </div>

            <div class="card">
                <h3>Security</h3>
                <p>
                    Applying security throughout the development and
                    deployment lifecycle.
                </p>
            </div>

        </div>
    </div>
</section>


<section>
    <div class="container">

        <div class="highlight">

            <div class="section-number">
                CURRENT FOCUS
            </div>

            <h2>
                Kubernetes & Cloud-Native Engineering
            </h2>

            <p>
                Currently developing practical Kubernetes skills including
                Pods, Deployments, Services, networking, container
                orchestration and troubleshooting.
            </p>

            <br>

            <a href="/labs/index.html" class="btn btn-primary">
                Explore My Labs →
            </a>

        </div>

    </div>
</section>


<section>
    <div class="container">

        <div class="section-header">
            <div class="section-number">Explore</div>

            <h2>
                Go deeper into my engineering work.
            </h2>
        </div>

        <div class="grid">

            <div class="card">
                <h3>Projects</h3>
                <p>Applications and infrastructure I have built.</p>
                <br>
                <a href="/projects/index.html">View Projects →</a>
            </div>

            <div class="card">
                <h3>Engineering Journal</h3>
                <p>What I learn, troubleshoot and build each week.</p>
                <br>
                <a href="/blog/index.html">Read Journal →</a>
            </div>

            <div class="card">
                <h3>Technical Skills</h3>
                <p>The technologies forming my DevSecOps foundation.</p>
                <br>
                <a href="/skills/index.html">View Skills →</a>
            </div>

        </div>
    </div>
</section>
"""


# ============================================================
# ABOUT
# ============================================================

about = """
<section class="hero">
    <div class="container">
        <div class="eyebrow">ABOUT FELIX</div>

        <h1>
            My journey into <span class="gradient">DevSecOps.</span>
        </h1>

        <p>
            A practical transition from professional engineering and
            security-focused environments into cloud and DevSecOps.
        </p>
    </div>
</section>

<section>
    <div class="container">

        <div class="grid">

            <div class="card">
                <h3>My Background</h3>
                <p>
                    My professional experience has taught me discipline,
                    responsibility, teamwork, safety awareness and the
                    importance of following structured processes.
                </p>
            </div>

            <div class="card">
                <h3>The Transition</h3>
                <p>
                    I am applying those same principles to technology while
                    building practical skills in Linux, Git, AWS, Terraform,
                    Docker, CI/CD and Kubernetes.
                </p>
            </div>

            <div class="card">
                <h3>My Approach</h3>
                <p>
                    I learn by building systems, breaking them, investigating
                    failures and documenting what I discover.
                </p>
            </div>

        </div>

    </div>
</section>

<section>
    <div class="container">

        <div class="highlight">

            <h2>My engineering philosophy</h2>

            <p>
                Understand the system. Automate what can be automated.
                Secure it from the beginning. Monitor what matters.
                Document the lessons.
            </p>

        </div>

    </div>
</section>
"""


# ============================================================
# SKILLS
# ============================================================

skills = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">TECHNICAL STACK</div>

        <h1>
            Technologies I am <span class="gradient">building with.</span>
        </h1>

        <p>
            My current DevSecOps toolkit and the practical areas I am
            developing through training and projects.
        </p>

    </div>
</section>

<section>
    <div class="container">

        <div class="grid">

            <div class="card">
                <h3>Linux</h3>
                <p>
                    Ubuntu, command line, permissions, processes,
                    services and troubleshooting.
                </p>
                <span class="tag">Ubuntu</span>
                <span class="tag">CLI</span>
            </div>

            <div class="card">
                <h3>Git & GitHub</h3>
                <p>
                    Version control, repositories, branches, commits,
                    GitHub workflows and signed commits.
                </p>
                <span class="tag">Git</span>
                <span class="tag">GitHub</span>
            </div>

            <div class="card">
                <h3>AWS</h3>
                <p>
                    EC2, IAM, VPC, security groups, ECR, ECS and
                    cloud networking fundamentals.
                </p>
                <span class="tag">EC2</span>
                <span class="tag">IAM</span>
                <span class="tag">ECR</span>
            </div>

            <div class="card">
                <h3>Terraform</h3>
                <p>
                    Infrastructure as Code, state management,
                    planning and repeatable provisioning.
                </p>
                <span class="tag">IaC</span>
                <span class="tag">HCL</span>
            </div>

            <div class="card">
                <h3>Docker</h3>
                <p>
                    Images, containers, Dockerfiles, networking,
                    registries and container troubleshooting.
                </p>
                <span class="tag">Containers</span>
                <span class="tag">Dockerfile</span>
            </div>

            <div class="card">
                <h3>Kubernetes</h3>
                <p>
                    Pods, Deployments, Services, workloads,
                    networking and cluster troubleshooting.
                </p>
                <span class="tag">Pods</span>
                <span class="tag">Services</span>
            </div>

            <div class="card">
                <h3>CI/CD</h3>
                <p>
                    Automated testing, validation, security scanning,
                    builds and deployment workflows.
                </p>
                <span class="tag">GitHub Actions</span>
                <span class="tag">Pipelines</span>
            </div>

            <div class="card">
                <h3>Security</h3>
                <p>
                    Shift-left security, secret management, least
                    privilege, scanning and secure configuration.
                </p>
                <span class="tag">DevSecOps</span>
                <span class="tag">Trivy</span>
            </div>

            <div class="card">
                <h3>Python</h3>
                <p>
                    Automation, scripting and Flask-based application
                    development.
                </p>
                <span class="tag">Python</span>
                <span class="tag">Flask</span>
            </div>

        </div>

    </div>
</section>
"""


# ============================================================
# PROJECTS
# ============================================================

projects = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">ENGINEERING PROJECTS</div>

        <h1>
            Building systems, not just <span class="gradient">tutorials.</span>
        </h1>

        <p>
            Projects where I apply cloud, containerization,
            automation and security concepts.
        </p>

    </div>
</section>

<section>
    <div class="container">

        <div class="card">

            <div class="section-number">
                FEATURED PROJECT
            </div>

            <h2>
                Secure Containerized Flask Application
            </h2>

            <p>
                A Python Flask application containerized with Docker
                and prepared for deployment using AWS services.
                The project focuses on understanding the complete
                application delivery workflow.
            </p>

            <br>

            <span class="tag">Python</span>
            <span class="tag">Flask</span>
            <span class="tag">Docker</span>
            <span class="tag">AWS ECR</span>
            <span class="tag">ECS/Fargate</span>
            <span class="tag">CI/CD</span>

        </div>

    </div>
</section>

<section>
    <div class="container">

        <div class="section-header">
            <div class="section-number">PROJECT WORKFLOW</div>

            <h2>
                From source code to deployment.
            </h2>
        </div>

        <div class="grid">

            <div class="card">
                <h3>01 — Source</h3>
                <p>
                    Application code is maintained in Git and GitHub
                    using version control practices.
                </p>
            </div>

            <div class="card">
                <h3>02 — Container</h3>
                <p>
                    The application is packaged into a Docker image
                    for consistent execution.
                </p>
            </div>

            <div class="card">
                <h3>03 — Security</h3>
                <p>
                    Security checks and validation are incorporated
                    into the delivery workflow.
                </p>
            </div>

            <div class="card">
                <h3>04 — Cloud</h3>
                <p>
                    Container images can be stored in Amazon ECR
                    and deployed through AWS services.
                </p>
            </div>

        </div>

    </div>
</section>
"""


# ============================================================
# LABS
# ============================================================

labs = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">HANDS-ON ENGINEERING</div>

        <h1>
            My <span class="gradient">DevSecOps Lab.</span>
        </h1>

        <p>
            This is where theory becomes practical experience.
            I use labs to test commands, deploy infrastructure,
            troubleshoot failures and understand systems.
        </p>

    </div>
</section>

<section>
    <div class="container">

        <div class="grid">

            <div class="card">
                <h3>Kubernetes Labs</h3>
                <p>
                    Working with Pods, Deployments, Services,
                    Minikube, kubectl and container workloads.
                </p>
            </div>

            <div class="card">
                <h3>Docker Labs</h3>
                <p>
                    Building images, creating containers,
                    networking and troubleshooting Docker environments.
                </p>
            </div>

            <div class="card">
                <h3>AWS Labs</h3>
                <p>
                    Practicing EC2, IAM, networking, security groups,
                    ECR and cloud deployment workflows.
                </p>
            </div>

            <div class="card">
                <h3>Terraform Labs</h3>
                <p>
                    Creating infrastructure as code and learning
                    how Terraform manages infrastructure state.
                </p>
            </div>

            <div class="card">
                <h3>CI/CD Labs</h3>
                <p>
                    Building automated workflows for validation,
                    security checks and deployment.
                </p>
            </div>

            <div class="card">
                <h3>Troubleshooting</h3>
                <p>
                    Investigating failed services, networking issues,
                    containers, Kubernetes clusters and pipelines.
                </p>
            </div>

        </div>

    </div>
</section>

<section>
    <div class="container">

        <div class="highlight">

            <h2>
                The failures are part of the learning.
            </h2>

            <p>
                A major part of my lab work is documenting what failed,
                understanding why it failed and identifying how to
                prevent the same problem in a production environment.
            </p>

        </div>

    </div>
</section>
"""


# ============================================================
# CERTIFICATIONS
# ============================================================

certifications = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">LEARNING & TRAINING</div>

        <h1>
            Building my <span class="gradient">technical foundation.</span>
        </h1>

        <p>
            My professional development is currently focused on
            practical DevSecOps and cloud engineering capability.
        </p>

    </div>
</section>

<section>
    <div class="container">

        <div class="timeline">

            <div class="timeline-item">
                <h3>DevSecOps Bootcamp</h3>
                <p>
                    Hands-on training covering Linux, Git & GitHub,
                    AWS, Terraform, Docker, CI/CD, Kubernetes and
                    security practices.
                </p>
            </div>

            <div class="timeline-item">
                <h3>Linux</h3>
                <p>
                    Completed practical Linux fundamentals including
                    command-line operations, permissions, processes
                    and system troubleshooting.
                </p>
            </div>

            <div class="timeline-item">
                <h3>Git & GitHub</h3>
                <p>
                    Completed version control training covering
                    repositories, branching, commits and collaboration.
                </p>
            </div>

            <div class="timeline-item">
                <h3>AWS</h3>
                <p>
                    Completed foundational cloud engineering training
                    covering compute, networking, IAM and AWS services.
                </p>
            </div>

            <div class="timeline-item">
                <h3>Terraform</h3>
                <p>
                    Completed Infrastructure as Code training covering
                    configuration, state and repeatable provisioning.
                </p>
            </div>

            <div class="timeline-item">
                <h3>Docker & CI/CD</h3>
                <p>
                    Completed practical containerization and automated
                    delivery workflows.
                </p>
            </div>

            <div class="timeline-item">
                <h3>Kubernetes</h3>
                <p>
                    Currently developing practical Kubernetes
                    orchestration skills.
                </p>
            </div>

        </div>

    </div>
</section>
"""


# ============================================================
# SECURITY
# ============================================================

security = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">DEVSECOPS SECURITY</div>

        <h1>
            Security from <span class="gradient">day one.</span>
        </h1>

        <p>
            Security should not be something added after deployment.
            It should be part of the engineering process.
        </p>

    </div>
</section>

<section>
    <div class="container">

        <div class="grid">

            <div class="card">
                <h3>Secret Management</h3>
                <p>
                    Avoiding hardcoded credentials and sensitive values
                    inside source code and infrastructure configuration.
                </p>
            </div>

            <div class="card">
                <h3>Least Privilege</h3>
                <p>
                    Designing access around the principle that users,
                    services and workloads should receive only the
                    permissions they require.
                </p>
            </div>

            <div class="card">
                <h3>Security Scanning</h3>
                <p>
                    Using automated security checks and container
                    scanning as part of the delivery process.
                </p>
            </div>

            <div class="card">
                <h3>Signed Commits</h3>
                <p>
                    Using GPG-signed Git commits as part of my
                    source-control security practices.
                </p>
            </div>

            <div class="card">
                <h3>CI/CD Security</h3>
                <p>
                    Integrating validation and security checks into
                    automated pipelines.
                </p>
            </div>

            <div class="card">
                <h3>Shift Left</h3>
                <p>
                    Finding security problems earlier in the software
                    development lifecycle rather than waiting until
                    production.
                </p>
            </div>

        </div>

    </div>
</section>

<section>
    <div class="container">

        <div class="highlight">

            <h2>
                My security mindset
            </h2>

            <p>
                Secure code. Secure infrastructure. Secure credentials.
                Secure pipelines. Security is a continuous engineering
                responsibility.
            </p>

        </div>

    </div>
</section>
"""


# ============================================================
# RESUME
# ============================================================

resume = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">PROFESSIONAL PROFILE</div>

        <h1>
            Felix <span class="gradient">Amoah.</span>
        </h1>

        <p>
            DevSecOps Engineer in Training focused on cloud
            infrastructure, automation, containers and security.
        </p>

    </div>
</section>

<section>
    <div class="container">

        <div class="grid">

            <div class="card">
                <h3>Current Role</h3>
                <p>
                    Assistant Pipe Fitter Cum Rigger<br>
                    EMKAN for Engineering & Contracting Services
                </p>
            </div>

            <div class="card">
                <h3>Technical Direction</h3>
                <p>
                    DevSecOps, Cloud Engineering,
                    Infrastructure Automation and Cloud Security.
                </p>
            </div>

            <div class="card">
                <h3>Core Technologies</h3>
                <p>
                    Linux, Git, GitHub, AWS, Terraform,
                    Docker, Kubernetes, CI/CD and Python.
                </p>
            </div>

        </div>

    </div>
</section>

<section>
    <div class="container">

        <div class="section-header">
            <div class="section-number">PROFESSIONAL EXPERIENCE</div>
            <h2>Experience beyond technology.</h2>
        </div>

        <div class="timeline">

            <div class="timeline-item">
                <h3>EMKAN for Engineering & Contracting Services</h3>
                <p>
                    Assistant Pipe Fitter Cum Rigger — supporting pipe
                    fitting, rigging, material handling, safety procedures
                    and team-based engineering operations.
                </p>
            </div>

            <div class="timeline-item">
                <h3>City Nights Contracting LLC — Dubai</h3>
                <p>
                    Security Personnel — maintaining security awareness,
                    monitoring activities, controlling access and
                    working responsibly in a professional environment.
                </p>
            </div>

            <div class="timeline-item">
                <h3>Oak Plaza Suites — Ghana</h3>
                <p>
                    Security Receptionist — supporting front-desk
                    responsibilities, security awareness and professional
                    customer interaction.
                </p>
            </div>

            <div class="timeline-item">
                <h3>Guinness Ghana Limited</h3>
                <p>
                    Warehouse experience involving material handling,
                    workplace discipline and structured operations.
                </p>
            </div>

        </div>

    </div>
</section>
"""


# ============================================================
# CONTACT
# ============================================================

contact = """
<section class="hero">
    <div class="container">

        <div class="eyebrow">CONTACT FELIX</div>

        <h1>
            Let's <span class="gradient">connect.</span>
        </h1>

        <p>
            I am developing my career in DevSecOps, cloud engineering
            and cloud security. Feel free to connect with me.
        </p>

        <div class="buttons">

            <a
                href="mailto:scriptsmith.dev@yahoo.com"
                class="btn btn-primary">
                Email Me
            </a>

            <a
                href="https://github.com/scriptsmithdev"
                target="_blank"
                rel="noopener noreferrer"
                class="btn btn-outline">
                GitHub →
            </a>

        </div>

    </div>
</section>

<section>
    <div class="container">

        <div class="grid">

            <div class="card">
                <h3>Email</h3>
                <p>
                    scriptsmith.dev@yahoo.com
                </p>
            </div>

            <div class="card">
                <h3>GitHub</h3>
                <p>
                    github.com/scriptsmithdev
                </p>
            </div>

            <div class="card">
                <h3>Focus</h3>
                <p>
                    DevSecOps • Cloud • Automation • Security
                </p>
            </div>

        </div>

    </div>
</section>
"""


# ============================================================
# WRITE PAGES
# ============================================================

CONTENT = {
    "index.html": homepage,
    "about/index.html": about,
    "skills/index.html": skills,
    "projects/index.html": projects,
    "labs/index.html": labs,
    "certifications/index.html": certifications,
    "security/index.html": security,
    "resume/index.html": resume,
    "contact/index.html": contact,
}


for relative_path, body in CONTENT.items():

    path = ROOT / relative_path

    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    title = PAGES[relative_path]["title"]

    document = html_document(title, body)

    path.write_text(document, encoding="utf-8")

    print(f"✓ Updated {relative_path}")


# ============================================================
# FINAL CHECK
# ============================================================

print("\n==============================================")
print("✓ PORTFOLIO RESTRUCTURE COMPLETE")
print("==============================================")

print("\nPages created/updated:")

for page in CONTENT:
    print(f"  ✓ {page}")

print("\nYour logo is configured as:")
print("  ✓ 15121.png")

print("\nBackups were created before modification.")

print("\nNext steps:")
print("  git status")
print("  git diff --stat")
print("  git add .")
print('  git commit -m "Restructure portfolio into dedicated pages"')
print("  git push origin main")

print("\n==============================================")
