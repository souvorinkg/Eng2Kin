import json
from playwright.sync_api import sync_playwright

def scrape_profile(url: str, output_file: str) -> None:
    """
    Scrape a X.com profile details e.g.: https://x.com/Scrapfly_dev
    """
    _xhr_calls = []

    def intercept_response(response):
        """capture all background requests and save them"""
        if response.request.resource_type == "xhr":
            _xhr_calls.append(response)
        return response

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        page.on("response", intercept_response)
        page.goto(url)
        page.wait_for_selector("[data-testid='primaryColumn']")

        profile_calls = [f for f in _xhr_calls if "UserBy" in f.url]
        for xhr in profile_calls:
            data = xhr.json()
            with open(output_file, 'w') as json_file:
                json.dump(data['data']['user']['result'], json_file, indent=4)

if __name__ == "__main__":
    output_file = "profile_data.json"
    scrape_profile("https://twitter.com/Scrapfly_dev", output_file)