"""Write all marketing pages (features, modules, solutions, integrations, pricing, security, about, demo, contact, customers, blog, changelog, docs, legal, comparison)."""
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"wrote {path}")

BASE = '/Users/bs01004/silence-website/src'
PAGES = BASE + '/pages'
CONTENT = BASE + '/content'

# ── features.astro ──────────────────────────────────────────────────────────
write(f'{PAGES}/features.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';

const categories = [
  {
    label: 'AI & Automation',
    icon: 'fa-solid fa-robot',
    features: [
      { title: 'AI Workflow Builder', desc: 'Build complex automations visually with AI-suggested steps.' },
      { title: 'Document Intelligence', desc: 'Extract, classify and process documents with AI accuracy.' },
      { title: 'Smart Predictions', desc: 'Forecast trends and anomalies across every module.' },
      { title: 'RPA Bots', desc: 'Automate repetitive tasks across web and desktop apps.' },
    ],
  },
  {
    label: 'Collaboration',
    icon: 'fa-solid fa-people-group',
    features: [
      { title: 'Real-time Docs', desc: 'Co-edit documents, spreadsheets and presentations together.' },
      { title: 'Team Chat', desc: 'Channels, direct messages and threaded conversations.' },
      { title: 'Video Meetings', desc: 'Built-in video conferencing with recording and AI summaries.' },
      { title: 'Shared Inbox', desc: 'Manage team email collaboratively with assignments and statuses.' },
    ],
  },
  {
    label: 'Project & Work Management',
    icon: 'fa-solid fa-diagram-project',
    features: [
      { title: 'Kanban Boards', desc: 'Visual boards for agile and waterfall workflows.' },
      { title: 'Gantt Charts', desc: 'Timeline views with dependency management.' },
      { title: 'Sprints', desc: 'Plan, run and review sprints with velocity tracking.' },
      { title: 'Time Tracking', desc: 'Log and report on time across tasks and projects.' },
    ],
  },
  {
    label: 'Business Operations',
    icon: 'fa-solid fa-building',
    features: [
      { title: 'CRM & Sales Pipeline', desc: 'Manage contacts, deals and the full sales cycle.' },
      { title: 'Invoicing & Billing', desc: 'Create, send and track invoices with automated reminders.' },
      { title: 'HR & Payroll', desc: 'Onboard employees, run payroll and track attendance.' },
      { title: 'Inventory & Procurement', desc: 'Track stock, manage suppliers and approve purchase orders.' },
    ],
  },
  {
    label: 'Enterprise & Security',
    icon: 'fa-solid fa-shield-halved',
    features: [
      { title: 'Multi-tenant Architecture', desc: 'Fully isolated tenants with per-tenant customisation.' },
      { title: 'Single Sign-On (SSO)', desc: 'SAML 2.0 and OIDC integration with any Identity Provider.' },
      { title: 'Granular Permissions', desc: 'Role-based and attribute-based access control.' },
      { title: 'Audit Logs', desc: 'Complete, tamper-evident activity history for compliance.' },
    ],
  },
  {
    label: 'Integrations',
    icon: 'fa-solid fa-plug',
    features: [
      { title: '500+ Connectors', desc: 'Pre-built integrations with Slack, SAP, Salesforce and more.' },
      { title: 'Webhook Engine', desc: 'Send and receive webhooks to any external system.' },
      { title: 'REST API', desc: 'Full REST API for custom integrations and data access.' },
      { title: 'iPaaS Ready', desc: 'Native connectors for Zapier, Make and n8n.' },
    ],
  },
];
---

<MarketingLayout
  title="Features"
  description="Explore all the features that make Silence the most complete enterprise automation platform — AI workflows, project management, CRM, HR, finance and more."
>
  <!-- Hero -->
  <section class="relative bg-[#0A0A14] section-padding text-center" aria-label="Features hero">
    <div class="absolute inset-0 pointer-events-none" aria-hidden="true">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 h-[400px] w-[700px] rounded-full bg-violet-600/8 blur-[100px]"></div>
    </div>
    <div class="relative mx-auto max-w-3xl">
      <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Full feature overview</p>
      <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">Everything you need. Nothing you don't.</h1>
      <p class="text-slate-400 text-lg leading-relaxed">Silence is engineered to replace your entire tool stack — without compromise on depth or power.</p>
    </div>
  </section>

  <!-- Feature grid -->
  <section class="bg-[#0A0A14] pb-24 px-6 lg:px-24" aria-label="Feature categories">
    <div class="mx-auto max-w-7xl space-y-20">
      {categories.map((cat) => (
        <div>
          <div class="flex items-center gap-3 mb-8">
            <div class="h-10 w-10 rounded-xl bg-violet-500/10 flex items-center justify-center">
              <i class={cat.icon + ' text-violet-400'} aria-hidden="true"></i>
            </div>
            <h2 class="text-xl font-bold text-white">{cat.label}</h2>
          </div>
          <ul class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4" role="list">
            {cat.features.map((f) => (
              <li class="p-6 rounded-2xl border border-white/5 bg-white/[0.02] hover:bg-violet-500/5 hover:border-violet-500/20 transition-all duration-200">
                <h3 class="text-sm font-semibold text-white mb-2">{f.title}</h3>
                <p class="text-xs text-slate-500 leading-relaxed">{f.desc}</p>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  </section>

  <!-- CTA -->
  <section class="bg-[#0C0C1A] section-padding text-center">
    <div class="mx-auto max-w-2xl">
      <h2 class="text-3xl font-bold text-white mb-4">See every feature in action</h2>
      <p class="text-slate-400 mb-8">Book a live demo tailored to your team's use case.</p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="/demo" class="inline-flex items-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
          <i class="fa-solid fa-calendar-check" aria-hidden="true"></i> Request Demo
        </a>
        <a href="/contact" class="inline-flex items-center gap-2 px-8 py-3.5 text-sm font-semibold text-slate-300 rounded-xl border border-white/10 hover:bg-white/5 hover:text-white transition-all duration-200">
          Contact Sales
        </a>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── modules/index.astro ──────────────────────────────────────────────────────
write(f'{PAGES}/modules/index.astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';

const modules = [
  { slug: 'workspace', icon: 'fa-solid fa-folder-open', label: 'Workspace', tagline: 'Create, share and collaborate', desc: 'Full-featured document editor, spreadsheet and file manager — a complete Google Workspace alternative built into Silence.', replaces: ['Google Docs', 'Google Sheets', 'Google Drive', 'Notion'] },
  { slug: 'communication', icon: 'fa-solid fa-comments', label: 'Communication', tagline: 'Chat, email and video in one', desc: 'Channels, direct messages, shared inbox and built-in video conferencing — no more switching between Slack, Gmail and Zoom.', replaces: ['Slack', 'Gmail', 'Zoom', 'Outlook'] },
  { slug: 'projects', icon: 'fa-solid fa-diagram-project', label: 'Projects', tagline: 'Plan, track and ship together', desc: 'Boards, backlogs, sprints, Gantt charts and time tracking — the complete Jira and Monday.com replacement.', replaces: ['Jira', 'Monday.com', 'Asana', 'Linear'] },
  { slug: 'crm', icon: 'fa-solid fa-handshake', label: 'CRM', tagline: 'Close more deals, faster', desc: 'Visual pipeline, contact management, email sequences and sales analytics all in one place.', replaces: ['Salesforce', 'HubSpot', 'Pipedrive'] },
  { slug: 'hr', icon: 'fa-solid fa-users', label: 'HR', tagline: 'Hire, onboard and retain talent', desc: 'Applicant tracking, onboarding workflows, time-off management, payroll and performance reviews.', replaces: ['BambooHR', 'Workday', 'Personio'] },
  { slug: 'finance', icon: 'fa-solid fa-file-invoice-dollar', label: 'Finance', tagline: 'Invoicing to accounting', desc: 'Create invoices, track expenses, manage budgets and reconcile accounts — all with AI-assisted categorisation.', replaces: ['QuickBooks', 'Xero', 'Sage'] },
  { slug: 'operations', icon: 'fa-solid fa-boxes-stacking', label: 'Operations', tagline: 'Inventory and procurement', desc: 'Manage stock levels, purchase orders, supplier relationships and warehouse operations end-to-end.', replaces: ['SAP', 'Oracle', 'NetSuite'] },
  { slug: 'ai-automation', icon: 'fa-solid fa-robot', label: 'AI & Automation', tagline: 'Automate anything', desc: 'Visual workflow builder, RPA bots, document intelligence and AI-powered predictions across every module.', replaces: ['Zapier', 'Make', 'UiPath'] },
  { slug: 'integrations', icon: 'fa-solid fa-plug', label: 'Integrations Hub', tagline: '500+ connectors', desc: 'Connect Silence to any external system via pre-built connectors, webhooks and REST API.', replaces: ['Zapier', 'n8n', 'Boomi'] },
  { slug: 'admin', icon: 'fa-solid fa-shield-halved', label: 'Admin', tagline: 'Enterprise-grade control', desc: 'Multi-tenancy, SSO, granular permissions, audit logs and data residency policies for IT and compliance teams.', replaces: ['Okta (partial)', 'Azure AD (partial)'] },
];
---

<MarketingLayout title="Modules" description="Explore all Silence modules — Workspace, Communication, Projects, CRM, HR, Finance, Operations, AI Automation and more.">
  <section class="relative bg-[#0A0A14] section-padding text-center">
    <div class="relative mx-auto max-w-3xl mb-16">
      <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">All modules</p>
      <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">One platform. Ten powerful modules.</h1>
      <p class="text-slate-400 text-lg">Replace your entire tool stack with a single, deeply integrated platform.</p>
    </div>

    <ul class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 text-left mx-auto max-w-7xl" role="list">
      {modules.map((mod) => (
        <li>
          <a href={'/modules/' + mod.slug} class="group flex flex-col h-full p-8 rounded-2xl border border-white/5 bg-white/[0.02] hover:bg-violet-500/5 hover:border-violet-500/20 transition-all duration-200">
            <div class="flex items-center gap-3 mb-4">
              <div class="h-10 w-10 rounded-xl bg-violet-500/10 flex items-center justify-center group-hover:bg-violet-500/20 transition-colors">
                <i class={mod.icon + ' text-violet-400'} aria-hidden="true"></i>
              </div>
              <div>
                <h2 class="text-sm font-bold text-white">{mod.label}</h2>
                <p class="text-xs text-violet-400">{mod.tagline}</p>
              </div>
            </div>
            <p class="text-sm text-slate-400 leading-relaxed flex-1 mb-4">{mod.desc}</p>
            <div class="flex flex-wrap gap-1.5">
              {mod.replaces.map((r) => (
                <span class="text-xs px-2 py-0.5 rounded-full border border-white/10 text-slate-500">replaces {r}</span>
              ))}
            </div>
          </a>
        </li>
      ))}
    </ul>
  </section>
</MarketingLayout>
""")

# ── modules/[slug].astro ─────────────────────────────────────────────────────
write(f'{PAGES}/modules/[slug].astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const entries = await getCollection('modules');
  return entries.map((entry) => ({
    params: { slug: entry.data.slug },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await entry.render();
const mod = entry.data;
---

<MarketingLayout title={mod.title} description={mod.description}>
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="flex items-center gap-3 mb-6">
        <a href="/modules" class="text-sm text-slate-500 hover:text-slate-300 transition-colors">Modules</a>
        <i class="fa-solid fa-chevron-right text-slate-600 text-xs" aria-hidden="true"></i>
        <span class="text-sm text-slate-300">{mod.title}</span>
      </div>

      <div class="grid lg:grid-cols-2 gap-16 items-start">
        <div>
          <div class="h-14 w-14 rounded-2xl bg-violet-500/10 flex items-center justify-center mb-6">
            <i class={mod.icon + ' text-2xl text-violet-400'} aria-hidden="true"></i>
          </div>
          <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-4">{mod.title}</h1>
          <p class="text-lg text-violet-400 font-medium mb-4">{mod.tagline}</p>
          <p class="text-slate-400 leading-relaxed mb-10">{mod.description}</p>
          <div class="flex flex-col sm:flex-row gap-3">
            <a href="/demo" class="inline-flex items-center justify-center gap-2 px-6 py-3 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
              <i class="fa-solid fa-calendar-check" aria-hidden="true"></i> Request Demo
            </a>
            <a href={'/docs/' + mod.slug} class="inline-flex items-center justify-center gap-2 px-6 py-3 text-sm font-semibold text-slate-300 rounded-xl border border-white/10 hover:bg-white/5 hover:text-white transition-all duration-200">
              <i class="fa-solid fa-book" aria-hidden="true"></i> View Docs
            </a>
          </div>
        </div>

        <!-- Feature list -->
        <div>
          <h2 class="text-lg font-bold text-white mb-6">Key features</h2>
          <ul class="space-y-4" role="list">
            {mod.features.map((f) => (
              <li class="flex items-start gap-4 p-4 rounded-xl border border-white/5 bg-white/[0.02]">
                <div class="h-9 w-9 rounded-lg bg-violet-500/10 flex items-center justify-center shrink-0">
                  <i class={f.icon + ' text-violet-400 text-sm'} aria-hidden="true"></i>
                </div>
                <div>
                  <h3 class="text-sm font-semibold text-white mb-1">{f.title}</h3>
                  <p class="text-xs text-slate-500 leading-relaxed">{f.description}</p>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <!-- MDX content -->
      {entry.body.trim() && (
        <div class="mt-20 prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400 prose-code:text-violet-300 prose-code:bg-white/5">
          <Content />
        </div>
      )}
    </div>
  </section>
</MarketingLayout>
""")

# ── solutions/enterprise.astro ───────────────────────────────────────────────
write(f'{PAGES}/solutions/enterprise.astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';

const benefits = [
  { icon: 'fa-solid fa-building-columns', title: 'Multi-tenant architecture', desc: 'Fully isolated environments per business unit, subsidiary or client — all managed centrally.' },
  { icon: 'fa-solid fa-shield-halved', title: 'Enterprise-grade security', desc: 'SSO/SAML 2.0, MFA, IP allowlisting, end-to-end encryption and granular RBAC.' },
  { icon: 'fa-solid fa-file-contract', title: 'Compliance ready', desc: 'GDPR, SOC 2, ISO 27001 compliant with data residency options across regions.' },
  { icon: 'fa-solid fa-headset', title: 'Dedicated support', desc: 'Named Customer Success Manager, SLA-backed support and onboarding assistance.' },
  { icon: 'fa-solid fa-gears', title: 'Custom integrations', desc: 'Professional services team for bespoke integrations with ERP, HRIS and legacy systems.' },
  { icon: 'fa-solid fa-scale-balanced', title: 'Flexible contracts', desc: 'Enterprise agreements with custom terms, volume pricing and multi-year options.' },
];
---

<MarketingLayout title="Silence for Enterprise" description="Silence for enterprise — AI-powered all-in-one automation for large organisations. Multi-tenant, SSO, compliance and dedicated support.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Enterprise</p>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">Built for enterprise scale</h1>
        <p class="text-slate-400 text-lg max-w-2xl mx-auto">Silence gives large organisations a single platform that is secure, compliant, deeply customisable and backed by a dedicated team.</p>
      </div>

      <ul class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-16" role="list">
        {benefits.map((b) => (
          <li class="p-8 rounded-2xl border border-white/5 bg-white/[0.02]">
            <div class="h-11 w-11 rounded-xl bg-violet-500/10 flex items-center justify-center mb-4">
              <i class={b.icon + ' text-violet-400'} aria-hidden="true"></i>
            </div>
            <h2 class="text-base font-bold text-white mb-2">{b.title}</h2>
            <p class="text-sm text-slate-400 leading-relaxed">{b.desc}</p>
          </li>
        ))}
      </ul>

      <div class="text-center p-12 rounded-2xl border border-violet-500/20 bg-violet-500/5">
        <h2 class="text-2xl font-bold text-white mb-4">Ready to talk enterprise?</h2>
        <p class="text-slate-400 mb-8 max-w-lg mx-auto">Our enterprise team will design a deployment tailored to your organisation's requirements.</p>
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <a href="/demo" class="inline-flex items-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
            <i class="fa-solid fa-calendar-check" aria-hidden="true"></i> Request Demo
          </a>
          <a href="/contact" class="inline-flex items-center gap-2 px-8 py-3.5 text-sm font-semibold text-slate-300 rounded-xl border border-white/10 hover:bg-white/5 hover:text-white transition-all duration-200">
            Contact Sales
          </a>
        </div>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── solutions/sme.astro ──────────────────────────────────────────────────────
write(f'{PAGES}/solutions/sme.astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';

const why = [
  { icon: 'fa-solid fa-circle-dollar-to-slot', title: 'Replace 10 tools with one', desc: 'Stop paying for Slack, Jira, Google Workspace and QuickBooks separately. Silence does it all.' },
  { icon: 'fa-solid fa-rocket', title: 'Up and running in days', desc: 'Guided onboarding, pre-built templates and a clean UI means your team is productive fast.' },
  { icon: 'fa-solid fa-arrows-up-to-line', title: 'Scales with you', desc: 'Start with the modules you need today and activate new ones as you grow.' },
  { icon: 'fa-solid fa-robot', title: 'AI from day one', desc: 'Even small teams benefit from AI automation — auto-classify invoices, summarise meetings and more.' },
];
---

<MarketingLayout title="Silence for SME" description="Silence for small and medium businesses — replace your entire tool stack with one AI-powered platform. Fast setup, fair pricing, all modules included.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Small & Medium Business</p>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">The all-in-one platform for growing businesses</h1>
        <p class="text-slate-400 text-lg max-w-2xl mx-auto">SMEs deserve enterprise-quality tools without enterprise complexity or price tags. Silence delivers.</p>
      </div>

      <ul class="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-20" role="list">
        {why.map((w) => (
          <li class="flex gap-5 p-8 rounded-2xl border border-white/5 bg-white/[0.02]">
            <div class="h-11 w-11 rounded-xl bg-violet-500/10 flex items-center justify-center shrink-0">
              <i class={w.icon + ' text-violet-400'} aria-hidden="true"></i>
            </div>
            <div>
              <h2 class="text-base font-bold text-white mb-2">{w.title}</h2>
              <p class="text-sm text-slate-400 leading-relaxed">{w.desc}</p>
            </div>
          </li>
        ))}
      </ul>

      <div class="text-center p-12 rounded-2xl border border-violet-500/20 bg-violet-500/5">
        <h2 class="text-2xl font-bold text-white mb-4">See Silence in action for your team</h2>
        <p class="text-slate-400 mb-8">Book a 30-minute demo and we'll show you exactly how Silence fits your business.</p>
        <a href="/demo" class="inline-flex items-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
          <i class="fa-solid fa-calendar-check" aria-hidden="true"></i> Request Demo
        </a>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── integrations.astro ───────────────────────────────────────────────────────
write(f'{PAGES}/integrations.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';

const featured = [
  { name: 'Slack', icon: 'fa-brands fa-slack', desc: 'Send notifications and create tasks directly from Slack messages.' },
  { name: 'Salesforce', icon: 'fa-solid fa-cloud', desc: 'Bi-directional sync of contacts, deals and activities.' },
  { name: 'SAP', icon: 'fa-solid fa-database', desc: 'Connect ERP data for finance, procurement and HR workflows.' },
  { name: 'Microsoft 365', icon: 'fa-brands fa-microsoft', desc: 'Import emails, calendar events and SharePoint documents.' },
  { name: 'Google Workspace', icon: 'fa-brands fa-google', desc: 'Import Drive files, Gmail threads and Google Calendar events.' },
  { name: 'Zapier', icon: 'fa-solid fa-bolt', desc: 'Connect Silence to 6000+ apps via Zapier automations.' },
  { name: 'Stripe', icon: 'fa-brands fa-stripe', desc: 'Sync payment data and trigger workflows on invoice events.' },
  { name: 'GitHub', icon: 'fa-brands fa-github', desc: 'Link commits and PRs to Silence project tasks.' },
  { name: 'HubSpot', icon: 'fa-solid fa-h', desc: 'Sync marketing contacts and campaign data with CRM.' },
  { name: 'Zendesk', icon: 'fa-solid fa-headset', desc: 'Create and update support tickets from Silence workflows.' },
  { name: 'Jira', icon: 'fa-solid fa-j', desc: 'Migrate from or sync issues between Jira and Silence Projects.' },
  { name: 'Make (Integromat)', icon: 'fa-solid fa-circle-nodes', desc: 'Build advanced multi-step automation with Make scenarios.' },
];
---

<MarketingLayout title="Integrations" description="Connect Silence to 500+ tools including Slack, Salesforce, SAP, Microsoft 365, Google Workspace, Zapier and more.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">500+ integrations</p>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">Connect everything you rely on</h1>
        <p class="text-slate-400 text-lg max-w-2xl mx-auto">Silence integrates with the tools your team already uses — or replaces them entirely.</p>
      </div>

      <ul class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 mb-16" role="list">
        {featured.map((int) => (
          <li class="flex items-start gap-4 p-6 rounded-2xl border border-white/5 bg-white/[0.02] hover:bg-white/5 hover:border-white/10 transition-all duration-200">
            <div class="h-10 w-10 rounded-xl bg-white/5 flex items-center justify-center shrink-0">
              <i class={int.icon + ' text-slate-300 text-lg'} aria-hidden="true"></i>
            </div>
            <div>
              <h2 class="text-sm font-semibold text-white mb-1">{int.name}</h2>
              <p class="text-xs text-slate-500 leading-relaxed">{int.desc}</p>
            </div>
          </li>
        ))}
      </ul>

      <div class="text-center p-10 rounded-2xl border border-white/5 bg-white/[0.02]">
        <p class="text-slate-400 mb-4">Need a custom integration? Our enterprise team can build it.</p>
        <a href="/contact" class="inline-flex items-center gap-2 text-sm font-semibold text-violet-400 hover:text-violet-300 transition-colors">
          Talk to us <i class="fa-solid fa-arrow-right text-xs" aria-hidden="true"></i>
        </a>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── pricing.astro ────────────────────────────────────────────────────────────
write(f'{PAGES}/pricing.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';

const faqs = [
  { q: 'How is Silence priced?', a: 'Silence is priced on a per-organisation basis, tailored to your team size, modules and deployment requirements. Contact our sales team for a custom quote.' },
  { q: 'Is there a free trial?', a: 'Yes. We offer a guided proof-of-concept for qualifying organisations. Request a demo and our team will set one up for you.' },
  { q: 'What is included in the enterprise plan?', a: 'All modules, unlimited users, multi-tenant support, SSO, dedicated Customer Success Manager, SLA-backed support and optional professional services.' },
  { q: 'Can I start with only a few modules?', a: 'Absolutely. You can activate only the modules you need today and expand at any time. Pricing reflects your active modules.' },
  { q: 'Is there a setup fee?', a: 'Setup and onboarding are included in enterprise agreements. For complex migrations, optional professional services are available.' },
  { q: 'What regions are available for data residency?', a: 'Silence supports EU (Frankfurt), US East, US West and Asia Pacific (Singapore). Additional regions are available on request.' },
];

const pricingLD = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: faqs.map((f) => ({
    "@type": "Question",
    name: f.q,
    acceptedAnswer: { "@type": "Answer", text: f.a },
  })),
};
---

<MarketingLayout title="Pricing" description="Silence enterprise pricing — custom plans for organisations of all sizes. Contact sales for a personalised quote.">
  <script type="application/ld+json" set:html={JSON.stringify(pricingLD)}></script>

  <!-- Hero -->
  <section class="relative bg-[#0A0A14] section-padding text-center">
    <div class="mx-auto max-w-3xl mb-16">
      <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Pricing</p>
      <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">Pricing built around your organisation</h1>
      <p class="text-slate-400 text-lg max-w-xl mx-auto">No rigid tiers. No per-seat surprises. Silence is priced to match your organisation's reality — modules, users and deployment model.</p>
    </div>

    <!-- Value props -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 mx-auto max-w-4xl mb-16">
      {[
        { icon: 'fa-solid fa-cubes', title: 'Module-based', desc: 'Pay only for the modules you activate.' },
        { icon: 'fa-solid fa-users', title: 'Unlimited users', desc: 'No per-seat fees — grow your team freely.' },
        { icon: 'fa-solid fa-handshake', title: 'Flexible terms', desc: 'Monthly, annual or multi-year contracts.' },
      ].map((v) => (
        <div class="p-8 rounded-2xl border border-white/5 bg-white/[0.02] text-left">
          <div class="h-10 w-10 rounded-xl bg-violet-500/10 flex items-center justify-center mb-4">
            <i class={v.icon + ' text-violet-400'} aria-hidden="true"></i>
          </div>
          <h2 class="text-base font-bold text-white mb-2">{v.title}</h2>
          <p class="text-sm text-slate-400">{v.desc}</p>
        </div>
      ))}
    </div>

    <!-- CTA card -->
    <div class="mx-auto max-w-lg p-12 rounded-2xl border border-violet-500/20 bg-violet-500/5">
      <h2 class="text-2xl font-bold text-white mb-3">Get a custom quote</h2>
      <p class="text-slate-400 mb-8">Tell us about your organisation and we'll put together a tailored proposal within 24 hours.</p>
      <div class="flex flex-col gap-3">
        <a href="/demo" class="inline-flex items-center justify-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
          <i class="fa-solid fa-calendar-check" aria-hidden="true"></i> Request Demo
        </a>
        <a href="/contact" class="inline-flex items-center justify-center gap-2 px-8 py-3.5 text-sm font-semibold text-slate-300 rounded-xl border border-white/10 hover:bg-white/5 hover:text-white transition-all duration-200">
          Contact Sales
        </a>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="bg-[#0C0C1A] section-padding" aria-labelledby="faq-heading">
    <div class="mx-auto max-w-3xl">
      <h2 id="faq-heading" class="text-2xl font-bold text-white mb-10 text-center">Frequently asked questions</h2>
      <dl class="space-y-4">
        {faqs.map((faq) => (
          <div class="p-6 rounded-2xl border border-white/5 bg-white/[0.02]">
            <dt class="text-sm font-semibold text-white mb-2">{faq.q}</dt>
            <dd class="text-sm text-slate-400 leading-relaxed">{faq.a}</dd>
          </div>
        ))}
      </dl>
    </div>
  </section>
</MarketingLayout>
""")

# ── security.astro ───────────────────────────────────────────────────────────
write(f'{PAGES}/security.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';

const pillars = [
  { icon: 'fa-solid fa-lock', title: 'End-to-end encryption', desc: 'All data is encrypted in transit (TLS 1.3) and at rest (AES-256). Encryption keys are managed per-tenant.' },
  { icon: 'fa-solid fa-id-badge', title: 'Single Sign-On', desc: 'SAML 2.0 and OpenID Connect (OIDC) support with any Identity Provider — Okta, Azure AD, Google and more.' },
  { icon: 'fa-solid fa-user-shield', title: 'Role-based access control', desc: 'Granular RBAC and attribute-based policies. Define exactly what each user can see, create and modify.' },
  { icon: 'fa-solid fa-file-shield', title: 'Audit logs', desc: 'Tamper-evident logs of every action across the platform. Export to SIEM for 24/7 monitoring.' },
  { icon: 'fa-solid fa-globe', title: 'Data residency', desc: 'Choose where your data lives — EU, US or APAC. Data never leaves your selected region without consent.' },
  { icon: 'fa-solid fa-certificate', title: 'Compliance', desc: 'SOC 2 Type II, ISO 27001, GDPR. Penetration tested annually by an independent third party.' },
];
---

<MarketingLayout title="Security" description="Silence enterprise security — end-to-end encryption, SSO, RBAC, audit logs, data residency and compliance certifications.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Security & Trust</p>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">Your data is safe with Silence</h1>
        <p class="text-slate-400 text-lg max-w-2xl mx-auto">Security is not an add-on at Silence — it is built into the foundation of every module, every API call and every data store.</p>
      </div>

      <ul class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-16" role="list">
        {pillars.map((p) => (
          <li class="p-8 rounded-2xl border border-white/5 bg-white/[0.02]">
            <div class="h-11 w-11 rounded-xl bg-violet-500/10 flex items-center justify-center mb-4">
              <i class={p.icon + ' text-violet-400'} aria-hidden="true"></i>
            </div>
            <h2 class="text-base font-bold text-white mb-2">{p.title}</h2>
            <p class="text-sm text-slate-400 leading-relaxed">{p.desc}</p>
          </li>
        ))}
      </ul>

      <div class="flex flex-wrap justify-center gap-6 p-10 rounded-2xl border border-white/5 bg-white/[0.02]">
        {['SOC 2 Type II', 'ISO 27001', 'GDPR', 'TLS 1.3', 'AES-256'].map((badge) => (
          <div class="flex items-center gap-2 px-4 py-2 rounded-full border border-green-500/20 bg-green-500/5">
            <i class="fa-solid fa-circle-check text-green-400 text-sm" aria-hidden="true"></i>
            <span class="text-sm font-medium text-slate-300">{badge}</span>
          </div>
        ))}
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── about.astro ──────────────────────────────────────────────────────────────
write(f'{PAGES}/about.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';
---

<MarketingLayout title="About Silence" description="Learn about Silence — the AI-powered enterprise automation platform. Our mission, story and team.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-4xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">About</p>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-6">We built the platform we always needed</h1>
        <p class="text-slate-400 text-lg leading-relaxed max-w-2xl mx-auto">
          Silence was born out of frustration. We were running a growing business stitched together with nine different SaaS tools, and nothing talked to each other properly. So we built Silence — the all-in-one AI platform we wish had existed.
        </p>
      </div>

      <!-- Mission -->
      <div class="mb-20 p-10 rounded-2xl border border-violet-500/20 bg-violet-500/5 text-center">
        <i class="fa-solid fa-bullseye text-3xl text-violet-400 mb-4" aria-hidden="true"></i>
        <h2 class="text-xl font-bold text-white mb-3">Our mission</h2>
        <p class="text-slate-300 text-lg leading-relaxed max-w-xl mx-auto">To give every enterprise and SME the power to go fully paperless and automate every workflow — without a 12-month implementation project.</p>
      </div>

      <!-- Values -->
      <div class="mb-20">
        <h2 class="text-2xl font-bold text-white mb-8 text-center">What we believe</h2>
        <ul class="grid grid-cols-1 sm:grid-cols-2 gap-6" role="list">
          {[
            { icon: 'fa-solid fa-layer-group', title: 'Integration over fragmentation', desc: 'Tools that talk to each other unlock exponential productivity.' },
            { icon: 'fa-solid fa-robot', title: 'AI should be invisible', desc: 'The best AI automation is the kind that just works, without configuration.' },
            { icon: 'fa-solid fa-people-group', title: 'People first', desc: 'Software should adapt to how teams work — not the other way around.' },
            { icon: 'fa-solid fa-lock', title: 'Security by default', desc: 'Enterprise data deserves enterprise-grade protection on day one.' },
          ].map((v) => (
            <li class="flex gap-4 p-6 rounded-2xl border border-white/5 bg-white/[0.02]">
              <div class="h-10 w-10 rounded-xl bg-violet-500/10 flex items-center justify-center shrink-0">
                <i class={v.icon + ' text-violet-400'} aria-hidden="true"></i>
              </div>
              <div>
                <h3 class="text-sm font-bold text-white mb-1">{v.title}</h3>
                <p class="text-sm text-slate-400">{v.desc}</p>
              </div>
            </li>
          ))}
        </ul>
      </div>

      <!-- CTA -->
      <div class="text-center">
        <h2 class="text-2xl font-bold text-white mb-4">Join the journey</h2>
        <p class="text-slate-400 mb-8">We are always looking for talented people who want to reshape how organisations work.</p>
        <a href="/contact" class="inline-flex items-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
          Get in touch
        </a>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── demo.astro ───────────────────────────────────────────────────────────────
write(f'{PAGES}/demo.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';
---

<MarketingLayout title="Request Demo" description="Request a personalised Silence demo. See how AI-powered enterprise automation works for your organisation.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-6xl grid lg:grid-cols-2 gap-16 items-start">
      <!-- Left: context -->
      <div class="pt-4">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Request Demo</p>
        <h1 class="text-4xl font-extrabold text-white mb-5">See Silence in action</h1>
        <p class="text-slate-400 leading-relaxed mb-10">
          In a 30-minute personalised demo, our team will show you exactly how Silence can replace your current tool stack — tailored to your industry, team size and use case.
        </p>
        <ul class="space-y-4">
          {[
            { icon: 'fa-solid fa-calendar-check', text: '30-minute live walkthrough with a product expert' },
            { icon: 'fa-solid fa-sliders', text: 'Tailored to your specific workflows and industry' },
            { icon: 'fa-solid fa-circle-question', text: 'Q&A on modules, integrations and migration' },
            { icon: 'fa-solid fa-file-lines', text: 'Custom proposal ready within 48 hours' },
          ].map((item) => (
            <li class="flex items-center gap-3">
              <span class="h-7 w-7 rounded-lg bg-violet-500/10 flex items-center justify-center shrink-0">
                <i class={item.icon + ' text-violet-400 text-xs'} aria-hidden="true"></i>
              </span>
              <span class="text-sm text-slate-300">{item.text}</span>
            </li>
          ))}
        </ul>
      </div>

      <!-- Right: form -->
      <div class="rounded-2xl border border-white/10 bg-white/[0.02] p-8">
        <h2 class="text-lg font-bold text-white mb-6">Book your demo</h2>
        <form name="request-demo" method="POST" data-netlify="true" class="space-y-5" novalidate>
          <input type="hidden" name="form-name" value="request-demo" />
          <div class="grid sm:grid-cols-2 gap-4">
            <div>
              <label for="first-name" class="block text-xs font-medium text-slate-400 mb-1.5">First name <span aria-hidden="true" class="text-violet-400">*</span></label>
              <input type="text" id="first-name" name="first-name" required autocomplete="given-name" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50" />
            </div>
            <div>
              <label for="last-name" class="block text-xs font-medium text-slate-400 mb-1.5">Last name <span aria-hidden="true" class="text-violet-400">*</span></label>
              <input type="text" id="last-name" name="last-name" required autocomplete="family-name" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50" />
            </div>
          </div>
          <div>
            <label for="email" class="block text-xs font-medium text-slate-400 mb-1.5">Work email <span aria-hidden="true" class="text-violet-400">*</span></label>
            <input type="email" id="email" name="email" required autocomplete="email" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50" />
          </div>
          <div>
            <label for="company" class="block text-xs font-medium text-slate-400 mb-1.5">Company <span aria-hidden="true" class="text-violet-400">*</span></label>
            <input type="text" id="company" name="company" required autocomplete="organization" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50" />
          </div>
          <div>
            <label for="team-size" class="block text-xs font-medium text-slate-400 mb-1.5">Team size</label>
            <select id="team-size" name="team-size" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-slate-300 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50">
              <option value="">Select...</option>
              <option value="1-10">1–10</option>
              <option value="11-50">11–50</option>
              <option value="51-200">51–200</option>
              <option value="201-1000">201–1000</option>
              <option value="1000+">1000+</option>
            </select>
          </div>
          <div>
            <label for="message" class="block text-xs font-medium text-slate-400 mb-1.5">What would you like to see? (optional)</label>
            <textarea id="message" name="message" rows="3" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50 resize-none"></textarea>
          </div>
          <button type="submit" class="w-full inline-flex items-center justify-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
            <i class="fa-solid fa-calendar-check" aria-hidden="true"></i>
            Book Demo
          </button>
          <p class="text-xs text-slate-600 text-center">We'll respond within one business day. No spam, ever.</p>
        </form>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── contact.astro ────────────────────────────────────────────────────────────
write(f'{PAGES}/contact.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';
---

<MarketingLayout title="Contact Sales" description="Contact the Silence sales team for pricing, enterprise plans, integrations and partnerships.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-6xl grid lg:grid-cols-2 gap-16 items-start">
      <div class="pt-4">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Contact Sales</p>
        <h1 class="text-4xl font-extrabold text-white mb-5">Let's talk</h1>
        <p class="text-slate-400 leading-relaxed mb-10">Whether you want a quote, have questions about a specific module, or want to discuss a partnership — our team is here.</p>
        <ul class="space-y-5">
          <li class="flex items-center gap-3">
            <span class="h-9 w-9 rounded-xl bg-violet-500/10 flex items-center justify-center">
              <i class="fa-solid fa-envelope text-violet-400 text-sm" aria-hidden="true"></i>
            </span>
            <a href="mailto:sales@silence.ai" class="text-sm text-slate-300 hover:text-white transition-colors">sales@silence.ai</a>
          </li>
          <li class="flex items-center gap-3">
            <span class="h-9 w-9 rounded-xl bg-violet-500/10 flex items-center justify-center">
              <i class="fa-solid fa-clock text-violet-400 text-sm" aria-hidden="true"></i>
            </span>
            <span class="text-sm text-slate-400">We respond within one business day</span>
          </li>
        </ul>
      </div>

      <div class="rounded-2xl border border-white/10 bg-white/[0.02] p-8">
        <h2 class="text-lg font-bold text-white mb-6">Send us a message</h2>
        <form name="contact-sales" method="POST" data-netlify="true" class="space-y-5" novalidate>
          <input type="hidden" name="form-name" value="contact-sales" />
          <div>
            <label for="name" class="block text-xs font-medium text-slate-400 mb-1.5">Your name <span aria-hidden="true" class="text-violet-400">*</span></label>
            <input type="text" id="name" name="name" required autocomplete="name" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50" />
          </div>
          <div>
            <label for="email" class="block text-xs font-medium text-slate-400 mb-1.5">Work email <span aria-hidden="true" class="text-violet-400">*</span></label>
            <input type="email" id="email" name="email" required autocomplete="email" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 focus:border-violet-500/50" />
          </div>
          <div>
            <label for="subject" class="block text-xs font-medium text-slate-400 mb-1.5">Subject</label>
            <select id="subject" name="subject" class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-slate-300 focus:outline-none focus:ring-2 focus:ring-violet-500/50">
              <option value="">Select...</option>
              <option value="pricing">Pricing & Quotes</option>
              <option value="demo">Request a Demo</option>
              <option value="integration">Integration Questions</option>
              <option value="partnership">Partnership</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div>
            <label for="message" class="block text-xs font-medium text-slate-400 mb-1.5">Message <span aria-hidden="true" class="text-violet-400">*</span></label>
            <textarea id="message" name="message" rows="5" required class="w-full px-4 py-2.5 text-sm bg-white/5 border border-white/10 rounded-lg text-white placeholder:text-slate-600 focus:outline-none focus:ring-2 focus:ring-violet-500/50 resize-none"></textarea>
          </div>
          <button type="submit" class="w-full inline-flex items-center justify-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
            <i class="fa-solid fa-paper-plane" aria-hidden="true"></i> Send Message
          </button>
        </form>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── customers/index.astro ────────────────────────────────────────────────────
write(f'{PAGES}/customers/index.astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';
import { getCollection } from 'astro:content';

const allStudies = await getCollection('caseStudies');
const sorted = allStudies.sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());
---

<MarketingLayout title="Customers" description="See how enterprises and SMEs use Silence to automate their workflows, go paperless and grow faster.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Customer stories</p>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">Trusted by teams worldwide</h1>
        <p class="text-slate-400 text-lg max-w-2xl mx-auto">Real organisations, real results. See how Silence is transforming the way businesses work.</p>
      </div>

      {sorted.length === 0 ? (
        <div class="text-center py-20 text-slate-500">
          <i class="fa-solid fa-building text-4xl mb-4 text-slate-700" aria-hidden="true"></i>
          <p>Case studies coming soon.</p>
        </div>
      ) : (
        <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" role="list">
          {sorted.map((study) => (
            <li>
              <a href={'/customers/' + study.id} class="group flex flex-col h-full p-8 rounded-2xl border border-white/5 bg-white/[0.02] hover:bg-violet-500/5 hover:border-violet-500/20 transition-all duration-200">
                <p class="text-xs font-semibold uppercase tracking-wider text-violet-400 mb-3">{study.data.industry}</p>
                <h2 class="text-base font-bold text-white mb-2 group-hover:text-violet-300 transition-colors">{study.data.title}</h2>
                <p class="text-sm text-slate-400 flex-1 mb-6">{study.data.description}</p>
                {study.data.results.length > 0 && (
                  <dl class="grid grid-cols-2 gap-3">
                    {study.data.results.slice(0, 2).map((r) => (
                      <div class="p-3 rounded-xl bg-violet-500/10 text-center">
                        <dt class="text-lg font-extrabold text-gradient">{r.value}</dt>
                        <dd class="text-xs text-slate-500 mt-0.5">{r.metric}</dd>
                      </div>
                    ))}
                  </dl>
                )}
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  </section>
</MarketingLayout>
""")

# ── customers/[slug].astro ───────────────────────────────────────────────────
write(f'{PAGES}/customers/[slug].astro', """\
---
import BlogLayout from '../../layouts/BlogLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const studies = await getCollection('caseStudies');
  return studies.map((entry) => ({ params: { slug: entry.id }, props: { entry } }));
}

const { entry } = Astro.props;
const { Content } = await entry.render();
const cs = entry.data;
---

<BlogLayout title={cs.title} description={cs.description} publishedAt={cs.publishedAt}>
  <div class="mx-auto max-w-3xl px-6 py-16 lg:px-0">
    <a href="/customers" class="inline-flex items-center gap-2 text-sm text-slate-500 hover:text-slate-300 mb-8 transition-colors">
      <i class="fa-solid fa-arrow-left text-xs" aria-hidden="true"></i> All customers
    </a>
    <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">{cs.industry}</p>
    <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-6">{cs.title}</h1>
    {cs.results.length > 0 && (
      <dl class="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-12">
        {cs.results.map((r) => (
          <div class="p-4 rounded-xl border border-white/5 bg-white/[0.02] text-center">
            <dt class="text-2xl font-extrabold text-gradient">{r.value}</dt>
            <dd class="text-xs text-slate-500 mt-1">{r.metric}</dd>
          </div>
        ))}
      </dl>
    )}
    <div class="prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400 prose-code:text-violet-300 prose-code:bg-white/5">
      <Content />
    </div>
  </div>
</BlogLayout>
""")

# ── blog/index.astro ─────────────────────────────────────────────────────────
write(f'{PAGES}/blog/index.astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';
import { getCollection } from 'astro:content';

const posts = (await getCollection('blog')).filter((p) => !p.data.draft).sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());
---

<MarketingLayout title="Blog" description="The latest articles, guides and product news from the Silence team — enterprise automation, AI and business productivity.">
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Blog</p>
        <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">Insights & resources</h1>
        <p class="text-slate-400 text-lg">Articles, guides and product news from the Silence team.</p>
      </div>

      {posts.length === 0 ? (
        <div class="text-center py-20 text-slate-500">
          <i class="fa-solid fa-pen-nib text-4xl mb-4 text-slate-700" aria-hidden="true"></i>
          <p>Articles coming soon.</p>
        </div>
      ) : (
        <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" role="list">
          {posts.map((post) => (
            <li>
              <a href={'/blog/' + post.id} class="group flex flex-col h-full p-8 rounded-2xl border border-white/5 bg-white/[0.02] hover:bg-violet-500/5 hover:border-violet-500/20 transition-all duration-200">
                <div class="flex flex-wrap gap-1.5 mb-4">
                  {post.data.tags.slice(0, 3).map((tag) => (
                    <span class="text-xs px-2 py-0.5 rounded-full bg-violet-500/10 text-violet-400">{tag}</span>
                  ))}
                </div>
                <h2 class="text-base font-bold text-white mb-2 group-hover:text-violet-300 transition-colors">{post.data.title}</h2>
                <p class="text-sm text-slate-400 flex-1 mb-6">{post.data.description}</p>
                <div class="flex items-center justify-between text-xs text-slate-600">
                  <span>{post.data.author}</span>
                  <time datetime={post.data.publishedAt.toISOString()}>{post.data.publishedAt.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })}</time>
                </div>
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  </section>
</MarketingLayout>
""")

# ── blog/[slug].astro ────────────────────────────────────────────────────────
write(f'{PAGES}/blog/[slug].astro', """\
---
import BlogLayout from '../../layouts/BlogLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  return posts.map((entry) => ({ params: { slug: entry.id }, props: { entry } }));
}

const { entry } = Astro.props;
const { Content } = await entry.render();
const post = entry.data;
---

<BlogLayout title={post.title} description={post.description} publishedAt={post.publishedAt} updatedAt={post.updatedAt} author={post.author} image={post.coverImage}>
  <div class="mx-auto max-w-3xl px-6 py-16 lg:px-0">
    <a href="/blog" class="inline-flex items-center gap-2 text-sm text-slate-500 hover:text-slate-300 mb-8 transition-colors">
      <i class="fa-solid fa-arrow-left text-xs" aria-hidden="true"></i> All articles
    </a>
    <div class="flex flex-wrap gap-1.5 mb-6">
      {post.tags.map((tag) => (
        <a href={'/blog/tag/' + tag} class="text-xs px-2.5 py-1 rounded-full bg-violet-500/10 text-violet-400 hover:bg-violet-500/20 transition-colors">{tag}</a>
      ))}
    </div>
    <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-4">{post.title}</h1>
    <div class="flex items-center gap-3 text-sm text-slate-500 mb-12">
      <span>{post.author}</span>
      <span aria-hidden="true">·</span>
      <time datetime={post.publishedAt.toISOString()}>{post.publishedAt.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</time>
    </div>
    <div class="prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400 prose-code:text-violet-300 prose-code:bg-white/5 prose-pre:bg-[#0C0C1A] prose-pre:border prose-pre:border-white/10">
      <Content />
    </div>
  </div>
</BlogLayout>
""")

# ── blog/tag/[tag].astro ─────────────────────────────────────────────────────
write(f'{PAGES}/blog/tag/[tag].astro', """\
---
import MarketingLayout from '../../../layouts/MarketingLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  const tags = [...new Set(posts.flatMap((p) => p.data.tags))];
  return tags.map((tag) => ({
    params: { tag },
    props: { posts: posts.filter((p) => p.data.tags.includes(tag)).sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime()) },
  }));
}

const { tag } = Astro.params;
const { posts } = Astro.props;
---

<MarketingLayout title={'Blog: ' + tag} description={'All Silence blog articles tagged ' + tag}>
  <section class="bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-7xl">
      <div class="mb-10">
        <a href="/blog" class="inline-flex items-center gap-2 text-sm text-slate-500 hover:text-slate-300 mb-6 transition-colors">
          <i class="fa-solid fa-arrow-left text-xs" aria-hidden="true"></i> All articles
        </a>
        <h1 class="text-3xl font-extrabold text-white">Tag: <span class="text-gradient">{tag}</span></h1>
        <p class="text-slate-400 mt-2">{posts.length} article{posts.length !== 1 ? 's' : ''}</p>
      </div>
      <ul class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" role="list">
        {posts.map((post) => (
          <li>
            <a href={'/blog/' + post.id} class="group flex flex-col h-full p-8 rounded-2xl border border-white/5 bg-white/[0.02] hover:bg-violet-500/5 hover:border-violet-500/20 transition-all duration-200">
              <h2 class="text-base font-bold text-white mb-2 group-hover:text-violet-300 transition-colors">{post.data.title}</h2>
              <p class="text-sm text-slate-400 flex-1">{post.data.description}</p>
            </a>
          </li>
        ))}
      </ul>
    </div>
  </section>
</MarketingLayout>
""")

# ── changelog/index.astro ────────────────────────────────────────────────────
write(f'{PAGES}/changelog/index.astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';
import { getCollection } from 'astro:content';

const entries = (await getCollection('changelog')).sort((a, b) => b.data.releasedAt.getTime() - a.data.releasedAt.getTime());
---

<MarketingLayout title="Changelog" description="Silence product changelog — release notes, new features and improvements.">
  <section class="bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-3xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Changelog</p>
        <h1 class="text-4xl font-extrabold text-white mb-4">What's new in Silence</h1>
        <p class="text-slate-400">Every release, every improvement — all in one place.</p>
      </div>

      {entries.length === 0 ? (
        <div class="text-center py-20 text-slate-600">
          <i class="fa-solid fa-code-commit text-4xl mb-4" aria-hidden="true"></i>
          <p>Release notes coming soon.</p>
        </div>
      ) : (
        <ol class="relative border-l border-white/5 pl-8 space-y-12" role="list">
          {entries.map((entry) => (
            <li class="relative">
              <span class="absolute -left-[41px] h-4 w-4 rounded-full bg-violet-500 border-4 border-[#0A0A14]"></span>
              <time class="text-xs text-slate-500 mb-1 block" datetime={entry.data.releasedAt.toISOString()}>
                {entry.data.releasedAt.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
              </time>
              <a href={'/changelog/' + entry.id} class="group">
                <h2 class="text-lg font-bold text-white mb-1 group-hover:text-violet-300 transition-colors">
                  v{entry.data.version} — {entry.data.title}
                </h2>
              </a>
              <p class="text-sm text-slate-400 mb-4">{entry.data.summary}</p>
              {entry.data.highlights.length > 0 && (
                <ul class="space-y-1.5">
                  {entry.data.highlights.map((h) => (
                    <li class="flex items-start gap-2 text-sm text-slate-400">
                      <i class="fa-solid fa-circle-check text-violet-500 text-xs mt-1 shrink-0" aria-hidden="true"></i>
                      {h}
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ol>
      )}
    </div>
  </section>
</MarketingLayout>
""")

# ── changelog/[version].astro ────────────────────────────────────────────────
write(f'{PAGES}/changelog/[version].astro', """\
---
import BlogLayout from '../../layouts/BlogLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const entries = await getCollection('changelog');
  return entries.map((entry) => ({ params: { version: entry.id }, props: { entry } }));
}

const { entry } = Astro.props;
const { Content } = await entry.render();
const cl = entry.data;
---

<BlogLayout title={'v' + cl.version + ' — ' + cl.title} description={cl.summary} publishedAt={cl.releasedAt}>
  <div class="mx-auto max-w-3xl px-6 py-16 lg:px-0">
    <a href="/changelog" class="inline-flex items-center gap-2 text-sm text-slate-500 hover:text-slate-300 mb-8 transition-colors">
      <i class="fa-solid fa-arrow-left text-xs" aria-hidden="true"></i> Changelog
    </a>
    <time class="text-xs text-slate-500" datetime={cl.releasedAt.toISOString()}>
      {cl.releasedAt.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
    </time>
    <h1 class="text-3xl font-extrabold text-white mt-2 mb-4">v{cl.version} — {cl.title}</h1>
    <p class="text-slate-400 mb-8">{cl.summary}</p>
    {cl.highlights.length > 0 && (
      <ul class="space-y-2 mb-10">
        {cl.highlights.map((h) => (
          <li class="flex items-start gap-3 text-sm text-slate-300">
            <i class="fa-solid fa-circle-check text-violet-500 text-xs mt-1 shrink-0" aria-hidden="true"></i>{h}
          </li>
        ))}
      </ul>
    )}
    <div class="prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400 prose-code:text-violet-300 prose-code:bg-white/5">
      <Content />
    </div>
  </div>
</BlogLayout>
""")

# ── docs/index.astro ─────────────────────────────────────────────────────────
write(f'{PAGES}/docs/index.astro', """\
---
import DocsLayout from '../../layouts/DocsLayout.astro';

const modules = [
  { slug: 'getting-started', icon: 'fa-solid fa-rocket', label: 'Getting Started', desc: 'Introduction, quick start and core concepts.' },
  { slug: 'workspace', icon: 'fa-solid fa-folder-open', label: 'Workspace', desc: 'Files, documents and spreadsheets.' },
  { slug: 'communication', icon: 'fa-solid fa-comments', label: 'Communication', desc: 'Chat, email and video conferencing.' },
  { slug: 'projects', icon: 'fa-solid fa-diagram-project', label: 'Projects', desc: 'Tasks, boards, sprints and Gantt.' },
  { slug: 'crm', icon: 'fa-solid fa-handshake', label: 'CRM', desc: 'Contacts, pipeline and sales.' },
  { slug: 'hr', icon: 'fa-solid fa-users', label: 'HR', desc: 'Payroll, recruitment and attendance.' },
  { slug: 'finance', icon: 'fa-solid fa-file-invoice-dollar', label: 'Finance', desc: 'Invoicing, expenses and accounting.' },
  { slug: 'operations', icon: 'fa-solid fa-boxes-stacking', label: 'Operations', desc: 'Inventory and procurement.' },
  { slug: 'ai-automation', icon: 'fa-solid fa-robot', label: 'AI & Automation', desc: 'Workflows, RPA and AI features.' },
  { slug: 'integrations', icon: 'fa-solid fa-plug', label: 'Integrations', desc: 'Connect to external tools.' },
  { slug: 'admin', icon: 'fa-solid fa-shield-halved', label: 'Admin', desc: 'Users, permissions and SSO.' },
];
---

<DocsLayout title="Documentation" description="Silence user documentation — getting started guides, module references and FAQ.">
  <h1 class="text-3xl font-extrabold text-white mb-4">Documentation</h1>
  <p class="text-slate-400 mb-12 leading-relaxed">Welcome to Silence Docs. Find guides, references and answers for every feature in the platform.</p>

  <h2 class="text-sm font-semibold uppercase tracking-wider text-slate-500 mb-6">Browse by module</h2>
  <ul class="grid grid-cols-1 sm:grid-cols-2 gap-4" role="list">
    {modules.map((mod) => (
      <li>
        <a href={'/docs/' + mod.slug} class="group flex items-start gap-4 p-5 rounded-xl border border-white/5 bg-white/[0.02] hover:bg-violet-500/5 hover:border-violet-500/20 transition-all duration-200">
          <div class="h-9 w-9 rounded-lg bg-violet-500/10 flex items-center justify-center shrink-0 group-hover:bg-violet-500/20 transition-colors">
            <i class={mod.icon + ' text-violet-400 text-sm'} aria-hidden="true"></i>
          </div>
          <div>
            <h3 class="text-sm font-semibold text-white mb-0.5 group-hover:text-violet-300 transition-colors">{mod.label}</h3>
            <p class="text-xs text-slate-500">{mod.desc}</p>
          </div>
        </a>
      </li>
    ))}
  </ul>
</DocsLayout>
""")

# ── docs/faq.astro ───────────────────────────────────────────────────────────
write(f'{PAGES}/docs/faq.astro', """\
---
import DocsLayout from '../../layouts/DocsLayout.astro';

const faqs = [
  { q: 'Can I import data from my existing tools?', a: 'Yes. Silence provides import tools for CSV, Excel, and direct integrations with Google Workspace, Microsoft 365, Jira and more. The onboarding team can assist with complex migrations.' },
  { q: 'Is Silence available on mobile?', a: 'Yes. Silence has native iOS and Android apps with full feature parity for core modules. The web app is also fully responsive.' },
  { q: 'How does multi-tenancy work?', a: 'Each organisation or business unit gets a fully isolated environment with its own users, data, branding and configuration. Environments can be managed from a parent admin console.' },
  { q: 'How long does onboarding take?', a: 'Most teams are fully onboarded within 1–5 business days. Enterprise rollouts with custom integrations may take 2–6 weeks, supported by our implementation team.' },
  { q: 'Can I customise fields, forms and workflows?', a: 'Yes. Every module supports custom fields, forms and workflow rules without coding. Advanced customisation is available via the workflow builder and REST API.' },
  { q: 'What happens to my data if I leave?', a: 'You can export all your data in standard formats (CSV, JSON, PDF) at any time. Upon contract termination, data is retained for 30 days then permanently deleted.' },
];

const faqLD = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: faqs.map(f => ({
    "@type": "Question",
    name: f.q,
    acceptedAnswer: { "@type": "Answer", text: f.a }
  }))
};
---

<DocsLayout title="FAQ" description="Frequently asked questions about Silence — onboarding, data import, mobile apps, multi-tenancy and more.">
  <script type="application/ld+json" set:html={JSON.stringify(faqLD)}></script>
  <h1 class="text-3xl font-extrabold text-white mb-4">Frequently Asked Questions</h1>
  <p class="text-slate-400 mb-10">Can't find your answer here? <a href="/contact" class="text-violet-400 hover:text-violet-300">Contact our team</a>.</p>

  <dl class="space-y-6">
    {faqs.map((faq) => (
      <div class="border-b border-white/5 pb-6">
        <dt class="text-base font-semibold text-white mb-2">{faq.q}</dt>
        <dd class="text-sm text-slate-400 leading-relaxed">{faq.a}</dd>
      </div>
    ))}
  </dl>
</DocsLayout>
""")

# ── vs/[slug].astro ──────────────────────────────────────────────────────────
write(f'{PAGES}/vs/[slug].astro', """\
---
import MarketingLayout from '../../layouts/MarketingLayout.astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const entries = await getCollection('comparisons');
  return entries.map((entry) => ({
    params: { slug: entry.data.competitorSlug },
    props: { entry },
  }));
}

const { entry } = Astro.props;
const { Content } = await entry.render();
const c = entry.data;
---

<MarketingLayout title={'Silence vs ' + c.competitor} description={c.description}>
  <section class="relative bg-[#0A0A14] section-padding">
    <div class="mx-auto max-w-4xl">
      <a href="/" class="inline-flex items-center gap-2 text-sm text-slate-500 hover:text-slate-300 mb-8 transition-colors">
        <i class="fa-solid fa-arrow-left text-xs" aria-hidden="true"></i> Home
      </a>

      <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-5">
        Silence <span class="text-slate-600">vs</span> {c.competitor}
      </h1>
      <p class="text-slate-400 text-lg mb-12">{c.description}</p>

      <!-- Comparison table -->
      <div class="overflow-x-auto mb-16">
        <table class="w-full text-sm border-collapse">
          <thead>
            <tr class="border-b border-white/10">
              <th class="text-left py-3 pr-6 text-slate-400 font-semibold w-1/2">Feature</th>
              <th class="py-3 px-4 text-center">
                <span class="text-violet-400 font-bold">Silence</span>
              </th>
              <th class="py-3 px-4 text-center">
                <span class="text-slate-400 font-semibold">{c.competitor}</span>
              </th>
            </tr>
          </thead>
          <tbody>
            {c.features.map((row) => (
              <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                <td class="py-3 pr-6 text-slate-300">
                  {row.name}
                  {row.note && <p class="text-xs text-slate-600 mt-0.5">{row.note}</p>}
                </td>
                <td class="py-3 px-4 text-center">
                  {row.silence ? (
                    <i class="fa-solid fa-circle-check text-violet-400" aria-label="Yes"></i>
                  ) : (
                    <i class="fa-solid fa-circle-xmark text-slate-600" aria-label="No"></i>
                  )}
                </td>
                <td class="py-3 px-4 text-center">
                  {row.competitor ? (
                    <i class="fa-solid fa-circle-check text-slate-400" aria-label="Yes"></i>
                  ) : (
                    <i class="fa-solid fa-circle-xmark text-slate-600" aria-label="No"></i>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <!-- Verdict -->
      <div class="p-8 rounded-2xl border border-violet-500/20 bg-violet-500/5 mb-12">
        <h2 class="text-lg font-bold text-white mb-3">The verdict</h2>
        <p class="text-slate-300 leading-relaxed">{c.verdict}</p>
      </div>

      <!-- MDX extended content -->
      {entry.body.trim() && (
        <div class="prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400 prose-code:text-violet-300 prose-code:bg-white/5 mb-12">
          <Content />
        </div>
      )}

      <!-- CTA -->
      <div class="flex flex-col sm:flex-row gap-4">
        <a href="/demo" class="inline-flex items-center justify-center gap-2 px-8 py-3.5 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
          <i class="fa-solid fa-calendar-check" aria-hidden="true"></i> Request Demo
        </a>
        <a href="/features" class="inline-flex items-center justify-center gap-2 px-8 py-3.5 text-sm font-semibold text-slate-300 rounded-xl border border-white/10 hover:bg-white/5 hover:text-white transition-all duration-200">
          See all features
        </a>
      </div>
    </div>
  </section>
</MarketingLayout>
""")

# ── privacy.astro ────────────────────────────────────────────────────────────
write(f'{PAGES}/privacy.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';
---

<MarketingLayout title="Privacy Policy" description="Silence privacy policy — how we collect, use and protect your data." noindex={false}>
  <div class="mx-auto max-w-3xl section-padding">
    <h1 class="text-3xl font-extrabold text-white mb-4">Privacy Policy</h1>
    <p class="text-sm text-slate-500 mb-10">Last updated: January 1, 2026</p>
    <div class="prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400 prose-code:text-violet-300">
      <p>This Privacy Policy describes how Silence ("we", "us", "our") collects, uses and shares information when you use our services.</p>
      <h2>Information we collect</h2>
      <p>We collect information you provide directly to us, such as when you create an account, request a demo or contact us. This may include your name, email address, company name and usage data.</p>
      <h2>How we use your information</h2>
      <p>We use the information we collect to provide, maintain and improve our services, communicate with you, and comply with legal obligations.</p>
      <h2>Data sharing</h2>
      <p>We do not sell your personal data. We may share information with service providers who assist in operating our platform, subject to appropriate data processing agreements.</p>
      <h2>Data residency</h2>
      <p>Enterprise customers can choose the region where their data is stored and processed. Data does not leave the selected region without explicit consent.</p>
      <h2>Your rights</h2>
      <p>Depending on your location, you may have rights to access, correct, delete or export your personal data. Contact us at <a href="mailto:privacy@silence.ai">privacy@silence.ai</a> to exercise these rights.</p>
      <h2>Contact</h2>
      <p>For privacy-related queries, email <a href="mailto:privacy@silence.ai">privacy@silence.ai</a>.</p>
    </div>
  </div>
</MarketingLayout>
""")

# ── terms.astro ──────────────────────────────────────────────────────────────
write(f'{PAGES}/terms.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';
---

<MarketingLayout title="Terms of Service" description="Silence terms of service — the agreement governing use of the Silence platform.">
  <div class="mx-auto max-w-3xl section-padding">
    <h1 class="text-3xl font-extrabold text-white mb-4">Terms of Service</h1>
    <p class="text-sm text-slate-500 mb-10">Last updated: January 1, 2026</p>
    <div class="prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400">
      <p>By accessing or using Silence, you agree to be bound by these Terms of Service.</p>
      <h2>Use of service</h2>
      <p>You may use Silence only in compliance with these terms and all applicable laws. You are responsible for all activity that occurs under your account.</p>
      <h2>Intellectual property</h2>
      <p>Silence and its licensors own all rights to the platform. You retain ownership of all data you upload or create using Silence.</p>
      <h2>Termination</h2>
      <p>We may suspend or terminate your access to Silence if you violate these terms. You may terminate your account at any time by contacting us.</p>
      <h2>Limitation of liability</h2>
      <p>To the maximum extent permitted by law, Silence is not liable for indirect, incidental or consequential damages arising from your use of the service.</p>
      <h2>Contact</h2>
      <p>For legal queries, email <a href="mailto:legal@silence.ai">legal@silence.ai</a>.</p>
    </div>
  </div>
</MarketingLayout>
""")

# ── cookies.astro ────────────────────────────────────────────────────────────
write(f'{PAGES}/cookies.astro', """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';
---

<MarketingLayout title="Cookie Policy" description="Silence cookie policy — how we use cookies and tracking technologies on silence.ai.">
  <div class="mx-auto max-w-3xl section-padding">
    <h1 class="text-3xl font-extrabold text-white mb-4">Cookie Policy</h1>
    <p class="text-sm text-slate-500 mb-10">Last updated: January 1, 2026</p>
    <div class="prose prose-invert prose-slate max-w-none prose-headings:font-bold prose-a:text-violet-400">
      <p>Silence uses cookies and similar technologies to operate the website and improve your experience.</p>
      <h2>What are cookies?</h2>
      <p>Cookies are small files stored on your device when you visit a website. They help us remember your preferences and understand how the site is used.</p>
      <h2>Types of cookies we use</h2>
      <ul>
        <li><strong>Essential cookies</strong> — required for the site to function.</li>
        <li><strong>Analytics cookies</strong> — help us understand how visitors use the site (aggregated, anonymised).</li>
        <li><strong>Marketing cookies</strong> — used to measure ad campaign effectiveness. Only set with your consent.</li>
      </ul>
      <h2>Managing cookies</h2>
      <p>You can control cookies via your browser settings. Disabling certain cookies may affect site functionality.</p>
      <h2>Contact</h2>
      <p>For cookie-related queries, email <a href="mailto:privacy@silence.ai">privacy@silence.ai</a>.</p>
    </div>
  </div>
</MarketingLayout>
""")

# ── robots.txt ───────────────────────────────────────────────────────────────
write(f'{BASE}/../public/robots.txt', """\
User-agent: *
Allow: /
Disallow: /404

Sitemap: https://silence.ai/sitemap-index.xml
""")

# ── favicon.svg ──────────────────────────────────────────────────────────────
write(f'{BASE}/../public/favicon.svg', """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#6D28D9"/>
    </linearGradient>
  </defs>
  <rect width="32" height="32" rx="8" fill="url(#g)"/>
  <path d="M16 6L6 11l10 5 10-5-10-5zM6 21l10 5 10-5M6 16l10 5 10-5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>
""")

print("\nAll pages written successfully!")
