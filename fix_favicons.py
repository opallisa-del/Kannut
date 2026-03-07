import os
from PIL import Image

def generate_favicons():
    workspace_dir = r"c:\Users\oscar\.gemini\antigravity\workspaces\galactic-gemini"
    logo_path = os.path.join(workspace_dir, "logo.png")
    
    if not os.path.exists(logo_path):
        print(f"Error: Could not find {logo_path}")
        return
        
    try:
        img = Image.open(logo_path)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
            
        print(f"Source image loaded. Size: {img.size}, Mode: {img.mode}")
        
        # 48x48 PNG
        img_48 = img.resize((48, 48), Image.Resampling.LANCZOS)
        img_48.save(os.path.join(workspace_dir, "favicon-48x48.png"))
        print("Generated favicon-48x48.png")
        
        # 192x192 PNG
        img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
        img_192.save(os.path.join(workspace_dir, "favicon-192x192.png"))
        print("Generated favicon-192x192.png")
        
        # ICO file with multiple sizes
        icon_sizes = [(16, 16), (32, 32), (48, 48)]
        img.save(os.path.join(workspace_dir, "favicon.ico"), format='ICO', sizes=icon_sizes)
        print("Generated favicon.ico (16x16, 32x32, 48x48)")
        
        print("All Google-compliant favicons generated successfully!")
        
    except Exception as e:
        print(f"Error generating favicons: {e}")

if __name__ == "__main__":
    generate_favicons()
