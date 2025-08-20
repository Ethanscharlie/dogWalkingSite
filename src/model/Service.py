from datetime import datetime, timedelta

DATE_COVERT_STRING = "%Y-%m-%d"

class Service:
    def __init__(self, start_date_string: str, end_date_string: str) -> None:
        self.start_date = self.__string_to_datetime(start_date_string)
        self.end_date = self.__string_to_datetime(end_date_string)

    @staticmethod
    def get_all_service_records():
        with open("src/model/booked_dates.txt", "r") as f:
            text = f.read()
            start_and_end_date_strings = [
                tuple(row.split('|'))
                for row in text.split('\n')
                if row # Whitespace protection
            ]

        dates = [
            Service(start_date_string, end_date_string)
            for start_date_string, end_date_string in start_and_end_date_strings
        ]

        return dates

    def get_all_booked_dates(self) -> list[datetime]:
        date_list = []
        current_date = self.start_date
        while current_date <= self.end_date:
            date_list.append(current_date)
            current_date += timedelta(days=1)
        
        return date_list

    def __string_to_datetime(self, string: str) -> datetime:
        return datetime.strptime(string, DATE_COVERT_STRING)
