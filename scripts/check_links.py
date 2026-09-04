#!/usr/bin/env python3
"""List internal /ToscaBase/... links in src/content/docs that have no page in dist/. Run after `npm run build`."""
import glob, os, re
missing: dict[str, set[str]] = {}
for f in glob.glob('src/content/docs/**/*.md*', recursive=True):
    for m in re.finditer(r'\]\((/ToscaBase/[^)#\s]*)', open(f, encoding='utf-8').read()):
        rel = m.group(1).rstrip('/')[len('/ToscaBase'):].lstrip('/')
        if not (os.path.exists(f'dist/{rel}/index.html') or os.path.exists(f'dist/{rel}')):
            missing.setdefault(m.group(1), set()).add(f)
print(f'{len(missing)} missing link targets')
for p, fs in sorted(missing.items()):
    print(f'{p}  <- {len(fs)} file(s): {sorted(fs)[0]}')
