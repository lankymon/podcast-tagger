from playwright.sync_api import sync_playwright
import os

PROFILE_DIR = os.path.join(os.getcwd(), "chrome-profile")

def fetch_bbc_sounds_episodes(brand_url: str) -> dict:
    with sync_playwright() as p:
        # Launch Chrome with a persistent profile
        browser = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=False,
        executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
        args=[
            "--start-maximized",
            "--disable-blink-features=AutomationControlled",
            "--enable-webgl",
            "--use-gl=desktop",
    ]
)

        page = browser.new_page()

        page.goto(brand_url, wait_until="networkidle")

        # Click the Episodes tab
        try:
            page.wait_for_selector("button:has-text('Episodes')", timeout=10000)
            page.click("button:has-text('Episodes')")
            page.wait_for_timeout(1500)
        except:
            print("Episodes tab not found")

        # Scroll to load all episodes
        for _ in range(12):
            page.mouse.wheel(0, 1500)
            page.wait_for_timeout(600)

        # Extract show title
        try:
            show_title = page.locator("h1").first.inner_text().strip()
        except:
            show_title = None

        # Extract episodes
        cards = page.locator("[data-testid='episode-card']")
        count = cards.count()

        episodes = []
        for i in range(count):
            card = cards.nth(i)
            try:
                title = card.locator("h2, h3").inner_text().strip()
                description = card.locator("p").inner_text().strip()
                date = card.locator("time").get_attribute("datetime")
                duration = card.locator("span").filter(has_text="min").first.inner_text().strip()
                image = card.locator("img").get_attribute("src")
            except:
                continue

            episodes.append({
                "number": i + 1,
                "title": title,
                "description": description,
                "date": date,
                "duration": duration,
                "image": image,
            })

        browser.close()

        return {
            "title": show_title,
            "episodes": episodes
        }