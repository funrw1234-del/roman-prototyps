# Сборка 5 вариантов из style-proto/video/index.html. Запуск: python _build/build.py
import os, shutil
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=os.path.join(ROOT,'..','style-proto','video')
src=open(os.path.join(SRC,'index.html'),encoding='utf-8').read()
V=[('cinema','kino','Кино тёмный','Шоурил на весь экран, чёрный фон, узкий шрифт, красная метка REC. Для рекламы.'),
   ('label','label','Лейбл','Чёрный гранж, золото, сетка клипов 4 в ряд — в духе gaz.team. Для клипов и музыки.'),
   ('wedding','fashion','Fashion','Белый фон, тонкие засечки заглавными, без цвета. Для брендов одежды и имиджевых роликов.'),
   ('editorial','editorial','Редакционный','Светлый фон, огромный жирный шрифт, ровная сетка. Для брендов и коммерции.'),
   ('content','bright','Яркий брендовый','Белый с салатовым, вертикальные ролики на первом экране. Для рекламы в соцсетях.')]
for f in ('logo-mask.png','favicon.png'): shutil.copy(os.path.join(SRC,f),os.path.join(ROOT,f))
def must(s,a,b):
    assert a in s,a[:60]; return s.replace(a,b,1)
for key,slug,name,desc in V:
    s=src
    s=must(s,"var KEY='style-proto-video-v2',S;","var KEY='videograf-"+slug+"',S;")
    s=must(s,"try{S=JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){}\n","")
    s=must(s,"if(!S)S=Object.assign({preset:'cinema'},P.cinema);","S=Object.assign({preset:'"+key+"'},P['"+key+"']);")
    s=must(s,'<aside class="panel" id="panel">','<aside class="panel min" id="panel">')
    s=must(s,'<span id="pt">свернуть ▾</span>','<span id="pt">развернуть ▴</span>')
    s=must(s,'<title>FILMED BY ROMARIO — прототип стиля</title>','<title>FILMED BY ROMARIO — '+name+'</title>\n<meta name="robots" content="noindex">')
    s=s.replace('href="favicon.png"','href="../favicon.png"').replace('url(logo-mask.png)','url(../logo-mask.png)')
    s=must(s,'<div class="note">Прототип стиля: видео — стилизованные заглушки, тексты и цены — примеры.</div>',
      '<div class="note"><a href="../" style="text-decoration:underline">← все варианты</a> · «'+name+'»: видео — заглушки, тексты и цены — примеры.</div>')
    os.makedirs(os.path.join(ROOT,slug),exist_ok=True); open(os.path.join(ROOT,slug,'index.html'),'w',encoding='utf-8').write(s)
cards=''.join(f'<a class="v" href="{slug}/"><span class="n">0{i+1}</span><b>{name}</b><p>{desc}</p><span class="go">Открыть →</span></a>' for i,(k,slug,name,desc) in enumerate(V))
idx=f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>FILMED BY ROMARIO — варианты прототипа</title><link rel="icon" type="image/png" href="favicon.png">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#0B0B0C;color:#EDEDED;font-family:Manrope,system-ui,sans-serif}}
.w{{max-width:1100px;margin:0 auto;padding:64px 24px}}
.mark{{display:block;width:84px;height:84px;background:#F2EEE6;-webkit-mask:url(logo-mask.png) center/contain no-repeat;mask:url(logo-mask.png) center/contain no-repeat;margin-bottom:28px}}
.e{{font:500 12px 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:#8B8B90}}
h1{{font-size:clamp(34px,6vw,64px);line-height:1;letter-spacing:-.04em;margin:14px 0 12px}}
.l{{color:#8B8B90;max-width:620px;font-size:17px;line-height:1.55}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px;margin-top:40px}}
.v{{display:flex;flex-direction:column;gap:10px;padding:26px;border:1px solid #26262A;border-radius:14px;color:inherit;text-decoration:none;transition:border-color .2s,transform .2s;background:#121214}}
.v:hover{{border-color:#E5484D;transform:translateY(-3px)}}
.n{{font:500 12px 'JetBrains Mono',monospace;color:#E5484D}}
.v b{{font-size:24px;letter-spacing:-.02em}}.v p{{margin:0;color:#9A9AA0;line-height:1.5;font-size:15px;flex:1}}
.go{{font-weight:600;font-size:14px}}
</style></head><body><div class="w">
<span class="mark" aria-hidden="true"></span>
<div class="e">FILMED BY ROMARIO · прототип сайта</div>
<h1>Пять вариантов<br>оформления</h1>
<p class="l">Реклама, fashion, клипы для брендов. Структура и тексты одинаковые — отличается только стиль. Видео и цены — заглушки. В каждом варианте справа внизу есть панель, в которой можно подкрутить шрифты, цвет и отступы.</p>
<div class="g">{cards}</div></div></body></html>'''
open(os.path.join(ROOT,'index.html'),'w',encoding='utf-8').write(idx)
print('built')
