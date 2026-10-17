import os, json, subprocess, shutil

BAHT='M755 -301H593V0H127V1314H593V1556H755V1313Q997 1303 1114 1231Q1248 1148 1248 966Q1248 870 1199.0 803.0Q1150 736 1057 703Q1176 671 1242 586Q1307 501 1307 377Q1307 187 1167 93Q1030 2 755 0ZM593 221V565H484V221ZM755 562V224Q827 232 869 264Q925 307 925 394Q925 480 869 522Q828 554 755 562ZM593 796V1074H484V796ZM755 1067V802Q795 810 821 831Q866 866 866 935Q866 1002 821 1038Q795 1059 755 1067Z'
CLT={'C': ['M1372 82Q1266 27 1151.0 -1.0Q1036 -29 911 -29Q538 -29 320.0 179.5Q102 388 102 745Q102 1103 320.0 1311.5Q538 1520 911 1520Q1036 1520 1151.0 1492.0Q1266 1464 1372 1409V1100Q1265 1173 1161.0 1207.0Q1057 1241 942 1241Q736 1241 618.0 1109.0Q500 977 500 745Q500 514 618.0 382.0Q736 250 942 250Q1057 250 1161.0 284.0Q1265 318 1372 391Z', 1503], 'L': ['M188 1493H573V291H1249V0H188Z', 1305], 'T': ['M10 1493H1386V1202H891V0H506V1202H10Z', 1397]}
URL='https://script.google.com/macros/s/AKfycbwmYohenNWDgWYfx9IJInMkgwCXou7b97f0P09PDAq8VSi8LLOUHF6N8X__wm6dY09_2g/exec'
NAME='CLT ค่ากะ-เบี้ยเลี้ยง'; SHORT='CLT ค่ากะ'; THEME='#D9701A'

def glyph(d,x,y,sc,fill):
    return f'<path transform="translate({x:.1f},{y}) scale({sc:.5f},{-sc:.5f})" d="{d}" fill="{fill}"/>'

def icon(mask=False):
    b='<rect width="512" height="512" fill="url(#g)"/>'
    inner='<circle cx="256" cy="218" r="150" fill="#fff" opacity="0.16"/>'
    sc=250/2048
    inner+=glyph(BAHT,256-1425*sc/2,286,sc,'#fff')
    s2=112/2048; gap=18
    total=sum(CLT[c][1]*s2 for c in 'CLT')+gap*2
    x=256-total/2
    for c in 'CLT':
        inner+=glyph(CLT[c][0],x,434,s2,'#fff'); x+=CLT[c][1]*s2+gap
    inner+='<path d="M356 92 l30 32 l56 -64" fill="none" stroke="#FFD166" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'
    if mask: inner='<g transform="translate(51.2 51.2) scale(0.8)">'+inner+'</g>'
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512"><defs>'
            '<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F08A24"/><stop offset="1" stop-color="#C85A0A"/></linearGradient></defs>'
            +b+inner+'</svg>')

PAGE='''<!doctype html>
<html lang="th"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>@NAME@</title>
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="@THEME@">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="@SHORT@">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<style>
:root{--theme:@THEME@;--bg:#f3f5f8;--text:#1d2733;--muted:#5f6b7a;--card:#fff;--line:#d6dce4}
@media(prefers-color-scheme:dark){:root{--bg:#10151c;--text:#e8edf3;--muted:#9aa7b5;--card:#18202a;--line:#2a3441}}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,"Sarabun","Noto Sans Thai",sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}
.card{width:100%;max-width:420px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:28px 22px;text-align:center}
.card img{width:112px;height:112px;border-radius:25px;box-shadow:0 6px 18px rgba(0,0,0,.18)}
h1{font-size:21px;margin:16px 0 6px}p{color:var(--muted);font-size:15px;line-height:1.55;margin:4px 0}
.btn{display:block;width:100%;padding:14px;margin-top:14px;border:0;border-radius:12px;font:inherit;font-weight:700;font-size:17px;text-decoration:none;cursor:pointer}
.go{background:var(--theme);color:#fff}.ins{background:transparent;color:var(--theme);border:2px solid var(--theme)}
.how{text-align:left;margin-top:20px;font-size:14px;color:var(--muted);line-height:1.6}.how b{color:var(--text)}
.how ol{margin:4px 0 12px;padding-left:20px}
</style></head><body>
<main class="card">
<img src="icons/icon-192.png" alt="">
<h1>@NAME@</h1>
<p>บันทึกค่ากะ/เบี้ยเลี้ยงวันหยุด พร้อมพิกัด GPS (ระบบ v2)</p>
<a class="btn go" href="@URL@">เปิดหน้าบันทึก</a>
<button class="btn ins" id="install" hidden>ติดตั้งลงหน้าจอมือถือ</button>
<div class="how">
<b>วิธีใส่ไอคอนบนหน้าจอมือถือ</b>
<ol><li><b>Android (Chrome):</b> กดเมนู &#8942; &gt; "ติดตั้งแอป" หรือ "เพิ่มลงในหน้าจอหลัก"</li>
<li><b>iPhone (Safari):</b> กดปุ่มแชร์ &gt; "เพิ่มไปยังหน้าจอโฮม"</li></ol>
กดไอคอนบนหน้าจอ จะเข้าหน้าบันทึกทันที (กด "อนุญาต" เมื่อมือถือถามตำแหน่ง)
</div></main>
<script>
var TARGET="@URL@";
var standalone=(window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||window.navigator.standalone===true||/[?&]source=pwa/.test(location.search);
if(standalone){location.replace(TARGET);}
if('serviceWorker' in navigator){navigator.serviceWorker.register('sw.js').catch(function(){});}
var dp=null,b=document.getElementById('install');
window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();dp=e;b.hidden=false;});
b.addEventListener('click',function(){if(!dp)return;dp.prompt();dp.userChoice.then(function(){dp=null;b.hidden=true;});});
</script></body></html>
'''
SW="""// minimal service worker (makes the launcher installable)
self.addEventListener('install',function(){self.skipWaiting();});
self.addEventListener('activate',function(e){e.waitUntil(self.clients.claim());});
self.addEventListener('fetch',function(){});
"""
def w(path,text):
    os.makedirs(os.path.dirname(path) or '.',exist_ok=True)
    open(path,'w',encoding='utf-8').write(text)
def render(svg,png,size):
    open('/tmp/_i.svg','w').write(svg)
    subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),'/tmp/_i.svg','-o',png],check=True)
O='_site'
shutil.rmtree(O,ignore_errors=True)
h=PAGE
for k,v in {'@NAME@':NAME,'@SHORT@':SHORT,'@THEME@':THEME,'@URL@':URL}.items(): h=h.replace(k,v)
w(O+'/index.html',h); w(O+'/sw.js',SW); w(O+'/.nojekyll','')
w(O+'/manifest.webmanifest',json.dumps({"id":"/shift-allowance-app/","name":NAME,"short_name":SHORT,"description":"บันทึกค่ากะ/เบี้ยเลี้ยงวันหยุด พร้อม GPS","lang":"th","start_url":"./?source=pwa","scope":"./","display":"standalone","orientation":"portrait","background_color":"#ffffff","theme_color":THEME,"icons":[{"src":"icons/icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"icons/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"},{"src":"icons/icon-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},ensure_ascii=False,indent=1))
os.makedirs(O+'/icons',exist_ok=True)
w(O+'/icons/icon.svg',icon())
for s in (180,192,512): render(icon(),f'{O}/icons/icon-{s}.png',s)
render(icon(True),O+'/icons/icon-maskable-512.png',512)
print('built')
