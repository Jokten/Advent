import re
import numpy as np
import requests
from bs4 import BeautifulSoup

def data_loader(year,day,two_parts=False):
    with open(f'{year}\\{day}\input.txt', 'r') as file:
        data = file.read()
    if two_parts:
        return [i.splitlines() for i in data.split('\n\n')]
    else:
        return data.splitlines()

def parse_numbers(data):
    return [[int(i) for i in re.findall(r'-?\d+', row)] for row in data]

def transpose(data):
    return list(map(list, zip(*data)))

def np_array(data, num=False):
    if num:data = [list(map(int, row)) for row in data]
    else: data = [list(row) for row in data]
    return np.array(data)



# Set your Advent of Code session cookie here
SESSION_COOKIE = "53616c7465645f5f53a6c2fe1167bd82d530759d6262cdd2812894a5ab13a3b9ef92411f7dc3fceb48283634d8339f5bafff0a1cee3e3806e51fd8dcf9f38828"
YEAR = 2024  # Change to the desired year
DAY = 10  # Change to the desired day

# Base URL for Advent of Code
BASE_URL = "https://adventofcode.com"

def get_data(year, day):
    # Build the URL for the specific day
    url = f"{BASE_URL}/{year}/day/{day}"
    print(SESSION_COOKIE)
    # Create session headers
    headers = {
        "Cookie": f"session={SESSION_COOKIE}",
        "User-Agent": "Mozilla/5.0 (compatible; AdventOfCodeScraper/1.0)"
    }
    
    # Fetch the page
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the problem description
    problem_description = soup.find("article", {"class": "day-desc"}).text
    
    # Extract input data (if available)
    input_url = f"{url}/input"
    input_response = requests.get(input_url, headers=headers)
    if input_response.status_code == 200:
        input_data = input_response.text
    else:
        input_data = None
    
    return problem_description, input_data

if __name__ == "__main__":
    try:
        description, input_data = get_aoc_data(YEAR, DAY)
        print(f"--- Day {DAY} ---\n")
        print(description)
        
        if input_data:
            print("\n--- Input Data ---\n")
            print(input_data[:500] + ("..." if len(input_data) > 500 else ""))  # Show first 500 chars
    except Exception as e:
        print(f"Error: {e}")
