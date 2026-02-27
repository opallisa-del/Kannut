import re

files = ['index.html', 'index2.html', 'index3.html', 'index4.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the feature cards and add IDs
    # For "Mi Visión 360", we look for "ds-card" followed heavily by "Mi Visi&oacute;n 360" or "Mi Visión 360"
    
    # Alternatively, just use regex with re.sub to inject IDs into the ds-card parent.
    # It's easier if we replace specific known blocks.
    
    replacements = {
        r'<div class="ds-card ds-card-highlight">(\s*<div[^>]*>\s*<svg[^>]*>.*?</svg>\s*</div>\s*<h3 class="ds-card-title">Mi Visión 360</h3>)': r'<div id="vision360" class="ds-card ds-card-highlight">\1',
        r'<div class="ds-card ds-card-highlight">(\s*<div[^>]*>\s*<img[^>]*>\s*</div>\s*<h3 class="ds-card-title">Mi Visión 360</h3>)': r'<div id="vision360" class="ds-card ds-card-highlight">\1',
    }
    
    # Wait, the cards in the HTML:
    # <div class="ds-card ds-card-highlight"> ... <h3 class="ds-card-title">Mi Visión 360</h3>
    # I can just do:
    content = re.sub(r'<div class="(ds-card ds-card-highlight|ds-card)">\s*<div class="ds-icon-box"[^>]*>[\s\S]*?</div>\s*<h3 class="ds-card-title">Mi Visión 360</h3>',  lambda m: m.group(0).replace('<div class="'+m.group(1)+'">', f'<div id="vision360" class="{m.group(1)}">'), content)
    
    content = re.sub(r'<div class="(ds-card ds-card-highlight|ds-card)">\s*<div class="ds-icon-box"[^>]*>[\s\S]*?</div>\s*<h3 class="ds-card-title">Mi Cartera</h3>',  lambda m: m.group(0).replace('<div class="'+m.group(1)+'">', f'<div id="cartera" class="{m.group(1)}">'), content)
    
    content = re.sub(r'<div class="(ds-card ds-card-highlight|ds-card)">\s*<div class="ds-icon-box"[^>]*>[\s\S]*?</div>\s*<h3 class="ds-card-title">Mi Asesor Personal</h3>',  lambda m: m.group(0).replace('<div class="'+m.group(1)+'">', f'<div id="asesor" class="{m.group(1)}">'), content)
    
    content = re.sub(r'<div class="(ds-card ds-card-highlight|ds-card)">\s*<div class="ds-icon-box"[^>]*>[\s\S]*?</div>\s*<h3 class="ds-card-title">Mi Futuro</h3>',  lambda m: m.group(0).replace('<div class="'+m.group(1)+'">', f'<div id="futuro" class="{m.group(1)}">'), content)
    
    content = re.sub(r'<div class="(ds-card ds-card-highlight|ds-card)">\s*<div class="ds-icon-box"[^>]*>[\s\S]*?</div>\s*<h3 class="ds-card-title">Mi Progreso</h3>',  lambda m: m.group(0).replace('<div class="'+m.group(1)+'">', f'<div id="progreso" class="{m.group(1)}">'), content)
    
    content = re.sub(r'<div class="(ds-card ds-card-highlight|ds-card)">\s*<div class="ds-icon-box"[^>]*>[\s\S]*?</div>\s*<h3 class="ds-card-title">Mi Configuración</h3>',  lambda m: m.group(0).replace('<div class="'+m.group(1)+'">', f'<div id="configuracion" class="{m.group(1)}">'), content)

    # Note that in the nav links, some have target #asesor but maybe there are spotlight sections.
    # To be fully safe and jump to the exact sections, we can ALSO add anchors to the spotlights if they match!
    # If the user clicks "Mi Asesor Personal", maybe they want to see the Spotlight section which is better?
    # Both work, but we'll modify the links in the <nav> to point to the IDs we just added into .ds-card elements. Wait! Let's check if the nav link already matches!
    # The nav links are:
    # <li><a href="#vision360">Mi Visi&oacute;n 360</a></li>
    # <li><a href="#cartera">Mi Cartera</a></li>
    # <li><a href="#asesor">Mi Asesor Personal</a></li>
    # <li><a href="#futuro">Mi Futuro</a></li>
    # <li><a href="#progreso">Mi Progreso</a></li>
    # <li><a href="#configuracion">Mi Configuraci&oacute;n</a></li>
    
    # If we add these IDs to the cards, it's done!

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
