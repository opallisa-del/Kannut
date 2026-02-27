import os

html1 = 'c:/Users/oscar/.gemini/antigravity/workspaces/galactic-gemini/index.html'
html2 = 'c:/Users/oscar/.gemini/antigravity/workspaces/galactic-gemini/index2.html'

svg_chat = '<svg class="ds-svg" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>'
svg_zap = '<svg class="ds-svg" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>'
svg_lock = '<svg class="ds-svg" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>'
svg_brain = '<svg class="ds-svg" viewBox="0 0 24 24"><path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.54 4 4 0 1 0 7.967 0 4 4 0 1 0 7.967 0 4 4 0 0 0 .556-6.54 4 4 0 0 0-2.526-5.77A3 3 0 1 0 12 5"></path></svg>'
svg_cash = '<svg class="ds-svg" viewBox="0 0 24 24"><rect x="2" y="6" width="20" height="12" rx="2" ry="2"></rect><circle cx="12" cy="12" r="2"></circle><path d="M6 12h.01M18 12h.01"></path></svg>'

def replace_emojis(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('🎉', '')
    content = content.replace('💬', svg_chat)
    content = content.replace('⚡', svg_zap)
    content = content.replace('🔒', svg_lock)
    content = content.replace('💵', svg_cash)
    content = content.replace('🧠', svg_brain)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_emojis(html1)
replace_emojis(html2)
print("Emojis removed")
