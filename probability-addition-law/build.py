#!/usr/bin/env python3
"""Build probability-addition-law/index.html in the BeamerRed layout of the existing decks."""
from pathlib import Path

HERE = Path(__file__).parent
_ref = (HERE.parent / 'probability' / 'index.html').read_text()
STYLE = _ref[_ref.index('<style>'):_ref.index('</style>') + 8]  # BeamerRed CSS with embedded fonts
OUT = HERE / 'index.html'

EXTRA_CSS = """<style>
/* ∩ ∪ ∅ ′ ≠ ⟺ from Latin Modern Math: the text font lacks them, so browsers would mix fallback fonts */
@font-face{font-family:MathSym;src:url(data:font/woff;base64,d09GRk9UVE8AAAk8AA0AAAAAC8wAAfWBAAAAAAAAAAAAAAAAAAAAAAAAAABDRkYgAAABOAAABHEAAAVE67nd60dERUYAAAhIAAAAFgAAABYAEQALR1BPUwAACGAAAAAQAAAAEAAZAAxHU1VCAAAIcAAAABoAAAAabYx0f01BVEgAAAiMAAAArgAAASoIyjgtT1MvMgAABjAAAABOAAAAYD/ExJVjbWFwAAAH7AAAAEcAAABcc91ds2hlYWQAAAWsAAAANgAAADYLXwg+aGhlYQAABhAAAAAgAAAAJA/RDTpobXR4AAAF5AAAACkAAAAsGCUBjW1heHAAAAEwAAAABgAAAAYAC1AAbmFtZQAABoAAAAFpAAACzkKpVEFwb3N0AAAINAAAABMAAAAg/ycAKAAAUAAACwAAeJx1UW1MU1cYvhe55YbSEhklLhI4MmHT0CJkZlMTM1GZc4BOPmKWWlPo7cdaWrz3VoFtWoulwEtbSjs2DTI3AwlxUQM6kGWJZpkJ+0gc019uy0JcgktMlJGcwnFk57bE7CPLm5zz5n3ej+fJwzLpaQzLsuuqzbLDXeOxCKK7xizb9YcEm9dlFhVMn9jIJIrZREla4sU1iXXpxJi1ZiIrfWU0fzErP3shXzPPJd7Nji0v5iQCaxkN3cfwzFrmeWYDo2cqmO1MJbOPaWBrWYE97nU7Kl6p2tXicHslg8sqpxKhLfWLlIMsiJLQLDs8btrrcQstrXK7JMhujywc85pdSqMsNNImCqJyw7at23Z7WttFh80uo4ot5RV6PX1fRlaPiJKaUEoUUlShA/VVqKkdVRrQfnOz03NCcjpK0UEDqpPFDsHV3NHuRGa3RakcdJjdSRy9RO80CXazy4o8VlQvHEZeiZ5HNtHjbZU2GVC93SGhEx7RiegvCi7BLAkW5HXTs0i2C+j1hrp6VOVxy6ja0Sy4JQHp9UgSBGSX5dbtZWWy12bwiLYyK22RylypHqlMGdNXHait11e/sXtvbd1eg9wmJ3VZBNnscEmG//HsP7IZ6mKQYUYZtjuDUSv+pDO/MY8YTM1VsznsevZ22ptpDeSednlbPncbh3UQDfYHQnuGa641TB8dt0633gwOBCKd4AO/nz7dfTT4i0fGzJdt/Mpm1eUrY9cv3ugL94UhDIP+uA86IRAMnmlttBqPWhqMNU172vhAT7ALAhCIdEV7Zttmmm4ZJy1XjaONkTPRYAwGIR6HQR7CvTSkGy3X7Vf45c0qu63FLB3p7e7thm7wxf2DEINoJDIwevPq9OT4remZa7PDfDQU6YcovzPP2GY6ZnHyK36V5ZJpxDg8PTw1Mn6JX/arxp1Tx6bbeO2SlapDmdqn2VjEHboNq9mnuqLVLKx7IVP7feKPvI3JD5t0xZnaksRh/EgHP/fi8q2/8ue/6z/PKSoL3oPu0wEvf9LEnYo6z1nhEOxvse60bO8qBwPUAqmee42XX+UU3gXnIPxB9BP+oynu4smxzlHA6TD58PwXIz+Ef4EfeZKH7+nI7qfz3Dt3AGfD7/AT3Dn77fD812NT8DGMBEa8/DdkRgeVsOvUvvaiRqERZJBi0gUeVyYecp+9BYSH0qRAvS5JjtyFr7ABDwE3GI8PKqVCEgKsxQ+4vhB1KpRyyg+dXT2dPMklC2QOOJ/f71P4FuK7UEcMZOjvpRAQLXnA9fZQM3rAF/N/SO2I9YdiPM7FC3gudapQSz7HkaW3dSWZ2qXh3MQjXew5JoNl12/asqtjYjZJ7k+V6tnaJZUqOaaeIKaMZ1U1EZuxqFKntJiasWm1K5GTgTVE85iU0tCUEE3B05wMZUSBCyj6ZPE+pZO7uKP4H4gyqCxTLihAcdEOKjq36P6Tgn8hRIM1JbiUhuYx1hSoL3QMHadev3866ONJFvmSmleBz3KR/tAADPDqvwCOLUDZAAAAAAEAAAAB9YGtk3TgXw889QALA+gAAAAA0C9n8gAAAADQL2fy++70DA/yDegAAAAIAAIAAAAAAAB4nGOUYGBg/cdgwczFYMFwj4EBhplmM9iCMOMXBn2QHKM5gw0ArcAHxQAAAHicY2BkYGBW+2/HcIL/0+93f//xf2IAiqAAbgDDJQgieJxjYGGawTiBgZWBh6mLaTcDA0MPhGa8z2DIyMTAwMTAyswABg0QKoEBGRxQMFL/xaz2347hBO8L7i9AEUaQMON6ptUMCkDICACUAg5RAAB4nIWRT0/CQBDFHwU1evDkyVPDSRPAP9GDHjViNChEqjHeUEppIEDaGpSP7Sfwt9stqBfTdOfN23lvZnclbehFZZUqm1LpS3K4pCpZjj1tezsOl7XlVR2uqOHVHF7Trlf4rFv+UlPN9KlEsSINlcnXsQ51xFrny/EJ7IDKhNhSj6pYE/AdXF8hfJ6ZnSGorUBN4ivOvi7UYL1l900jFHOlxFg12I7d66JLtMBpTM0C1Qi2h2t/WdNBYZiV3tce2cT2CenbQz0gm9o1gHsmvlNtJkzBEXEKMyPbt64Butjuze35TN88T+w0Ia5G37dOE3da354zJF7rkekDUNPOktkbijlFSJbaGnOPvsUmM3ecMcG5DvgyXCMmMb0j8oFzScHjXz6GKbrV6dbWvUUt3fCKV2Rd1gbaDztF8V5m4oxTxPil7P//fg8wEXONyRNev6EznfKvlD91har+R/fkbj12b7T0+QZ5IG8TAAAAeJxjYGBgYmBgYAZiESDJCKZZGDyANB8DB1COTcFIiVVJSElLKUH91///DAxQviaEf//GPea7H+7evbvyBjtYNxIAAGBfElQAeJxjYGYAg/8qDBoMWAAAHukBTwAAAQAAAAwAAAAAAAAAAgABAAEACgABAAAAAQAAAAoADAAOAAAAAAAAAAEAAAAKABYAGAABbWF0aAAIAAAAAAAAAAAAAHicZY+tCgJBFIW/O+6AiMGwLFabeZPB7DNoEbuC1WcwG8RkEZtPYDL5AGbxAeyCIHhmZlHQvdz5zp4584cBDW7cGVD63Ods5DzBTuDW0g/poXgWp+qO9Cxl2FZzvTTPXL3XOnl2FHfiSDzIX0i3U8ZV+4WsLX9y3ZSNrLSNxcm//9GlevX9twJeF+k+dVU4taXOaUYaBRZpODLSV1OF2101ZhpDGT6+Sd4bhZMhGAAA)format("woff")}
.sym{font-family:MathSym,serif;font-style:normal;font-weight:400}
.math i,.task i,.eq i,.thm i,.def i,.remark i,.key i,.solution i,p i,li i{font-style:italic}
.eq.big{font-size:26px}
.formula{display:block;line-height:1.25}.formula.law{font-size:30px;text-align:center;margin:14px 0}.formula .fraction{margin:0 4px}
.grid-table{border-collapse:collapse;font-size:22px;margin:8px 0 12px}
.grid-table th,.grid-table td{border:1px solid #bbb;width:44px;height:38px;text-align:center}
.grid-table th{color:#600;background:#f5f0f0}
.grid-table td.hl{background:#ecd4d4;color:#900;font-weight:700}
.grid-table td.hl:not(.shown){background:none;color:#bbb;font-weight:400}
.two{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.steps p{margin:6px 0}
.task p+p{margin-top:6px}
.center{text-align:center}
.solution{color:#b22222;margin:5px 0;font-size:24px;line-height:1.35}
.solution b,.solution strong{color:#b22222}
.solution.formula{margin:6px 0;font-size:24px}
.columns .solution,.two .solution{font-size:21px}
.section-body{flex-direction:column;gap:22px}
.section-lead{font-size:22px;color:#333;max-width:760px;text-align:center}
</style>"""

SCRIPT = r"""<script>const slides=[...document.querySelectorAll('.slide')];let current=0,step=0;
slides.forEach(s=>{let n=0;s.querySelectorAll('.reveal').forEach(r=>{if(!r.dataset.step)r.dataset.step=++n;else n=Math.max(n,+r.dataset.step)})});
const counts=slides.map(s=>Math.max(0,...[...s.querySelectorAll('.reveal')].map(r=>+r.dataset.step)));
const prev=document.querySelector('#prev'),next=document.querySelector('#next'),status=document.querySelector('#status');
function resize(){document.documentElement.style.setProperty('--scale',Math.min(innerWidth/980,innerHeight/551.25))}
function render(){slides.forEach((s,i)=>{s.hidden=i!==current;s.querySelectorAll('.reveal').forEach(r=>r.classList.toggle('shown',+r.dataset.step<=step));s.querySelectorAll('.nav-dot').forEach((d,j)=>{d.classList.toggle('active',j===current);d.classList.toggle('visited',j<current);d.setAttribute('aria-current',j===current?'step':'false')})});status.textContent=`${current+1} / ${slides.length}`;document.querySelector('#hint').textContent=counts[current]?`Step ${step} / ${counts[current]}`:'';prev.disabled=current===0&&step===0;next.disabled=current===slides.length-1&&step===counts[current];try{history.replaceState(null,'',`#/${current+1}/${step}`)}catch(e){}}
function go(i,s=0){current=Math.max(0,Math.min(slides.length-1,i));step=Math.max(0,Math.min(counts[current],s));render()}
function forward(){if(step<counts[current])step++;else if(current<slides.length-1){current++;step=0}render()}
function backward(){if(step>0)step--;else if(current>0){current--;step=counts[current]}render()}
function route(){const m=location.hash.match(/^#\/(\d+)(?:\/(\d+))?/);go(m?Number(m[1])-1:0,m?Number(m[2]||0):0)}
function overview(){document.body.classList.toggle('overview')}
prev.onclick=backward;next.onclick=forward;document.querySelector('#overview').onclick=overview;document.querySelector('#fullscreen').onclick=()=>document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();
document.querySelectorAll('[data-go]').forEach(b=>b.onclick=e=>{e.stopPropagation();go(Number(b.dataset.go))});
slides.forEach((s,i)=>s.onclick=()=>{if(document.body.classList.contains('overview')){document.body.classList.remove('overview');go(i)}});
addEventListener('keydown',e=>{if(e.target.closest('input,textarea,select')||(e.key===' '&&e.target.closest('button')))return;if(['ArrowRight','ArrowDown',' ','PageDown'].includes(e.key)){e.preventDefault();forward()}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();backward()}if(e.key==='Home')go(0);if(e.key==='End')go(slides.length-1,counts.at(-1));if(e.key==='Escape')document.body.classList.remove('overview');if(e.key.toLowerCase()==='o')overview();if(e.key.toLowerCase()==='f')document.querySelector('#fullscreen').click()});
addEventListener('hashchange',route);addEventListener('resize',resize);route();resize();</script>"""

TOOLBAR = """<nav class="toolbar" aria-label="Presentation controls"><button id="fullscreen" aria-label="Full screen" title="Full screen (F)">⛶</button><button id="prev" aria-label="Previous step">←</button><button id="next" aria-label="Next step">→</button><button id="overview" aria-label="Slide overview" title="Overview (O)">▦</button><output id="status" aria-live="polite"></output><span class="reveal-hint" id="hint"></span></nav>"""


def fr(a, b):
	return f'<span class="fraction"><span>{a}</span><span>{b}</span></span>'


def r(html, step=None):
	"""Reveal block, optionally with an explicit step number."""
	s = f' data-step="{step}"' if step else ''
	return f'<div class="reveal"{s}>{html}</div>'


def sol(html, step=None):
	"""One solution step in firebrick, revealed on its own."""
	return r(f'<p class="solution">{html}</p>', step)


def solf(html, step=None):
	"""Solution step containing fractions."""
	return r(f'<div class="solution formula compact">{html}</div>', step)


A, B = '<i>A</i>', '<i>B</i>'
P = 'P'
CAP, CUP = ' ∩ ', ' ∪ '


# ---------------------------------------------------------------- Venn

def venn(uid, hl=None, hl_step=None, numbers=None, selected=(), disjoint=False, aria='Venn diagram of two events A and B'):
	"""Two-set Venn diagram. hl: 'A', 'B', 'AB' (intersection), 'union', 'outside'."""
	if disjoint:
		a, b, rad = (120, 165), (280, 165), 78
	else:
		a, b, rad = (158, 165), (242, 165), 100
	parts = [f'<svg viewBox="0 0 400 350" role="img" aria-label="{aria}">',
		f'<defs><clipPath id="a-{uid}"><circle cx="{a[0]}" cy="{a[1]}" r="{rad}"/></clipPath>'
		f'<mask id="out-{uid}"><rect width="400" height="340" fill="white"/><circle cx="{a[0]}" cy="{a[1]}" r="{rad}" fill="black"/><circle cx="{b[0]}" cy="{b[1]}" r="{rad}" fill="black"/></mask></defs>',
		'<rect x="12" y="12" width="376" height="310" fill="white" stroke="#999"/>']
	if hl:
		s = f' data-step="{hl_step}"' if hl_step else ''
		fill = 'fill="#ecd4d4"'
		shape = {
			'A': f'<circle cx="{a[0]}" cy="{a[1]}" r="{rad}" {fill}/>',
			'B': f'<circle cx="{b[0]}" cy="{b[1]}" r="{rad}" {fill}/>',
			'AB': f'<circle cx="{b[0]}" cy="{b[1]}" r="{rad}" {fill} clip-path="url(#a-{uid})"/>',
			'union': f'<circle cx="{a[0]}" cy="{a[1]}" r="{rad}" {fill}/><circle cx="{b[0]}" cy="{b[1]}" r="{rad}" {fill}/>',
			'outside': f'<rect x="12" y="12" width="376" height="310" {fill} mask="url(#out-{uid})"/>',
		}[hl]
		parts.append(f'<g class="reveal hl"{s}>{shape}</g>')
	parts.append(f'<g fill="none" stroke="#777" stroke-width="1.6"><circle cx="{a[0]}" cy="{a[1]}" r="{rad}"/><circle cx="{b[0]}" cy="{b[1]}" r="{rad}"/></g>')
	if numbers:
		if disjoint:
			pos = [(a[0], 170), None, (b[0], 170), (48, 298)]
		else:
			pos = [(108, 170), (200, 170), (292, 170), (48, 298)]
		t = []
		for k, (n, p) in enumerate(zip(numbers, pos)):
			if p is None or n is None:
				continue
			cls = 'selected' if k in selected else ''
			t.append(f'<text x="{p[0]}" y="{p[1]}" class="{cls}">{n}</text>')
		parts.append('<g class="numbers">' + ''.join(t) + '</g>')
	la = (a[0] - rad * 0.72, 48) if not disjoint else (a[0] - 60, 70)
	lb = (b[0] + rad * 0.72, 48) if not disjoint else (b[0] + 60, 70)
	parts.append(f'<g class="labels"><text x="{la[0]:.0f}" y="{la[1]}" font-style="italic">A</text><text x="{lb[0]:.0f}" y="{lb[1]}" font-style="italic">B</text><text x="18" y="344" font-style="italic">U</text></g>')
	parts.append('</svg>')
	return ''.join(parts)


# ---------------------------------------------------------------- slides

slides = []


def cover(title, subtitle, meta):
	slides.append(('cover', title, subtitle, meta))


def slide(section, subsection, body):
	slides.append(('default', section, subsection, body))


def section(title, lead):
	slides.append(('section', title, lead, None))


cover('Probability', 'The addition law and independent events',
	['Chapter 11 F–G · Mathematics Core Topics HL', 'September 2026'])

slide('F Addition law', 'Compound events', f'''
<div class="columns"><div>{venn('s2', hl='AB', hl_step=1)}</div>
<div>
<h3 class="lead">Two events {A} and {B} in a sample space <i>U</i></h3>
{r(f'<div class="def"><p><b>{A}{CAP}{B}</b>: both {A} and {B} occur</p><p class="small">read: “{A} intersection {B}”</p></div>', 1)}
{r(f'<div class="def"><p><b>{A}{CUP}{B}</b>: {A} or {B} or both occur</p><p class="small">read: “{A} union {B}”</p></div>', 2)}
</div></div>''')

# union shading for step 2 is added by a second highlight layer
slides[-1] = slides[-1][:3] + (slides[-1][3].replace(
	'<g class="reveal hl" data-step="1">',
	'<g class="reveal" data-step="2"><circle cx="158" cy="165" r="100" fill="#ecd4d4"/><circle cx="242" cy="165" r="100" fill="#ecd4d4"/></g><g class="reveal hl" data-step="1">'),)

slide('F Addition law', 'Counting first', f"""
<div class="columns"><div>{venn('s3', hl='AB', hl_step=3, numbers=['12', '2', '17', '68'], selected=(1,))}</div>
<div>
<div class="task q"><p><i>U</i> = {{1, 2, …, 99}}</p><p>{A}: multiples of 7, {B}: multiples of 5</p></div>
{sol(f'n({A}) = 14', 1)}
{sol(f'n({B}) = 19', 2)}
{sol(f'n({A}{CAP}{B}) = 2 (35 and 70)', 3)}
{sol(f'n({A}{CUP}{B}) = 31, not 14 + 19 = 33', 4)}
{sol('35 and 70 are counted twice.', 5)}
{r(f'<div class="thm"><p>n({A}{CUP}{B}) = n({A}) + n({B}) − n({A}{CAP}{B})</p></div>', 6)}
</div></div>""")

slide('F Addition law', 'The addition law of probability', f"""
<p>Dividing by n(<i>U</i>) gives the addition law:</p>
<div class="thm"><div class="thm-title">Addition law</div>
<div class="formula law">P({A}{CUP}{B}) = P({A}) + P({B}) − P({A}{CAP}{B})</div>
<p class="center">P(either {A} or {B} or both) = P({A}) + P({B}) − P(both {A} and {B})</p></div>
{r(f'<div class="remark"><p>P({A}{CAP}{B}) is subtracted because it is contained in P({A}) and in P({B}).</p></div>')}
""")

slide('F Addition law', 'Example 13', f"""
<div class="task q"><p>If P({A}) = 0.6, P({A}{CUP}{B}) = 0.7 and P({A}{CAP}{B}) = 0.3, find P({B}).</p></div>
{sol(f'P({A}{CUP}{B}) = P({A}) + P({B}) − P({A}{CAP}{B})')}
{sol(f'0.7 = 0.6 + P({B}) − 0.3')}
{sol(f'0.7 = 0.3 + P({B})')}
{sol(f'P({B}) = <b>0.4</b>')}
""")

slide('F Addition law', 'Mutually exclusive events', f"""
<div class="columns"><div>{venn('s6', disjoint=True, aria='Venn diagram of two disjoint events A and B')}</div>
<div>
<div class="def"><div class="thm-title">Definition</div><p>{A} and {B} are <b>mutually exclusive</b> (disjoint) if they cannot occur at the same time:</p>
<p class="center">{A}{CAP}{B} = ∅, so P({A}{CAP}{B}) = 0</p></div>
{r(f'<div class="thm"><p>For mutually exclusive events the addition law becomes</p><div class="formula law">P({A}{CUP}{B}) = P({A}) + P({B})</div></div>')}
</div></div>""")

slide('F Addition law', 'Example 14', f"""
<div class="task q"><p>30 students write a History test: 7 score an A, 11 score a B. One student is selected at random.</p>
<p>{A}: the student scored an A, {B}: the student scored a B</p>
<p><b>a)</b> Are {A} and {B} mutually exclusive? <b>b)</b> Find P({A}), P({B}), P({A}{CAP}{B}) and P({A}{CUP}{B}).</p></div>
<div class="two"><div>
{sol('<b>a)</b> No student can score both an A and a B.')}
{sol(f'{A} and {B} are mutually exclusive.')}
</div><div>
{solf(f'<b>b)</b> P({A}) = {fr(7, 30)}, P({B}) = {fr(11, 30)}')}
{sol(f'P({A}{CAP}{B}) = 0')}
{solf(f'P({A}{CUP}{B}) = {fr(7, 30)} + {fr(11, 30)} = {fr(18, 30)} = <b>{fr(3, 5)}</b>')}
</div></div>
""")

slide('F Exercise 1', 'Using the addition law', f"""
<div class="columns"><div>{venn('s8', hl='outside', hl_step=4, numbers=['0.10', '0.25', '0.25', '0.40'], selected=(3,))}</div>
<div>
<div class="task q"><p>P({A}) = 0.35, P({B}) = 0.5 and P({A}{CUP}{B}) = 0.6</p>
<p><b>a)</b> Find P({A}{CAP}{B}). <b>b)</b> Find the probability that neither {A} nor {B} occurs. <b>c)</b> Are {A} and {B} mutually exclusive?</p></div>
{sol(f'<b>a)</b> P({A}{CAP}{B}) = P({A}) + P({B}) − P({A}{CUP}{B})', 1)}
{sol(f'= 0.35 + 0.5 − 0.6 = <b>0.25</b>', 2)}
{sol(f"<b>b)</b> P(({A}{CUP}{B})′) = 1 − P({A}{CUP}{B})", 4)}
{sol('= 1 − 0.6 = <b>0.4</b>', 5)}
{sol(f'<b>c)</b> P({A}{CAP}{B}) = 0.25 ≠ 0: not mutually exclusive', 6)}
</div></div>""")
# numbers in the Venn diagram appear after a)
slides[-1] = slides[-1][:3] + (slides[-1][3].replace('<g class="numbers">', '<g class="numbers reveal" data-step="3">'),)

slide('F Exercise 2', 'Tickets 1 to 20', f"""
<div class="task q"><p>A ticket is drawn at random from tickets numbered 1 to 20.</p>
<p>{A}: multiple of 3, {B}: multiple of 4, <i>C</i>: odd number</p>
<p><b>a)</b> Find P({A}{CUP}{B}). <b>b)</b> Are {B} and <i>C</i> mutually exclusive? Find P({B}{CUP}<i>C</i>).</p></div>
<div class="two"><div>
{sol(f'<b>a)</b> {A} = {{3, 6, 9, 12, 15, 18}}')}
{sol(f'{B} = {{4, 8, 12, 16, 20}}')}
{sol(f'{A}{CAP}{B} = {{12}}')}
{solf(f'P({A}{CUP}{B}) = {fr(6, 20)} + {fr(5, 20)} − {fr(1, 20)} = <b>{fr(1, 2)}</b>')}
</div><div>
{sol('<b>b)</b> Multiples of 4 are even.')}
{sol(f'{B}{CAP}<i>C</i> = ∅: mutually exclusive')}
{solf(f'P({B}{CUP}<i>C</i>) = {fr(5, 20)} + {fr(10, 20)} = <b>{fr(3, 4)}</b>')}
</div></div>""")

section('G Independent events', 'Two events are independent if the occurrence of each event does not affect the occurrence of the other.')

cells_h = ''.join('<td>·</td>' for _ in range(5)) + '<td class="hl reveal" data-step="1">×</td>'
cells_t = ''.join('<td>·</td>' for _ in range(6))
slide('G Independent events', 'Coin and die', f"""
<div class="two"><div>
<h3 class="lead">A coin is tossed and a die is rolled.</h3>
<table class="grid-table"><tr><th></th>{''.join(f'<th>{k}</th>' for k in range(1, 7))}</tr>
<tr><th>H</th>{cells_h}</tr><tr><th>T</th>{cells_t}</tr></table>
<p class="small">12 equally likely outcomes. The coin does not affect the die.</p>
</div><div>
{solf(f'P(H{CAP}6) = {fr(1, 12)}', 1)}
{solf(f'P(H) · P(6) = {fr(1, 2)} · {fr(1, 6)} = {fr(1, 12)}', 2)}
</div></div>
{r(f'<div class="thm"><div class="thm-title">Independent events</div><p class="center" style="font-size:26px">{A} and {B} are independent ⟺ P({A}{CAP}{B}) = P({A}) · P({B})</p></div>', 3)}
""")

slide('G Independent events', 'Example', f"""
<div class="task q"><p>{A} and {B} are independent with P({A}) = 0.3 and P({B}) = 0.5. Find P({A}{CAP}{B}) and P({A}{CUP}{B}).</p></div>
{sol(f'P({A}{CAP}{B}) = P({A}) · P({B}) = 0.3 · 0.5 = <b>0.15</b>')}
{sol(f'P({A}{CUP}{B}) = P({A}) + P({B}) − P({A}{CAP}{B})')}
{sol(f'P({A}{CUP}{B}) = 0.3 + 0.5 − 0.15 = <b>0.65</b>')}
{r(f'<div class="remark"><div class="thm-title" style="color:#c47a00">Careful</div><p>Mutually exclusive does not mean independent. If P({A}) &gt; 0, P({B}) &gt; 0 and {A}, {B} are mutually exclusive, then P({A}{CAP}{B}) = 0 ≠ P({A}) · P({B}): if {A} occurs, {B} cannot occur.</p></div>')}
""")

slide('G Dependent events', 'Drawing without replacement', f"""
<div class="def"><p>Two events are <b>dependent</b> if the occurrence of one affects the probability of the other.</p></div>
<div class="task q"><p>A bag contains 3 red and 2 blue marbles. Two marbles are drawn. Find P(both red).</p></div>
<div class="two"><div>
{sol('With replacement: the second draw is again 3 red of 5.')}
{solf(f'P(RR) = {fr(3, 5)} · {fr(3, 5)} = <b>{fr(9, 25)}</b>')}
</div><div>
{sol('Without replacement: after a red marble only 2 red of 4 are left.')}
{solf(f'P(RR) = {fr(3, 5)} · {fr(2, 4)} = <b>{fr(3, 10)}</b>')}
</div></div>
""")

slide('G Exercise 3', 'Testing for independence', f"""
<div class="task q"><p>P({A}) = 0.4, P({B}) = 0.5 and P({A}{CUP}{B}) = 0.7. Are {A} and {B} independent?</p></div>
{sol(f'P({A}{CAP}{B}) = P({A}) + P({B}) − P({A}{CUP}{B})')}
{sol(f'P({A}{CAP}{B}) = 0.4 + 0.5 − 0.7 = 0.2')}
{sol(f'P({A}) · P({B}) = 0.4 · 0.5 = 0.2')}
{sol(f'P({A}{CAP}{B}) = P({A}) · P({B}), so {A} and {B} are <b>independent</b>.')}
""")

slide('G Exercise 4', 'Two archers', f"""
<div class="task q"><p>Anna and Ben shoot at a target independently. Anna hits with probability 0.7, Ben with probability 0.6.</p>
<p>Find the probability that <b>a)</b> both hit, <b>b)</b> at least one hits, <b>c)</b> neither hits.</p></div>
{sol(f'<b>a)</b> P({A}{CAP}{B}) = 0.7 · 0.6 = <b>0.42</b>')}
{sol(f'<b>b)</b> P({A}{CUP}{B}) = 0.7 + 0.6 − 0.42 = <b>0.88</b>')}
{sol(f"<b>c)</b> P({A}′{CAP}{B}′) = 0.3 · 0.4 = <b>0.12</b>")}
{sol('Check: 1 − 0.88 = 0.12')}
""")

section('Practice', 'Exercise 11F: 1, 4, 5<br><span class="small" style="color:#777">Mathematics Core Topics HL, pp. 266–267</span>')


# ---------------------------------------------------------------- render

N = len(slides)


def dots():
	return '<nav class="nav-dots" aria-label="Slides">' + ''.join(
		f'<button class="nav-dot" data-go="{k}" aria-label="Slide {k + 1}"></button>' for k in range(N)) + '</nav>'


def footer(k):
	return f'<footer class="slide-footer"><span class="footer-right">{k + 1}/{N}</span></footer>'


SYMS = '∩∪∅′≠⟺'


def sym(text):
	return ''.join(f'<span class="sym">{c}</span>' if c in SYMS else c for c in text)


html = []
for k, s in enumerate(slides):
	kind = s[0]
	if kind == 'cover':
		_, title, sub, meta = s
		html.append(f'<section class="slide layout-cover" aria-label="Slide {k + 1}" hidden><div class="cover-body"><div class="cover-title-box"><h1 class="cover-title">{title}</h1><p class="cover-subtitle">{sub}</p></div><div class="cover-meta">' + ''.join(f'<div>{m}</div>' for m in meta) + f'</div></div>{footer(k)}</section>')
	elif kind == 'section':
		_, title, lead, _ = s
		html.append(f'<section class="slide layout-section" aria-label="Slide {k + 1}" hidden>{dots()}<div class="section-body"><div class="section-title-box"><h1>{title}</h1></div><p class="section-lead">{lead}</p></div>{footer(k)}</section>')
	else:
		_, sec, sub, body = s
		html.append(f'<section class="slide layout-default" aria-label="Slide {k + 1}" hidden><header class="slide-header bands-2"><div class="header-section">{sec}</div><div class="header-subsection">{sub}</div></header>{dots()}<div class="slide-content">{body}</div>{footer(k)}</section>')

page = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
	'<title>Probability · Addition law and independent events</title>'
	'<meta name="description" content="Chapter 11 F–G: the addition law, mutually exclusive, independent and dependent events, with step-by-step exercises.">'
	+ STYLE + EXTRA_CSS + '</head><body><main id="stage">' + sym(''.join(html)) + '</main>' + TOOLBAR + SCRIPT + '</body></html>')
OUT.write_text(page)
print(OUT, N, 'slides', len(page) // 1024, 'KB')
