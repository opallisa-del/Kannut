import re

files = ['index.html', 'index2.html', 'index3.html', 'index4.html']

extra_info = {
    "vision360": "Visualiza tu patrimonio neto actualizado en tiempo real. Analiza tu rentabilidad histórica (YTD), el yield promedio de tus inversiones y monitorea los ingresos pasivos generados mes a mes frente a tus objetivos.",
    "cartera": "Desglosa tus inversiones por clase de activo (Acciones, ETFs, REITs, Bonos, Crypto). Detecta desviaciones respecto a tu asset allocation ideal y descubre qué activos impulsan tu rentabilidad (Top Movers).",
    "asesor": "Interactúa con Gemini, un asistente de IA avanzado que conoce el contexto de tu cartera. Resuelve tus dudas financieras, pide análisis de rebalanceo y obtén educación financiera personalizada al instante, 24/7.",
    "futuro": "Proyecta tu libertad financiera. Un simulador de ciclo de vida que cruza tus ahorros, rentabilidad esperada, planes de compensación a largo plazo (LTIP) y estimaciones de pensión pública para calcular tu año exacto de jubilación.",
    "progreso": "Mantén el rumbo con KPIs precisos. Compara tu ahorro acumulado del año con la meta que te fijaste. Observa la media mensual de crecimiento y corrige desviaciones a tiempo para asegurar tu éxito financiero.",
    "configuracion": "El motor de Kannut. Ajusta parámetros clave: tu año de nacimiento (horizonte temporal), retención fiscal (IRPF), expectativas de pensión pública y objetivo de ingresos pasivos, logrando que cada cálculo sea 100% fiel a tu realidad."
}

def generate_details_html(info_text):
    return f"""
                    <details class="ds-card-details">
                        <summary>Saber más</summary>
                        <p>{info_text}</p>
                    </details>
"""

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        for block_id, info in extra_info.items():
            # Example card:
            # <div id="vision360" class="ds-card ds-card-highlight">
            #   ...
            #   <span class="ds-card-tags">...</span>
            # </div>
            
            # The regex looks for the block starting with `<div id="block_id"`,
            # captures everything until the tags, captures the closing div,
            # and injects the details block before the closing div.
            
            pattern = re.compile(
                r'(<div id="' + block_id + r'" class="[^"]*">[\s\S]*?<span class="ds-card-tags">[^<]*</span>\s*)(</div>)',
                re.IGNORECASE
            )
            
            match = pattern.search(content)
            if match:
                # check if it already has ds-card-details
                if 'ds-card-details' not in match.group(0):
                    replacement = match.group(1) + generate_details_html(info) + match.group(2)
                    content = content[:match.start()] + replacement + content[match.end():]

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")

