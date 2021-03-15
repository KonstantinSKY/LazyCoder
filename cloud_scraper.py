import cloudscraper

scraper = cloudscraper.create_scraper()
# Or: scraper = cloudscraper.CloudScraper()
print(scraper.get("https://leetcode.com/problems/decode-xored-array/").text)
