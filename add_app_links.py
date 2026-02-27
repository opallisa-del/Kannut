import re

files = ["index.html", "index2.html", "index3.html", "index4.html"]

badges_html = """
        <div class="hero-badges">
            <a href="#cta" class="badge-pill">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 18H12.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
                App Store — iOS
            </a>
            <a href="#cta" class="badge-pill">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="5 3 19 12 5 21 5 3" />
                </svg>
                Google Play — Android
            </a>
        </div>"""

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Update Login Nav
    content = content.replace('<a href="#" class="nav-login">Login</a>', '<a href="login.html" class="nav-login">Login</a>')
    
    # 1. Inject under <div class="hero-actions"> if not already there
    # We use regex to find the closing div of hero-actions and append badges_html
    # But ONLY if hero-badges is not already in the file (e.g. index3.html hero)
    
    # We know index3.html already has it in the hero. So let's check.
    if '<div class="hero-badges">' not in content:
        # Match hero-actions block and append
        # This regex matches the hero-actions div and its children up to its closing </div>
        # A simpler way is to just inject after <a href="#section-dashboard" class="btn-hero-secondary">Ver la app ↓</a></div>
        # Or we can do a naive replace:
        content = re.sub(
            r'(<div class="hero-actions">[\s\S]*?</div>)',
            r'\1' + badges_html,
            content,
            count=1 # Only first match (hero)
        )
        
    # 2. Inject under <div class="cta-actions" ...>
    # Match something like <div class="cta-actions reveal reveal-d3">
    # And inject underneath its closing </div>
    
    if '<div class="cta-actions' in content:
        # Find the CTA actions div closing tag.
        # It usually contains 2 links.
        # We can just inject badges_html right before <p class="cta-disclaimer
        content = content.replace('<p class="cta-disclaimer', badges_html + '\n                <p class="cta-disclaimer')

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"Updated {f}")
