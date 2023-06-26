import requests
from PyPDF2 import PdfReader
import io


def extract_data():
    response = requests.get(
        "https://cityofraleigh0drupal.blob.core.usgovcloudapi.net/drupal-prod/COR25/FinishedWaterQualityReportMay23.pdf"
    )
    with io.BytesIO(response.content) as f:
        pdf = PdfReader(f)
        contents = pdf._get_page(0).extract_text()
        print(contents)


def main():
    print(extract_data())

if __name__ == "__main__":
    main()
