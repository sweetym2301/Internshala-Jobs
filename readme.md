# 💼 Internshala Job Trends Dashboard

This project analyzes and visualizes **job market trends on Internshala**, focusing on full-time roles. It scrapes live data from Internshala, processes it with Python, and presents it through an interactive Power BI dashboard.

It demonstrates:
- 🕸️ **Web scraping** using BeautifulSoup and `requests`
- 🧹 **Data cleaning** and structuring using `pandas`
- 📈 **Interactive dashboard** creation with Power BI
- 🔍 Filters by **Title**, **Company**, **Location**, and **Experience**
- 🔗 Extracted **Apply Links** for direct access to job pages

---

## ✅ Project Structure

```
JOB_TRENDS_SCRAPER/
├── data  
├── logs/
│   └── internshala_scraper.log        # Log file  
├── outputs/
│   ├── job_data_internshala_1-150.csv     # Extracted job data
│   └── dashboard.pbix                   # Power BI dashboard
├── proj2_env/                           # Virtual environment (not pushed to GitHub)
├── .gitignore                           # Ignored files/folders
├── read.md                            # Project documentation
├── requirements.txt                      # Python dependencies
├── scraper_internshala.py                 # Python Script file for data exporting                     
                             
```
---
## ⚙️ Tech Stack
- Python (Web scraping & data export)

  - requests, BeautifulSoup, pandas

- Power BI (Dashboard & visualization)

- Logging (Using Python's logging module)
---

## 🚀 How to Run This Project
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/sweetym2301/Internshala-Jobs.git
cd Internshala-Jobs
```

2️⃣ **Create and Activate Virtual Environment**
```bash
# Create
python -m venv proj2_env

# Activate (Command Prompt)
proj2_env\Scripts\activate

# OR Activate (PowerShell)
.\proj2_env\Scripts\Activate

```

3️⃣ **Install Requirements**
```bash
pip install -r requirements.txt
```
4️⃣ **Run the Scraper**
```bash
python scraper_internshala.py
```
---
You'll be prompted to enter start and end page numbers. The script will scrape and save data into /outputs/job_data_internshala_<start>-<end>.csv.

---
## 📈 Dashboard
After extracting the data:

 Open the dashboard.pbix file in Power BI Desktop.

 Refresh the dataset to see the latest scraped job data.

Analyze job trends, top companies, Exp vs Salary, and more!

---
## 👩‍💻 Author

**Sweety**

---

## 📜 License

This project is for learning and demonstration purposes.  
Feel free to fork & extend it!

---

✅ **Happy analyzing!**


