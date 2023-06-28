from utils import get_previous_month_and_year, extract_most_recent_raleigh_water_data


def format_extracted_data(list):
    pass


def main():
    previous_month_name, current_year_end_digits = get_previous_month_and_year()
    data = extract_most_recent_raleigh_water_data(
        previous_month_name, current_year_end_digits
    )
    print(data)


if __name__ == "__main__":
    main()
