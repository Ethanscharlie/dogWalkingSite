from ..model.Service import Service
from datetime import datetime, timedelta

DATE_COVERT_STRING = "%b %d %A"
PERIOD_DAYS = 30

class Day:
    def __init__(self, date: datetime, services: list[Service]) -> None:
        self.date = date
        self.services = services

    @staticmethod
    def get_days_for_period():
        all_services = Service.get_all_service_records()
        return [
            Day(
                datetime.today() + timedelta(days=i),
                Day.get_services_that_match_day(all_services, datetime.today() + timedelta(days=i))
            )
            for i in range(PERIOD_DAYS)
        ]

    @staticmethod
    def get_services_that_match_day(services: list[Service], date: datetime) -> list[Service]:
        return [
            service
            for service in services
            if Day.service_matches_date(service, date)
        ]    

    @staticmethod
    def service_matches_date(service: Service, date: datetime) -> bool:
        all_booked_dates = service.get_all_booked_dates()
        for service_date in all_booked_dates:
            if service_date.date() == date.date():
                return True

        return False


def get_info_for_calendar() -> list[str]:
    days = Day.get_days_for_period()
    return [
        f"{day.date.strftime(DATE_COVERT_STRING)} {__get_booked_string(day.services)}"
        for day in days
    ]

def __get_booked_string(services: list[str]) -> str:
    if len(services) > 0: return "BOOKED"
    return ""
