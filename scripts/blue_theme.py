"""
Replace violet/purple brand colors with blue across all Astro files and global.css.
Blue brand palette: blue-600 as primary, blue-700 as deep, cyan-500 as accent.
Run: python3 /Users/bs01004/silence-website/scripts/blue_theme.py
"""
import os, glob

BASE = '/Users/bs01004/silence-website/src'

def transform(content):
    replacements = [
        # ── Gradient buttons (multi-token, process FIRST) ────────────────────
        ('from-violet-600 to-purple-600 hover:from-violet-500 hover:to-purple-500',
         'from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600'),
        ('from-violet-500 to-purple-700',   'from-blue-500 to-blue-700'),
        ('from-violet-500 to-purple-600',   'from-blue-500 to-blue-600'),
        ('from-violet-600 to-purple-600',   'from-blue-600 to-blue-700'),

        # ── Named prose hover combos (must come before single-token) ─────────
        ('prose-a:text-blue-600 hover:prose-a:text-blue-700',
         'prose-a:text-blue-600 hover:prose-a:text-blue-700'),  # already correct if run twice

        # ── Violet → blue (each shade) ───────────────────────────────────────
        ('violet-50',   'blue-50'),
        ('violet-100',  'blue-100'),
        ('violet-200',  'blue-200'),
        ('violet-300',  'blue-300'),
        ('violet-400',  'blue-400'),
        ('violet-500',  'blue-500'),
        ('violet-600',  'blue-600'),
        ('violet-700',  'blue-700'),
        ('violet-900',  'blue-900'),

        # ── Purple → blue ────────────────────────────────────────────────────
        ('purple-400',  'blue-400'),
        ('purple-500',  'blue-500'),
        ('purple-600',  'blue-600'),
        ('purple-700',  'blue-700'),
    ]

    for old, new in replacements:
        content = content.replace(old, new)
    return content


# ── Astro files ──────────────────────────────────────────────────────────────
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

# ── global.css ───────────────────────────────────────────────────────────────
css_path = f'{BASE}/styles/global.css'
with open(css_path) as f:
    css = f.read()

css = (css
    .replace('--color-brand-primary: #6C3CE1;',    '--color-brand-primary: #2563EB;')
    .replace('--color-brand-secondary: #7C3AED;',  '--color-brand-secondary: #1D4ED8;')
    # gradient: blue-600 → blue-500 → cyan-500
    .replace('from-violet-600 via-purple-600 to-sky-600', 'from-blue-600 via-blue-500 to-cyan-500')
    # violet variants in global.css
    .replace('violet-200', 'blue-200')
    .replace('violet-900', 'blue-900')
    # glow shadows: violet-600 rgb(108,60,225) → blue-600 rgb(37,99,235)
    .replace('rgba(108, 60, 225, 0.25)', 'rgba(37, 99, 235, 0.25)')
    .replace('rgba(108, 60, 225, 0.35)', 'rgba(37, 99, 235, 0.35)')
)

with open(css_path, 'w') as f:
    f.write(css)
print(f'  updated  styles/global.css')

print(f'\nDone — {changed} Astro files + global.css updated.')
