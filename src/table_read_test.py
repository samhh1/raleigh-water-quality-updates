# import camelot
# tables = camelot.read_pdf(r"C:\Users\SamHayden\Downloads\FinishedWaterQualityReportMay23.pdf")
# print(tables[0])

from tabula import read_pdf


url = "https://cityofraleigh0drupal.blob.core.usgovcloudapi.net/drupal-prod/COR25/FinishedWaterQualityReportMay23.pdf"

tables = read_pdf(url, pages="all")  # substitute your file name
monthly_measurements = [entry for entry in tables[1]["May"]]

categories = [entry for entry in tables[1]["Parameter"]]

monthly_info = zip(categories, monthly_measurements)
for items in monthly_info:
    print(items)
