import os
import glob
from PIL import Image

temp_media_dir = r"c:\Users\oscar\.gemini\antigravity\brain\542ea9da-9db1-40fb-a70e-c8994666ff36\.tempmediaStorage"
list_of_files = glob.glob(f"{temp_media_dir}\\*.png")
if not list_of_files:
    print("No PNG files found!")
    exit(1)

latest_file = max(list_of_files, key=os.path.getctime)
print(f"Using image: {latest_file}")

target_dir = r"c:\Users\oscar\.gemini\antigravity\workspaces\galactic-gemini"

try:
    img = Image.open(latest_file)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
        
    img_apple = img.resize((180, 180), Image.Resampling.LANCZOS)
    apple_bg = Image.new('RGB', (180, 180), (255, 255, 255))
    apple_bg.paste(img_apple, mask=img_apple.split()[3])
    apple_bg.save(os.path.join(target_dir, "apple-touch-icon.png"))
    
    img_fav = img.resize((64, 64), Image.Resampling.LANCZOS)
    img_fav.save(os.path.join(target_dir, "favicon.png"))
    
    img_fav.save(os.path.join(target_dir, "favicon.ico"), format='ICO', sizes=[(64,64)])
    
    og_bg = Image.new('RGB', (1200, 630), (139, 92, 246)) # a nice purple matching the logo
    img_og = img.resize((400, 400), Image.Resampling.LANCZOS)
    
    bg_w, bg_h = og_bg.size
    img_w, img_h = img_og.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    
    og_bg.paste(img_og, offset, img_og)
    og_bg.save(os.path.join(target_dir, "og-image.png"))
    
    print("Images generated successfully!")
    
except Exception as e:
    print(f"Error processing image: {e}")
    exit(1)
