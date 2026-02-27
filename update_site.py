import re
import os

HTML1 = 'c:/Users/oscar/.gemini/antigravity/workspaces/galactic-gemini/index.html'
HTML2 = 'c:/Users/oscar/.gemini/antigravity/workspaces/galactic-gemini/index2.html'
CSS1 = 'c:/Users/oscar/.gemini/antigravity/workspaces/galactic-gemini/styles.css'
CSS2 = 'c:/Users/oscar/.gemini/antigravity/workspaces/galactic-gemini/styles2.css'

# The SVG definitions matching the requested design:
svg_bar = '<svg class="ds-svg" viewBox="0 0 24 24"><path d="M18 20V10M12 20V4M6 20v-6"></path></svg>'
svg_calendar = '<svg class="ds-svg" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'
svg_bot = '<svg class="ds-svg" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8.01" y2="16"></line><line x1="16" y1="16" x2="16.01" y2="16"></line></svg>'
svg_linechart = '<svg class="ds-svg" viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>'
svg_guage = '<svg class="ds-svg" viewBox="0 0 24 24"><path d="M12 14v4"></path><path d="M12 2A10 10 0 0 1 22 12A10 10 0 0 1 2 12A10 10 0 0 1 12 2Z"></path><path d="M12 14L15.5 10.5"></path></svg>'
svg_settings = '<svg class="ds-svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>'

ds_cards_html = f"""
      <div class="ds-feature-grid">
        <div class="ds-card ds-card-highlight">
          <div class="ds-icon-box" style="background:#5559E8;">
            {svg_bar}
          </div>
          <h3 class="ds-card-title">Dashboard en Tiempo Real</h3>
          <p class="ds-card-desc">KPIs clave, evolución temporal de tu patrimonio, top movers del día y progreso hacia tu objetivo de jubilación — todo en una sola pantalla.</p>
          <span class="ds-card-tags">PATRIMONIO · YIELD · YTD</span>
        </div>

        <div class="ds-card">
          <div class="ds-icon-box" style="background:var(--ds-emerald-500);">
            {svg_calendar}
          </div>
          <h3 class="ds-card-title">Gestión de Cartera</h3>
          <p class="ds-card-desc">Añade, edita y organiza tus posiciones. Visualiza ganancias y pérdidas por activo, calcula el rebalanceo óptimo y controla tu coste medio.</p>
          <span class="ds-card-tags">ACCIONES · ETFs · REITs · BONOS</span>
        </div>

        <div class="ds-card">
          <div class="ds-icon-box" style="background:var(--ds-violet-500);">
            {svg_bot}
          </div>
          <h3 class="ds-card-title">Asesor IA Personalizado</h3>
          <p class="ds-card-desc">Chatea con un asesor financiero potenciado por IA que conoce tu cartera al detalle. Pregunta, analiza y recibe recomendaciones en segundos.</p>
          <span class="ds-card-tags">GEMINI · ANÁLISIS · CONSEJOS</span>
        </div>

        <div class="ds-card">
          <div class="ds-icon-box" style="background:var(--ds-sky-500);">
            {svg_linechart}
          </div>
          <h3 class="ds-card-title">Simulador de Jubilación</h3>
          <p class="ds-card-desc">Proyecta el crecimiento de tu patrimonio con diferentes escenarios de ahorro, rentabilidad esperada y rentabilidad por dividendos.</p>
          <span class="ds-card-tags">PROYECCIONES · ESCENARIOS</span>
        </div>

        <div class="ds-card">
          <div class="ds-icon-box" style="background:var(--ds-amber-500);">
            {svg_guage}
          </div>
          <h3 class="ds-card-title">Seguimiento de Ahorro Anual</h3>
          <p class="ds-card-desc">Registra y visualiza tu progreso de ahorro mes a mes. Compara tu ritmo real vs. tu objetivo y mantente en camino.</p>
          <span class="ds-card-tags">METAS · PROGRESO · HÁBITOS</span>
        </div>

        <div class="ds-card">
          <div class="ds-icon-box" style="background:var(--ds-rose-500);">
            {svg_settings}
          </div>
          <h3 class="ds-card-title">Configuración Inteligente</h3>
          <p class="ds-card-desc">Onboarding guiado, configuración de pensión pública, LTIP, tipo marginal y objetivos de ingresos pasivos mensuales personalizados.</p>
          <span class="ds-card-tags">ONBOARDING · LTIP · PENSIÓN</span>
        </div>
      </div>
"""

def update_file(path, features_regex, login_btn_style):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Link design system css
    if 'design-system.css' not in content:
        content = content.replace('<link rel="stylesheet" href="styles', '<link rel="stylesheet" href="design-system.css" />\n  <link rel="stylesheet" href="styles')
    
    # Replace feature grid
    content = re.sub(features_regex, ds_cards_html, content, flags=re.DOTALL)

    # Emoji replacements
    content = content.replace('💎', '<svg class="ds-svg" viewBox="0 0 24 24"><polygon points="12 2 2 7 12 22 22 7 12 2"></polygon></svg>')
    content = content.replace('🤖', svg_bot)
    content = content.replace('📊', svg_bar)
    content = content.replace('💼', svg_calendar)
    content = content.replace('📉', svg_linechart)
    content = content.replace('📈', svg_linechart)
    content = content.replace('🎯', svg_guage)
    content = content.replace('⚙️', svg_settings)
    content = content.replace('🏖️', svg_linechart)
    
    content = content.replace('💰', '<svg class="ds-svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v8M8 12h8"></path></svg>')
    content = content.replace('🟢', '')
    content = content.replace('🔮', '')
    content = content.replace('🏦', '<svg class="ds-svg" viewBox="0 0 24 24"><polygon points="12 2 2 7 22 7"></polygon><rect x="4" y="9" width="4" height="11"></rect><rect x="16" y="9" width="4" height="11"></rect><rect x="2" y="20" width="20" height="2"></rect></svg>')
    content = content.replace('📅', svg_calendar)

    # 3. Insert Login and Download Buttons
    # Nav links manipulation
    login_html = '<li><a href="#" class="nav-login">Login</a></li>'
    if 'class="nav-login"' not in content:
        # insert before the CTA
        if 'class="nav-cta"' in content:
            content = content.replace('<li><a href="#cta" class="nav-cta">', login_html + '\\n        <li><a href="#cta" class="nav-cta">')
        elif 'class="nav-btn"' in content:
            content = content.replace('<li><a href="#cta" class="nav-btn">', login_html + '\\n                <li><a href="#cta" class="nav-btn">')

    # Also add download buttons to hero actions
    app_stores = """
          <div class="ds-app-badges" style="margin-top: 16px;">
             <a href="#"><img src="https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us?size=250x83&amp;releaseDate=1276560000&h=7e7b68fad19738b5649a1bfb78ff46e9" class="ds-app-badge" alt="Download on App Store"></a>
             <a href="#"><img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" class="ds-app-badge" style="height:56px; margin-top:-8px;" alt="Get it on Google Play"></a>
          </div>
    """
    if "ds-app-badges" not in content:
        # index.html wrapper
        content = content.replace('Ver funcionalidades\\n          </a>\\n        </div>', 'Ver funcionalidades\\n          </a>\\n        </div>\\n' + app_stores)
        # index2.html wrapper
        content = content.replace('Ver la app ↓\\n            </a>\\n        </div>', 'Ver la app ↓\\n            </a>\\n        </div>\\n' + app_stores)

    # Add class ds-applied to body
    content = content.replace('<body>', '<body class="ds-applied">')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


# Run for index.html
update_file(HTML1, r'<div class="features-grid">.*?</div>\s*</div>\s*</section>', f'<div class="container">{ds_cards_html}</div>\n    </div>\n  </section>')

# Run for index2.html
update_file(HTML2, r'<div class="mosaic-grid">.*?</div>\s*</section>', f'{ds_cards_html}\n    </section>')
print("Done updating files.")
