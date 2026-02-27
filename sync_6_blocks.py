import re

files_v1 = ["index.html", "index4.html"]
files_v2 = ["index2.html", "index3.html"]

nav_links_v1 = """      <ul class="nav-links">
        <li><a href="#vision360">Mi Visi&oacute;n 360</a></li>
        <li><a href="#cartera">Mi Cartera</a></li>
        <li><a href="#asesor">Mi Asesor Personal</a></li>
        <li><a href="#futuro">Mi Futuro</a></li>
        <li><a href="#progreso">Mi Progreso</a></li>
        <li><a href="#configuracion">Mi Configuraci&oacute;n</a></li>
        <li><a href="login.html" class="nav-login">Login</a></li>
        <li><a href="#cta" class="nav-cta">Empezar gratis &rarr;</a></li>
      </ul>"""

nav_links_v2 = """            <ul class="nav-links">
                <li><a href="#vision360">Mi Visi&oacute;n 360</a></li>
                <li><a href="#cartera">Mi Cartera</a></li>
                <li><a href="#asesor">Mi Asesor Personal</a></li>
                <li><a href="#futuro">Mi Futuro</a></li>
                <li><a href="#progreso">Mi Progreso</a></li>
                <li><a href="#configuracion">Mi Configuraci&oacute;n</a></li>
                <li><a href="login.html" class="nav-login">Login</a></li>
                <li><a href="#cta" class="nav-btn">Empezar gratis</a></li>
            </ul>"""

configuracion_mosaic = """
            <!-- Mi Configuracion -->
            <div class="mosaic-card reveal">
                <div class="mc-glow" style="background:rgba(225,29,72,0.12);"></div>
                <div class="mc-icon-wrap" style="background:linear-gradient(135deg,#e11d48,#fb7185);">
                    <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.9)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="3"></circle>
                        <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                    </svg>
                </div>
                <div class="mc-tag">Mi Configuraci&oacute;n</div>
                <div class="mc-title">Perfiles e<br>impuestos.</div>
                <p class="mc-body">Personaliza tu perfil: a&ntilde;o de nacimiento, objetivo de rentas, pensi&oacute;n p&uacute;blica, LTIP y marginal de IRPF. Todo para c&aacute;lculos precisos.</p>
                <span class="mc-stat rose" style="font-size:2rem;margin-top:auto;">100%</span>
                <span class="mc-subtitle">Personalizable</span>
            </div>
"""

# Extract the <section id="features"...> from index4.html
with open("index4.html", "r", encoding="utf-8") as f:
    content4 = f.read()

features_match = re.search(r'(<section id="features" class="section">[\s\S]*?</section>)', content4)
if features_match:
    features_html_v1 = features_match.group(1)

# Process V1 files
for file in files_v1:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace nav links
    content = re.sub(r'<ul class="nav-links">[\s\S]*?</ul>', nav_links_v1, content)
    
    # Inject exact features section into index.html if it's not identical 
    # (they both use the same structure)
    if "index.html" in file and features_match:
        content = re.sub(r'<section id="features" class="section">[\s\S]*?</section>', features_html_v1, content)
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file}")

# Process V2 files
for file in files_v2:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace nav links
    content = re.sub(r'<ul class="nav-links">[\s\S]*?</ul>', nav_links_v2, content)
    
    # Rename items in the mosaic
    content = content.replace('<div class="mc-tag">Mi Dashboard</div>', '<div class="mc-tag">Mi Visi&oacute;n 360</div>')
    content = content.replace('<div class="mc-tag">Mi Asesor</div>', '<div class="mc-tag">Mi Asesor Personal</div>')
    
    # Inject "Mi Configuracion" if not present
    if "Mi Configuraci" not in content and '<div class="mosaic-grid">' in content:
        # find the end of the last mosaic-card inside mosaic-grid
        # actually, just append it before the ending </div> of the mosaic-grid.
        # But wait, mosaic grid ends right before </section>. Let's inject after the last mosaic card.
        # So we can search for the end of the mosaic grid.
        # A simpler way:
        content = re.sub(r'(</div>\s*</section>)', configuracion_mosaic + r'\1', content, count=1)
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file}")
