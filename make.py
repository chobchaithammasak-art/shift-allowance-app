import os

def svg(body,defs=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512"><defs>{defs}</defs>{body}</svg>'
def grad(id,c1,c2):
    return f'<linearGradient id="{id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
def pin(cx,cy,s,fill='#fff',dot='#0F766E'):
    # map pin, tip at (cx,cy+s)
    return (f'<g transform="translate({cx},{cy})"><path d="M0,{s} C{-s*0.9},{s*0.1} {-s*0.75},{-s*0.95} 0,{-s*0.95} C{s*0.75},{-s*0.95} {s*0.9},{s*0.1} 0,{s} Z" fill="{fill}"/>'
            f'<circle cx="0" cy="{-s*0.28}" r="{s*0.32}" fill="{dot}"/></g>')
BAHT='M755 -301H593V0H127V1314H593V1556H755V1313Q997 1303 1114 1231Q1248 1148 1248 966Q1248 870 1199.0 803.0Q1150 736 1057 703Q1176 671 1242 586Q1307 501 1307 377Q1307 187 1167 93Q1030 2 755 0ZM593 221V565H484V221ZM755 562V224Q827 232 869 264Q925 307 925 394Q925 480 869 522Q828 554 755 562ZM593 796V1074H484V796ZM755 1067V802Q795 810 821 831Q866 866 866 935Q866 1002 821 1038Q795 1059 755 1067Z'
def baht(x,y,size,fill,w=800):
    sc=size/2048
    return f'<path transform="translate({x-1425*sc/2:.1f},{y}) scale({sc:.5f},{-sc:.5f})" d="{BAHT}" fill="{fill}"/>'
# ---------- Style A : clock + coin ----------
def clock(cx,cy,r,bg='#fff',fg='#1F4E78'):
    t=''
    import math
    for i in range(12):
        a=math.radians(i*30); l=r*0.14 if i%3 else r*0.22
        x1=cx+math.sin(a)*(r*0.86); y1=cy-math.cos(a)*(r*0.86)
        x2=cx+math.sin(a)*(r*0.86-l); y2=cy-math.cos(a)*(r*0.86-l)
        t+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{fg}" stroke-width="{10 if i%3==0 else 6}" stroke-linecap="round"/>'
    t+=f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-r*0.5}" stroke="{fg}" stroke-width="14" stroke-linecap="round"/>'
    t+=f'<line x1="{cx}" y1="{cy}" x2="{cx+r*0.36}" y2="{cy+r*0.2}" stroke="{fg}" stroke-width="14" stroke-linecap="round"/>'
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg}"/>'+t+f'<circle cx="{cx}" cy="{cy}" r="11" fill="{fg}"/>'
def A(c1,c2,gps):
    b=f'<rect width="512" height="512" fill="url(#g)"/>'
    b+=clock(240,246,132,'#fff',c1)
    b+='<circle cx="352" cy="356" r="82" fill="#F5A623" stroke="#fff" stroke-width="12"/>'+baht(352,392,104,'#fff')
    if gps: b+=pin(384,126,62,'#fff',c1)
    return svg(b,grad('g',c1,c2))
# ---------- Style B : sun / moon ----------
def B(c1,c2,gps):
    import math
    b='<rect width="512" height="512" fill="url(#g)"/>'
    # circle split: left sun, right moon
    b+='<clipPath id="L"><rect x="0" y="0" width="256" height="512"/></clipPath><clipPath id="R"><rect x="256" y="0" width="256" height="512"/></clipPath>'
    b+='<circle cx="256" cy="256" r="150" fill="#FFD166" clip-path="url(#L)"/>'
    b+='<circle cx="256" cy="256" r="150" fill="#E9EEF7" clip-path="url(#R)"/>'
    b+='<circle cx="300" cy="226" r="112" fill="#223a63" clip-path="url(#R)"/>'
    b+='<circle cx="256" cy="256" r="150" fill="none" stroke="#fff" stroke-width="10"/>'
    for i in range(7):
        a=math.radians(100+i*27); x1=256+math.cos(a)*172; y1=256+math.sin(a)*172; x2=256+math.cos(a)*208; y2=256+math.sin(a)*208
        b+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#FFD166" stroke-width="14" stroke-linecap="round"/>'
    b+='<circle cx="256" cy="256" r="46" fill="#fff"/>'+baht(256,290,76,'#1F4E78')
    if gps: b+=pin(396,112,58,'#fff','#223a63')
    return svg(b,grad('g',c1,c2))
# ---------- Style C : bold baht monogram ----------
def C(c1,c2,gps):
    b='<rect width="512" height="512" fill="url(#g)"/>'
    b+='<circle cx="256" cy="236" r="160" fill="#fff" opacity="0.16"/>'
    b+=baht(256,318,300,'#fff')
    # check-list ticks bar
    b+='<rect x="136" y="392" width="240" height="22" rx="11" fill="#fff" opacity=".9"/>'
    if gps: b+=pin(398,118,62,'#FFD166',c1)
    else:  b+='<path d="M366 96 l30 32 l56 -64" transform="translate(-10,0)" fill="none" stroke="#FFD166" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'
    return svg(b,grad('g',c1,c2))
SVGS={}
sets={
 'A':(A,('#1F4E78','#163A5A'),('#0F766E','#0B4F4A')),
 'B':(B,('#2D5BA8','#1B2F5C'),('#0E8A7D','#0A4D58')),
 'C':(C,('#F08A24','#C85A0A'),('#334155','#0F172A')),
}
RECT='<rect width="512" height="512" fill="url(#g)"/>'
def mask(full):
    i=full.index(RECT)+len(RECT); j=full.rindex('</svg>')
    return full[:i]+'<g transform="translate(51.2 51.2) scale(0.8)">'+full[i:j]+'</g></svg>'
for k,(fn,v1,v2) in sets.items():
    for v,col,gps in (('v1',v1,False),('v2',v2,True)):
        t=fn(*col,gps)
        SVGS[f'{k}-{v}']=t
        SVGS[f'{k}-{v}-mask']=mask(t)


# ===================== เว็บไซต์ =====================
import json,subprocess,shutil
PAGE='<!doctype html>\n<html lang="th"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<title>@NAME@</title>\n<link rel="manifest" href="manifest.webmanifest">\n<meta name="theme-color" content="@THEME@">\n<link rel="icon" href="../icons/@V@-192.png">\n<link rel="apple-touch-icon" href="../icons/@V@-180.png">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="@SHORT@">\n<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n<style>\n:root{--theme:@THEME@;--bg:#f3f5f8;--text:#1d2733;--muted:#5f6b7a;--card:#fff;--line:#d6dce4}\n@media(prefers-color-scheme:dark){:root{--bg:#10151c;--text:#e8edf3;--muted:#9aa7b5;--card:#18202a;--line:#2a3441}}\n*{box-sizing:border-box}body{margin:0;font-family:system-ui,"Sarabun","Noto Sans Thai",sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}\n.card{width:100%;max-width:420px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:28px 22px;text-align:center}\n.card img{width:112px;height:112px;border-radius:25px;box-shadow:0 6px 18px rgba(0,0,0,.18)}\nh1{font-size:21px;margin:16px 0 6px}p{color:var(--muted);font-size:15px;line-height:1.55;margin:4px 0}\n.btn{display:block;width:100%;padding:14px;margin-top:14px;border:0;border-radius:12px;font:inherit;font-weight:700;font-size:17px;text-decoration:none;cursor:pointer}\n.go{background:var(--theme);color:#fff}.ins{background:transparent;color:var(--theme);border:2px solid var(--theme)}\n.how{text-align:left;margin-top:20px;font-size:14px;color:var(--muted);line-height:1.6}.how b{color:var(--text)}\n.how ol{margin:4px 0 12px;padding-left:20px}\n#redir{display:none}\n</style></head><body>\n<main class="card">\n<img src="../icons/@V@-192.png" alt="">\n<h1>@NAME@</h1>\n<p>@DESC@</p>\n<a class="btn go" id="open" href="@URL@">เปิดระบบ</a>\n<button class="btn ins" id="install" hidden>ติดตั้งลงหน้าจอมือถือ</button>\n<div class="how">\n<b>วิธีใส่ไอคอนบนหน้าจอมือถือ</b>\n<ol><li><b>Android (Chrome):</b> กดเมนู ⋮ &gt; "ติดตั้งแอป" หรือ "เพิ่มลงในหน้าจอหลัก"</li>\n<li><b>iPhone (Safari):</b> กดปุ่มแชร์ &gt; "เพิ่มไปยังหน้าจอโฮม"</li></ol>\nเมื่อเปิดจากไอคอนบนหน้าจอ ระบบจะพาไปหน้าบันทึกข้อมูลโดยอัตโนมัติ\n</div></main>\n<script>\nvar TARGET="@URL@";\nvar standalone=(window.matchMedia&&matchMedia(\'(display-mode: standalone)\').matches)||window.navigator.standalone===true||/[?&]source=pwa/.test(location.search);\nif(standalone){location.replace(TARGET);}\nif(\'serviceWorker\' in navigator){navigator.serviceWorker.register(\'../sw.js\',{scope:\'../\'}).catch(function(){});}\nvar dp=null,b=document.getElementById(\'install\');\nwindow.addEventListener(\'beforeinstallprompt\',function(e){e.preventDefault();dp=e;b.hidden=false;});\nb.addEventListener(\'click\',function(){if(!dp)return;dp.prompt();dp.userChoice.then(function(){dp=null;b.hidden=true;});});\n</script></body></html>\n'
APPS={'v1': {'@NAME@': 'ค่ากะ-เบี้ยเลี้ยง (ฟอร์ม)', '@SHORT@': 'ค่ากะ ฟอร์ม', '@THEME@': '#1F4E78', '@DESC@': 'ระบบ v1 — บันทึกค่ากะ/เบี้ยเลี้ยงวันหยุดด้วย Google Form', '@URL@': 'https://docs.google.com/forms/d/e/1FAIpQLSf44XQ48oDyGGEuOj3bQ9_6kE0t5LriQAls-VZi4pqh10oS3w/viewform'}, 'v2': {'@NAME@': 'ค่ากะ-เบี้ยเลี้ยง GPS', '@SHORT@': 'ค่ากะ GPS', '@THEME@': '#0F766E', '@DESC@': 'ระบบ v2 — บันทึกค่ากะ/เบี้ยเลี้ยงพร้อมพิกัด GPS (เปิดตำแหน่งให้เบราว์เซอร์)', '@URL@': 'https://script.google.com/macros/s/AKfycbwmYohenNWDgWYfx9IJInMkgwCXou7b97f0P09PDAq8VSi8LLOUHF6N8X__wm6dY09_2g/exec'}}
SW="""// minimal service worker (makes the launcher installable)
self.addEventListener('install',function(){self.skipWaiting();});
self.addEventListener('activate',function(e){e.waitUntil(self.clients.claim());});
self.addEventListener('fetch',function(){});
"""
INDEX='<!doctype html>\n<html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n<title>ค่ากะ-เบี้ยเลี้ยง | ติดตั้งลงมือถือ</title>\n<link rel="icon" href="icons/v1-192.png">\n<style>\n:root{--bg:#f3f5f8;--text:#1d2733;--muted:#5f6b7a;--card:#fff;--line:#d6dce4;--navy:#1F4E78}\n@media(prefers-color-scheme:dark){:root{--bg:#10151c;--text:#e8edf3;--muted:#9aa7b5;--card:#18202a;--line:#2a3441;--navy:#6fa8dc}}\n*{box-sizing:border-box}body{margin:0;font-family:system-ui,"Sarabun","Noto Sans Thai",sans-serif;background:var(--bg);color:var(--text);padding:20px}\nmain{max-width:560px;margin:0 auto}h1{font-size:22px}h2{font-size:17px;margin:28px 0 8px}p{color:var(--muted);line-height:1.55}\n.app{display:flex;gap:14px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px;margin:12px 0;text-decoration:none;color:var(--text)}\n.app img{width:72px;height:72px;border-radius:16px;flex:none}.app b{display:block;font-size:17px}.app span{color:var(--muted);font-size:14px}\n.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;text-align:center}.grid img{width:100%;max-width:110px;border-radius:24%}\n.grid small{display:block;color:var(--muted);margin-top:4px}\n</style></head><body><main>\n<h1>ค่ากะ-เบี้ยเลี้ยง</h1>\n<p>เปิดหน้านี้บนมือถือ แล้วเลือกระบบที่ต้องการ จากนั้นทำตามขั้นตอนเพื่อใส่ไอคอนบนหน้าจอ</p>\n<a class="app" href="v1/"><img src="icons/v1-192.png" alt=""><div><b>ระบบ v1 — ฟอร์ม</b><span>บันทึกค่ากะ/เบี้ยเลี้ยงด้วย Google Form</span></div></a>\n<a class="app" href="v2/"><img src="icons/v2-192.png" alt=""><div><b>ระบบ v2 — GPS</b><span>บันทึกพร้อมพิกัด GPS</span></div></a>\n<h2>ไอคอนทั้ง 3 แบบ (สำหรับเลือก)</h2>\n<div class="grid">\n<div><img src="options/A-v1.png" alt=""><img src="options/A-v2.png" alt=""><small>A นาฬิกา + เหรียญ</small></div>\n<div><img src="options/B-v1.png" alt=""><img src="options/B-v2.png" alt=""><small>B เช้า / ดึก</small></div>\n<div><img src="options/C-v1.png" alt=""><img src="options/C-v2.png" alt=""><small>C สัญลักษณ์ ฿</small></div>\n</div>\n</main></body></html>\n'
def w(path,text):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    open(path,'w',encoding='utf-8').write(text)
def render(svg,png,size):
    p='/tmp/_i.svg'; open(p,'w').write(svg)
    subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),p,'-o',png],check=True)
SET=open('icon.txt').read().strip() or 'A'
OUTD='_site'
shutil.rmtree(OUTD,ignore_errors=True)
w(OUTD+'/index.html',INDEX); w(OUTD+'/sw.js',SW); w(OUTD+'/.nojekyll','')
for v,a in APPS.items():
    h=PAGE
    for k,val in a.items(): h=h.replace(k,val)
    h=h.replace('@V@',v)
    w(f'{OUTD}/{v}/index.html',h)
    w(f'{OUTD}/{v}/manifest.webmanifest',json.dumps({"id":"/"+v+"/","name":a['@NAME@'],"short_name":a['@SHORT@'],"description":a['@DESC@'],"lang":"th","start_url":"./?source=pwa","scope":"./","display":"standalone","orientation":"portrait","background_color":"#ffffff","theme_color":a['@THEME@'],"icons":[{"src":"../icons/"+v+"-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"../icons/"+v+"-512.png","sizes":"512x512","type":"image/png","purpose":"any"},{"src":"../icons/"+v+"-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},ensure_ascii=False,indent=1))
    os.makedirs(OUTD+'/icons',exist_ok=True)
    for s in (180,192,512): render(SVGS[SET+'-'+v],f'{OUTD}/icons/{v}-{s}.png',s)
    render(SVGS[SET+'-'+v+'-mask'],f'{OUTD}/icons/{v}-maskable-512.png',512)
os.makedirs(OUTD+'/options',exist_ok=True)
for k in 'ABC':
    for v in ('v1','v2'): render(SVGS[k+'-'+v],f'{OUTD}/options/{k}-{v}.png',256)
print('built set',SET)
