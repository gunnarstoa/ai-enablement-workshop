#!/usr/bin/env python3
"""
AI Enablement Lab Guide — Anaplan Partner Onboarding
Build script: generates all HTML pages for the workshop.
Run: python3 build.py
"""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ──────────────────────────────────────────────
# NAV
# ──────────────────────────────────────────────
NAV_LINKS = [
    ("section", "Getting Started"),
    ("index.html",             "Workshop Home"),
    ("01-overview.html",       "Workshop Overview"),
    ("02-case-study.html",     "Case Study: NovaTrend"),
    ("section", "CoModeler"),
    ("03-comodeler.html",      "CoModeler Deep-Dive + Labs"),
    ("section", "Agent Studio"),
    ("04-agent-studio.html",   "Agent Studio + Custom Analyst"),
    ("section", "Pre-Sales"),
    ("05-presales-demo.html",  "Pre-Sales Demo Playbook"),
    ("section", "Reference"),
    ("06-limitations.html",    "Limitations Quick Reference"),
    ("07-roadmap.html",        "Roadmap Snapshot (Apr 2026)"),
    ("08-partner-enablement.html", "Partner Enablement"),
    ("09-qanda.html",          "Q&amp;A from Session"),
    ("10-facilitator.html",    "Facilitator Guide"),
]

def nav(active_file):
    items = []
    for entry in NAV_LINKS:
        if entry[0] == "section":
            items.append(f'      <li class="nav-section-title">{entry[1]}</li>')
        else:
            href, label = entry
            cls = ' active' if href == active_file else ''
            items.append(f'      <li><a class="nav-link{cls}" href="./{href}">{label}</a></li>')
    nav_items = "\n".join(items)
    return f"""  <nav class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">AI Enablement</div>
      <div class="sidebar-subtitle">Anaplan Partner Onboarding</div>
    </div>
    <ul class="nav-list">
{nav_items}
    </ul>
  </nav>"""

# ──────────────────────────────────────────────
# PAGE SHELL
# ──────────────────────────────────────────────
def page(title, filename, header_h1, subtitle, badges, body, prevnext=None):
    badge_html = "".join(f'        <span class="content-badge">{b}</span>\n' for b in badges)
    pn = prevnext_html(prevnext) if prevnext else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — AI Enablement Lab Guide</title>
  <link rel="stylesheet" href="./css/style.css">
</head>
<body>
  <div class="mobile-header">
    <button id="hamburger">☰</button>
    <span>AI Enablement Lab Guide</span>
  </div>

{nav(filename)}

  <main class="main-content">
    <div class="content-header">
      <h1>{header_h1}</h1>
      <p class="subtitle">{subtitle}</p>
      <div class="badge-row">
{badge_html}      </div>
    </div>
    <div class="content-body">
{body}
{pn}
    </div>
  </main>
  <script src="./js/nav.js"></script>
</body>
</html>"""

def prevnext_html(pn):
    parts = []
    if pn.get("prev"):
        parts.append(f'      <a class="prevnext-prev" href="./{pn["prev"][0]}">&larr; {pn["prev"][1]}</a>')
    else:
        parts.append('      <span></span>')
    if pn.get("next"):
        parts.append(f'      <a class="prevnext-next" href="./{pn["next"][0]}">{pn["next"][1]} &rarr;</a>')
    else:
        parts.append('      <span></span>')
    return f"""      <div class="prevnext-nav">
{chr(10).join(parts)}
      </div>"""

# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────
def callout(kind, label, content):
    return f"""      <div class="callout-{kind}">
        <span class="callout-label">{label}</span>
        <p>{content}</p>
      </div>"""

def tsd_banner(tell, show, do_):
    return f"""      <div class="tsd-banner">
        <div class="tsd-step tsd-step-tell">
          <div class="tsd-step-label">📖 Tell</div>
          <div class="tsd-step-desc">{tell}</div>
        </div>
        <div class="tsd-step tsd-step-show">
          <div class="tsd-step-label">🖥️ Show</div>
          <div class="tsd-step-desc">{show}</div>
        </div>
        <div class="tsd-step tsd-step-do">
          <div class="tsd-step-label">🛠️ Do</div>
          <div class="tsd-step-desc">{do_}</div>
        </div>
      </div>"""

def table(headers, rows):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for row in rows:
        tds = "".join(f"<td>{c}</td>" for c in row)
        trs += f"        <tr>{tds}</tr>\n"
    return f"""      <div class="table-wrap">
        <table>
          <thead><tr>{ths}</tr></thead>
          <tbody>
{trs}          </tbody>
        </table>
      </div>"""

def ss(src, alt, caption=""):
    cap = f'\n        <p class="screenshot-caption">{caption}</p>' if caption else ""
    return f"""      <div class="screenshot-wrap">
        <img src="{src}" alt="{alt}" class="screenshot">
        {cap}
      </div>"""

def ss_placeholder(label):
    return f"""      <div class="screenshot-placeholder">
        <span>📷 {label}</span>
      </div>"""

def mini_lab(number, title, duration, objective, steps, debrief):
    steps_html = "\n".join(f"          <li>{s}</li>" for s in steps)
    debrief_html = "\n".join(f"          <li>{d}</li>" for d in debrief)
    return f"""      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">{number}</div>
          <div class="mini-lab-title">{title}</div>
          <div class="mini-lab-duration">⏱ {duration}</div>
        </div>
        <div class="mini-lab-body">
          <p><strong>Objective:</strong> {objective}</p>
          <h4>Steps</h4>
          <ol>
{steps_html}
          </ol>
          <h4>Debrief</h4>
          <ul>
{debrief_html}
          </ul>
        </div>
      </div>"""

# ──────────────────────────────────────────────
# PAGE BODIES
# ──────────────────────────────────────────────

# ─── index.html ───
INDEX_BODY = """
      <p>Welcome to the <strong>AI Enablement Lab Guide</strong> for Anaplan Partner Onboarding.
      This guide covers Anaplan's GA AI products as of April 2026: <strong>CoModeler</strong> and
      <strong>Agent Studio / Custom Analyst</strong>. It is sourced directly from Leo Nunes'
      April 2, 2026 onboarding session.</p>

      <h2>Who This Is For</h2>
      <ul>
        <li>Solutions Consultants and Solution Architects doing pre-sales demos</li>
        <li>Technical Consultants building or extending Anaplan models</li>
        <li>Partner practice leads who need to brief their teams on AI readiness</li>
      </ul>

      <h2>Prerequisites</h2>
      <ul class="checklist">
        <li>Partner tenant entitled for AI (CoModeler + Agent Studio)</li>
        <li>Tenant admin has assigned AI Admin role to relevant users</li>
        <li>Access to an Anaplan model (non-deployed, standard model)</li>
        <li>Seismic access for enablement blueprints</li>
        <li>Anaplan Academy login for self-paced CoModeler course</li>
      </ul>

      <h2>Workshop Modules</h2>
      <div class="module-grid">
        <a class="module-card" href="./01-overview.html">
          <div class="module-icon">🗺️</div>
          <div class="module-name">Workshop Overview</div>
          <div class="module-desc">AI journey, GA vs roadmap, learning path</div>
        </a>
        <a class="module-card" href="./02-case-study.html">
          <div class="module-icon">🏢</div>
          <div class="module-name">Case Study</div>
          <div class="module-desc">NovaTrend — fictional lab context</div>
        </a>
        <a class="module-card" href="./03-comodeler.html">
          <div class="module-icon">🤖</div>
          <div class="module-name">CoModeler Deep-Dive</div>
          <div class="module-desc">Capabilities, limits, prompting + 3 labs</div>
        </a>
        <a class="module-card" href="./04-agent-studio.html">
          <div class="module-icon">🎛️</div>
          <div class="module-name">Agent Studio</div>
          <div class="module-desc">Admin layer, Custom Analyst + 2 labs</div>
        </a>
        <a class="module-card" href="./05-presales-demo.html">
          <div class="module-icon">🎯</div>
          <div class="module-name">Pre-Sales Playbook</div>
          <div class="module-desc">Demo flow, objections, what to avoid</div>
        </a>
        <a class="module-card" href="./06-limitations.html">
          <div class="module-icon">⚠️</div>
          <div class="module-name">Limitations Reference</div>
          <div class="module-desc">Quick-ref card for customer conversations</div>
        </a>
        <a class="module-card" href="./07-roadmap.html">
          <div class="module-icon">📅</div>
          <div class="module-name">Roadmap Snapshot</div>
          <div class="module-desc">GA vs H2 2026 vs coming soon</div>
        </a>
        <a class="module-card" href="./08-partner-enablement.html">
          <div class="module-icon">📚</div>
          <div class="module-name">Partner Enablement</div>
          <div class="module-desc">Seismic, Academy, provisioning, contacts</div>
        </a>
        <a class="module-card" href="./09-qanda.html">
          <div class="module-icon">💬</div>
          <div class="module-name">Q&amp;A Reference</div>
          <div class="module-desc">All questions from Leo's session</div>
        </a>
        <a class="module-card" href="./10-facilitator.html">
          <div class="module-icon">🎙️</div>
          <div class="module-name">Facilitator Guide</div>
          <div class="module-desc">Delivery script, timing, debrief keys</div>
        </a>
      </div>

      <h2>Quick Links</h2>
      <ul>
        <li><a href="./06-limitations.html">⚠️ Limitations Quick Reference</a> — keep open during customer calls</li>
        <li><a href="./07-roadmap.html">📅 Roadmap Snapshot</a> — GA vs. roadmap as of April 2, 2026</li>
        <li><a href="./05-presales-demo.html">🎯 Pre-Sales Playbook</a> — demo flow and objection handling</li>
        <li><a href="./09-qanda.html">💬 Q&amp;A Reference</a> — real questions from the session</li>
      </ul>
"""

# ─── 01-overview.html ───
OVERVIEW_BODY = """
      <h2>Anaplan's AI Journey</h2>
      <p>Anaplan has been building toward connected, intelligent planning since 2018. Leo Nunes walked the partner cohort through the full timeline in the April 2, 2026 kickoff. Here is the arc:</p>

      <div class="screenshot-wrap">
        <img src="./img/ss-0120.jpg" alt="Anaplan AI Evolution — roadmap from 2019 to Agent Studio" class="screenshot">
        <p class="screenshot-caption">Anaplan AI evolution slide from Leo's April 2, 2026 session — Phase I through Agent Studio</p>
      </div>


      <div class="step">
        <div class="step-badge">2018</div>
        <div class="step-content"><strong>Anaplan Optimizer</strong> — First ML-type problem solver. GA since 2018. Still available.</div>
      </div>
      <div class="step">
        <div class="step-badge">2019</div>
        <div class="step-content"><strong>PlanIQ</strong> — Predecessor to Forecaster. Statistical forecasting engine. Now part of Forecaster.</div>
      </div>
      <div class="step">
        <div class="step-badge">2023</div>
        <div class="step-content"><strong>Syrup acquisition</strong> — Demand planning engine for Apparel, now baked into Supply Chain applications.</div>
      </div>
      <div class="step">
        <div class="step-badge">Late 2024</div>
        <div class="step-content"><strong>CoPlanet</strong> — First conversational AI tool for AFP and Demand Planning. Standalone product, now evolved into Finance Analysts.</div>
      </div>
      <div class="step">
        <div class="step-badge">2025</div>
        <div class="step-content"><strong>Finance Analysts + CoModeler GA</strong> — Built-in intelligence, role-based. Agent Studio released as admin layer.</div>
      </div>
      <div class="step">
        <div class="step-badge">H2 2026</div>
        <div class="step-content"><strong>LLM upgrade (ChatGPT 4.0 → Claude), Anomaly Detector, Model Optimizer, Workflow Agents</strong> — Roadmap items, not yet GA.</div>
      </div>

      <div class="callout-note">
        <span class="callout-label">📝 Important</span>
        <p>The <strong>Anaplan Machine Learning APIs</strong> (bring-your-own model) are <em>roadmap only</em> as of April 2026. Leo flagged this explicitly — the slide in the onboarding deck incorrectly marks it as "Phase 1" rather than roadmap. Do not promise this to customers.</p>
      </div>

      <h2>GA Products — What You Can Sell and Deliver Today</h2>
      """ + table(
    ["Product", "What It Is", "Who Uses It", "Status"],
    [
        ["CoModeler", "AI model-building assistant — creates, extends, documents, and checks health of Anaplan models", "Model builders, TCs, SAs", "✅ GA"],
        ["Agent Studio", "Admin control plane for all Anaplan AI — configure analysts, control workspace access", "Tenant admins, AI admins", "✅ GA"],
        ["Custom Analyst", "Configurable conversational AI for end users — natural language queries against Anaplan data", "End users, business users", "✅ GA"],
        ["Anaplan Analysts (Finance, WFP, SC, Sales)", "Pre-built analysts for specific functions", "End users in respective domains", "✅ GA"],
        ["Forecaster (PlanIQ)", "Statistical forecasting engine", "Supply chain, FP&A", "✅ GA"],
    ]
) + """

      <h2>Token Usage</h2>
      <p>As of April 2026, Leo confirmed that <strong>tokens are not being counted</strong> for partner tenants. The product team is not billing or throttling partner usage. This is the right time to experiment extensively.</p>

      <div class="callout-tip">
        <span class="callout-label">💡 Tip</span>
        <p>Use this window to run all three CoModeler labs, build at least one Custom Analyst configuration, and export documentation from a real model. Build your prompt library now while there are no token constraints.</p>
      </div>

      <h2>Learning Path</h2>
      <p>This workshop is structured as a self-contained enablement path. Follow the modules in order for the first pass. After that, use the reference pages (Limitations, Roadmap, Q&amp;A) as standing references during customer engagements.</p>

      <div class="step">
        <div class="step-badge">1</div>
        <div class="step-content"><strong>Workshop Overview</strong> (this page) — Understand the AI landscape and what's GA vs. roadmap.</div>
      </div>
      <div class="step">
        <div class="step-badge">2</div>
        <div class="step-content"><strong>Case Study</strong> — Meet NovaTrend. All labs are grounded in this scenario.</div>
      </div>
      <div class="step">
        <div class="step-badge">3</div>
        <div class="step-content"><strong>CoModeler Deep-Dive + Labs 2A/2B/2C</strong> — 45–60 minutes. Core model-building AI.</div>
      </div>
      <div class="step">
        <div class="step-badge">4</div>
        <div class="step-content"><strong>Agent Studio + Custom Analyst + Labs 3A/3B</strong> — 30–40 minutes. Admin layer and end-user AI.</div>
      </div>
      <div class="step">
        <div class="step-badge">5</div>
        <div class="step-content"><strong>Pre-Sales Demo Playbook</strong> — Review before any prospect demo. Not a lab — a reference.</div>
      </div>
      <div class="step">
        <div class="step-badge">6</div>
        <div class="step-content"><strong>Reference Pages</strong> — Limitations, Roadmap, Q&amp;A. Keep these open during customer conversations.</div>
      </div>
"""

# ─── 02-case-study.html ───
CASE_STUDY_BODY = """
      <p>All labs in this workshop are grounded in a single fictional customer: <strong>NovaTrend</strong>. Use this scenario whenever a lab asks you to make a configuration decision or write a prompt.</p>

      <h2>NovaTrend</h2>

      <div class="callout-note">
        <span class="callout-label">🏢 Company Profile</span>
        <p><strong>NovaTrend</strong> is a mid-market consumer goods company with ~1,200 employees across four regions (North America, EMEA, LATAM, APAC). They sell through retail and DTC channels and have been on Anaplan for two years. Their planning team has 15 model builders and approximately 400 end users across finance, supply chain, and sales.</p>
      </div>

      <table>
        <tbody>
          <tr><th>Industry</th><td>Consumer Goods</td></tr>
          <tr><th>Revenue</th><td>~$600M ARR</td></tr>
          <tr><th>Regions</th><td>4 (NA, EMEA, LATAM, APAC)</td></tr>
          <tr><th>Anaplan tenure</th><td>2 years, live on FP&amp;A and Supply Chain</td></tr>
          <tr><th>AI maturity</th><td>Low — leadership curious, team cautious</td></tr>
          <tr><th>Primary AI interest</th><td>Reduce model documentation burden; give planners self-service data access</td></tr>
        </tbody>
      </table>

      <h2>Why They Care About AI</h2>
      <ul>
        <li>Model documentation is currently done manually — takes 2–3 weeks per model, always out of date</li>
        <li>Planners constantly ask IT and the model builder team for basic data questions ("what is the forecast for region X in Q3?")</li>
        <li>Leadership wants to expand Anaplan usage but doesn't want to hire more model builders</li>
      </ul>

      <div class="callout-tip">
        <span class="callout-label">💡 Lab Note</span>
        <p>When writing CoModeler prompts in the labs, address NovaTrend's FP&amp;A model. When configuring a Custom Analyst, target their revenue planning module. This keeps the labs grounded and makes debrief discussions more useful.</p>
      </div>
"""

# ─── 03-comodeler.html ───
COMODELER_BODY = tsd_banner(
    "Understand what CoModeler is, what it can and cannot do, and how to prompt it effectively.",
    "See CoModeler opened in an Anaplan model. Walk through the Agent Studio configuration for CoModeler access.",
    "Complete Labs 2A, 2B, and 2C using the NovaTrend scenario."
) + """

      <div class="screenshot-wrap">
        <img src="./img/ss-1080.jpg" alt="CoModeler Overview slide from Leo's session" class="screenshot">
        <p class="screenshot-caption">CoModeler Overview — what it is, how it processes requests, key limitations (slide 21)</p>
      </div>

      <h2>What CoModeler Is</h2>
      <p>CoModeler is Anaplan's AI-powered model-building assistant. Leo's definition from the session: <em>"A very junior model builder that knows a lot."</em> It has deep business context (trained on the internet), knows Anaplan well (fine-tuned on Anapedia and plan content), but requires supervision — especially on complex models.</p>

      <p>It lives <strong>inside a model</strong>. It cannot interact with anything outside the model: no tenant management, no user management, no UX, no ADO, no workflow.</p>

      <h2>Capabilities</h2>
      """ + table(
    ["Capability", "Strength", "Notes"],
    [
        ["Build new models from scratch", "Strong", "Can generate modules, lists, line items from a prompt or spec file. Not perfect — check output."],
        ["Bulk rename / bulk edit", "Very strong", "Experts love this. Rename all line items on a module, change naming conventions across a model."],
        ["Document a model", "Strongest capability", "Line item dictionaries, notes on line items, exportable documentation. Wow factor."],
        ["Model health check", "Moderate", "Identifies unused modules/line items, best-practice issues. Points you to problems; doesn't fix them."],
        ["Extend application models", "Moderate (with guidance)", "Works better when you provide context (e.g. 'this is a Polaris model — use Polaris best practices')."],
        ["Formula optimization suggestions", "Limited", "Can suggest improvements but cannot make the change itself yet."],
        ["Data import setup", "Partial", "Can read a CSV, set up import action. Cannot execute the import."],
        ["Fix broken formulas", "Weak", "Better to build rev 02 of a module with corrections than ask it to fix rev 01."],
    ]
) + """

      <div class="screenshot-wrap">
        <img src="./img/ss-1500.jpg" alt="CoModeler Core Capabilities — Supported, Out of Scope, Known Opportunities" class="screenshot">
        <p class="screenshot-caption">CoModeler capabilities matrix from Leo's session — green = supported, amber = out of scope, orange = known opportunities (slide 24)</p>
      </div>

      <h2>Limitations Table</h2>
      """ + table(
    ["Cannot Do", "Why It Matters"],
    [
        ["Work on deployed models", "Standard model only. Always check model status before using CoModeler."],
        ["Classic dashboards", "No UX work. Pages, grids, charts — all out of scope."],
        ["ALM (Application Lifecycle Management)", "Cannot push changes through ALM pipeline."],
        ["User / tenant management", "Completely out of scope. Anything outside the model."],
        ["Change calendar / time ranges", "Time settings are immutable from CoModeler."],
        ["Import data (execute)", "Can set up the import action; cannot run it."],
        ["Bulk copy actions", "Cannot create or manage action sets."],
        ["Count cells / sum values", "Poor at math/aggregation within conversations."],
        ["Read conversation history", "No memory across sessions. Start fresh each time."],
        ["Interact with other AI products", "CoModeler and Custom Analyst do not communicate."],
        ["Work across multiple models simultaneously", "One model, one context window."],
    ]
) + """

      <div class="callout-warning">
        <span class="callout-label">⚠️ Delete Operations</span>
        <p>CoModeler will attempt delete operations when asked, but often fails silently if there are dependencies. It always asks you to approve before acting — but it does not always detect dependency chains before prompting. Always verify after any delete request.</p>
      </div>

      <h2>Prompting Best Practices</h2>
      <p>CoModeler is not chatty like ChatGPT. It thrives on precision, not conversation. Here is what works:</p>

      <h3>Be Specific</h3>
      <ul>
        <li><strong>Weak:</strong> "I need help with my budget model"</li>
        <li><strong>Strong:</strong> "In module REV-01, create 5 new line items: [names], all summing parent SUM-REV, formatted as currency, two decimals"</li>
      </ul>

      <h3>Use the Spec File Pattern</h3>
      <p>A spec file is a CSV that describes what you want built. Think of it as typing out your requirements in a structured format before asking CoModeler to execute. Columns typically include: module name, list dimensions, line item names, format, formula skeleton.</p>

      <div class="callout-tip">
        <span class="callout-label">💡 Spec File Tip</span>
        <p>Upload the CSV, then write a short prompt: "Using the attached spec file, create the modules and line items described. Use these naming conventions: [your standard]." This consistently outperforms plain text prompts for model-building tasks.</p>
      </div>

      <h3>Context Injection (for Application Models)</h3>
      <p>CoModeler cannot currently distinguish between a Polaris app model and a custom-built model. When working on application extensions, explicitly tell it:</p>
      <ul>
        <li>"This is an Anaplan Polaris model — please follow Polaris best practices"</li>
        <li>"This model uses the [app name] naming convention: [describe it]"</li>
      </ul>

      <h3>Parallel Tabs</h3>
      <p>Expert builders open multiple CoModeler tabs. While one is "thinking" (can take 3–5 minutes for large tasks), they work in another module via a second tab. Treat it like co-authoring with a colleague.</p>

      <h3>Context Window — 5 Interactions</h3>
      <p>Keep conversations to ~5 interactions. Beyond that, CoModeler loses earlier context. If a conversation goes sideways or hallucinates, start a new one — there is no recovering from a hallucination loop within the same conversation.</p>

      <h2>Prompt Library</h2>
      <p>Leo shared a prompt library in the partner folder. Key prompts from the session:</p>

      <div class="callout-note">
        <span class="callout-label">📋 Prompt: Model Health Check</span>
        <p>"Review this model for health issues. Identify: (1) modules with no downstream references, (2) line items that are never used in formulas, (3) any modules that appear to be orphaned. Present findings as a list with module name and issue type."</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">📋 Prompt: Line Item Dictionary</span>
        <p>"Generate a complete line item dictionary for module [MODULE NAME]. For each line item include: name, format, applies to dimensions, formula (if any), and a plain English description of what it represents in a [BUSINESS CONTEXT] planning model."</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">📋 Prompt: Bulk Rename</span>
        <p>"In module [MODULE NAME], rename all line items to match this naming convention: [CONVENTION]. Here are the current names and their intended new names: [LIST]. Apply all renames."</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">📋 Prompt: New Module from Scratch</span>
        <p>"Create a new module called [NAME] dimensioned by [LIST1] × [LIST2] × Time. Add the following line items: [LIST with formats]. This module will [PURPOSE]. Use best practices for module layout."</p>
      </div>

      <h2>LLM Roadmap</h2>
      <p>CoModeler currently runs on <strong>ChatGPT 4.0</strong>. The upgrade to <strong>Claude</strong> is targeted for H2 2026 (treat this as December 31, 2026 until Anaplan announces a specific date). The new model will enable:</p>
      <ul>
        <li>Better ability to distinguish application models from custom builds</li>
        <li>Persistent prompt notepad (save prompts inside CoModeler)</li>
        <li>Model Optimizer capability (suggest and apply formula improvements)</li>
      </ul>

      <hr>
      <h2>Lab 2A — First Conversation</h2>
      """ + mini_lab(
    "2A",
    "First Conversation with CoModeler",
    "15 min",
    "Open CoModeler in a real model and produce a line item dictionary for one module.",
    [
        "Open your Anaplan model (must be a standard, non-deployed model).",
        "Click the CoModeler icon in the top toolbar.",
        "If you don't see it, confirm your tenant admin has enabled CoModeler for your workspace via Agent Studio.",
        "Type this prompt: \"What is this model about? List the modules you can see and describe the purpose of each in one sentence.\"",
        "Review the response. Note: CoModeler is reading the model structure in real-time.",
        "Follow up: \"Generate a line item dictionary for the module with the most line items. Include: name, format, dimensions, and a plain English description.\"",
        "Download the response (use the download icon in the chat).",
        "Save the output — you will use it in Lab 3B.",
    ],
    [
        "How long did CoModeler take to respond to each prompt?",
        "Did the line item descriptions make sense for the business context? Did any seem hallucinated?",
        "What module did it identify as the most complex? Does that match your expectation?",
    ]
) + """

      <hr>
      <h2>Lab 2B — Spec File Build</h2>
      """ + mini_lab(
    "2B",
    "Build a Module Using a Spec File",
    "20 min",
    "Create a CSV spec file for a simple NovaTrend revenue module and use CoModeler to build it.",
    [
        "Create a CSV file with columns: Module, Dimension1, Dimension2, LineItem, Format, Formula, Description.",
        "Add 3–5 rows for a simple Revenue Actuals module. Use NovaTrend's regions as Dimension1, Products as Dimension2.",
        "Save as <code>novatrend-revenue-spec.csv</code>.",
        "In CoModeler, upload the CSV file.",
        "Type this prompt: \"Using the attached spec file, create the module and line items described. Apply standard Anaplan naming conventions. This is a consumer goods revenue model.\"",
        "Approve each step as CoModeler presents it.",
        "After creation, ask: \"Add a description note to each line item you just created explaining its purpose.\"",
        "Verify the module was created correctly in the model.",
    ],
    [
        "Did CoModeler follow the spec exactly? What did it get right or wrong?",
        "How did the description notes compare to what you would have written manually?",
        "What would you change in the spec file format to get better output?",
    ]
) + """

      <hr>
      <h2>Lab 2C — Documentation &amp; Model Health</h2>
      """ + mini_lab(
    "2C",
    "Documentation Export and Model Health Check",
    "15 min",
    "Use CoModeler to generate exportable model documentation and run a health check.",
    [
        "In CoModeler, type: \"Run a model health check. Identify any modules with no downstream references, unused line items, or orphaned lists. Present as a prioritized list.\"",
        "Review the output. Note any issues flagged.",
        "Next, type: \"Generate documentation for this entire model. For each module, include: purpose, dimensions, key line items, and how it connects to other modules. Format for export.\"",
        "Download the documentation export.",
        "Open the exported file and review quality. This is what you would hand a new model builder joining the project.",
        "Optional: Paste the documentation text into ChatGPT or Claude and ask it to enrich the descriptions. Compare the two versions.",
    ],
    [
        "What health issues did CoModeler find? Were they real issues or false positives?",
        "How complete was the documentation? Would you trust it without a manual review?",
        "How long would this documentation have taken to produce manually?",
    ]
)

# ─── 04-agent-studio.html ───
AGENT_STUDIO_BODY = tsd_banner(
    "Understand Agent Studio's role as the admin layer for all Anaplan AI. Learn the role chain: Tenant Admin → AI Admin → Custom Analyst configuration.",
    "Walk through Agent Studio: workspace enablement for CoModeler, Analyst list, Custom Analyst configuration panel.",
    "Complete Labs 3A (explore Agent Studio) and 3B (configure a Custom Analyst)."
) + """

      <h2>What Agent Studio Is</h2>
      <p>Agent Studio is the <strong>administration layer</strong> for all Anaplan AI products. It is not an AI tool itself — it is the control plane that governs which users can access AI, which workspaces have CoModeler enabled, and how Custom Analysts are configured.</p>

      <p>It was released after CoPlanet was sunsetted. The vision: a single admin destination for every Anaplan AI capability, current and future.</p>

      <div class="screenshot-wrap">
        <img src="./img/ss-0840.jpg" alt="Agent Studio title slide" class="screenshot">
        <p class="screenshot-caption">Agent Studio — the admin layer for all Anaplan AI products (session slide 15)</p>
      </div>

      <div class="screenshot-wrap">
        <img src="./img/ss-2700.jpg" alt="Custom Analyst — Embedded, Trusted, Purpose-Built pillars" class="screenshot">
        <p class="screenshot-caption">Custom Analyst with Agent Studio — three product pillars: Embedded, Trusted, Purpose-Built (slide 40)</p>
      </div>

      <h2>Architecture</h2>
      """ + table(
    ["Layer", "Who", "What They Control"],
    [
        ["Tenant Admin", "Customer IT / Anaplan admin", "Assigns AI Admin role to specific users. One-time setup per tenant."],
        ["AI Admin", "Partner or customer power user", "Enables CoModeler per workspace. Creates and configures Custom Analysts."],
        ["End User", "Business user / planner", "Queries Custom Analysts. Uses CoModeler if assigned to an enabled workspace."],
    ]
) + """

      <div class="callout-note">
        <span class="callout-label">📝 Partner Access Note</span>
        <p>As a partner, you <strong>can</strong> be assigned the AI Admin role on a customer's tenant — as long as the customer has licensed AI. This is different from Integration Admin, which is home-tenant locked. Partners can configure and manage AI on customer tenants directly.</p>
      </div>

      <div class="callout-warning">
        <span class="callout-label">⚠️ Partner Tenant Only</span>
        <p>Today, you will only see CoModeler inside your Carter (partner) tenant, <em>not</em> on customer tenants. This is by design — Anaplan wants customers to purchase CoModeler. Once the customer has licensed it, you can use it in their tenant.</p>
      </div>

      <h2>CoModeler Configuration in Agent Studio</h2>
      <p>From Agent Studio → CoModeler tab, an AI Admin can:</p>
      <ul>
        <li>Enable or disable CoModeler for specific workspaces (workspace-level granularity)</li>
        <li>Add new workspaces to the enabled list</li>
        <li>All workspace administrators in enabled workspaces automatically get CoModeler access</li>
      </ul>

      <h2>Custom Analyst Architecture</h2>
      <p>Custom Analyst is the Anaplan Analyst that <em>you</em> configure for your custom modules. Same underlying technology as the pre-built Finance Analysts — the difference is that you define the data scope, questions, context, and vocabulary.</p>

      <p>How it works:</p>
      <div class="step">
        <div class="step-badge">1</div>
        <div class="step-content">End user asks a question in plain language via the Custom Analyst interface.</div>
      </div>
      <div class="step">
        <div class="step-badge">2</div>
        <div class="step-content">Question is sent to the LLM (currently OpenAI), which writes an Anaplan query based on the modules and line items you pre-configured.</div>
      </div>
      <div class="step">
        <div class="step-badge">3</div>
        <div class="step-content">Query is executed in Anaplan <strong>as the user who asked</strong> — security and access filters apply automatically.</div>
      </div>
      <div class="step">
        <div class="step-badge">4</div>
        <div class="step-content">Raw data returns to the LLM, which formats the final answer and presents it with a source link.</div>
      </div>
      <div class="step">
        <div class="step-badge">5</div>
        <div class="step-content">If the question cannot be answered (data not in scope, user lacks access), the analyst says so — it does not hallucinate an answer.</div>
      </div>

      <h2>Security Model</h2>
      <p>This is a key customer question. The answer is clear:</p>
      <ul>
        <li><strong>Queries run as the end user</strong> — not as the AI Admin or a service account</li>
        <li><strong>Row-level security</strong> is enforced — if a user can't see a number in Anaplan, the analyst can't tell them that number</li>
        <li><strong>Scope is pre-configured</strong> — the analyst only looks at modules and line items you explicitly add to its configuration. Nothing else is accessible.</li>
        <li><strong>No hallucination path</strong> — if Anaplan doesn't have the answer, the analyst returns "I can't answer that" rather than generating a plausible-sounding wrong number.</li>
      </ul>

      <h2>Custom Analyst Configuration</h2>
      <p>From Agent Studio → Analysts → New Custom Analyst:</p>
      <ol>
        <li><strong>Name &amp; AI Context</strong> — Give the analyst a name and write a description of what this configuration is for. The more detail here, the better the LLM understands context. Example: "This is a revenue planning analyst for NovaTrend's consumer goods FP&amp;A model covering regional and product-level forecast and actuals data."</li>
        <li><strong>Data Sources</strong> — Add modules and select specific line items. Each line item gets a semantic description. Good semantics = good answers.</li>
        <li><strong>Suggested Questions</strong> — Pre-configure 5–10 questions that the business uses naturally. Use the customer's vocabulary, not model builder vocabulary.</li>
        <li><strong>Vocabulary</strong> — Add definitions for business terms. "OPEX = operating expenditure, including [specific line items in this model]."</li>
      </ol>

      <div class="callout-tip">
        <span class="callout-label">💡 Best Practice: Use CoModeler to Seed the Analyst</span>
        <p>From Lab 2C, you exported a line item dictionary. Paste that into ChatGPT or Claude and ask: "Enrich these line item descriptions for use as semantic definitions in a conversational AI system. Make each description clear to a non-technical business user." Then import the enriched descriptions into your Custom Analyst. This is the workflow Leo demonstrated.</p>
      </div>

      <h2>Current Limitations</h2>
      <ul>
        <li>Context window: ~5 follow-up questions per conversation before context is lost</li>
        <li>No cross-analyst queries — analysts cannot call each other</li>
        <li>No API access — cannot be integrated externally yet</li>
        <li>Visualizations are auto-generated (time series → line chart, rank → bar chart) but not configurable</li>
        <li>No conversation history saved — each session starts fresh</li>
        <li>LLM transition to Claude targeted H2 2026 — reconfiguration should not be required</li>
      </ul>

      <hr>
      <h2>Lab 3A — Explore Agent Studio</h2>
      """ + mini_lab(
    "3A",
    "Navigate Agent Studio and Verify Access",
    "15 min",
    "Confirm Agent Studio access, review CoModeler workspace configuration, and explore the Analysts list.",
    [
        "Log into Anaplan with an account that has the AI Admin role.",
        "Click the top-right dropdown → Agent Studio.",
        "If you don't see Agent Studio, your tenant admin has not assigned you the AI Admin role yet. Contact your workspace admin.",
        "Navigate to the CoModeler tab. Confirm your workspace appears in the enabled list.",
        "Navigate to the Analysts tab. Review any existing configurations.",
        "Click on a pre-built Anaplan Analyst (Finance or another if available). Note the data source configuration — how many modules and line items are pre-loaded?",
        "Return to Analysts → note the configuration structure (name, AI context, data sources, suggested questions).",
    ],
    [
        "Which workspaces are currently enabled for CoModeler in your tenant?",
        "How many pre-built analysts are available? What functions do they cover?",
        "What is the AI Context field in the pre-built analyst? How detailed is it?",
    ]
) + """

      <hr>
      <h2>Lab 3B — Configure a Custom Analyst</h2>
      """ + mini_lab(
    "3B",
    "Configure a Custom Analyst for NovaTrend",
    "25 min",
    "Create a working Custom Analyst configuration targeting NovaTrend's revenue module.",
    [
        "In Agent Studio → Analysts → Create New Custom Analyst.",
        "Name: 'NovaTrend Revenue Analyst'.",
        "AI Context: Write 2–3 sentences describing NovaTrend's business (use the case study). Include: industry, planning scope, key metrics the analyst should understand.",
        "Add Data Source: Select the module you built in Lab 2B (or any revenue/FP&amp;A module available).",
        "Select 3–5 line items. For each, write a semantic description using business language (not model builder language).",
        "Add 3 Suggested Questions that a NovaTrend planner would actually ask. Use their language: 'What is the forecast revenue for North America in Q3 2026?'",
        "Save the configuration.",
        "Open the analyst interface and test all 3 suggested questions. Note which ones return good answers and which fail.",
        "For any failed question, adjust the semantic description of the relevant line item and retest.",
    ],
    [
        "Did all 3 test questions return correct answers? If not, what was wrong?",
        "Did the analyst provide a source link showing where the data came from?",
        "What semantic description change had the most impact on answer quality?",
        "If a user asked a question outside your configured scope, what did the analyst say?",
    ]
)

# ─── 05-presales-demo.html ───
PRESALES_BODY = """
      <p>This playbook is for partner SCs and SAs who need to demonstrate CoModeler and Custom Analyst to prospects. It is sourced from Leo Nunes' pre-sales session (recorded, available in the Seismic blueprint folder) and the April 2, 2026 onboarding session.</p>

      <div class="callout-important">
        <span class="callout-label">🎯 Golden Rule</span>
        <p>Never demo a live AI system without having run through it completely the day before. AI output is non-deterministic — the response you got yesterday may not be the response you get tomorrow. Build a demo script. Know your fallback if a prompt produces an unexpected result.</p>
      </div>

      <h2>What to Show — CoModeler</h2>
      <p>The highest-impact CoModeler demos for prospects are in this order:</p>

      <div class="step">
        <div class="step-badge">1</div>
        <div class="step-content">
          <strong>Documentation generation</strong> — This is the strongest wow moment. Pick a module with 15–20 line items. Ask CoModeler to generate a line item dictionary. Show the output populating in real-time. Then show the export. Say: "This used to take your model builder 2–3 days. This took 90 seconds."
        </div>
      </div>
      <div class="step">
        <div class="step-badge">2</div>
        <div class="step-content">
          <strong>Bulk rename</strong> — Show renaming all line items in a module to a naming convention in a single prompt. Business value: "Your legacy models don't follow naming standards. CoModeler can standardize them in minutes, not days."
        </div>
      </div>
      <div class="step">
        <div class="step-badge">3</div>
        <div class="step-content">
          <strong>Model health check</strong> — Show the health check output. Prospects love seeing issues identified automatically. Frame it as: "This is your audit assistant — finds what a human would miss."
        </div>
      </div>

      <div class="callout-warning">
        <span class="callout-label">⚠️ Do NOT Demo Live</span>
        <p>Do not attempt to build a new model from scratch in a live demo. The time-to-response is unpredictable (3–10+ minutes for complex tasks) and the output quality varies. Use pre-recorded segments or a pre-built model that you can show results from.</p>
      </div>

      <h2>What to Show — Custom Analyst</h2>
      <div class="step">
        <div class="step-badge">1</div>
        <div class="step-content">
          <strong>Natural language query → number</strong> — Ask: "What is the forecast revenue for [Region] in [Month]?" Show the answer appear with a source link. Click the source link to show the data origin. This is the transparency differentiator.
        </div>
      </div>
      <div class="step">
        <div class="step-badge">2</div>
        <div class="step-content">
          <strong>Time series visualization</strong> — Ask a question that spans months: "Show me forecast revenue for the past 12 months." The analyst auto-generates a line chart. No configuration needed — it just does it.
        </div>
      </div>
      <div class="step">
        <div class="step-badge">3</div>
        <div class="step-content">
          <strong>Out-of-scope question handling</strong> — Ask a question that's outside the configured scope. Show the analyst saying "I can't answer that." This is a <em>feature</em>, not a failure. Say: "This is how we prevent hallucinations — the system is honest about what it doesn't know."
        </div>
      </div>

      <h2>Demo Order</h2>
      <p>Recommended sequence for a 20-minute AI demo:</p>
      <ol>
        <li>1 min — Context setting: "Anaplan AI as of today" (use the roadmap snapshot)</li>
        <li>3 min — CoModeler: documentation generation demo</li>
        <li>2 min — CoModeler: bulk rename or health check</li>
        <li>3 min — Agent Studio: show the admin layer (30 seconds each: workspace config, Analysts list)</li>
        <li>5 min — Custom Analyst: live query demo (3 questions, 1 out-of-scope)</li>
        <li>3 min — "What's coming" (H2 2026 roadmap items)</li>
        <li>3 min — Q&amp;A buffer</li>
      </ol>

      <h2>Anticipate These Questions</h2>
      """ + table(
    ["Question", "Answer"],
    [
        ["Can it fix bugs in our existing model?", "Not directly. It can document and identify issues. For fixes, the pattern is: build a corrected version of the module alongside the original, validate, then replace."],
        ["Will it hallucinate?", "CoModeler can make mistakes — always review output. Custom Analyst is designed not to hallucinate: if it can't answer, it says so. Show the out-of-scope demo."],
        ["Is our data secure?", "Custom Analyst runs queries as the logged-in user — their security filters apply. CoModeler runs inside the model with model-level permissions. No data leaves Anaplan."],
        ["Does it work with our app (Polaris/classic)?", "CoModeler works with both Polaris and classic models, but currently cannot distinguish between them without your guidance. Tell it which type it's working with."],
        ["When is the Claude upgrade?", "Targeted H2 2026. No reconfiguration expected — the abstraction layer stays Anaplan-side."],
        ["Can it build a full application?", "Building a full application end-to-end is out of scope. It excels at targeted tasks: modules, documentation, bulk edits. An application has too many dependencies and business decisions that require human judgment."],
    ]
) + """

      <h2>Handling "What Can't It Do?"</h2>
      <p>This question will come up. Answer it directly — don't dodge it. Prospects respect honest limitation conversations more than evasion.</p>

      <div class="callout-note">
        <span class="callout-label">📋 Suggested Answer</span>
        <p>"Great question — here's what it can't do today: it doesn't touch UX, workflows, or ALM. It can't import data — it can set up the import, but you hit run. It can't work on deployed models. For Custom Analyst, it's limited to the data sources you explicitly configure — it won't go looking through your whole tenant. And the context window is about five interactions per conversation. These are real constraints, and our team tracks the roadmap closely to know when each one changes."</p>
      </div>
"""

# ─── 06-limitations.html ───
LIMITS_BODY = """
      <p>Quick-reference card for customer conversations. Keep this page open during calls. Last updated: <strong>April 2, 2026</strong> (Leo Nunes onboarding session).</p>

      <div class="callout-important">
        <span class="callout-label">📌 Freeze Date</span>
        <p>This page reflects the GA state as of April 2, 2026. Do not extrapolate to roadmap items without checking the Roadmap Snapshot page.</p>
      </div>

      <h2>CoModeler Limitations</h2>
      """ + table(
    ["Limitation", "Detail", "Workaround"],
    [
        ["Deployed models only — blocked", "CoModeler only works on standard (non-deployed) models.", "Confirm model status before demo or workshop."],
        ["No UX capabilities", "Cannot build, modify, or view pages, dashboards, or grids.", "Manual UX work required after model build."],
        ["No ALM", "Cannot push changes through Application Lifecycle Management.", "ALM pipeline remains fully manual."],
        ["No user / tenant management", "Completely out of scope.", "N/A"],
        ["No calendar / time range changes", "Cannot modify time settings on a model.", "Manual change required in model settings."],
        ["Cannot execute data imports", "Can set up the import action; cannot run it.", "Trigger import manually after CoModeler sets it up."],
        ["No bulk copy actions", "Cannot create or manage action sets.", "Manual action creation."],
        ["Poor at counting / math in context", "Unreliable for aggregation questions within the chat.", "Run calculations in the model directly."],
        ["No cross-session memory", "Conversation history is not saved. Each session starts fresh.", "Save prompts externally. Download conversation transcripts."],
        ["Context window ~5 interactions", "Beyond ~5 follow-ups, CoModeler loses earlier context.", "Start a new conversation for new tasks."],
        ["Cannot distinguish app types", "Does not know if a model is Polaris, classic, or custom-built.", "Tell it explicitly in your prompt."],
        ["CSV upload only (today)", "File upload is CSV only — no Excel, no JSON.", "Convert to CSV before uploading a spec file."],
        ["No Model Optimizer (yet)", "Can suggest formula improvements; cannot apply them.", "Apply suggestions manually. Roadmap: H2 2026."],
        ["LLM: ChatGPT 4.0", "Current model. Claude upgrade targeted H2 2026.", "No action needed; reconfiguration not expected."],
    ]
) + """

      <h2>Custom Analyst Limitations</h2>
      """ + table(
    ["Limitation", "Detail", "Workaround"],
    [
        ["Scope is configuration-bound", "Only answers questions about modules/line items you explicitly configured.", "Design the configuration scope carefully with the business users."],
        ["No cross-analyst queries", "Analysts cannot call each other or share context.", "Configure a broader single analyst if cross-domain queries are needed."],
        ["Context window ~5 interactions", "Conversation context degrades after ~5 follow-ups.", "Start a new conversation for each distinct question thread."],
        ["No conversation history saved", "Sessions do not persist.", "Users must re-ask questions each session."],
        ["Visualizations not configurable", "Chart type is auto-selected (time → line, rank → bar). Cannot override.", "Accept auto-visualization or export to custom charts."],
        ["No external API access", "Cannot be embedded in external applications or triggered programmatically.", "Roadmap item."],
        ["Semantic quality = answer quality", "Poor line item descriptions produce poor answers.", "Invest in good semantic descriptions. Use CoModeler + ChatGPT enrichment workflow."],
    ]
) + """

      <h2>Agent Studio Limitations</h2>
      """ + table(
    ["Limitation", "Detail"],
    [
        ["Workspace-level CoModeler control only", "Cannot enable CoModeler at user level — it's all users in an enabled workspace."],
        ["No external agent import (yet)", "Cannot bring third-party agents into Agent Studio. Roadmap."],
        ["Agents do not communicate", "Finance Analyst, Sales Analyst, CoModeler — no cross-agent queries or handoffs."],
        ["No workflow agents (yet)", "Future agents will handle 'why is my revenue low?' type workflow questions. Not yet GA."],
    ]
)

# ─── 07-roadmap.html ───
ROADMAP_BODY = """
      <p>Frozen as of <strong>April 2, 2026</strong> — Leo Nunes onboarding session. Use this table to anchor customer conversations without over-promising. When in doubt, use the words "targeted" and "H2 2026" rather than specific dates.</p>

      <div class="callout-warning">
        <span class="callout-label">⚠️ Anaplan Date Convention</span>
        <p>"H2 2026" in Anaplan roadmap language should be treated as a range of Q3 2026 through January 2027. As Leo said on the call: "H2 2026 in Anaplan means 31st of December, which might as well be January 31st." Plan accordingly and do not commit customers to specific dates.</p>
      </div>

      <h2>GA Today (April 2026)</h2>
      """ + table(
    ["Product / Feature", "Description", "Notes"],
    [
        ["CoModeler", "AI model-building assistant inside Anaplan models", "Based on ChatGPT 4.0. GA."],
        ["Agent Studio", "Admin control plane for all AI products", "Tenant-level management. GA."],
        ["Custom Analyst", "Configurable conversational AI for end users", "GA. Requires AI Admin config."],
        ["Anaplan Analysts (Finance, WFP, SC, Sales)", "Pre-built function-specific analysts", "GA. Pre-configured by Anaplan."],
        ["Forecaster (PlanIQ)", "Statistical forecasting engine", "GA. Been available since 2019."],
        ["Optimizer", "ML-based optimization solver", "GA since 2018."],
        ["Syrup (Supply Chain Demand Planning)", "Demand planning for Apparel — baked into SC apps", "GA via acquisition."],
    ]
) + """

      <h2>H2 2026 Roadmap (Targeted — Not Committed)</h2>
      """ + table(
    ["Feature", "Product", "What It Does", "Current State"],
    [
        ["LLM Upgrade: ChatGPT 4.0 → Claude", "CoModeler", "Smarter base model, better app-type awareness, new training data ingestion", "Targeted H2 2026"],
        ["Persistent Prompt Notepad", "CoModeler", "Save and reuse prompts inside CoModeler — no more external prompt libraries", "Roadmap"],
        ["Model Optimizer", "CoModeler", "Suggest AND apply formula improvements automatically", "Roadmap — currently suggest only"],
        ["LLM change (OpenAI → Claude?)", "Custom Analyst", "Possible, unconfirmed. If it happens, no reconfiguration expected.", "Unconfirmed — Leo flagged uncertainty"],
        ["Anomaly Detector", "ADO / Agent Studio", "Automatic detection of data quality and anomaly issues", "Roadmap"],
        ["Data Quality Agent", "ADO / Agent Studio", "Proactive data health monitoring", "Roadmap"],
        ["Workflow Agents", "Agent Studio", "Answer questions like 'why is my revenue low?' and trigger workflows", "Roadmap — not GA"],
        ["Cross-agent communication", "Agent Studio", "Finance Analyst can query Sales Analyst, etc.", "Roadmap — agents currently isolated"],
        ["External agent import", "Agent Studio", "Bring third-party LLM agents into the Agent Studio ecosystem", "Roadmap"],
        ["ML APIs (bring-your-own model)", "Forecaster", "Plug custom ML models into Forecaster and other Anaplan apps", "Roadmap — not released"],
        ["CoModeler file type expansion", "CoModeler", "Support Excel, JSON beyond CSV for spec file uploads", "Roadmap"],
    ]
) + """

      <h2>How to Use This With Customers</h2>
      <ul>
        <li><strong>Do:</strong> Share the "GA Today" table confidently. Everything in that table is shipped and available.</li>
        <li><strong>Do:</strong> Reference "H2 2026" items as things on the roadmap Anaplan has announced publicly.</li>
        <li><strong>Don't:</strong> Promise specific dates. Use "targeted" or "on the roadmap for second half of 2026."</li>
        <li><strong>Don't:</strong> Present roadmap items in demos as if they're available today. Leo flagged that internal Anaplan decks sometimes incorrectly mark roadmap features as Phase 1.</li>
        <li><strong>Do:</strong> Use the ML APIs note specifically — if a customer asks about bring-your-own model, the answer is "roadmap only, not yet GA as of April 2026."</li>
      </ul>
"""

# ─── 08-partner-enablement.html ───
PARTNER_BODY = """
      <div class="screenshot-wrap">
        <img src="./img/ss-0480.jpg" alt="Enablement Blueprint matrix from Leo's session" class="screenshot">
        <p class="screenshot-caption">Custom Analyst with Agent Studio Enablement Blueprint — partner outcomes and content resources</p>
      </div>

      <h2>Seismic Enablement Blueprint</h2>
      <p>All AI enablement materials are published on Seismic. The enablement blueprint is on the Seismic splash page.</p>
      <ul>
        <li><strong>Access:</strong> Log into Seismic. AI enablement blueprint is on the home splash page.</li>
        <li><strong>No access?</strong> Submit a request through the Partner Portal — Seismic access is provisioned within 1–2 business days.</li>
        <li><strong>Important:</strong> Always use the Seismic links rather than the SharePoint folder Leo shared during the session. Leo mentioned he will be cleaning up and possibly deleting the SharePoint folder.</li>
      </ul>

      <h3>What's in the Blueprint</h3>
      """ + table(
    ["Audience", "Content", "Format"],
    [
        ["Sales", "Basic AI overview (15 min), pitch decks, onboarding deck, demo recording", "Video + slides"],
        ["Pre-Sales / SC", "Pre-sales demo recording, how to run CoModeler lab with customers", "Video (recorded session)"],
        ["Technical", "Full model building workshop (Academy), CoModeler lab guide, Custom Analyst config workshop", "Academy course + workshop"],
        ["All", "Enablement blueprint overview, current deck (April 2026)", "Slides"],
    ]
) + """

      <h2>Academy Courses</h2>
      <ul>
        <li><strong>CoModeler Workshop</strong> — Full model building lab. Available on Anaplan Academy. Recommended for TCs and SAs before customer delivery.</li>
        <li><strong>Custom Analyst Configuration</strong> — Step-by-step configuration course. Available on Academy.</li>
        <li><strong>Note from Leo:</strong> If you've already completed the Academy course, there's no need to repeat the live technical workshop — the content is the same.</li>
      </ul>

      <h2>Tenant Provisioning Checklist</h2>
      <ul class="checklist">
        <li>Partner tenant is entitled for AI (CoModeler + Agent Studio) — confirm with your Anaplan Partner Success Director</li>
        <li>Tenant admin has assigned AI Admin role to at least one user per workspace</li>
        <li>CoModeler is enabled for at least one workspace in Agent Studio</li>
        <li>Target models are standard (non-deployed) models</li>
        <li>All practitioners have Seismic access (verify before running a workshop)</li>
        <li>All practitioners have Academy access</li>
      </ul>

      <h2>Demo Environment Request</h2>
      <p>Anaplan maintains a demo AI copy that can be used for customer demos and internal practice. To request access:</p>
      <ul>
        <li>Contact your Anaplan Partner Success Director (Ben / Leo's counterparts)</li>
        <li>Leo mentioned during the session: "We need to check if they were giving access to that AI demo copy. If not, we need to copy this over to them. Please add me to the workspace and I'm happy to copy it."</li>
        <li>Reference the April 2, 2026 session when making the request</li>
      </ul>

      <h2>Token Guidance</h2>
      <p>As of April 2, 2026, partner tokens are <strong>not being counted</strong>. The product team confirmed this during the session. Use this window to:</p>
      <ul>
        <li>Run all workshop labs without cost concern</li>
        <li>Build your prompt library extensively</li>
        <li>Practice Custom Analyst configuration iterations</li>
        <li>Generate documentation from real models to establish quality baselines</li>
      </ul>

      <div class="screenshot-wrap">
        <img src="./img/ss-2100.jpg" alt="SharePoint folder with CoModeler workshop materials and prompt library" class="screenshot">
        <p class="screenshot-caption">Leo's shared folder — CoModeler workshop materials, prompt library CSV, and session recordings (access via Seismic blueprint, not SharePoint)</p>
      </div>

      <div class="callout-warning">
        <span class="callout-label">⚠️ Monitor for Changes</span>
        <p>Token counting will likely begin at some point. When it does, guidance on token budgets for customer deployments will come through the partner channel. Watch your Seismic blueprint for updates.</p>
      </div>

      <h2>Key Contacts</h2>
      """ + table(
    ["Role", "Person", "Scope"],
    [
        ["Partner Success Director (AI)", "Leo Nunes", "AI enablement, pre-sales support, workshop coordination"],
        ["Partner Success Director", "Ben (last name not provided in session)", "Overall partner relationship, coordination"],
        ["Partner Coordinators", "Mackenzie, Paul", "AI admin provisioning, tenant access coordination"],
        ["Escalation", "Email Leo directly", "Any questions that can't be answered async — Leo committed to responding or taking to experts"],
    ]
) + """

      <div class="callout-note">
        <span class="callout-label">📝 Follow-Up Process</span>
        <p>Leo's invitation: "Send all and any questions over email, and we'll be happy to help you until we organize some sort of weekly or bi-weekly catch-ups." Use this channel for anything not covered in this guide.</p>
      </div>
"""

# ─── 09-qanda.html ───
QANDA_BODY = """
      <p>All questions from Leo Nunes' April 2, 2026 AI Enablement Onboarding Session. Organized by topic. Leo's answers are verbatim or closely paraphrased.</p>

      <h2>Tenant Access &amp; Provisioning</h2>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> To get the AI Admin setting, does it need to be in our primary workspace, or can we as partners be assigned the AI Admin role in our clients' workspaces?</p>
        <p><strong>A:</strong> You can be assigned the AI Admin role on the client's workspace — as long as the partner has a licensed AI. The customer needs to have licensed AI. This is different from the Integration Admin role, which only works if it's your home tenant. For AI Admin, you can be assigned and operate on the client's workspace.</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> Why can't we see CoModeler in customer tenants today?</p>
        <p><strong>A:</strong> This is by design. Anaplan wants the customers to buy CoModeler. In an ideal situation, you'd be working with a customer who has purchased CoModeler and you can leverage it there. Today you'll only see it inside Carter's (partner) own tenant.</p>
      </div>

      <hr>
      <h2>CoModeler Capabilities</h2>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> If a client had CoModeler, could they go in when a bug comes up — say a user tried to input a driver but it's not flowing through to the income statement — could it identify where that is or does it need specific directions?</p>
        <p><strong>A:</strong> CoModeler will not efficiently fix a formula. A better pattern: "Look at module REV-01. Build module REV-02 similar to REV-01 but with X, Y, Z changes." If CoModeler picked up what was wrong, it might say "this line item might not be optimized" — but it won't fix it by itself.</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> Is CoModeler more for trained model builders rather than newer builders?</p>
        <p><strong>A:</strong> Both, but differently. Expert model builders love it for bulk tasks — rename all line items, create list hierarchies 50 levels deep with sample items, or rename all line items on a module to a naming convention. The boring stuff is where they see the biggest value. For less experienced builders, it's more like an intelligent assistant — "propose how to start building something," "how would you design this?" For new model builders, think Level 3 training: instead of designing from scratch, ask CoModeler to propose a design and iterate from there.</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> Can CoModeler mass-change line item references in a formula — from Line Item One to Module, Line Item Two?</p>
        <p><strong>A:</strong> Leo flagged this as uncertain and said he would check with colleagues. No confirmed answer was provided in the session. Follow up with Leo via email for confirmation.</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> How long does it take CoModeler to build something like a supply chain model from a prompt?</p>
        <p><strong>A:</strong> Variable and inconsistent. In the Academy exercise, results have ranged from building modules + line items + populating formulas in one pass to stopping after step one and requiring follow-up prompts. Rough estimate: 5 minutes for CoModeler to generate a build plan after your prompt, then another 5–10 minutes to execute. Use multiple tabs while waiting — open a second CoModeler tab to work on a different module in parallel.</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> When CoModeler is thinking on a large task, does it lock the model for other users?</p>
        <p><strong>A:</strong> It depends on the task. If CoModeler is working on a specific module and a colleague is working on a different module, it's similar to co-authoring — both can work simultaneously. As with the classic Anaplan multi-builder situation, complications arise if multiple builders work on the same module at the same time. The same principle applies with CoModeler.</p>
      </div>

      <hr>
      <h2>Custom Analyst &amp; Agent Studio</h2>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> When Anaplan transitions from OpenAI to Claude for CoModeler, does that mean we need to retrain the agents? Will the dataset translate automatically?</p>
        <p><strong>A:</strong> Leo confirmed: OpenAI → Claude for CoModeler. Not confirmed for Custom Analyst. For reconfiguration: he does not expect partners to need to rewrite analyst configurations when the LLM changes. The reason: the abstraction layer is all Anaplan-side — the modules, line items, semantic descriptions, and configured questions live in Anaplan. The LLM just reads that configuration. A new LLM would be trained to read it the same way.</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> When is the OpenAI to Claude change happening?</p>
        <p><strong>A:</strong> "Second half this year" — which in Anaplan means treat it as December 31, 2026. Could also be January 2027. Do not commit customers to a date. Leo's exact words: "H2 2026 in Anaplan means 31st of December, which might as well be 31st of January 2027."</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> Does Custom Analyst understand synonyms? If a user asks a question not aligned with the exact wording it was trained on, will it re-ask or figure it out?</p>
        <p><strong>A:</strong> It does understand synonyms, and there are better and worse ways to configure for this. "Revenue" is too generic — "total sales revenue" is better because it characterizes the concept. Better semantics produce better answers. Recommendation: start with 5–10 questions, then refine based on how business users naturally ask. Use ChatGPT or Gemini to enrich the semantic descriptions further before loading them into the analyst.</p>
      </div>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> Are the prompts that users give to Custom Analyst archived or saved? Does it lose context like ChatGPT does?</p>
        <p><strong>A:</strong> No, conversation history is not saved. Context is maintained within a conversation for about 5 interactions — both CoModeler and Custom Analyst. Beyond that, context is likely to be lost. If either goes down a hallucination route, there is no recovering within that conversation — start a new one. Leo's recommendation: keep interactions to 5, then start fresh.</p>
      </div>

      <hr>
      <h2>Next Steps &amp; Logistics</h2>

      <div class="callout-note">
        <span class="callout-label">Q</span>
        <p><strong>Q:</strong> Can you send us the recording and the deck so we can share with those who couldn't make it?</p>
        <p><strong>A:</strong> The deck is already in the shared SharePoint folder. The recording will be shared by Ben. Note: Leo plans to clean up the SharePoint folder at some point — use Seismic links as the permanent reference.</p>
      </div>
"""

# ─── 10-facilitator.html ───
FACILITATOR_BODY = """
      <h2>About This Guide</h2>
      <p>This guide is for facilitators running the AI Enablement workshop with a partner cohort. It follows the April 2, 2026 session structure from Leo Nunes. All timing is approximate — adjust based on group engagement and Q&amp;A depth.</p>

      <h2>Setup Checklist</h2>
      <ul class="checklist">
        <li>All participants provisioned as AI Admins on partner tenant</li>
        <li>CoModeler enabled for at least one shared workspace in Agent Studio</li>
        <li>Anaplan model available (standard, non-deployed) with 10+ modules for demo</li>
        <li>Seismic blueprint accessible and links verified</li>
        <li>April 2, 2026 recording available for reference (confirm Ben cascaded to group)</li>
        <li>CoModeler prompt library CSV uploaded to SharePoint / shared folder</li>
        <li>Demo AI tenant copy available — coordinate with Leo/Ben if not yet provisioned</li>
        <li>Academy links verified and active for CoModeler course</li>
        <li>Screen sharing tested — browser with Anaplan open, CoModeler visible</li>
      </ul>

      <h2>Delivery Script</h2>

      <h3>Opening (5 min)</h3>
      <p><em>Script:</em> "Welcome, everyone. Today's session is the AI Enablement Onboarding and Kickoff. The goal is simple: get you started on Anaplan AI, point you to the enablement, introduce both AI products, and answer your questions. We'll get through the products in about 15 minutes each, check on tenant access, and finish with next steps. Feel free to ask questions as we go — I'll try to keep an eye on chat."</p>

      <div class="callout-tip">
        <span class="callout-label">💡 Facilitator Note</span>
        <p>Open by asking who has already used CoModeler. A show of hands tells you how to calibrate depth. If most have — go faster on basics, deeper on limitations and prompting. If few have — spend more time on the first demo.</p>
      </div>

      <h3>AI Journey (10 min)</h3>
      <p><em>Script:</em> "Before we dive into the products, let me give you context on how we got here. Anaplan's AI story starts in 2018 with Optimizer. [Walk through the timeline — 2018 Optimizer, 2019 PlanIQ, 2023 Syrup, late 2024 CoPlanet, 2025 CoModeler + Agent Studio GA.]"</p>
      <p><em>Key point to make:</em> "One important clarification before we start — the ML APIs, which would let customers bring their own machine learning models, are roadmap only. They are not GA. You might see them in some Anaplan decks without that roadmap label — that's our mistake internally, not yours to make with customers."</p>

      <h3>Tenant Provisioning Check (10 min)</h3>
      <p><em>Script:</em> "Let me show you how CoModeler and Agent Studio access works from the admin side — and we'll use this to check that everyone in the room has access."</p>
      <p><em>Steps:</em></p>
      <ol>
        <li>Open Anaplan → top-right dropdown → Administration → show "AI Admin" role assignment</li>
        <li>Open Agent Studio → CoModeler tab → show workspace enablement</li>
        <li>Ask participants: "Are you seeing CoModeler in your model? If not, raise your hand."</li>
        <li>Resolve access issues live or note for follow-up with Ben/Mackenzie/Paul</li>
      </ol>
      <p><em>Script after check:</em> "Remember — today you'll only see CoModeler inside Carter's (partner) tenant, not on customer tenants. That's by design. Once a customer buys CoModeler, you can use it in their workspace."</p>

      <h3>CoModeler Overview (15 min)</h3>
      <p><em>Script:</em> "CoModeler is our intelligent AI builder. My favorite definition: a very junior model builder that knows a lot. It knows Anaplan. It knows business context. But you have to watch over what it does — it can make mistakes, and you have to check the output."</p>
      <p><em>Demo points (in order):</em></p>
      <ol>
        <li>Show CoModeler opening in a model</li>
        <li>Run documentation generation — show line item dictionary populating</li>
        <li>Show the limitations (UX, ALM, deployed models) — be honest</li>
        <li>Mention spec file pattern and share that the prompt library is in the shared folder</li>
      </ol>
      <p><em>Q&amp;A buffer: 5 min</em></p>

      <div class="callout-tip">
        <span class="callout-label">💡 Facilitator Note</span>
        <p>The "5 interaction context window" and "no cross-session memory" points almost always generate questions. Prepare for: "So I have to redo everything each session?" Answer: "Yes — save your prompts externally and download conversation transcripts before closing. This is a roadmap item (persistent prompt notepad coming H2 2026)."</p>
      </div>

      <h3>Custom Analyst + Agent Studio (15 min)</h3>
      <p><em>Script:</em> "Custom Analyst is our conversational AI for end users — not model builders. A planner can ask 'What is the forecast revenue for North America in Q3 2026?' and get the answer directly, without filing a request with IT or the model builder team."</p>
      <p><em>Demo points (in order):</em></p>
      <ol>
        <li>Show Agent Studio → Analysts tab</li>
        <li>Open a configured Custom Analyst — show the data source configuration</li>
        <li>Run a live query — show the answer with source link</li>
        <li>Show a time series question generating a visualization automatically</li>
        <li>Run an out-of-scope question — show the "I can't answer that" response</li>
        <li>Highlight security: "Queries run as the logged-in user — their row-level security applies"</li>
      </ol>
      <p><em>Q&amp;A buffer: 5 min</em></p>

      <h3>Next Steps (5 min)</h3>
      <p><em>Script:</em> "Before we wrap — a few things to do before our next touchpoint. First: complete the Enablement Blueprint on Seismic. If you don't have Seismic access, submit a Partner Portal request. Second: the technical workshop. I'm away next week, but I'm happy to run a live workshop — coordinate with Ben. Third: check your Academy access and start the CoModeler course if you haven't already. And send any questions over email — I'll respond or route them to the right person."</p>

      <h2>Timing Guide</h2>
      """ + table(
    ["Section", "Time", "Cumulative"],
    [
        ["Opening + intro", "5 min", "0:05"],
        ["AI journey timeline", "10 min", "0:15"],
        ["Tenant provisioning check", "10 min", "0:25"],
        ["CoModeler overview + demo", "15 min", "0:40"],
        ["CoModeler Q&A", "5 min", "0:45"],
        ["Agent Studio + Custom Analyst overview + demo", "15 min", "1:00"],
        ["Custom Analyst Q&A", "5 min", "1:05"],
        ["Next steps + wrap", "5 min", "1:10"],
        ["Buffer", "10 min", "1:20"],
    ]
) + """

      <h2>Debrief Answer Keys</h2>

      <h3>Lab 2A — First Conversation</h3>
      <ul>
        <li><strong>Response time:</strong> Expect 30–90 seconds for model overview. Line item dictionary can take 2–5 minutes for large modules.</li>
        <li><strong>Quality check:</strong> Descriptions should reflect business context. Hallucination signs: circular definitions, invented formula references, generic descriptions like "this line item stores data."</li>
        <li><strong>Common issue:</strong> CoModeler picks a module that's simple (few line items) rather than the most complex. If this happens, explicitly name the module in the follow-up prompt.</li>
      </ul>

      <h3>Lab 2B — Spec File Build</h3>
      <ul>
        <li><strong>Common failures:</strong> Dimension columns not in the right format (CoModeler expects the list name as it exists in the model). If the list doesn't exist, CoModeler will either create it or fail silently.</li>
        <li><strong>Good output indicator:</strong> Module appears in the model with correct dimensions and all line items visible. Description notes appear on hover.</li>
        <li><strong>Most common variation:</strong> CoModeler creates the module but stops before adding descriptions. Prompt: "Now add description notes to each line item in [MODULE NAME]."</li>
      </ul>

      <h3>Lab 2C — Documentation &amp; Health Check</h3>
      <ul>
        <li><strong>Health check false positives:</strong> CoModeler frequently flags modules as "no downstream references" when those modules are actually referenced via saved views or exports. Always verify manually before acting on health check results.</li>
        <li><strong>Documentation quality:</strong> Best when the model has good naming conventions. Poor names (REV01, TEMP, TEST) produce poor descriptions.</li>
        <li><strong>Manual enrichment benchmark:</strong> A 50-module model would take 1–2 weeks of manual documentation. CoModeler produces a first draft in 20–30 minutes. Quality gap: ~20–30% — requires human review and correction.</li>
      </ul>

      <h3>Lab 3A — Explore Agent Studio</h3>
      <ul>
        <li><strong>Common issue:</strong> Participant doesn't see Agent Studio in dropdown. Resolution: Tenant admin has not assigned the AI Admin role. Coordinate with Mackenzie/Paul.</li>
        <li><strong>Expected finding:</strong> Pre-built analysts for Finance, WFP, SC, Sales. Each has 10–30 pre-configured line items with Anaplan-written semantic descriptions.</li>
      </ul>

      <h3>Lab 3B — Configure a Custom Analyst</h3>
      <ul>
        <li><strong>Most impactful change for answer quality:</strong> Improving the AI Context field. A vague context like "FP&amp;A model" produces worse results than "NovaTrend consumer goods FP&amp;A model covering regional and product-level revenue forecast and actuals for North America, EMEA, LATAM, and APAC."</li>
        <li><strong>Out-of-scope response:</strong> Should say something like "I don't have access to that information" or "That question is outside my current scope." If it attempts to answer with made-up data, the semantic descriptions are too vague — tighten them.</li>
        <li><strong>Visualization check:</strong> A time-series question (last 12 months) should auto-generate a line chart. If it produces just a number, the time dimension was not included in the configured line items.</li>
      </ul>
"""

# ──────────────────────────────────────────────
# WRITE ALL FILES
# ──────────────────────────────────────────────
PAGES = [
    ("index.html", "AI Enablement Lab Guide", "index.html",
     "AI Enablement Lab Guide",
     "Anaplan Partner Onboarding — CoModeler &amp; Agent Studio",
     ["April 2026", "Partner Onboarding", "CoModeler", "Agent Studio"],
     INDEX_BODY,
     None),

    ("01-overview.html", "Workshop Overview", "01-overview.html",
     "Workshop Overview",
     "Anaplan AI journey, GA vs roadmap, token usage, learning path",
     ["Overview", "AI Journey", "April 2026"],
     OVERVIEW_BODY,
     {"next": ("02-case-study.html", "Case Study")}),

    ("02-case-study.html", "Case Study — NovaTrend", "02-case-study.html",
     "Case Study: NovaTrend",
     "Fictional customer scenario for all labs",
     ["Case Study", "Lab Context"],
     CASE_STUDY_BODY,
     {"prev": ("01-overview.html", "Workshop Overview"),
      "next": ("03-comodeler.html", "CoModeler Deep-Dive")}),

    ("03-comodeler.html", "CoModeler Deep-Dive + Labs", "03-comodeler.html",
     "CoModeler Deep-Dive + Labs",
     "Capabilities, limitations, prompting best practices + Labs 2A, 2B, 2C",
     ["CoModeler", "AI Builder", "Labs 2A–2C", "60 min"],
     COMODELER_BODY,
     {"prev": ("02-case-study.html", "Case Study"),
      "next": ("04-agent-studio.html", "Agent Studio")}),

    ("04-agent-studio.html", "Agent Studio + Custom Analyst", "04-agent-studio.html",
     "Agent Studio + Custom Analyst",
     "Admin architecture, security model, configuration walkthrough + Labs 3A, 3B",
     ["Agent Studio", "Custom Analyst", "Labs 3A–3B", "40 min"],
     AGENT_STUDIO_BODY,
     {"prev": ("03-comodeler.html", "CoModeler Deep-Dive"),
      "next": ("05-presales-demo.html", "Pre-Sales Playbook")}),

    ("05-presales-demo.html", "Pre-Sales Demo Playbook", "05-presales-demo.html",
     "Pre-Sales Demo Playbook",
     "What to show, demo order, objections, limitations handling",
     ["Pre-Sales", "Demo", "Partner Reference"],
     PRESALES_BODY,
     {"prev": ("04-agent-studio.html", "Agent Studio"),
      "next": ("06-limitations.html", "Limitations Reference")}),

    ("06-limitations.html", "Limitations Quick Reference", "06-limitations.html",
     "Limitations &amp; Gotchas — Quick Reference",
     "CoModeler, Custom Analyst, Agent Studio limits as of April 2, 2026",
     ["Reference Card", "Limitations", "April 2026"],
     LIMITS_BODY,
     {"prev": ("05-presales-demo.html", "Pre-Sales Playbook"),
      "next": ("07-roadmap.html", "Roadmap Snapshot")}),

    ("07-roadmap.html", "Roadmap Snapshot", "07-roadmap.html",
     "Roadmap Snapshot — April 2, 2026",
     "GA today vs H2 2026 roadmap — frozen for partner reference",
     ["Roadmap", "Reference Card", "April 2026"],
     ROADMAP_BODY,
     {"prev": ("06-limitations.html", "Limitations Reference"),
      "next": ("08-partner-enablement.html", "Partner Enablement")}),

    ("08-partner-enablement.html", "Partner Enablement Reference", "08-partner-enablement.html",
     "Partner Enablement Reference",
     "Seismic blueprint, Academy courses, provisioning, demo env, key contacts",
     ["Partner", "Enablement", "Resources"],
     PARTNER_BODY,
     {"prev": ("07-roadmap.html", "Roadmap Snapshot"),
      "next": ("09-qanda.html", "Q&amp;A Reference")}),

    ("09-qanda.html", "Q&A Reference", "09-qanda.html",
     "Q&amp;A from the April 2, 2026 Session",
     "All real questions with Leo Nunes' answers — organized by topic",
     ["Q&amp;A", "Session Reference"],
     QANDA_BODY,
     {"prev": ("08-partner-enablement.html", "Partner Enablement"),
      "next": ("10-facilitator.html", "Facilitator Guide")}),

    ("10-facilitator.html", "Facilitator Guide", "10-facilitator.html",
     "Facilitator Guide",
     "Delivery script, timing, setup checklist, debrief answer keys",
     ["Facilitator", "Delivery", "Script"],
     FACILITATOR_BODY,
     {"prev": ("09-qanda.html", "Q&amp;A Reference")}),
]

for (filename, title, active, h1, subtitle, badges, body, pn) in PAGES:
    outpath = os.path.join(OUT, filename)
    html = page(title, active, h1, subtitle, badges, body, pn)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {filename}")

print(f"\nDone — {len(PAGES)} pages written to {OUT}")
