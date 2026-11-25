"""Общая морская палитра карточек профиля и обновляемой статистики."""
import re

PALETTE = {
    '#141414': '#061E29', '#1A1A1A': '#0A2B38', '#303030': '#235360',
    '#EDEDED': '#E5F4F4', '#A1A1A1': '#A2C2CA', '#F4F4F5': '#67DDE0',
    '#52A8FF': '#4ECBD3', '#B4D8FF': '#B3E5E7', '#D4D4D8': '#8DD9DE',
    '#242424': '#0D2A35', '#173C61': '#14424E', '#245D94': '#1B6572',
    '#3387D4': '#2895A2',
}


def oceanize(svg):
    """Сохраняет содержимое SVG; оформляет фон, рамки, значки и акценты."""
    if 'data-ocean-theme="1"' in svg:
        return svg
    svg = re.sub(r'#[0-9A-Fa-f]{6}', lambda m: PALETTE.get(m[0].upper(), m[0]), svg)
    match = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    if not match:
        raise ValueError('Карточка должна иметь viewBox')
    width, height = map(float, match.groups())
    svg = svg.replace('<svg ', '<svg data-ocean-theme="1" ', 1)
    definitions = f'''<defs>
<linearGradient id="sea-panel" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0C3441"/><stop offset=".6" stop-color="#06232F"/><stop offset="1" stop-color="#041822"/></linearGradient>
<clipPath id="sea-clip"><rect x="1" y="1" width="{width-2:g}" height="{height-2:g}" rx="18"/></clipPath>
</defs>'''
    svg = re.sub(r'(<title>.*?</title>)', lambda m: m[0]+definitions, svg, count=1)
    # Only the main background uses the gradient; tiles retain a solid readable fill.
    svg = svg.replace('fill="#061E29"', 'fill="url(#sea-panel)"', 1)
    decoration = f'''<g clip-path="url(#sea-clip)" aria-hidden="true"><g transform="scale({width/780:g} {height/330:g})" opacity=".18">
<path d="M300 330C400 240 451 305 520 263S654 244 780 172V330Z" fill="#146174"/>
<path d="M328 330C427 266 478 321 552 281S672 260 780 218" stroke="#59CED8" stroke-width="1.2"/>
<path d="M370 330C450 294 505 337 585 297S703 291 780 250" stroke="#59CED8"/>
<path d="M407 330C487 308 542 350 620 316S727 311 780 284" stroke="#B3E5E7"/>
</g></g>'''
    # Insert after the card background so all labels/icons remain above the waves.
    start = svg.index('</defs>')+len('</defs>')
    main_rect_end = svg.index('/>', svg.index('<rect ', start))+2
    return svg[:main_rect_end]+decoration+svg[main_rect_end:]
