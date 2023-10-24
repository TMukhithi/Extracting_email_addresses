from bs4 import BeautifulSoup
import openpyxl

# Load the HTML file
with open('First Year engineering email addresses - tendani.mukhithi@gmail.com - Gmail.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all email addresses in <span> tags
email_addresses = []
tbody_tags = soup.find_all('tbody')
for tbody in tbody_tags:
    tr_tags = tbody.find_all('tr')
    for tr in tr_tags:
        span_tags = tr.find_all('span', style="font-size:12.0pt;color:black")
        for span in span_tags:
            anchor_tags = span.find_all('a')
            for anchor in anchor_tags:
                email = anchor.get_text()
                if '@' in email:  # Simple check to filter out potential email addresses
                    email_addresses.append(email)

# Create an Excel workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Write the email addresses to the Excel file
for i, email in enumerate(email_addresses, start=1):
    worksheet.cell(row=i, column=1, value=email)

# Save the Excel file
workbook.save('email_addresses.xlsx')
