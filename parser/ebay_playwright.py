from playwright.sync_api import sync_playwright

def parse_ebay(query, limit=5):
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page.set_extra_http_headers({
            "Accept-Language": "en-US,en;q=0.9"
        })
        page.goto(f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ','+')}")
        page.wait_for_selector("li.s-card", timeout=60000)
        items = page.query_selector_all("li.s-card")
        for item in items:
            title_tag = item.query_selector("span.su-styled-text.primary.default")
            price_tag = item.query_selector(".s-card__price")
            link_tag = item.query_selector("a.s-card__link")
            if title_tag and price_tag and link_tag:
                title = title_tag.inner_text().strip()
                url = link_tag.get_attribute("href")
                # filter
                if "Shop on eBay" in title:
                    continue
                price_text = price_tag.inner_text().replace("$","").replace(",","").split()[0]
                try:
                    price = float(price_text)
                except:
                    continue
                url = link_tag.get_attribute("href")
                results.append({"name": title, "price": price, "url": url})
                if len(results) >= limit:
                    break
        browser.close()
    return results
