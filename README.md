
# HTML Email Extractor

## The Lazy Student's Solution to Email Invitations
I am in charge of organizing a Microsoft Teams call between university students and a guest speaker. My colleague emailed me a list of email addresses in a table format. It would be more convenient to send out invitations if the emails were in an Excel file. This way, I could simply copy and paste them into the guest section when I'm sending out the invites. To achieve this, I decided to save the email my colleague sent me as an HTML file. I then wrote a simple Python program that extracts the emails from the table and stores them in an Excel file. This will enable me to easily copy and paste them into the guest section.


## Here's how you can test its workings

1. **Clone the repository and Open it in your IDE**: VS code, IntelliJ or any other of your favorite choice

2. **Install Dependencies**: Install the following library by running this command in the terminal
   pip install beautifulsoup4 openpyxl

3. **To run the program** : Type in the following command in your terminal
   python3 first_years_emails.py 

## And there you have it. The Excel file should now be in your folder with the name: email_addresses.xlsx

