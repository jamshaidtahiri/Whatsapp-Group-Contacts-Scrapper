import os
import csv
import time
import tkinter as tk
from tkinter import filedialog, simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Function to get the current username
def get_username():
    return os.getlogin()

# Function to get the search query from the user using a dialog box
def get_search_query():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    search_query = simpledialog.askstring("WhatsApp Search", "Enter your search query:")
    return search_query

# Function to extract the title attribute
def extract_title_attribute():
    try:
        # Get the current username
        username = get_username()

        # Prompt the user to select the Chrome driver executable
        executable_path = filedialog.askopenfilename(title="Select Chrome WebDriver executable", filetypes=[("Executable Files", "*.exe")])

        # Check if the user provided path is valid
        if not os.path.isfile(executable_path):
            raise FileNotFoundError(f"Invalid Chrome WebDriver executable path: {executable_path}")

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

        # Get the search query from the user using a dialog box
        search_query = get_search_query()

        # Find the search input element and input the search query
        search_input_element = driver.find_element(By.CSS_SELECTOR, 'div[title="Search input textbox"]')
        search_input_element.click()
        search_input_element.send_keys(search_query)
        time.sleep(2)

        # Find all elements with 'span' tag and 'title' attribute
        chat_elements = driver.find_elements(By.XPATH, '//div[@role="row"]//div[@data-testid="cell-frame-container"]//div[@class="y_sn4"]//span[@title]')

        # Target string to search for at the beginning of the title
        target_starting_string = search_query.lower()

        # Variable to store the elements with the target title
        target_elements = []

        # Iterate through each 'span' element and check the title
        for chat_element in chat_elements:
            title = chat_element.get_attribute("title").lower()
            if target_starting_string in title:
                target_elements.append(chat_element)

        # Check if the target elements were found and print additional information

        if target_elements:
            print(f"{len(target_elements)} Target elements found!")

            # Loop through all the target elements and click on them one by one
            for index, target_element in enumerate(target_elements):
                print("Title: ", target_element.get_attribute("title"))
                print("Text: ", target_element.text)

                target_element.click()
                time.sleep(5)  # Wait for the contact page to load
                
                try:
                # Find the element containing the contact names using CSS Selector
                    contact_element = driver.find_element(By.CSS_SELECTOR, '#main > header > div._2au8k > div.p357zi0d.r15c9g6i.g4oj0cdv.ovllcyds.l0vqccxk.pm5hny62 > span')

                # Extract and print the contact names
                    contact_names = contact_element.get_attribute('title')
                    print("Contact Names:", contact_names)
                    print("=========================================")

        
        # ... (rest of the code remains unchanged) ...

        # Split the comma-separated data into a list
                    contact_names = contact_names.split(', ')

                    filename = f"Contact_List_{index + 1}_{target_element.get_attribute('title')}.csv"

        # Save the extracted title to a CSV file
                    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(['Title'])
                        for item in contact_names:
                            writer.writerow([item])

                    print(f'Contact list saved to "{filename}"')
                    print("=========================================")
                except NoSuchElementException:
                    print("Contact element not found. Skipping this target element.")
                    print("=========================================")
                    continue  # Skip this iteration and continue with the next target element


        else:
            print("No target elements found.")

        # Close the browser (Optional: Comment this line if you want to keep the WhatsApp Web session active)
        driver.quit()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    extract_title_attribute()
