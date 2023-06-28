from datetime import datetime
from tabula import read_pdf


def test_func(x):
    return 1 + x
    

def get_previous_month_and_year():
    current_month = datetime.now().month
    previous_month = current_month - 1
    previous_month_name = datetime(1900, previous_month, 1).strftime("%b")
    current_year = datetime.now().year
    current_year_end_digits = str(current_year)[2:]
    return previous_month_name, current_year_end_digits


def extract_most_recent_raleigh_water_data(month_name, year_end_digits):
    url = f"https://cityofraleigh0drupal.blob.core.usgovcloudapi.net/drupal-prod/COR25/FinishedWaterQualityReport{month_name}{year_end_digits}.pdf"
    tables = read_pdf(url, pages="all")
    # figure out how to get most recent
    monthly_measurements = [entry for entry in tables[1][month_name]]
    categories = [entry for entry in tables[1]["Parameter"]]
    monthly_info = zip(categories, monthly_measurements)
    return list(monthly_info)