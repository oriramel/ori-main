#!/usr/bin/env python3
"""
NBA Playoff Data Scraper

This script scrapes team name data from the Basketball Reference website
for the 2019 NBA playoffs.
"""

import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    """
    Fetch and parse a webpage using requests and BeautifulSoup.
    
    Args:
        url (str): The URL to fetch
        
    Returns:
        BeautifulSoup: Parsed HTML content
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
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
    soup = fetch_webpage(url)
    
    if soup:
        team_names = extract_team_names(soup)
        
        if team_names:
            print("\nTeam names found in the 2019 NBA Playoffs:")
            for i, team in enumerate(team_names, 1):
                print(f"{i}. {team}")
            print(f"\nTotal teams found: {len(team_names)}")
        else:
            print("No team names found")

if __name__ == "__main__":
    main()