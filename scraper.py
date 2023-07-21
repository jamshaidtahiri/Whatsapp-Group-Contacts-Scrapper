import os
import csv
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to get the current username
def get_username():
    return os.getlogin()

# Function to extract the title attribute
def extract_title_attribute():
    try:
 # Get the current username
        username = get_username()
        print(username)

        # Ask the user for the Chrome driver path
##        executable_path = input("Enter the path to the Chrome WebDriver executable: ")

        # Create a Tkinter root window (it will not be visible)
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Prompt the user to select the Chrome driver executable
        executable_path = filedialog.askopenfilename(title="Select Chrome WebDriver executable", filetypes=[("Executable Files", "*.exe")])

        # Check if the user provided path is valid
        if not os.path.isfile(executable_path):
            raise FileNotFoundError(f"Invalid Chrome WebDriver executable path: {executable_path}")
        
        # Update the 'executable_path' variable with the path to the existing Chrome WebDriver executable
##        executable_path = r'C:\Users\MR MJT\Desktop\awais\chromedriver-win64\chromedriver-win64\chromedriver.exe'

        # Specify the user data directory where the Chrome profile with an active WhatsApp Web session is located
        user_data_directory = fr'C:\Users\{username}\AppData\Local\Google\Chrome\User Data'  

        # Initialize the Chrome webdriver with the existing WebDriver executable using the Service class
        options = Options()
        options.add_argument(f'--user-data-dir={user_data_directory}')
        service = Service(executable_path=executable_path)
        driver = webdriver.Chrome(service=service, options=options)

        # Open WhatsApp Web URL
        driver.get('https://web.whatsapp.com/')

        # Wait for the user to scan the QR code and open WhatsApp Web session
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pane-side')))
        time.sleep(5)  # Wait for a while to interact with the page



        search_input_element = driver.find_element(By.CSS_SELECTOR, 'div[title="Search input textbox"]')
        search_input_element.click()

        def get_search_query():
            root = tk.Tk()
            root.withdraw()  # Hide the main tkinter window
            search_query = simpledialog.askstring("WhatsApp Search", "Enter your search query:")
    # Ask the user for the search query using a dialog box 
            return search_query
        search_query = get_search_query()
        # Input text into the search input
        search_input_element.send_keys(search_query)

        time.sleep(2)
        
        first_chat = driver.find_elements(By.CSS_SELECTOR, 'span[title]')
        
        
        # Find all elements with 'span' tag and 'title' attribute
        first_chat = driver.find_elements(By.CSS_SELECTOR, 'span[title]')

        # Target string to search for at the beginning of the title
        target_starting_string = search_query

# Variable to store the element with the target title
        target_element = None

# Iterate through each 'span' element and check the title
        for chat_element in first_chat:
            title = chat_element.get_attribute("title")
            print(title)

    # Check if the title starts with the target starting string
            if title.startswith(target_starting_string):
                target_element = chat_element
                break  # Stop the loop once the target element is found

# Check if the target element was found and print additional information
        if target_element:
            print("Target element found!")
            print("Title: ", target_element.get_attribute("title"))
            print("Text: ", target_element.text)
        else:
            print("Target element not found.")

        target_element.click()

        time.sleep(5)
        # Find the element containing the contact names using CSS Selector
        contact_element = driver.find_element(By.CSS_SELECTOR, '#main > header > div._2au8k > div.p357zi0d.r15c9g6i.g4oj0cdv.ovllcyds.l0vqccxk.pm5hny62 > span')

        # Extract and print the contact names
        contact_names = contact_element.get_attribute('title')
        print(contact_names)

        
        # Find the span element using the CSS selector
##        span_element = driver.find_element(By.CSS_SELECTOR, "#main > header > div._2au8k > div.p357zi0d.r15c9g6i.g4oj0cdv.ovllcyds.l0vqccxk.pm5hny62 > span")

##        if span_element:
            # Extract the 'title' attribute
##            title_attribute = span_element.get_attribute('title')
##            print(title_attribute)

            # Split the comma-separated data into a list
##            data_list = title_attribute.split(', ')
        data_list = contact_names.split(', ')

            # Save the extracted title to a CSV file
        with open('Group_Contact_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title'])
            for item in data_list:
                writer.writerow([item])
                
        print('Group Contact list saved to "Group_Contact_list.csv".')

##        else:
##            print("Span element not found.")

        # Close the browser (Optional: Comment this line if you want to keep the WhatsApp Web session active)
        driver.quit()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    extract_title_attribute()
