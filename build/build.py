import markdown, re, sys, html
src = open(sys.argv[1], encoding='utf-8').read()
src = src.replace("Oct 30, 2026 · @Arihant Jain", "Updated Oct 30, 2026 · Free & FOSS only · Built for Debian 13 / Plasma 6.3")
body = src.split('\n',1)[1]  # drop H1
md = markdown.Markdown(extensions=['tables','fenced_code','toc','sane_lists'], extension_configs={'toc':{'toc_depth':'2-2'}})
content = md.convert(body)
# external links open new tab
content = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', content)
# wrap tables
content = content.replace('<table>', '<div class="tw"><table>').replace('</table>', '</table></div>')
# wrap sections
parts = re.split(r'(?=<h2 )', content)
out=[]
for p in parts:
    if p.startswith('<h2 '):
        out.append('<section class="card">'+p+'</section>')
    else:
        out.append('<div class="lead">'+p+'</div>')
content = '\n'.join(out)
toc = []
for t in md.toc_tokens:
    name = t['name']
    m = re.match(r'(\d\d) // (.*)', name)
    num, label = (m.group(1), m.group(2)) if m else ('##', name)
    label = re.sub(r'\s*\(.*?\)\s*$', '', label)
    toc.append(f'<a href="#{t["id"]}"><span class="n">{num}</span>{label}</a>')
tpl = open(sys.argv[2], encoding='utf-8').read()
open(sys.argv[3],'w',encoding='utf-8').write(tpl.replace('%%TOC%%','\n'.join(toc)).replace('%%CONTENT%%',content))
