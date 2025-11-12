from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# --- Config ---
url = "https://www.canlii.org/"
spacing = 100       # distance between grid lines (px)
color = "red"        # line + text color
thickness = 1        # line width
font_size = 10       # px
output_path = "grid_with_coords.png"

# --- Launch browser ---
options = Options()
#options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--window-size=1920,1080')
options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
# options.add_argument("--headless=new")  # uncomment for headless
driver = webdriver.Chrome(options=options)

try:
    driver.get(url)
    time.sleep(10)  # wait for page to load

    # --- Inject coordinate grid overlay ---
    js = f"""
    (function() {{
        const existing = document.getElementById('selenium_grid_overlay');
        if (existing) existing.remove();

        const grid = document.createElement('div');
        grid.id = 'selenium_grid_overlay';
        grid.style.position = 'fixed';
        grid.style.top = 0;
        grid.style.left = 0;
        grid.style.width = '100%';
        grid.style.height = '100%';
        grid.style.pointerEvents = 'none';
        grid.style.zIndex = 999999;

        // Create a canvas to draw the grid and coordinates
        const canvas = document.createElement('canvas');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        grid.appendChild(canvas);

        const ctx = canvas.getContext('2d');
        ctx.strokeStyle = '{color}';
        ctx.lineWidth = {thickness};
        ctx.font = '{font_size}px monospace';
        ctx.fillStyle = '{color}';

        // Draw vertical lines
        for (let x = 0; x <= window.innerWidth; x += {spacing}) {{
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, window.innerHeight);
            ctx.stroke();
        }}

        // Draw horizontal lines
        for (let y = 0; y <= window.innerHeight; y += {spacing}) {{
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(window.innerWidth, y);
            ctx.stroke();
        }}

        // Draw coordinate labels at intersections
        for (let x = 0; x <= window.innerWidth; x += {spacing}) {{
            for (let y = 0; y <= window.innerHeight; y += {spacing}) {{
                const text = `(${{x}}, ${{y}})`;
                ctx.fillText(text, x + 2, y + {font_size} + 2);
            }}
        }}

        document.body.appendChild(grid);
    }})();
    """
    driver.execute_script(js)
    time.sleep(0.3)

    # --- Screenshot ---
    driver.save_screenshot(output_path)
    print("✅ Grid with coordinates saved as:", output_path)

finally:
    # Cleanup
    try:
        driver.execute_script("var g=document.getElementById('selenium_grid_overlay'); if(g) g.remove();")
    except Exception:
        pass
    driver.quit()
