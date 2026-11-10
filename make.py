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
/* ไอคอนบนหน้าจอ: เปิดแล้วไปหน้าบันทึกทันที */
(function(){var s=(window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||navigator.standalone===true||/[?&]source=pwa/.test(location.search);
if(s){location.replace("@URL@");return;}
/* เปิดจาก LINE: ให้ LINE เปิดในเบราว์เซอร์ปกติ (Chrome/Safari) อัตโนมัติ */
if(/\bLine\//i.test(navigator.userAgent)&&!/openExternalBrowser=1/.test(location.search)){
location.replace(location.pathname+(location.search?location.search+'&':'?')+'openExternalBrowser=1'+location.hash);}})();
</script>
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="@THEME@">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="@SHORT@">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<style>
:root{--theme:@THEME@;--bg:#f3f5f8;--text:#1d2733;--muted:#5f6b7a;--card:#fff;--line:#d6dce4;--warn:#fff4e5;--warnt:#8a4b00;--ok:#e8f6ec;--okt:#1c6b34}
@media(prefers-color-scheme:dark){:root{--bg:#10151c;--text:#e8edf3;--muted:#9aa7b5;--card:#18202a;--line:#2a3441;--warn:#3a2a14;--warnt:#ffcf8a;--ok:#163322;--okt:#9be3b2}}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,"Sarabun","Noto Sans Thai",sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px}
.card{width:100%;max-width:420px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px 20px;text-align:center}
.logo{width:104px;height:104px;border-radius:24px;box-shadow:0 6px 18px rgba(0,0,0,.18)}
h1{font-size:21px;margin:14px 0 4px}p{color:var(--muted);font-size:15px;line-height:1.55;margin:4px 0}
.btn{display:block;width:100%;padding:15px;margin-top:12px;border:0;border-radius:12px;font:inherit;font-weight:700;font-size:17px;text-decoration:none;cursor:pointer;text-align:center}
.pri{background:var(--theme);color:#fff}.sec{background:transparent;color:var(--theme);border:2px solid var(--theme)}
.box{text-align:left;margin-top:16px;padding:14px 16px;border-radius:12px;font-size:15px;line-height:1.65}
.warn{background:var(--warn);color:var(--warnt)}.ok{background:var(--ok);color:var(--okt)}
.steps{text-align:left;margin-top:16px;border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:15px;line-height:1.65}
.steps h2{font-size:16px;margin:0 0 6px}.steps ol{margin:0;padding-left:22px}.steps li{margin:6px 0}
.k{display:inline-block;min-width:26px;padding:0 6px;border:1px solid var(--line);border-radius:6px;font-weight:700;text-align:center;background:var(--bg)}
.small{font-size:13px;color:var(--muted);margin-top:14px}
[hidden]{display:none!important}
</style></head><body>
<main class="card">
<img class="logo" src="icons/icon-192.png" alt="">
<h1>@NAME@</h1>
<p>บันทึกค่ากะ/เบี้ยเลี้ยงวันหยุด</p>

<div id="inapp" class="box warn" hidden></div>
<a id="chrome" class="btn pri" hidden>เปิดใน Chrome เพื่อติดตั้ง</a>
<button id="copy" class="btn sec" hidden>คัดลอกลิงก์</button>

<button id="install" class="btn pri">ติดตั้งไอคอนลงหน้าจอมือถือ</button>
<div id="done" class="box ok" hidden>✓ ติดตั้งแล้ว — กดไอคอน <b>@SHORT@</b> บนหน้าจอมือถือเพื่อเข้าบันทึก</div>
<div id="steps" class="steps" hidden></div>

<a class="btn sec" href="@URL@">เปิดหน้าบันทึก (ไม่ติดตั้ง)</a>
<p class="small">กดไอคอนบนหน้าจอ จะเข้าหน้าบันทึกทันที (กด "อนุญาต" เมื่อมือถือถามตำแหน่ง)</p>
</main>
<script>
var ua=navigator.userAgent,$=function(i){return document.getElementById(i)};
var iOS=/iPhone|iPad|iPod/.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
var android=/Android/i.test(ua);
var inApp=/\bLine\/|FBAN|FBAV|FB_IAB|Instagram|Messenger|MicroMessenger|TikTok|Twitter|; wv\)/i.test(ua);
var samsung=/SamsungBrowser/i.test(ua);
var iosOther=iOS&&/CriOS|FxiOS|EdgiOS|OPiOS|GSA\//.test(ua);
var huaweiEtc=android&&/HuaweiBrowser|MiuiBrowser|HeyTapBrowser|VivoBrowser|OPR\/|Firefox/i.test(ua);
var link=location.origin+location.pathname;
var dp=null;

if('serviceWorker' in navigator){navigator.serviceWorker.register('sw.js').catch(function(){});}
window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();dp=e;});
window.addEventListener('appinstalled',function(){dp=null;showDone();});

function showDone(){$('install').hidden=true;$('steps').hidden=true;$('done').hidden=false;}
function steps(title,items){var s=$('steps');s.innerHTML='<h2>'+title+'</h2><ol><li>'+items.join('</li><li>')+'</li></ol>';s.hidden=false;s.scrollIntoView({behavior:'smooth',block:'center'});}

/* แอปอื่นที่ติดตั้งไม่ได้ (LINE ที่เปิดเองไม่ได้, Facebook, Messenger ฯลฯ) */
if(inApp){
  $('install').hidden=true;
  if(android){
    $('inapp').innerHTML='<b>หน้านี้เปิดอยู่ในแอป LINE/แชท ซึ่งติดตั้งไอคอนไม่ได้</b><br>กดปุ่มด้านล่างเพื่อเปิดใน Chrome แล้วกด "ติดตั้ง" อีกครั้ง';
    var c=$('chrome');c.href='intent://'+location.host+location.pathname+'#Intent;scheme=https;package=com.android.chrome;S.browser_fallback_url='+encodeURIComponent(link)+';end';c.hidden=false;
  }else{
    $('inapp').innerHTML='<b>หน้านี้เปิดอยู่ในแอป LINE/แชท ซึ่งติดตั้งไอคอนไม่ได้</b><br>กดปุ่ม <span class="k">⋯</span> หรือ <span class="k">↗</span> แล้วเลือก <b>"เปิดใน Safari"</b><br>หรือกด "คัดลอกลิงก์" แล้วไปวางในแอป Safari';
  }
  $('inapp').hidden=false;$('copy').hidden=false;
}else if(huaweiEtc){
  $('inapp').innerHTML='แนะนำให้ติดตั้งผ่าน <b>Chrome</b> — กดปุ่มด้านล่าง (ถ้าไม่สำเร็จ ลองทำตามขั้นตอนเมนูของเบราว์เซอร์นี้ได้)';
  var c2=$('chrome');c2.href='intent://'+location.host+location.pathname+'#Intent;scheme=https;package=com.android.chrome;S.browser_fallback_url='+encodeURIComponent(link)+';end';c2.hidden=false;$('inapp').hidden=false;
}

$('copy').addEventListener('click',function(){
  var done=function(){$('copy').textContent='✓ คัดลอกแล้ว — ไปวางในเบราว์เซอร์';};
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(link).then(done,fallback);}else fallback();
  function fallback(){var t=document.createElement('textarea');t.value=link;document.body.appendChild(t);t.select();try{document.execCommand('copy');done();}catch(e){prompt('คัดลอกลิงก์นี้',link);}t.remove();}
});

$('install').addEventListener('click',function(){
  if(dp){dp.prompt();dp.userChoice.then(function(r){dp=null;if(r.outcome==='accepted')showDone();else manual();});return;}
  manual();
});
function manual(){
  if(iOS&&iosOther) steps('ติดตั้งบน iPhone (Chrome)',['กดปุ่มแชร์ <span class="k">↗</span> ที่ช่องที่อยู่ด้านบน','เลื่อนลงแล้วเลือก <b>"เพิ่มไปยังหน้าจอโฮม"</b>','กด <b>"เพิ่ม"</b> มุมขวาบน','ถ้าไม่มีเมนูนี้ ให้เปิดลิงก์นี้ในแอป <b>Safari</b> แทน']);
  else if(iOS) steps('ติดตั้งบน iPhone (Safari)',['กดปุ่มแชร์ <span class="k">↗</span> ด้านล่างจอ (iOS ใหม่: กด <span class="k">⋯</span> ก่อน แล้วกด "แชร์")','เลื่อนลงแล้วเลือก <b>"เพิ่มไปยังหน้าจอโฮม"</b> (ถ้าไม่เห็น กด "ดูเพิ่มเติม")','กด <b>"เพิ่ม"</b> มุมขวาบน','ไอคอนส้ม <b>@SHORT@</b> จะอยู่บนหน้าจอ']);
  else if(samsung) steps('ติดตั้งบน Samsung Internet',['กดเมนู <span class="k">≡</span> ด้านล่างขวา','เลือก <b>"เพิ่มหน้าไปยัง"</b> &gt; <b>"หน้าจอหลัก"</b>','กด <b>"เพิ่ม"</b>']);
  else if(android) steps('ติดตั้งบน Android (Chrome)',['กดเมนู <span class="k">⋮</span> มุมขวาบน','เลือก <b>"ติดตั้งแอป"</b> หรือ <b>"เพิ่มลงในหน้าจอหลัก"</b>','กด <b>"ติดตั้ง"</b> / <b>"เพิ่ม"</b> แล้วรอ 2–3 วินาที','ถ้าไม่เห็นเมนูนี้: ปิด Chrome แล้วเปิดลิงก์ใหม่อีกครั้ง หรืออัปเดต Chrome ใน Play Store']);
  else steps('ติดตั้งบนมือถือ',['เปิดลิงก์นี้บนมือถือด้วย Chrome (Android) หรือ Safari (iPhone)','กดปุ่ม "ติดตั้งไอคอนลงหน้าจอมือถือ" อีกครั้ง']);
}
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
    .catch(function(){return caches.match(r,{ignoreSearch:true}).then(function(m){return m||caches.match('./index.html');});}));
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
for k,v in {'@NAME@':NAME,'@SHORT@':SHORT,'@THEME@':THEME,'@URL@':URL}.items(): h=h.replace(k,v)
import time
w(O+'/index.html',h); w(O+'/sw.js',SW.replace('@VER@',str(int(time.time())))); w(O+'/.nojekyll','')
w(O+'/manifest.webmanifest',json.dumps({"id":"/shift-allowance-app/","name":NAME,"short_name":SHORT,"description":"บันทึกค่ากะ/เบี้ยเลี้ยงวันหยุด พร้อม GPS","lang":"th","start_url":"./?source=pwa","scope":"./","prefer_related_applications":False,"display":"standalone","orientation":"portrait","background_color":"#ffffff","theme_color":THEME,"icons":[{"src":"icons/icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"icons/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"},{"src":"icons/icon-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},ensure_ascii=False,indent=1))
os.makedirs(O+'/icons',exist_ok=True)
w(O+'/icons/icon.svg',icon())
for s in (180,192,512): render(icon(),f'{O}/icons/icon-{s}.png',s)
render(icon(True),O+'/icons/icon-maskable-512.png',512)
print('built')
