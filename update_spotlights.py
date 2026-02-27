import re

filename = 'index.html'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize newlines just in case
content = content.replace('\r\n', '\n')

# 1. Remove details accordions if any exist
content = re.sub(
    r'\s*<details class="ds-card-details">.*?</details>\n*', 
    '\n', 
    content, 
    flags=re.DOTALL
)

# 2. Add New Spotlight: Mi Cartera (After SPOTLIGHT 1: DASHBOARD aka Mi Visión 360)
cartera_html = """
    <!-- ════════════════════════════════════════
     SPOTLIGHT 1.5: MI CARTERA
  ════════════════════════════════════════ -->
    <section id="cartera-spotlight" class="section spotlight" style="background:rgba(16,185,129,0.02)">
        <div class="bg-glow glow-emerald"
            style="width:600px;height:600px;top:50%;left:-100px;transform:translateY(-50%);opacity:0.3;"></div>
        <div class="container">
            <div class="spotlight-grid reverse">
                
                <!-- UI Panel: Asset Allocation -->
                <div class="ui-panel reveal reveal-delay-2">
                    <div style="font-size:0.65rem;color:var(--text-tertiary);font-weight:600;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:16px;">
                        ASSET ALLOCATION</div>
                    
                    <div style="display:flex; justify-content:center; margin:20px 0;">
                        <!-- Mock Donut Chart using SVG -->
                        <svg viewBox="0 0 100 100" width="160" height="160">
                            <!-- Background ring -->
                            <circle cx="50" cy="50" r="40" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="15" />
                            <!-- Acciones (60%) -->
                            <circle cx="50" cy="50" r="40" fill="none" stroke="#6366f1" stroke-width="15" stroke-dasharray="150.8 251.2" stroke-dashoffset="0" transform="rotate(-90 50 50)" />
                            <!-- ETFs (20%) -->
                            <circle cx="50" cy="50" r="40" fill="none" stroke="#8b5cf6" stroke-width="15" stroke-dasharray="50.24 251.2" stroke-dashoffset="-150.8" transform="rotate(-90 50 50)" />
                            <!-- Efectivo (10%) -->
                            <circle cx="50" cy="50" r="40" fill="none" stroke="#10b981" stroke-width="15" stroke-dasharray="25.12 251.2" stroke-dashoffset="-201.04" transform="rotate(-90 50 50)" />
                            <!-- Crypto (10%) -->
                            <circle cx="50" cy="50" r="40" fill="none" stroke="#f59e0b" stroke-width="15" stroke-dasharray="25.12 251.2" stroke-dashoffset="-226.16" transform="rotate(-90 50 50)" />
                        </svg>
                    </div>

                    <div class="ret-items" style="margin-top:24px;">
                        <div class="ret-item">
                            <div class="ret-item-label"><span class="ret-item-dot" style="background:#6366f1;"></span>Acciones Totales</div>
                            <div class="ret-item-val" style="color:var(--text-primary);">60.0%</div>
                        </div>
                        <div class="ret-item">
                            <div class="ret-item-label"><span class="ret-item-dot" style="background:#8b5cf6;"></span>ETFs (Indexados)</div>
                            <div class="ret-item-val" style="color:var(--text-primary);">20.0%</div>
                        </div>
                        <div class="ret-item">
                            <div class="ret-item-label"><span class="ret-item-dot" style="background:#10b981;"></span>Efectivo & Renta Fija</div>
                            <div class="ret-item-val" style="color:var(--text-primary);">10.0%</div>
                        </div>
                        <div class="ret-item">
                            <div class="ret-item-label"><span class="ret-item-dot" style="background:#f59e0b;"></span>Criptomonedas</div>
                            <div class="ret-item-val" style="color:var(--text-primary);">10.0%</div>
                        </div>
                    </div>
                </div>

                <!-- Text -->
                <div class="spotlight-text reveal">
                    <div class="section-tag"><svg class="ds-svg" viewBox="0 0 24 24">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="16" y1="2" x2="16" y2="6"></line>
                            <line x1="8" y1="2" x2="8" y2="6"></line>
                            <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg> Mi Cartera</div>
                    <h2 class="display-md">Diversificación inteligente.<br /><span class="gradient-text">Control absoluto.</span></h2>
                    <p class="body-md" style="margin-bottom:32px;">Controla tu cartera y aprende cómo equilibrarla según tu perfil de riesgo, sin recomendaciones de fondos concretos.</p>

                    <div class="spotlight-bullets">
                        <div class="bullet-item">
                            <div class="bullet-icon" style="background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.2);">
                                <svg class="ds-svg" viewBox="0 0 24 24">
                                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                                    <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                                    <line x1="12" y1="22.08" x2="12" y2="12"></line>
                                </svg>
                            </div>
                            <div>
                                <strong>Asset Allocation Detallado</strong>
                                <span>Desglosa tus inversiones por clase de activo: Acciones, ETFs, REITs, Bonos y Crypto de un solo vistazo.</span>
                            </div>
                        </div>
                        <div class="bullet-item">
                            <div class="bullet-icon" style="background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.2);">
                                <svg class="ds-svg" viewBox="0 0 24 24">
                                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                                </svg>
                            </div>
                            <div>
                                <strong>Top Movers y Rentabilidad</strong>
                                <span>Detecta rápidamente qué activos están impulsando tu rentabilidad y analiza las desviaciones.</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

# 3. Add New Spotlight: Mi Progreso (After SPOTLIGHT 3: MI FUTURO)
progreso_html = """
    <!-- ════════════════════════════════════════
     SPOTLIGHT 4: MI PROGRESO
  ════════════════════════════════════════ -->
    <section id="progreso-spotlight" class="section spotlight" style="background:rgba(245,158,11,0.02)">
        <div class="bg-glow glow-amber"
            style="width:500px;height:500px;top:50%;right:-100px;transform:translateY(-50%);opacity:0.3;"></div>
        <div class="container">
            <div class="spotlight-grid">
                
                <!-- Text -->
                <div class="spotlight-text reveal">
                    <div class="section-tag" style="color:#f59e0b; border-color:rgba(245,158,11,0.3); background:rgba(245,158,11,0.1);">
                        <svg class="ds-svg" viewBox="0 0 24 24" style="color:#f59e0b;">
                            <path d="M12 14v4"></path>
                            <path d="M12 2A10 10 0 0 1 22 12A10 10 0 0 1 2 12A10 10 0 0 1 12 2Z"></path>
                            <path d="M12 14L15.5 10.5"></path>
                        </svg> Mi Progreso
                    </div>
                    <h2 class="display-md">Tus metas, cumplidas.<br /><span style="background:linear-gradient(90deg,#f59e0b,#fbbf24);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Sin excusas.</span></h2>
                    <p class="body-md" style="margin-bottom:32px;">Control de ahorro anual. KPIs de Crecimiento del Año, Media Mensual y Desviación respecto a tu objetivo configurado.</p>

                    <div class="spotlight-bullets">
                        <div class="bullet-item">
                            <div class="bullet-icon" style="background:rgba(245,158,11,0.15);border-color:rgba(245,158,11,0.2);">
                                <svg class="ds-svg" viewBox="0 0 24 24" style="color:#f59e0b;">
                                    <path d="M3 3v18h18"></path>
                                    <path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"></path>
                                </svg>
                            </div>
                            <div>
                                <strong>Control de Ahorro YTD</strong>
                                <span>Compara tu ahorro acumulado del año actual (Year-To-Date) con la meta ambiciosa que te fijaste.</span>
                            </div>
                        </div>
                        <div class="bullet-item">
                            <div class="bullet-icon" style="background:rgba(245,158,11,0.15);border-color:rgba(245,158,11,0.2);">
                                <svg class="ds-svg" viewBox="0 0 24 24" style="color:#f59e0b;">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <polyline points="12 6 12 12 16 14"></polyline>
                                </svg>
                            </div>
                            <div>
                                <strong>Media Mensual y Desviaciones</strong>
                                <span>Observa la media mensual de crecimiento y corrige desviaciones a tiempo para asegurar tu éxito a final de año.</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- UI Panel: Progress KPI -->
                <div class="ui-panel reveal reveal-delay-2" style="border-top:4px solid #f59e0b;">
                    <div style="font-size:0.65rem;color:var(--text-tertiary);font-weight:600;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:16px;">
                        OBJETIVO DE AHORRO 2026</div>

                    <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:12px;">
                        <div>
                            <div style="font-size:2rem; font-weight:700; color:var(--text-primary); letter-spacing:-0.03em;">€9.000</div>
                            <div style="font-size:0.85rem; color:var(--text-tertiary);">Ahorro YTD Acumulado</div>
                        </div>
                        <div style="text-align:right;">
                            <div style="font-size:1.1rem; font-weight:600; color:var(--text-secondary);">€12.000</div>
                            <div style="font-size:0.85rem; color:var(--text-tertiary);">Meta Anual</div>
                        </div>
                    </div>
                    
                    <div class="ret-goal-bar" style="height:12px; margin-bottom:24px;">
                        <div class="ret-goal-fill" style="width:75%; background:linear-gradient(90deg,#f59e0b,#fbbf24);"></div>
                    </div>

                    <div class="ret-items">
                        <div class="ret-item" style="background:rgba(255,255,255,0.02); padding:12px; border-radius:8px; border:1px solid var(--border);">
                            <div class="ret-item-label" style="font-size:0.75rem;">Progreso Total</div>
                            <div class="ret-item-val" style="color:#f59e0b; font-size:1.2rem; font-weight:700;">75.0%</div>
                        </div>
                        <div class="ret-item" style="background:rgba(255,255,255,0.02); padding:12px; border-radius:8px; border:1px solid var(--border);">
                            <div class="ret-item-label" style="font-size:0.75rem;">Media Mensual</div>
                            <div class="ret-item-val" style="color:var(--text-primary); font-size:1.2rem; font-weight:700;">€1.125</div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

# Inject Cartera
# Look for "<!-- ════════════════════════════════════════\n     SPOTLIGHT 2: AI ADVISOR"
content, count = re.subn(
    r'(<!-- [═]+\n\s+SPOTLIGHT 2: AI ADVISOR)', 
    cartera_html + r'\1', 
    content
)
if count > 0:
    print("Injected Cartera Spotlight.")

# Inject Progreso
# Look for FOOTER
content, count2 = re.subn(
    r'(<!-- [═]+\n\s+FOOTER)', 
    progreso_html + r'\1', 
    content
)
if count2 > 0:
    print("Injected Progreso Spotlight.")

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Total injections: Cartera ({count}), Progreso ({count2})")
