"""Script to write large Astro page files that can't be written via terminal heredoc."""
import os

BASE = '/Users/bs01004/silence-website/src/pages'
os.makedirs(BASE, exist_ok=True)

# ─── index.astro ────────────────────────────────────────────────────────────
index = """\
---
import MarketingLayout from '../layouts/MarketingLayout.astro';

const modules = [
  { icon: 'fa-solid fa-folder-open', label: 'Workspace', desc: 'Files, docs & spreadsheets', href: '/modules/workspace' },
  { icon: 'fa-solid fa-comments', label: 'Communication', desc: 'Chat, email & video', href: '/modules/communication' },
  { icon: 'fa-solid fa-diagram-project', label: 'Projects', desc: 'Tasks, boards & sprints', href: '/modules/projects' },
  { icon: 'fa-solid fa-handshake', label: 'CRM', desc: 'Pipeline, contacts & deals', href: '/modules/crm' },
  { icon: 'fa-solid fa-users', label: 'HR', desc: 'Payroll, recruitment & attendance', href: '/modules/hr' },
  { icon: 'fa-solid fa-file-invoice-dollar', label: 'Finance', desc: 'Invoicing & accounting', href: '/modules/finance' },
  { icon: 'fa-solid fa-boxes-stacking', label: 'Operations', desc: 'Inventory & procurement', href: '/modules/operations' },
  { icon: 'fa-solid fa-robot', label: 'AI & Automation', desc: 'Workflows, RPA & smart actions', href: '/modules/ai-automation' },
  { icon: 'fa-solid fa-plug', label: 'Integrations Hub', desc: 'Third-party connectors', href: '/modules/integrations' },
  { icon: 'fa-solid fa-shield-halved', label: 'Admin', desc: 'Multi-tenancy, SSO & permissions', href: '/modules/admin' },
];
const integrations = [
  { name: 'Slack', icon: 'fa-brands fa-slack' },
  { name: 'Microsoft 365', icon: 'fa-brands fa-microsoft' },
  { name: 'Google Workspace', icon: 'fa-brands fa-google' },
  { name: 'Salesforce', icon: 'fa-solid fa-cloud' },
  { name: 'SAP', icon: 'fa-solid fa-database' },
];
const stats = [
  { value: '10+', label: 'Integrated Modules' },
  { value: '500+', label: 'Integrations' },
  { value: '99.9%', label: 'Uptime SLA' },
  { value: '100%', label: 'Multi-tenant' },
];
const testimonials = [
  { quote: 'Silence replaced seven different tools. Our team is more productive and nothing falls through the cracks anymore.', author: 'Sarah Chen', role: 'CTO, Meridian Group', initials: 'SC' },
  { quote: 'The AI automation features alone saved us 40 hours a week in manual data entry and report generation.', author: 'Markus Bauer', role: 'Head of Operations, Nexova AG', initials: 'MB' },
  { quote: 'Finally, an enterprise platform that actually feels modern. Onboarding was smooth and support is outstanding.', author: 'Priya Nair', role: 'VP Product, Luminary Corp', initials: 'PN' },
];
---

<MarketingLayout title="Silence" description="AI-powered enterprise automation. The all-in-one platform to go paperless and fully automate any enterprise or SME.">

  <!-- HERO -->
  <section class="relative overflow-hidden bg-[#0A0A14]" aria-label="Hero">
    <div class="absolute inset-0 overflow-hidden pointer-events-none" aria-hidden="true">
      <div class="absolute top-[-20%] left-1/2 -translate-x-1/2 h-[600px] w-[900px] rounded-full bg-violet-600/10 blur-[120px]"></div>
      <div class="absolute bottom-0 left-0 h-[300px] w-[500px] rounded-full bg-purple-800/10 blur-[100px]"></div>
      <div class="absolute top-1/4 right-0 h-[400px] w-[400px] rounded-full bg-sky-800/10 blur-[120px]"></div>
    </div>
    <div class="relative mx-auto max-w-7xl section-padding text-center">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-violet-500/30 bg-violet-500/10 text-violet-300 text-sm font-medium mb-8">
        <i class="fa-solid fa-bolt text-violet-400" aria-hidden="true"></i>
        AI-Powered Enterprise Automation
      </div>
      <h1 class="text-5xl md:text-6xl lg:text-7xl font-extrabold tracking-tight leading-[1.08] mb-6">
        <span class="text-white">One platform.</span><br />
        <span class="text-gradient">Every workflow.</span>
      </h1>
      <p class="text-lg md:text-xl text-slate-400 max-w-2xl mx-auto mb-10 leading-relaxed">
        Silence replaces Google Workspace, Jira, Microsoft 365 and dozens of other tools — bringing all your enterprise operations into a single AI-native platform.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
        <a href="/demo" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-3.5 text-base font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm shadow-lg">
          <i class="fa-solid fa-calendar-check" aria-hidden="true"></i>
          Request Demo
        </a>
        <a href="/features" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-3.5 text-base font-semibold text-slate-300 rounded-xl border border-white/10 hover:bg-white/5 hover:text-white transition-all duration-200">
          Explore Features <i class="fa-solid fa-arrow-right text-sm" aria-hidden="true"></i>
        </a>
      </div>
      <!-- Product visual placeholder -->
      <div class="relative mx-auto max-w-5xl rounded-2xl border border-white/10 bg-gradient-to-b from-[#111122] to-[#0d0d1e] overflow-hidden shadow-2xl shadow-black/60">
        <div class="flex items-center gap-2 px-4 py-3 border-b border-white/5">
          <span class="h-3 w-3 rounded-full bg-red-500/60"></span>
          <span class="h-3 w-3 rounded-full bg-yellow-500/60"></span>
          <span class="h-3 w-3 rounded-full bg-green-500/60"></span>
        </div>
        <div class="aspect-[16/9] flex items-center justify-center bg-gradient-to-br from-[#111122] to-[#0d0d1e]">
          <div class="text-center">
            <div class="inline-flex items-center justify-center h-20 w-20 rounded-2xl bg-violet-500/10 border border-violet-500/20 mb-4">
              <i class="fa-solid fa-display text-3xl text-violet-400" aria-hidden="true"></i>
            </div>
            <p class="text-slate-500 text-sm">Product screenshot / demo video</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- STATS -->
  <section class="border-y border-white/5 bg-[#0C0C1A]" aria-label="Key metrics">
    <div class="mx-auto max-w-7xl px-6 py-12">
      <dl class="grid grid-cols-2 md:grid-cols-4 gap-8">
        {stats.map((stat) => (
          <div class="text-center">
            <dt class="text-3xl md:text-4xl font-extrabold text-gradient">{stat.value}</dt>
            <dd class="mt-1 text-sm text-slate-500">{stat.label}</dd>
          </div>
        ))}
      </dl>
    </div>
  </section>

  <!-- MODULES -->
  <section class="bg-[#0A0A14] section-padding" aria-labelledby="modules-heading">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Everything in one place</p>
        <h2 id="modules-heading" class="text-3xl md:text-4xl font-bold text-white mb-4">Every module your business needs</h2>
        <p class="text-slate-400 max-w-xl mx-auto">From HR and finance to project management and AI automation — all under one roof.</p>
      </div>
      <ul class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4" role="list">
        {modules.map((mod) => (
          <li>
            <a href={mod.href} class="group flex flex-col p-6 rounded-2xl border border-white/5 bg-white/[0.02] hover:bg-violet-500/5 hover:border-violet-500/20 transition-all duration-200">
              <div class="h-10 w-10 rounded-xl bg-violet-500/10 flex items-center justify-center mb-4 group-hover:bg-violet-500/20 transition-colors">
                <i class={mod.icon + ' text-violet-400'} aria-hidden="true"></i>
              </div>
              <h3 class="text-sm font-semibold text-white mb-1">{mod.label}</h3>
              <p class="text-xs text-slate-500 leading-relaxed">{mod.desc}</p>
            </a>
          </li>
        ))}
      </ul>
      <div class="text-center mt-10">
        <a href="/modules" class="inline-flex items-center gap-2 text-sm text-violet-400 hover:text-violet-300 font-medium transition-colors">
          View all modules <i class="fa-solid fa-arrow-right text-xs" aria-hidden="true"></i>
        </a>
      </div>
    </div>
  </section>

  <!-- AI VALUE PROP -->
  <section class="bg-[#0C0C1A] section-padding" aria-labelledby="ai-heading">
    <div class="mx-auto max-w-7xl grid lg:grid-cols-2 gap-16 items-center">
      <div>
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Powered by AI</p>
        <h2 id="ai-heading" class="text-3xl md:text-4xl font-bold text-white mb-6 leading-tight">
          Automation that thinks.<br /><span class="text-gradient">Not just executes.</span>
        </h2>
        <p class="text-slate-400 leading-relaxed mb-8">
          Silence embeds AI across every module — automatically categorise documents, draft emails, generate reports and build complex workflows without writing a single line of code.
        </p>
        <ul class="space-y-4">
          <li class="flex items-start gap-3">
            <span class="h-6 w-6 rounded-lg bg-violet-500/10 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-wand-magic-sparkles text-violet-400 text-xs" aria-hidden="true"></i></span>
            <span class="text-sm text-slate-300">Smart document processing and extraction</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="h-6 w-6 rounded-lg bg-violet-500/10 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-arrows-spin text-violet-400 text-xs" aria-hidden="true"></i></span>
            <span class="text-sm text-slate-300">Visual workflow builder with AI suggestions</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="h-6 w-6 rounded-lg bg-violet-500/10 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-chart-line text-violet-400 text-xs" aria-hidden="true"></i></span>
            <span class="text-sm text-slate-300">Predictive analytics across all modules</span>
          </li>
          <li class="flex items-start gap-3">
            <span class="h-6 w-6 rounded-lg bg-violet-500/10 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-robot text-violet-400 text-xs" aria-hidden="true"></i></span>
            <span class="text-sm text-slate-300">RPA bots for repetitive tasks</span>
          </li>
        </ul>
        <div class="mt-10">
          <a href="/modules/ai-automation" class="inline-flex items-center gap-2 px-6 py-3 text-sm font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-sm">
            Explore AI Module <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
          </a>
        </div>
      </div>
      <div class="relative">
        <div class="rounded-2xl border border-white/10 bg-[#111122] p-6 space-y-3">
          <div class="flex items-center gap-3 p-3 rounded-xl bg-white/[0.03] border border-white/5">
            <span class="h-2.5 w-2.5 rounded-full bg-green-400 shrink-0"></span>
            <span class="text-sm text-slate-300 flex-1">Invoice processed automatically</span>
            <span class="text-xs text-slate-600">just now</span>
          </div>
          <div class="flex items-center gap-3 p-3 rounded-xl bg-white/[0.03] border border-white/5">
            <span class="h-2.5 w-2.5 rounded-full bg-violet-400 animate-pulse shrink-0"></span>
            <span class="text-sm text-slate-300 flex-1">Workflow triggered: Onboarding</span>
            <span class="text-xs text-slate-600">2s ago</span>
          </div>
          <div class="flex items-center gap-3 p-3 rounded-xl bg-white/[0.03] border border-white/5">
            <span class="h-2.5 w-2.5 rounded-full bg-amber-400 shrink-0"></span>
            <span class="text-sm text-slate-300 flex-1">Anomaly detected in Q3 expenses</span>
            <span class="text-xs text-slate-600">1m ago</span>
          </div>
          <div class="flex items-center gap-3 p-3 rounded-xl bg-white/[0.03] border border-white/5">
            <span class="h-2.5 w-2.5 rounded-full bg-green-400 shrink-0"></span>
            <span class="text-sm text-slate-300 flex-1">Monthly summary report generated</span>
            <span class="text-xs text-slate-600">3m ago</span>
          </div>
        </div>
        <div class="absolute -inset-4 -z-10 rounded-3xl bg-violet-600/5 blur-2xl"></div>
      </div>
    </div>
  </section>

  <!-- INTEGRATIONS -->
  <section class="bg-[#0A0A14] section-padding" aria-labelledby="integrations-heading">
    <div class="mx-auto max-w-7xl text-center">
      <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Works with everything</p>
      <h2 id="integrations-heading" class="text-3xl md:text-4xl font-bold text-white mb-4">Seamless integrations</h2>
      <p class="text-slate-400 max-w-xl mx-auto mb-12">Connect Silence to the tools you already use. 500+ integrations available out of the box.</p>
      <div class="flex flex-wrap items-center justify-center gap-4 mb-10">
        {integrations.map((item) => (
          <div class="flex items-center gap-3 px-6 py-3 rounded-xl border border-white/10 bg-white/[0.02] hover:bg-white/5 transition-colors">
            <i class={item.icon + ' text-xl text-slate-400'} aria-hidden="true"></i>
            <span class="text-sm font-medium text-slate-300">{item.name}</span>
          </div>
        ))}
      </div>
      <a href="/integrations" class="inline-flex items-center gap-2 text-sm text-violet-400 hover:text-violet-300 font-medium transition-colors">
        Browse all integrations <i class="fa-solid fa-arrow-right text-xs" aria-hidden="true"></i>
      </a>
    </div>
  </section>

  <!-- TESTIMONIALS -->
  <section class="bg-[#0C0C1A] section-padding" aria-labelledby="testimonials-heading">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-16">
        <p class="text-violet-400 text-sm font-semibold uppercase tracking-wider mb-3">Customer stories</p>
        <h2 id="testimonials-heading" class="text-3xl md:text-4xl font-bold text-white">Trusted by teams worldwide</h2>
      </div>
      <ul class="grid grid-cols-1 md:grid-cols-3 gap-6" role="list">
        {testimonials.map((t) => (
          <li class="flex flex-col p-8 rounded-2xl border border-white/5 bg-white/[0.02]">
            <div class="flex gap-1 mb-4" aria-label="5 out of 5 stars">
              <i class="fa-solid fa-star text-amber-400 text-sm" aria-hidden="true"></i>
              <i class="fa-solid fa-star text-amber-400 text-sm" aria-hidden="true"></i>
              <i class="fa-solid fa-star text-amber-400 text-sm" aria-hidden="true"></i>
              <i class="fa-solid fa-star text-amber-400 text-sm" aria-hidden="true"></i>
              <i class="fa-solid fa-star text-amber-400 text-sm" aria-hidden="true"></i>
            </div>
            <blockquote class="flex-1">
              <p class="text-slate-300 leading-relaxed text-sm">"{t.quote}"</p>
            </blockquote>
            <footer class="mt-6 flex items-center gap-3">
              <div class="h-9 w-9 rounded-full bg-gradient-to-br from-violet-500 to-purple-700 flex items-center justify-center text-white text-xs font-bold shrink-0" aria-hidden="true">{t.initials}</div>
              <div>
                <cite class="text-sm font-semibold text-white not-italic">{t.author}</cite>
                <p class="text-xs text-slate-500">{t.role}</p>
              </div>
            </footer>
          </li>
        ))}
      </ul>
      <div class="text-center mt-10">
        <a href="/customers" class="inline-flex items-center gap-2 text-sm text-violet-400 hover:text-violet-300 font-medium transition-colors">
          Read all case studies <i class="fa-solid fa-arrow-right text-xs" aria-hidden="true"></i>
        </a>
      </div>
    </div>
  </section>

  <!-- FINAL CTA -->
  <section class="relative overflow-hidden bg-[#0A0A14] section-padding" aria-labelledby="cta-heading">
    <div class="absolute inset-0 pointer-events-none" aria-hidden="true">
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-violet-600/5 to-transparent"></div>
    </div>
    <div class="relative mx-auto max-w-3xl text-center">
      <h2 id="cta-heading" class="text-3xl md:text-5xl font-extrabold text-white mb-6 leading-tight">
        Ready to run your entire<br />business on <span class="text-gradient">Silence?</span>
      </h2>
      <p class="text-slate-400 text-lg mb-10">Book a personalised demo and see how Silence can transform your organisation in days, not months.</p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="/demo" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-4 text-base font-semibold text-white rounded-xl bg-gradient-to-r from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500 transition-all duration-200 glow-md shadow-lg">
          <i class="fa-solid fa-calendar-check" aria-hidden="true"></i>
          Request Demo
        </a>
        <a href="/contact" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-4 text-base font-semibold text-slate-300 rounded-xl border border-white/10 hover:bg-white/5 hover:text-white transition-all duration-200">
          Contact Sales
        </a>
      </div>
    </div>
  </section>

</MarketingLayout>
"""

with open(f'{BASE}/index.astro', 'w') as f:
    f.write(index)
print(f"index.astro written: {len(index.splitlines())} lines")
