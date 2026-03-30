"""
Convert all Astro files from dark theme to white/light theme.
Run from anywhere: python3 /Users/bs01004/silence-website/scripts/light_theme.py
"""
import os, glob

BASE = '/Users/bs01004/silence-website/src'

def transform(content):
    # ── Step 1: Protect elements that MUST keep text-white ──────────────────
    # CTA gradient buttons (horizontal gradient: bg-gradient-to-r)
    content = content.replace('text-white rounded-xl bg-gradient-to-r', '_PROT_XL_ bg-gradient-to-r')
    content = content.replace('text-white rounded-lg bg-gradient-to-r', '_PROT_LG_ bg-gradient-to-r')
    # Logo/icon SVGs that use text-white as fill color
    content = content.replace('text-white" viewBox="0 0 24 24" fill="currentColor"',
                               '_PROT_SVG_" viewBox="0 0 24 24" fill="currentColor"')

    # ── Step 2: Ordered replacements (more specific / multi-token FIRST) ────
    replacements = [
        # Remove dark mode from html element
        ('lang="en" class="dark"',          'lang="en"'),

        # Dark page / section backgrounds → white / light grays
        ('bg-[#0A0A14]/90',                 'bg-white/95'),
        ('bg-[#0A0A14]',                    'bg-white'),
        ('bg-[#0C0C1A]',                    'bg-slate-50'),
        ('bg-[#111122]',                    'bg-slate-100'),

        # Atmospheric hero glow blobs
        ('bg-violet-600/8',                 'bg-violet-200/30'),

        # Violet opaque backgrounds → named light colors
        ('bg-violet-600/40',                'bg-violet-200'),
        ('bg-violet-500/20',                'bg-violet-100'),
        ('bg-violet-500/10',                'bg-violet-50'),
        ('bg-violet-500/5',                 'bg-violet-50/50'),

        # Violet opaque borders → light named
        ('border-violet-500/20',            'border-violet-200'),
        ('border-violet-500/5',             'border-violet-100'),

        # Green badge variants
        ('bg-green-500/5',                  'bg-green-50'),
        ('border-green-500/20',             'border-green-200'),
        ('text-green-400',                  'text-green-600'),

        # Semi-transparent card / form field backgrounds → light solids
        ('bg-white/[0.02]',                 'bg-white'),
        ('bg-white/5',                      'bg-gray-100'),

        # Hover backgrounds
        ('hover:bg-white/5',                'hover:bg-violet-50'),
        ('hover:bg-violet-500/5',           'hover:bg-violet-50'),
        ('hover:bg-violet-500/20',          'hover:bg-violet-100'),
        ('group-hover:bg-violet-500/20',    'group-hover:bg-violet-100'),

        # Borders (dark transparent → light opaque)
        ('border-white/5',                  'border-gray-200'),
        ('border-white/10',                 'border-gray-200'),

        # Shadows
        ('shadow-2xl shadow-black/50',      'shadow-xl'),

        # ── Prose typography (multi-token rules FIRST) ──────────────────────
        ('prose-invert prose-slate',        'prose-slate'),
        ('prose-invert',                    ''),
        # Combined rule before individual violet replacements fire
        ('prose-a:text-violet-400 hover:prose-a:text-violet-300',
         'prose-a:text-violet-600 hover:prose-a:text-violet-700'),
        ('hover:prose-a:text-violet-300',   'hover:prose-a:text-violet-700'),
        ('prose-a:text-violet-400',         'prose-a:text-violet-600'),
        ('prose-code:bg-white/5',           'prose-code:bg-violet-50'),
        ('prose-h2:border-t prose-h2:border-white/5',
         'prose-h2:border-t prose-h2:border-gray-200'),
        ('prose-pre:border prose-pre:border-white/10',
         'prose-pre:border-gray-200'),
        ('prose-pre:bg-[#0C0C1A]',          'prose-pre:bg-gray-50'),
        ('prose-blockquote:text-slate-400', 'prose-blockquote:text-slate-600'),
        ('prose-hr:border-white/10',        'prose-hr:border-gray-200'),

        # Focus ring (form inputs)
        ('focus:ring-violet-500/50',        'focus:ring-violet-400/40'),
        ('focus:border-violet-500/50',      'focus:border-violet-400'),

        # ── Violet text → higher contrast values for light bg ───────────────
        ('group-hover:text-violet-300',     'group-hover:text-violet-700'),
        ('hover:text-violet-300',           'hover:text-violet-700'),
        ('text-violet-300',                 'text-violet-600'),
        ('text-violet-400',                 'text-violet-600'),
        ('text-violet-500',                 'text-violet-600'),

        # ── White / bright text → dark equivalents ───────────────────────────
        ('hover:text-white',                'hover:text-gray-900'),
        ('text-white',                      'text-slate-900'),

        # ── Slate text — shift entire scale darker for light bg ──────────────
        # Process hover: variants BEFORE bare variants to avoid double-replace
        ('hover:text-slate-200',            'hover:text-slate-900'),
        ('hover:text-slate-300',            'hover:text-slate-700'),
        ('text-slate-100',                  'text-slate-900'),
        ('text-slate-200',                  'text-slate-800'),
        ('text-slate-300',                  'text-slate-700'),
        ('text-slate-400',                  'text-slate-600'),
        # text-slate-500 and text-slate-600 remain unchanged — good on light bg

        # Changelog timeline dot — its border was paired with dark page bg
        ('bg-violet-500 border-4 border-[#0A0A14]', 'bg-violet-500 border-4 border-white'),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    # ── Step 3: Restore protected white text ────────────────────────────────
    content = content.replace('_PROT_XL_ bg-gradient-to-r', 'text-white rounded-xl bg-gradient-to-r')
    content = content.replace('_PROT_LG_ bg-gradient-to-r', 'text-white rounded-lg bg-gradient-to-r')
    content = content.replace('_PROT_SVG_" viewBox="0 0 24 24" fill="currentColor"',
                               'text-white" viewBox="0 0 24 24" fill="currentColor"')
    return content


files = glob.glob(f'{BASE}/**/*.astro', recursive=True)
changed = 0
for fp in sorted(files):
    with open(fp) as f:
        original = f.read()
    updated = transform(original)
    if updated != original:
        with open(fp, 'w') as f:
            f.write(updated)
        print(f'  updated  {os.path.relpath(fp, BASE)}')
        changed += 1
    else:
        print(f'  no-change {os.path.relpath(fp, BASE)}')

print(f'\nDone — {changed}/{len(files)} files updated.')
