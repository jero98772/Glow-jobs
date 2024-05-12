import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from subprocess import run
FILENAME="data/jobs.txt"

def run_crawler():
    run("python crawler.py",shell=True)

def search_job_posts(url, job_title):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_posts = soup.find_all('div', class_='job-post')
    for job_post in job_posts:
        title = job_post.find('h2', class_='job-title').text.strip()
        company = job_post.find('span', class_='company-name').text.strip()
        location = job_post.find('span', class_='location').text.strip()
        job_url = urljoin(url, job_post.find('a')['href'])
    return [title,company,location,job_url]

def write_txt(name,content,mode='a'):
	"""
	write_txt(name,content) , write in txt file something  
	"""
	content =str(content)
	with open(name, mode) as file:
		file.write(content)
		file.close()



def get_jobs(soup, url):
    """
    Extract information of job positions, companies, and salaries from the HTML soup.
    """
    job_cards = soup.find_all("article", class_="mg_job_card_mobile_magneto-ui-card-mobile-jobs_18tcb")
    job_data = []

    for card in job_cards:
        # Extract job position
        job_position_element = card.find("h2", class_="mg_job_card_mobile_magneto-ui-card-mobile-jobs--row2_position_18tcb")
        job_position = job_position_element.text.strip() if job_position_element else None

        # Extract company name
        company_element = card.find("h3")
        company = company_element.text.strip() if company_element else None

        # Extract salary
        salary_element = card.find("p", string=lambda text: "$" in text)
        salary = salary_element.text.strip() if salary_element else None

        # Append job data to the list
        job_data.append({
            "job_position": job_position,
            "company": company,
            "salary": salary
        })

    return job_data
def get_jobs(soup,url):
    """
    change function for extract information of works
    """
    links = soup.find_all('a', href=True)
    return [urljoin(url, link['href']) for link in links]

def get_links(soup,url):
    """
    this function analize the webpage, searching inside the html code for <a> tags and get the argument of href and return a list with that, all links
    """
    links = soup.find_all('a', href=True)
    return [urljoin(url, link['href']) for link in links]
def scrapper(url):
    """
    this function get the webpage and apply 2 functions get_links(),get_jobs()
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_information=0#get_jobs(soup,url)
    links = get_links(soup,url)
    return links,job_information
def crawl(url, depth=6):
    visited = set()
    queue = [(url, 0)]
    while queue:
        current_url, current_depth = queue.pop(0)
        
        if current_url in visited or current_depth >= depth:
            continue
        
        visited.add(current_url)
        print(f'Crawling {current_url} at depth {current_depth}')
        links,job_information = scrapper(current_url)
        for link in links:
            queue.append((link, current_depth + 1))
            write_txt(FILENAME,link+"\n")          


"""
pip install BeautifulSoup4
"""
