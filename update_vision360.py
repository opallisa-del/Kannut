import re

files = ["index.html", "index2.html", "index4.html"]

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace "Mi Dashboard" with "Mi Visión 360"
    content = content.replace('Mi Dashboard', 'Mi Visión 360')

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"Updated {f}")
