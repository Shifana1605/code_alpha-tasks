import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Step 1: URL to scrape
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Extract job data
job_elements = soup.find_all('div', class_='card-content')

jobs = []
for job_element in job_elements:
    title = job_element.find('h2', class_='title').text.strip()
    company = job_element.find('h3', class_='company').text.strip()
    location = job_element.find('p', class_='location').text.strip()

    jobs.append({
        "Job Title": title,
        "Company": company,
        "Location": location
    })

# Step 3: Save data to CSV inside /data folder
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, 'job_listings.csv')
pd.DataFrame(jobs).to_csv(output_file, index=False)

print(f"Scraping complete! Data saved to {output_file}")
