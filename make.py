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

PAGE=r'''<!doctype html>
<html lang="th"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>@NAME@</title>
<script>
(function(){var s=(window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||navigator.standalone===true||/[?&]source=pwa/.test(location.search);
if(s){location.replace("@URL@");return;}
/* เปิดจาก LINE: ให้ LINE เปิดในเบราว์เซอร์ปกติ (Chrome/Safari) */
if(/\bLine\//i.test(navigator.userAgent)&&!/openExternalBrowser=1/.test(location.search)){
location.replace(location.pathname+(location.search?location.search+'&':'?')+'openExternalBrowser=1'+location.hash);}})();
</script>
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="@THEME@">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="apple-touch-icon" sizes="152x152" href="icons/icon-152.png">
<link rel="apple-touch-icon" sizes="167x167" href="icons/icon-167.png">
<link rel="apple-touch-icon" sizes="180x180" href="icons/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="@SHORT@">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<style>
:root{--theme:@THEME@;--bg:#f3f5f8;--text:#1d2733;--muted:#5f6b7a;--card:#fff;--line:#d6dce4;--warn:#fff4e5;--warnt:#8a4b00;--ok:#e8f6ec;--okt:#1c6b34;--sel:#fff3e8}
@media(prefers-color-scheme:dark){:root{--bg:#10151c;--text:#e8edf3;--muted:#9aa7b5;--card:#18202a;--line:#2a3441;--warn:#3a2a14;--warnt:#ffcf8a;--ok:#163322;--okt:#9be3b2;--sel:#33240f}}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,"Sarabun","Noto Sans Thai",sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;align-items:flex-start;justify-content:center;padding:16px}
.card{width:100%;max-width:440px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px 18px;text-align:center}
.logo{width:88px;height:88px;border-radius:20px;box-shadow:0 6px 18px rgba(0,0,0,.18)}
h1{font-size:20px;margin:12px 0 2px}p{color:var(--muted);font-size:15px;line-height:1.55;margin:4px 0}
.q{font-weight:700;color:var(--text);margin:18px 0 8px;font-size:16px}
.pick{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.os{border:2px solid var(--line);background:var(--card);color:var(--text);border-radius:14px;padding:14px 6px;font:inherit;font-weight:700;font-size:16px;cursor:pointer}
.os svg{display:block;margin:0 auto 6px;width:34px;height:34px}
.os small{display:block;font-weight:400;color:var(--muted);font-size:12px;margin-top:2px}
.os[aria-pressed=true]{border-color:var(--theme);background:var(--sel);color:var(--theme)}
.btn{display:block;width:100%;padding:15px;margin-top:12px;border:0;border-radius:12px;font:inherit;font-weight:700;font-size:17px;text-decoration:none;cursor:pointer;text-align:center}
.pri{background:var(--theme);color:#fff}.sec{background:transparent;color:var(--theme);border:2px solid var(--theme)}
.box{text-align:left;margin-top:14px;padding:12px 14px;border-radius:12px;font-size:14.5px;line-height:1.6}
.warn{background:var(--warn);color:var(--warnt)}.ok{background:var(--ok);color:var(--okt)}
.steps{text-align:left;margin-top:14px;border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-size:15px;line-height:1.6}
.steps h2{font-size:16px;margin:0 0 4px}.steps h3{font-size:14px;margin:12px 0 0;color:var(--muted)}
.steps ol{margin:0;padding:0}.steps li{display:flex;gap:10px;align-items:flex-start;list-style:none;margin:9px 0}
.n{flex:0 0 24px;height:24px;border-radius:50%;background:var(--theme);color:#fff;font-weight:700;text-align:center;line-height:24px;font-size:13px}
.k{display:inline-block;min-width:24px;padding:0 6px;border:1px solid var(--line);border-radius:6px;font-weight:700;text-align:center;background:var(--bg)}
.ic{width:21px;height:21px;vertical-align:-5px;margin:0 2px;color:#0a84ff}
.small{font-size:13px;color:var(--muted);margin-top:14px}
[hidden]{display:none!important}
</style></head><body>
<main class="card">
<img class="logo" src="icons/icon-192.png" alt="">
<h1>@NAME@</h1>
<p>บันทึกค่ากะ/เบี้ยเลี้ยงวันหยุด</p>

<div class="q">เลือกมือถือของคุณ</div>
<div class="pick">
<button class="os" id="b-and" aria-pressed="false"><svg viewBox="0 0 24 24" fill="#3ddc84"><path d="M17.6 9.48l1.84-3.18a.38.38 0 0 0-.66-.38l-1.86 3.22a11.4 11.4 0 0 0-9.84 0L5.22 5.92a.38.38 0 0 0-.66.38L6.4 9.48A10.8 10.8 0 0 0 1 18h22a10.8 10.8 0 0 0-5.4-8.52zM7 15.25a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5zm10 0a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5z"/></svg>Android<small>Samsung, Oppo, Vivo, Xiaomi ฯลฯ</small></button>
<button class="os" id="b-ios" aria-pressed="false"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.4-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8 1.6 0 2 .8 3.4.8 1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9 0 0-2.7-1-2.7-4.1zM13.9 4.9c.7-.9 1.2-2 1-3.2-1 0-2.3.7-3 1.6-.7.8-1.2 2-1.1 3.1 1.2.1 2.3-.6 3.1-1.5z"/></svg>iPhone / iPad<small>iOS</small></button>
</div>

<!-- Android -->
<section id="p-and" hidden>
<button id="install" class="btn pri">ติดตั้งไอคอนเลย</button>
<div id="done" class="box ok" hidden>✓ ติดตั้งแล้ว — กดไอคอน <b>@SHORT@</b> บนหน้าจอมือถือเพื่อเข้าบันทึก</div>
<div class="steps">
<h2>วิธีติดตั้งบน Android</h2>
<h3>Chrome (แนะนำ)</h3>
<ol><li><span class="n">1</span><span>กดปุ่ม "ติดตั้งไอคอนเลย" ด้านบน แล้วกด <b>"ติดตั้ง"</b></span></li>
<li><span class="n">2</span><span>ถ้าไม่มีหน้าต่างขึ้น: กดเมนู <span class="k">⋮</span> มุมขวาบน &gt; <b>"ติดตั้งแอป"</b> หรือ <b>"เพิ่มลงในหน้าจอหลัก"</b> &gt; <b>"ติดตั้ง"</b></span></li>
<li><span class="n">3</span><span>รอ 2–3 วินาที ไอคอนส้ม <b>@SHORT@</b> จะอยู่บนหน้าจอ</span></li></ol>
<h3>Samsung Internet</h3>
<ol><li><span class="n">1</span><span>กดเมนู <span class="k">≡</span> ด้านล่างขวา &gt; <b>"เพิ่มหน้าไปยัง"</b> &gt; <b>"หน้าจอหลัก"</b> &gt; <b>"เพิ่ม"</b></span></li></ol>
<h3>ถ้าเปิดอยู่ในแอป LINE / Facebook</h3>
<ol><li><span class="n">1</span><span>กดเมนู <span class="k">⋮</span> มุมขวาบน &gt; <b>"เปิดในเบราว์เซอร์"</b> หรือกด "คัดลอกลิงก์" ด้านล่าง แล้วไปวางในแอป <b>Chrome</b></span></li></ol>
</div>
</section>

<!-- iOS -->
<section id="p-ios" hidden>
<div class="box warn">iPhone ต้องติดตั้งผ่านแอป <b>Safari</b> เท่านั้น — ถ้าเปิดอยู่ในแอปอื่น (LINE, Facebook, Google) ให้กด "คัดลอกลิงก์" ด้านล่าง แล้วไปวางในแอป Safari</div>
<div class="steps">
<h2>วิธีติดตั้งบน iPhone (Safari)</h2>
<ol><li><span class="n">1</span><span>กดปุ่มแชร์ @SHARE@ ด้านล่างกลางจอ<br><small>iOS 26: กดปุ่ม <span class="k">⋯</span> ด้านล่างขวาก่อน แล้วกด @SHARE@ "แชร์" — iPad: ปุ่มแชร์อยู่ด้านบนขวา</small></span></li>
<li><span class="n">2</span><span>เลื่อนลงแล้วกด @ADD@ <b>"เพิ่มไปยังหน้าจอโฮม"</b><br><small>ถ้าไม่เห็น เลื่อนลงสุดแล้วกด "แก้ไขการทำงาน"/"ดูเพิ่มเติม"</small></span></li>
<li><span class="n">3</span><span>กด <b>"เพิ่ม"</b> มุมขวาบน — ไอคอนส้ม <b>@SHORT@</b> จะอยู่บนหน้าจอโฮม</span></li></ol>
<h3>ใช้ Chrome บน iPhone</h3>
<ol><li><span class="n">1</span><span>กดปุ่มแชร์ @SHARE@ ที่ช่องที่อยู่ด้านบนขวา &gt; <b>"เพิ่มไปยังหน้าจอโฮม"</b> &gt; <b>"เพิ่ม"</b> (ถ้าไม่มีเมนูนี้ ให้ใช้ Safari)</span></li></ol>
</div>
</section>

<button id="copy" class="btn sec" hidden>คัดลอกลิงก์</button>
<a class="btn sec" href="@URL@">เปิดหน้าบันทึก (ไม่ติดตั้ง)</a>
<p class="small">กดไอคอนบนหน้าจอ จะเข้าหน้าบันทึกทันที (กด "อนุญาต" เมื่อมือถือถามตำแหน่ง)</p>
</main>
<script>
var ua=navigator.userAgent,$=function(i){return document.getElementById(i)};
var isIOS=/iPhone|iPad|iPod/.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
var link=location.origin+location.pathname;
var dp=null;
try{if('serviceWorker' in navigator)navigator.serviceWorker.register('sw.js').catch(function(){});}catch(e){}
window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();dp=e;});
window.addEventListener('appinstalled',function(){dp=null;$('done').hidden=false;$('install').hidden=true;});

function choose(os,scroll){
  $('b-and').setAttribute('aria-pressed',os==='and');$('b-ios').setAttribute('aria-pressed',os==='ios');
  $('p-and').hidden=os!=='and';$('p-ios').hidden=os!=='ios';$('copy').hidden=false;
  try{history.replaceState(null,'','#'+os);}catch(e){}
  if(scroll)$('p-'+os).scrollIntoView({behavior:'smooth',block:'start'});
}
$('b-and').onclick=function(){choose('and',true)};
$('b-ios').onclick=function(){choose('ios',true)};
var h=location.hash.replace('#','');
choose(h==='and'||h==='ios'?h:(isIOS?'ios':(/Android/i.test(ua)?'and':'')),false);
if(!/Android/i.test(ua)&&!isIOS&&!h){$('p-and').hidden=true;$('p-ios').hidden=true;$('copy').hidden=true;$('b-and').setAttribute('aria-pressed',false);$('b-ios').setAttribute('aria-pressed',false);}

$('install').onclick=function(){
  if(dp){dp.prompt();dp.userChoice.then(function(r){dp=null;if(r.outcome==='accepted'){$('done').hidden=false;$('install').hidden=true;}});}
  else{$('p-and').querySelector('.steps').scrollIntoView({behavior:'smooth',block:'start'});}
};
$('copy').onclick=function(){
  var done=function(){$('copy').textContent='✓ คัดลอกแล้ว — ไปวางในเบราว์เซอร์';};
  function fb(){var t=document.createElement('textarea');t.value=link;document.body.appendChild(t);t.select();try{document.execCommand('copy');done();}catch(e){prompt('คัดลอกลิงก์นี้',link);}t.remove();}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(link).then(done,fb);}else fb();
};
</script></body></html>
'''
SW="""// service worker: เก็บหน้า launcher ไว้ในเครื่อง (ทำให้ Chrome ทุกรุ่นยอมติดตั้ง และเปิดได้แม้เน็ตช้า)
var C='clt-launcher-@VER@';
var FILES=['./','./index.html','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png','./icons/icon-180.png'];
self.addEventListener('install',function(e){self.skipWaiting();e.waitUntil(caches.open(C).then(function(c){return c.addAll(FILES);}).catch(function(){}));});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(n){return n!==C;}).map(function(n){return caches.delete(n);}));}).then(function(){return self.clients.claim();}));});
self.addEventListener('fetch',function(e){
  var r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
  e.respondWith(fetch(r).then(function(res){if(res&&res.ok){var cp=res.clone();caches.open(C).then(function(c){c.put(r,cp);});}return res;})
    .catch(function(){return caches.match(r,{ignoreSearch:true}).then(function(m){return m||caches.match('./index.html').then(function(x){return x||new Response('<meta charset=utf-8><p style="font:18px sans-serif;padding:20px">ไม่มีอินเทอร์เน็ต กรุณาลองใหม่</p>',{headers:{'Content-Type':'text/html; charset=utf-8'}});});});}));
});
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
SHARE_SVG='<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7.5 7.5 12 3l4.5 4.5"/><path d="M8 10H6v10h12V10h-2"/></svg>'
ADD_SVG='<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M12 8v8M8 12h8"/></svg>'
for k,v in {'@SHARE@':SHARE_SVG,'@ADD@':ADD_SVG,'@NAME@':NAME,'@SHORT@':SHORT,'@THEME@':THEME,'@URL@':URL}.items(): h=h.replace(k,v)
import time
w(O+'/index.html',h); w(O+'/sw.js',SW.replace('@VER@',str(int(time.time())))); w(O+'/.nojekyll','')
w(O+'/manifest.webmanifest',json.dumps({"id":"/shift-allowance-app/","name":NAME,"short_name":SHORT,"description":"บันทึกค่ากะ/เบี้ยเลี้ยงวันหยุด พร้อม GPS","lang":"th","start_url":"./?source=pwa","scope":"./","prefer_related_applications":False,"display":"standalone","orientation":"portrait","background_color":"#ffffff","theme_color":THEME,"icons":[{"src":"icons/icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"icons/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"},{"src":"icons/icon-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},ensure_ascii=False,indent=1))
os.makedirs(O+'/icons',exist_ok=True)
w(O+'/icons/icon.svg',icon())
for s in (152,167,180,192,512): render(icon(),f'{O}/icons/icon-{s}.png',s)
render(icon(True),O+'/icons/icon-maskable-512.png',512)
print('built')
