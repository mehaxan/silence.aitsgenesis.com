"""Write module MDX seed files"""
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"wrote {path}")

BASE = '/Users/bs01004/silence-website/src/content'

modules = {
    'workspace.mdx': """\
---
title: Workspace
tagline: Create, share and collaborate
description: A complete Google Workspace alternative — document editor, spreadsheets, file manager and team wiki all in one deeply integrated platform.
icon: fa-solid fa-folder-open
slug: workspace
order: 1
features:
  - title: Document Editor
    description: Real-time collaborative editing with comments, suggestions and version history.
    icon: fa-solid fa-file-lines
  - title: Spreadsheets
    description: Full-featured spreadsheet engine with formulas, pivot tables and charts.
    icon: fa-solid fa-table
  - title: File Manager
    description: Hierarchical folder structure with granular sharing, versioning and search.
    icon: fa-solid fa-folder-tree
  - title: Team Wiki
    description: Structured knowledge base with nested pages, templates and cross-linking.
    icon: fa-solid fa-book-open
replaces: ["Google Docs", "Google Sheets", "Google Drive", "Notion", "Confluence"]
---

## Getting started with Workspace

Workspace is the foundation of Silence — every file, document and piece of knowledge lives here, accessible to all other modules.
""",

    'communication.mdx': """\
---
title: Communication
tagline: Chat, email and video in one
description: Replace Slack, Gmail and Zoom with a single integrated communication hub — channels, direct messages, shared inbox, email and built-in video conferencing.
icon: fa-solid fa-comments
slug: communication
order: 2
features:
  - title: Channels & DMs
    description: Organised team communication with public/private channels and direct messages.
    icon: fa-solid fa-hashtag
  - title: Shared Inbox
    description: Manage team email collaboratively with assignments, statuses and canned responses.
    icon: fa-solid fa-inbox
  - title: Video Conferencing
    description: Built-in HD video meetings with screen sharing, recording and AI summaries.
    icon: fa-solid fa-video
  - title: AI Meeting Notes
    description: Automatically extract action items and decisions from video meeting transcripts.
    icon: fa-solid fa-robot
replaces: ["Slack", "Microsoft Teams", "Gmail", "Zoom", "Google Meet"]
---

## Getting started with Communication

Communication connects your team without the tab chaos. All context — files, tasks, CRM records — is available inline.
""",

    'projects.mdx': """\
---
title: Projects
tagline: Plan, track and ship together
description: The complete Jira and Monday.com replacement — Kanban boards, backlogs, sprints, Gantt charts, time tracking and agile reporting in one unified workspace.
icon: fa-solid fa-diagram-project
slug: projects
order: 3
features:
  - title: Kanban Boards
    description: Drag-and-drop visual boards with customisable columns, WIP limits and swimlanes.
    icon: fa-solid fa-table-columns
  - title: Sprints & Backlog
    description: Full agile sprint management with velocity charts and burndown reports.
    icon: fa-solid fa-arrows-spin
  - title: Gantt Charts
    description: Timeline views with dependency arrows, critical path and milestone markers.
    icon: fa-solid fa-chart-gantt
  - title: Time Tracking
    description: Log time against tasks and generate detailed reports for billing or planning.
    icon: fa-solid fa-clock
replaces: ["Jira", "Monday.com", "Asana", "Linear", "Trello"]
---

## Getting started with Projects

Create your first project from a template or from scratch. Import existing work from Jira or CSV.
""",

    'crm.mdx': """\
---
title: CRM
tagline: Close more deals, faster
description: Visual sales pipeline, contact and company management, email sequences, call logging and deep analytics — everything your team needs to grow revenue.
icon: fa-solid fa-handshake
slug: crm
order: 4
features:
  - title: Visual Pipeline
    description: Drag deals through customisable stages with probability weighting and forecasting.
    icon: fa-solid fa-filter
  - title: Contact Management
    description: Unified contact and company profiles enriched with communication and activity history.
    icon: fa-solid fa-address-card
  - title: Email Sequences
    description: Automated multi-step outreach sequences with AI-optimised send times.
    icon: fa-solid fa-envelope-open-text
  - title: Sales Analytics
    description: Revenue dashboards, conversion rates, rep performance and pipeline health.
    icon: fa-solid fa-chart-line
replaces: ["Salesforce", "HubSpot", "Pipedrive", "Zoho CRM"]
---

## Getting started with CRM

Import your contacts from CSV or connect your existing CRM for a zero-downtime migration.
""",

    'hr.mdx': """\
---
title: HR
tagline: Hire, onboard and retain talent
description: The complete HR platform — applicant tracking, onboarding workflows, time-off management, payroll engine and 360° performance reviews.
icon: fa-solid fa-users
slug: hr
order: 5
features:
  - title: Applicant Tracking
    description: Full recruitment funnel from job posting to offer letter with AI CV ranking.
    icon: fa-solid fa-magnifying-glass-chart
  - title: Onboarding Workflows
    description: Automated first-day checklists, document signing and equipment provisioning.
    icon: fa-solid fa-person-walking-dashed-line-arrow-right
  - title: Payroll Engine
    description: Automated gross-to-net payroll with tax compliance for EU and US jurisdictions.
    icon: fa-solid fa-money-check-dollar
  - title: Performance Reviews
    description: 360° feedback cycles, OKR tracking and development plans.
    icon: fa-solid fa-star-half-stroke
replaces: ["BambooHR", "Workday", "Personio", "Greenhouse"]
---

## Getting started with HR

Set up your HR module by importing your organisational structure and employee records from CSV or your existing HRIS.
""",

    'finance.mdx': """\
---
title: Finance
tagline: From invoicing to accounting
description: Create and send invoices, track expenses, manage budgets, run bank reconciliation and produce financial reports — with AI-assisted categorisation.
icon: fa-solid fa-file-invoice-dollar
slug: finance
order: 6
features:
  - title: Invoicing & Billing
    description: Create polished invoices, send automatically and track payment status in real time.
    icon: fa-solid fa-receipt
  - title: Expense Management
    description: Capture receipts on mobile, auto-categorise with AI and generate expense reports.
    icon: fa-solid fa-wallet
  - title: Bank Reconciliation
    description: Connect your bank feeds and auto-match transactions with a click.
    icon: fa-solid fa-building-columns
  - title: Financial Reporting
    description: P&L, balance sheet, cash flow and custom reports at any date range.
    icon: fa-solid fa-chart-pie
replaces: ["QuickBooks", "Xero", "Sage", "FreshBooks"]
---

## Getting started with Finance

Connect your bank account, set up your chart of accounts, and you're ready to invoice your first customer.
""",

    'operations.mdx': """\
---
title: Operations
tagline: Inventory and procurement
description: Manage stock levels, purchase orders, supplier relationships, warehouse operations and delivery tracking in one unified operations suite.
icon: fa-solid fa-boxes-stacking
slug: operations
order: 7
features:
  - title: Inventory Management
    description: Track stock across multiple locations with real-time level syncing and low-stock alerts.
    icon: fa-solid fa-warehouse
  - title: Purchase Orders
    description: Create, approve and track POs with automated supplier notifications.
    icon: fa-solid fa-file-invoice
  - title: Supplier Management
    description: Centralised supplier directory with scorecards, contracts and SLA tracking.
    icon: fa-solid fa-truck
  - title: Delivery Tracking
    description: Track inbound and outbound shipments with carrier integration and exception alerts.
    icon: fa-solid fa-location-dot
replaces: ["SAP (basic)", "Oracle (basic)", "NetSuite (basic)", "TradeGecko"]
---

## Getting started with Operations

Import your product catalogue and current stock levels to begin tracking inventory immediately.
""",

    'ai-automation.mdx': """\
---
title: AI & Automation
tagline: Automate anything
description: Build complex automations with a visual drag-and-drop builder, deploy RPA bots to automate web and desktop tasks, and use AI to predict, classify and extract across every module.
icon: fa-solid fa-robot
slug: ai-automation
order: 8
features:
  - title: Visual Workflow Builder
    description: Drag-and-drop automation builder with 200+ action steps, branches and loops.
    icon: fa-solid fa-circle-nodes
  - title: RPA Bots
    description: Automate repetitive browser and desktop tasks with no-code bot recorder.
    icon: fa-solid fa-gears
  - title: Document Intelligence
    description: Extract structured data from invoices, contracts and forms with AI accuracy.
    icon: fa-solid fa-file-magnifying-glass
  - title: AI Predictions
    description: Forecast churn, sales win probability, stock runout and more across your data.
    icon: fa-solid fa-wand-magic-sparkles
replaces: ["Zapier", "Make (Integromat)", "UiPath", "Power Automate"]
---

## Getting started with AI & Automation

Start with a pre-built template from the automation library, or build your first workflow from a blank canvas.
""",

    'integrations.mdx': """\
---
title: Integrations Hub
tagline: Connect everything you rely on
description: 500+ pre-built connectors, a webhook engine, REST API, and native support for Zapier, Make and n8n — connect Silence to any external tool.
icon: fa-solid fa-plug
slug: integrations
order: 9
features:
  - title: 500+ Pre-built Connectors
    description: Production-ready connectors for Slack, Salesforce, SAP, M365, Google Workspace and more.
    icon: fa-solid fa-puzzle-piece
  - title: Webhook Engine
    description: Send and receive webhooks from any system with payload transformation support.
    icon: fa-solid fa-bolt
  - title: REST API
    description: Full REST API with OpenAPI spec, SDKs and API key management.
    icon: fa-solid fa-code
  - title: iPaaS Ready
    description: Official connectors for Zapier, Make and n8n for advanced automation.
    icon: fa-solid fa-share-nodes
replaces: ["Zapier (standalone)", "n8n", "Boomi", "Mulesoft (basic)"]
---

## Getting started with Integrations

Browse the integration catalogue, click Connect, and authenticate. Most integrations are live within minutes.
""",

    'admin.mdx': """\
---
title: Admin
tagline: Enterprise-grade control
description: Multi-tenancy, SSO (SAML 2.0 + OIDC), SCIM provisioning, granular RBAC and ABAC, audit logs, data residency and compliance tooling for IT and security teams.
icon: fa-solid fa-shield-halved
slug: admin
order: 10
features:
  - title: Multi-tenancy
    description: Fully isolated tenant environments with per-tenant branding, modules and configuration.
    icon: fa-solid fa-building-columns
  - title: Single Sign-On
    description: SAML 2.0 and OIDC integration with any IdP. SCIM for automated provisioning.
    icon: fa-solid fa-id-badge
  - title: Granular Permissions
    description: Role-based and attribute-based access control down to individual record level.
    icon: fa-solid fa-user-lock
  - title: Audit & Compliance
    description: Tamper-evident audit logs, data export, right-to-erasure workflows and DLP policies.
    icon: fa-solid fa-file-shield
replaces: ["Okta (partial)", "Azure AD (partial)", "Sailpoint (basic)"]
---

## Getting started with Admin

Admin is pre-configured with sensible defaults. Most enterprises start by connecting their Identity Provider for SSO, then customising roles and permissions.
""",
}

for filename, content in modules.items():
    write(f'{BASE}/modules/{filename}', content)

# ── Comparison seed files ────────────────────────────────────────────────────
comparisons = {
    'jira.mdx': """\
---
title: Silence vs Jira
competitor: Jira
competitorSlug: jira
description: See how Silence Projects compares to Jira — kanban, sprints, pricing, integrations and more.
publishedAt: "2026-01-01"
verdict: "Silence Projects matches Jira on core project management capabilities while adding CRM, Finance and HR in the same subscription — with no per-seat fees."
features:
  - name: Kanban boards
    silence: true
    competitor: true
  - name: Sprint planning & backlog
    silence: true
    competitor: true
  - name: Gantt charts
    silence: true
    competitor: false
    note: Paid add-on in Jira (Advanced Roadmaps)
  - name: Time tracking
    silence: true
    competitor: true
    note: Jira requires Tempo plugin
  - name: CRM built-in
    silence: true
    competitor: false
  - name: Finance module built-in
    silence: true
    competitor: false
  - name: Chat & communication built-in
    silence: true
    competitor: false
  - name: Per-seat pricing
    silence: false
    competitor: true
    note: Silence charges per-org, not per-seat
  - name: AI workflow automation
    silence: true
    competitor: false
  - name: On-premise / data residency
    silence: true
    competitor: true
---
""",

    'google-workspace.mdx': """\
---
title: Silence vs Google Workspace
competitor: Google Workspace
competitorSlug: google-workspace
description: How Silence compares to Google Workspace — docs, sheets, drive, email and meetings.
publishedAt: "2026-01-01"
verdict: "Silence covers everything Google Workspace does for productivity, and extends it with CRM, project management, HR, finance and AI automation — all in one platform."
features:
  - name: Document editor
    silence: true
    competitor: true
  - name: Spreadsheets
    silence: true
    competitor: true
  - name: File storage & sharing
    silence: true
    competitor: true
  - name: Video conferencing
    silence: true
    competitor: true
  - name: Team chat
    silence: true
    competitor: true
    note: Google Chat is basic vs Silence Communication
  - name: CRM
    silence: true
    competitor: false
  - name: Project management
    silence: true
    competitor: false
  - name: HR & payroll
    silence: true
    competitor: false
  - name: Finance & invoicing
    silence: true
    competitor: false
  - name: AI workflow automation
    silence: true
    competitor: false
    note: Google has AI features but no unified workflow engine
---
""",

    'microsoft-365.mdx': """\
---
title: Silence vs Microsoft 365
competitor: Microsoft 365
competitorSlug: microsoft-365
description: Silence vs Microsoft 365 — productivity, collaboration, project management and AI automation.
publishedAt: "2026-01-01"
verdict: "Microsoft 365 is the incumbent for document productivity. Silence matches its core capabilities and adds real project management, CRM, HR and finance without requiring a separate Dynamics or Project licence."
features:
  - name: Document editor (Word equiv.)
    silence: true
    competitor: true
  - name: Spreadsheets (Excel equiv.)
    silence: true
    competitor: true
  - name: Presentations (PowerPoint equiv.)
    silence: true
    competitor: false
    note: Silence does not yet have a presentations module
  - name: Email (Outlook equiv.)
    silence: true
    competitor: true
  - name: Team chat (Teams equiv.)
    silence: true
    competitor: true
  - name: Video conferencing
    silence: true
    competitor: true
  - name: Project management
    silence: true
    competitor: false
    note: Requires separate Microsoft Project licence
  - name: CRM
    silence: true
    competitor: false
    note: Requires separate Dynamics 365 licence
  - name: HR & payroll
    silence: true
    competitor: false
    note: Requires separate Dynamics HR licence
  - name: AI workflow automation
    silence: true
    competitor: false
    note: Power Automate available but separate learning curve
---
""",

    'monday.mdx': """\
---
title: Silence vs Monday.com
competitor: Monday.com
competitorSlug: monday
description: Silence Projects vs Monday.com — work management, automations, integrations and pricing.
publishedAt: "2026-01-01"
verdict: "Monday.com excels at visual work management. Silence matches it on boards and automations, and adds full project management (sprints, Gantt, backlogs) plus CRM, HR and finance in one subscription."
features:
  - name: Visual boards (Kanban equiv.)
    silence: true
    competitor: true
  - name: Sprint & backlog management
    silence: true
    competitor: false
    note: Monday lacks native agile sprint workflows
  - name: Gantt / timeline view
    silence: true
    competitor: true
    note: Monday timeline requires Standard plan or above
  - name: Built-in automations
    silence: true
    competitor: true
  - name: CRM module
    silence: true
    competitor: true
    note: Monday CRM is a board template, not a dedicated CRM
  - name: HR module
    silence: true
    competitor: false
  - name: Finance module
    silence: true
    competitor: false
  - name: Per-seat pricing
    silence: false
    competitor: true
---
""",

    'notion.mdx': """\
---
title: Silence vs Notion
competitor: Notion
competitorSlug: notion
description: Silence vs Notion — knowledge management, docs, project tracking, databases and AI.
publishedAt: "2026-01-01"
verdict: "Notion is a powerful knowledge and documents tool. Silence matches its wiki and document capabilities while adding fully-featured project management, CRM, HR and finance that Notion's database approach cannot match for operational complexity."
features:
  - name: Rich document editor
    silence: true
    competitor: true
  - name: Team wiki / knowledge base
    silence: true
    competitor: true
  - name: Database views (table, board, calendar)
    silence: true
    competitor: true
  - name: Full agile project management
    silence: true
    competitor: false
    note: Notion Projects is basic vs dedicated PM tools
  - name: CRM (dedicated module)
    silence: true
    competitor: false
  - name: HR & payroll
    silence: true
    competitor: false
  - name: Finance & invoicing
    silence: true
    competitor: false
  - name: AI writing assistant
    silence: true
    competitor: true
  - name: AI workflow automation
    silence: true
    competitor: false
---
""",
}

for filename, content in comparisons.items():
    write(f'{BASE}/comparisons/{filename}', content)

# ── Case study seed ──────────────────────────────────────────────────────────
write(f'{BASE}/case-studies/apex-logistics.mdx', """\
---
title: How Apex Logistics replaced 8 tools with Silence in 60 days
company: Apex Logistics
industry: Logistics & Supply Chain
description: A 1,200-person logistics firm consolidated 8 separate SaaS tools into Silence, cutting software costs by 40% and reducing invoice processing time by 75%.
publishedAt: "2026-01-20"
featured: true
results:
  - metric: Tools replaced
    value: "8 → 1"
  - metric: Cost reduction
    value: "40%"
  - metric: Invoice processing
    value: "75% faster"
  - metric: Onboarding time
    value: "60 days"
---

## The challenge

Apex Logistics was running Jira, Slack, Google Workspace, Salesforce, QuickBooks, BambooHR, and two custom-built internal tools. The integrations between them were fragile, the data was inconsistent, and the monthly software bill had reached six figures.

"We had three people whose full-time job was keeping our integrations running," said the CTO. "Every time one system updated its API, something broke."

## Why Silence

The Silence team ran a two-week proof-of-concept focused on the three modules Apex cared most about: Projects, Finance and CRM. The POC demonstrated that Silence could handle Apex's core workflows without customisation.

## The migration

The migration was completed in 60 days:

- **Week 1–2:** Data migration (Jira issues, Salesforce contacts, QuickBooks ledger)
- **Week 3–4:** Configuration and workflow setup
- **Week 5–6:** Pilot with 50 users
- **Week 7–8:** Full rollout to 1,200 users

## The results

Twelve months after go-live, Apex reported:

- Software costs down 40%
- Invoice processing time reduced by 75% (Document Intelligence)
- Zero integration outages (vs. an average of 4 per month previously)
- 3 integration-maintenance roles redeployed to product engineering
""")

# ── Docs seed files ──────────────────────────────────────────────────────────
write(f'{BASE}/docs/getting-started/introduction.mdx', """\
---
title: Introduction to Silence
description: What Silence is, how it is structured and how to navigate the platform.
module: getting-started
section: Overview
order: 1
---

Welcome to Silence — the AI-powered enterprise automation platform.

## What is Silence?

Silence is an all-in-one business platform that replaces the fragmented collection of SaaS tools most organisations rely on. It combines:

- **Workspace** — documents, spreadsheets and file storage
- **Communication** — chat, email and video
- **Projects** — tasks, boards and sprints
- **CRM** — contacts, pipeline and deals
- **HR** — recruitment, payroll and attendance
- **Finance** — invoicing and accounting
- **Operations** — inventory and procurement
- **AI & Automation** — workflows, RPA and document intelligence

All modules share a single data model, so a contact in CRM is the same record as a customer in Finance and an assignee in Projects.

## Navigating the platform

Use the left sidebar to switch between modules. The top bar shows your notifications, search and user settings.

## Next steps

- [Quick start guide](/docs/getting-started/quick-start)
- [Invite your team](/docs/admin/invite-users)
- [Connect your first integration](/docs/integrations/connect)
""")

write(f'{BASE}/docs/getting-started/quick-start.mdx', """\
---
title: Quick Start
description: Get your organisation up and running in Silence in under 30 minutes.
module: getting-started
section: Overview
order: 2
---

## Step 1: Set up your organisation

When you first log in, you'll be prompted to name your organisation and choose your primary modules. You can activate additional modules at any time from **Admin → Modules**.

## Step 2: Import your data

Go to **Admin → Data Import** to import from:

- **CSV / Excel** — for contacts, tasks, products and more
- **Google Workspace** — Drive files, Gmail contacts and Calendar events
- **Microsoft 365** — SharePoint files, Outlook contacts
- **Jira** — projects and issues
- **Salesforce** — contacts and opportunities

## Step 3: Invite your team

Navigate to **Admin → Users → Invite Users**. Enter email addresses, assign roles and send invites. Users will receive a welcome email with a one-click setup link.

## Step 4: Connect integrations

Go to **Integrations Hub** and connect the tools you still use externally (Slack, Stripe, GitHub, etc.).

## Step 5: Start working

You're ready. Browse the module documentation below for guides on each area of the platform.
""")

write(f'{BASE}/docs/projects/getting-started.mdx', """\
---
title: Getting Started with Projects
description: Create your first project, add tasks and set up a Kanban board in Silence Projects.
module: projects
section: Getting Started
order: 1
---

## Create a project

1. Click **Projects** in the left sidebar
2. Click **New Project**
3. Choose a template (Software, Marketing, Operations or Blank) or start from scratch
4. Give the project a name, description and set the default view (Board, List or Gantt)

## Add tasks

Tasks can be added from any view:

- **Board view** — click the **+** button at the top of any column
- **List view** — click **Add Task** at the bottom of the list
- **Quick entry** — press `T` anywhere in the platform

## Set up columns

In Board view, click **Manage Columns** to rename, reorder or add columns. Each column maps to a status in your workflow.

## Assign and set due dates

Open any task to add an assignee, due date, priority, labels and description. Tasks are instantly visible to all project members.
""")

print("\nAll content seed files written!")
