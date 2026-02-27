import re

# 1. Read index4.html to extract its ds-feature-grid
with open('index4.html', 'r', encoding='utf-8') as f:
    content4 = f.read()

match = re.search(r'(<div class="ds-feature-grid">[\s\S]*?</div>\s*</div>\s*</section>)', content4)
if match:
    grid_html = match.group(1)
    
    # 2. Inject into index2.html
    with open('index2.html', 'r', encoding='utf-8') as f2:
        content2 = f2.read()
        
    # Replace ds-feature-grid in index2
    content2 = re.sub(r'<div class="ds-feature-grid">[\s\S]*?</div>\s*</div>\s*</section>', grid_html, content2)
    
    with open('index2.html', 'w', encoding='utf-8') as f2:
        f2.write(content2)
    print("index2.html updated successfully.")
else:
    print("Could not find ds-feature-grid in index4.html")
