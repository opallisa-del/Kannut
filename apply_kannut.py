import os

files = [
    r"C:\Users\oscar\.gemini\antigravity\workspaces\galactic-gemini\index.html",
    r"C:\Users\oscar\.gemini\antigravity\workspaces\galactic-gemini\index2.html",
    r"C:\Users\oscar\.gemini\antigravity\workspaces\galactic-gemini\index3.html",
    r"C:\Users\oscar\.gemini\antigravity\workspaces\galactic-gemini\index4.html"
]

# We will apply specific replacements across all files.

replacements = [
    # Hero badge (index, index4)
    (
        "Nuevo — Asesor IA Gemini con acceso a tu cartera",
        "Conoce tu cartera y define tus objetivos: la app que enseña para que tú decidas."
    ),
    (
        "Nuevo — Modo Simulador",
        "Tu guía financiera personal: educación, seguimiento y planificación, sin recomendaciones de productos específicos."
    ),

    # Dashboard 
    (
        "El dashboard es tu centro de control financiero. Refleja en tiempo real tu patrimonio neto, tus ingresos pasivos generados y la distancia exacta hasta tu independencia financiera.",
        "Sigue tu progreso financiero, define metas y toma decisiones informadas con datos claros y objetivos."
    ),
    (
        "Patrimonio Total con tendencia YTD, Ingreso Pasivo Real (solo distribución — dividendos, cupones, rentas), Rendimiento Medio ponderado y el anillo de progreso hacia tu jubilación. Todo en la pantalla de inicio.",
        "Sigue tu progreso financiero, define metas y toma decisiones informadas con datos claros y objetivos."
    ),

    # Cartera 
    (
        "Añade activos con búsqueda de ticker/ISIN, actualización automática de precios y dividendos. Activos de distribución vs acumulación. Rebalanceo recomendado y análisis de volatilidad.",
        "Controla tu cartera y aprende cómo equilibrarla según tu perfil de riesgo, sin recomendaciones de fondos concretos."
    ),

    # Mi Futuro
    (
        "No te limites a proyecciones simples. Mi Futuro calcula tu patrimonio neto nominal y real (ajustado por inflación) integrando tu LTIP empresarial y tu pensión pública estimada.",
        "Planifica tu jubilación y tu salud financiera a largo plazo, de manera independiente y educativa."
    ),
    (
        "Dos modos: Ciclo de Vida completo (acumulación + jubilación + longevidad) y Simulaciones personalizadas con sliders interactivos. LTIP, Pensión pública e IRPF integrados.",
        "Planifica tu jubilación y tu salud financiera a largo plazo, de manera independiente y educativa."
    ),

    # Mi Asesor / Educación
    (
        "Mi Asesor no es un chatbot genérico. Es una herramienta de análisis avanzado que procesa tus posiciones reales, IRPF y LTIP para ofrecerte modelos teóricos y educación financiera basada en tus propios datos.",
        "Educación financiera práctica para que tomes decisiones con autonomía, lejos de bancos y comisiones innecesarias."
    ),
    (
        "Mi Asesor analiza todas tus posiciones, rentabilidades y perfil para ofrecerte modelos de datos personalizados. Cada respuesta es un análisis técnico, no una recomendación. Powered by Gemini.",
        "Educación financiera práctica para que tomes decisiones con autonomía, lejos de bancos y comisiones innecesarias."
    ),
    (
        "Powered by Gemini. Conoce cada posición de tu cartera, tu objetivo de jubilación y tu perfil de riesgo. Está disponible en todas las pantallas como botón flotante — sin cita previa.",
        "Educación financiera práctica para que tomes decisiones con autonomía, lejos de bancos y comisiones innecesarias."
    ),
    
    # Feature mosaic specific
    # AI Advisor extra
    (
        "Análisis en streaming con modelo IA que procesa tus posiciones y perfil. Provee educación financiera y análisis de datos disponible en todas las pantallas vía FAB.",
        "Educación financiera práctica para que tomes decisiones con autonomía, lejos de bancos y comisiones innecesarias."
    ),

    # Confianza y transparencia (Testimonials intro, Stats intro)
    (
        "Inversores que ya<br /><span class=\"gradient-text\">han tomado el control.</span>",
        "Confianza y<br /><span class=\"gradient-text\">transparencia total.</span>"
    ),
    (
        "Lo que dicen<br><span class=\"accent\">quienes ya lo usan.</span>",
        "Confianza y<br><span class=\"accent\">transparencia.</span>"
    ),
    (
        "Desde el seguimiento diario de rentas pasivas hasta la planificación de tu jubilación con LTIP y pensión — Patrimonio 360 lo cubre todo.",
        "Independiente, educativa y transparente: todo lo que necesitas para entender tu dinero y planificar tu futuro."
    ),
    (
        "Desde el seguimiento diario de rentas pasivas hasta la planificación de tu jubilación con LTIP y pensión — Kannut lo cubre todo.",
        "Independiente, educativa y transparente: todo lo que necesitas para entender tu dinero y planificar tu futuro."
    ),
    
    # "Tu única relación con la app es como usuario: nada de productos, nada de intermediarios."
    (
        "100% de los datos encriptados con seguridad bancaria.",
        "Tu única relación con la app es como usuario: nada de productos, nada de intermediarios."
    ),
    # Add an explicit Testimonial text replacement with the empowerment verbatim
    (
        "Lo que empezó como curiosidad por el asesor IA se ha convertido en mi herramienta diaria. Gemini me ayuda a ver baches en mi cartera que yo ignoraba.",
        "Empoderamos a los usuarios para que tomen decisiones informadas, sin vender ni recomendar productos. Kannut ha sido clave para entender mis finanzas."
    ),
    (
        "El anillo de progreso hacia la jubilación me cambió la perspectiva. Ver que estoy al 68% de mi objetivo en tiempo real me motiva a seguir ahorrando cada mes.",
        "Empoderamos a los usuarios para que tomen decisiones informadas, sin vender ni recomendar productos."
    ),

    # CTAs
    (
        "Construye tu libertad<br />financiera hoy mismo.",
        "Empieza a educarte y<br />planificar tu futuro hoy."
    ),
    (
        "Accede a Patrimonio 360 y empieza a gestionar tu futuro con la herramienta más potente para el inversor serio.",
        "Aprende, organiza y decide: la app financiera que pone el control en tus manos."
    ),
    (
        "Accede a Kannut y empieza a gestionar tu futuro con la herramienta más potente para el inversor serio.",
        "Aprende, organiza y decide: la app financiera que pone el control en tus manos."
    ),
    (
        "Comienza tu viaje a la<br><span class=\"accent\">independencia financiera.</span>",
        "Conviértete en el experto<br><span class=\"accent\">de tu propio dinero.</span>"
    ),
]

for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        for old, new in replacements:
            content = content.replace(old, new)
            # Try replacing \n format if needed
            content = content.replace(old.replace('<br>', '<br>\n').replace('<br />', '<br />\n'), new)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Applied replacements in {fpath}")
    except Exception as e:
        print(f"Error on {fpath}: {e}")
