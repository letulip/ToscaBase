#!/usr/bin/env python3
"""Fill `docs` in raw/manifest.json from the `sources` frontmatter of every EN doc. Idempotent."""
import glob, json, re
manifest_path = 'raw/manifest.json'
m = json.load(open(manifest_path, encoding='utf-8'))
by_id = {v['id']: v for v in m['videos']}
for v in m['videos']:
    v['docs'] = []
unknown = set()
for f in sorted(glob.glob('src/content/docs/**/*.md', recursive=True)):
    if '/docs/ru/' in f:
        continue
    fm = re.match(r'---\n(.*?)\n---', open(f, encoding='utf-8').read(), re.S)
    if not fm:
        continue
    rel = f.replace('src/content/docs/', '').removesuffix('.md')
    for vid in re.findall(r'^\s*-\s*id:\s*"?([A-Za-z0-9_-]{11})"?', fm.group(1), re.M):
        if vid in by_id:
            if rel not in by_id[vid]['docs']:
                by_id[vid]['docs'].append(rel)
        else:
            unknown.add(vid)
json.dump(m, open(manifest_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open(manifest_path, 'a').write('\n')
with_docs = sum(1 for v in m['videos'] if v['docs'])
print(f'{with_docs}/{len(m["videos"])} videos linked to docs; unknown ids in docs: {sorted(unknown) or "none"}')
print('videos without docs:', [v['id'] for v in m['videos'] if not v['docs']])
