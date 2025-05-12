#!/usr/bin/env python3
"""
NBA Playoff Data Scraper

This script fetches and outputs the HTML content of the Basketball Reference website
for the 2019 NBA playoffs.
"""

import urllib.request
import urllib.error

# Import for future use when parsing HTML
# from bs4 import BeautifulSoup

def fetch_webpage(url):
    """
    Fetch a webpage using urllib.
    
    Args:
        url (str): The URL to fetch
        
    Returns:
        str: HTML content of the page
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f"Error fetching webpage: {e}")
        return None

def extract_team_names(soup):
    """
    Extract team names from the playoff table.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        
    Returns:
        list: List of team names
    """
    if not soup:
        return []
    
    # Find the table with id "all_all_playoffs"
    table = soup.find('table', {'id': 'all_all_playoffs'})
    
    if not table:
        print("Table with id 'all_all_playoffs' not found")
        return []
    
    # Extract team name links
    team_links = table.find_all('a', href=True)
    team_names = [link.text for link in team_links if '/teams/' in link.get('href', '')]
    
    # Remove duplicates while preserving order
    unique_teams = []
    for team in team_names:
        if team not in unique_teams:
            unique_teams.append(team)
    
    return unique_teams

def main():
    """Main function to execute the scraping process."""
    # Define the URL
    url = "https://www.basketball-reference.com/playoffs/NBA_2019.html"
    
    print(f"Fetching data from {url}...")
    html_content = fetch_webpage(url)
    
    if html_content:
        print("\nHTML Content of the page:")
        print(html_content)
    else:
        print("Failed to fetch HTML content")
    
    # The team name extraction functionality is preserved in the extract_team_names function
    # but not used at this time

if __name__ == "__main__":
    main()