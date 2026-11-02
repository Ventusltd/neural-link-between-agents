"""Lines of text blobs at HEAD inside a few app folders, counted by the wafer's own rule (count_lines.py:60-61:
NUL in the first 8,000 bytes is binary, else newlines plus one if no trailing newline)."""
import subprocess, sys
def count(repo, prefix):
    ls = subprocess.run(['git','-C',repo,'ls-tree','-r','-z','HEAD',prefix], capture_output=True).stdout.split(b'\0')
    shas = [e.split(b'\t')[0].split(b' ')[2] for e in ls if e]
    p = subprocess.run(['git','-C',repo,'cat-file','--batch'], input=b'\n'.join(shas)+b'\n', capture_output=True).stdout
    i = 0; lines = 0; files = 0; binary = 0
    for sha in shas:
        nl = p.index(b'\n', i); hdr = p[i:nl].split(); size = int(hdr[2]); body = p[nl+1:nl+1+size]; i = nl+1+size+1
        files += 1
        if b'\x00' in body[:8000]: binary += 1; continue
        lines += body.count(b'\n') + (1 if body and not body.endswith(b'\n') else 0)
    return files, binary, lines
for repo, prefix in [('/home/user/estate/kuiper-belt','see-through/202610050609'), ('/home/user/estate/kuiper-belt','learn-the-kuiper/202610050609'),
                     ('/home/user/estate/kuiper-belt','editions/202611012027'), ('/home/user/estate/testcode','spider/20260914T143049Z-v5-linkify-frontdoor-brandfaithful'),
                     ('/home/user/estate/gridatlas','atlas/releases/202608300453-atlas-v9'), ('/home/user/estate/gridatlas','atlas/cartridges'), ('/home/user/estate/elements','')]:
    f, b, l = count(repo, prefix); print(f'{repo.split("/")[-1]}/{prefix}: files {f}, binary {b}, text lines {l}')
