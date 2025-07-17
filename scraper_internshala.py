# Step-1 : Import the Required Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import os

# Step-2 : Setup Logging
logging.basicConfig(filename="logs/internshala_scraper.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Step-3 : Define Function to Scrape a Single Page
def scrape_page(page_number):
    url = f"https://internshala.com/jobs/page-{page_number}/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        logging.error(f"Exception during request to page {page_number}: {e}")
        return []

    if response.status_code != 200:
        logging.error(f"Failed to fetch page {page_number}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    job_cards = soup.find_all("div", class_="individual_internship")
    job_list = []

    for job in job_cards:
        try:
            # Title
            title = job.find('a', class_="job-title-href").get_text(strip=True)

            # Company
            company = job.find('p', class_="company-name").get_text(strip=True)

            # Location
            location_tag = job.find('p', class_="locations")
            location = location_tag.get_text(strip=True) if location_tag else "Not mentioned"

            # Salary
            salary_div = job.find("div", class_="row-1-item")
            salary = salary_div.get_text(strip=True) if salary_div else "Not specified"

            # Experience (searching for briefcase icon)
            experience = "Not mentioned"
            for item in job.find_all("div", class_="row-1-item"):
                icon = item.find("i")
                if icon and "ic-16-briefcase" in icon.get("class", []):
                    experience = item.get_text(strip=True)
                    break

            # Posted Date
            posted = job.find("div", class_="status-inactive").get_text(strip=True)

            # Apply Link
            relative_link = job.get("data-href")
            apply_link = f"https://internshala.com{relative_link}" if relative_link else "N/A"

            # Add to job list
            job_list.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Salary": salary,
                "Experience": experience,
                "Posted": posted,
                "Apply Link": apply_link
            })

        except Exception as e:
            logging.warning(f"Skipping job due to error: {e}")
            continue

    return job_list

# Step-4 : Ask User for Page Range
start_page = int(input("Enter start page number (e.g., 1): "))
end_page = int(input("Enter end page number (e.g., 5): "))

all_jobs = []

# Step-5 : Loop through Pages and Collect Jobs
for page in range(start_page, end_page + 1):
    logging.info(f"Scraping page {page}")
    jobs = scrape_page(page)
    all_jobs.extend(jobs)

# Step-6 : Convert to DataFrame and Export
df = pd.DataFrame(all_jobs)

# Ensure 'outputs/' directory exists
os.makedirs("outputs", exist_ok=True)

output_file = f"outputs/job_data_internshala_{start_page}-{end_page}.csv"
df.to_csv(output_file, index=False)

logging.info(f"✅ Scraped {len(df)} job listings from page {start_page} to {end_page}")
print(f"\n✅ Scraped {len(df)} jobs and saved to {output_file}")
print(df.head())
