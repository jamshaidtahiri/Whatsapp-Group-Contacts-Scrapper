WhatsApp Web Scraper
====================

Overview
--------
This script allows you to extract the contacts from a specific WhatsApp group. It uses Selenium to automate WhatsApp Web and requires the Chrome WebDriver executable compatible with your Chrome browser version.

Prerequisites
--------------
1. Make sure you are logged into your WhatsApp Web account before running the script.
2. Close all other Chrome browser tabs to prevent any interference during the scraping process.

Chrome WebDriver
-----------------
1. Download the Chrome WebDriver compatible with your Chrome browser version from "https://googlechromelabs.github.io/chrome-for-testing/".
2. During the execution of the scraper, you will be prompted to select the downloaded Chrome WebDriver executable.

Execution
---------
1. Run "scraper.exe" to execute the script.
2. A file dialog will appear, asking you to select the Chrome WebDriver executable. Browse and select the downloaded WebDriver.
3. A dialog box will ask you to enter the name of the WhatsApp group from which you want to extract contacts.
4. After entering the group name, the script will launch a Chrome browser and open WhatsApp Web.
5. Scan the QR code and wait for the WhatsApp Web session to load.
6. Once the session is loaded, the script will search for the specified group and extract its contacts.
7. The script will create a CSV file named "Group_Contact_list.csv" containing the extracted contacts.
8. The CSV file will be saved in the same directory where the script is located.

Note
----
- If you face any issues during the execution, make sure you have provided the correct Chrome WebDriver executable and that your Chrome browser is up to date.
- Ensure you have an active internet connection during the execution of the script.
- For any problems or inquiries, feel free to contact the developer at [Your Email Address].

Happy WhatsApp Web Scraping!
