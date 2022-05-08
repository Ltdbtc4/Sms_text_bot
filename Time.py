from datetime import timedelta, datetime


class DateTime:
    def __init__(self):
        self.__placeholderToday = datetime.today()
        self.Today = self.__placeholderToday.strftime("%B %d, %Y")
        self.__placeholderTime = datetime.today()
        self.Time = self.__placeholderTime.strftime("%H:%M")

    @staticmethod
    def ChangeDate(degree_to_move, time_format):
        next_date = datetime.today() + timedelta(days=degree_to_move)
        if time_format == "google":
            return next_date.strftime("%Y-%m-%d")
        elif time_format == "normal":
            return next_date.strftime("%B %d, %Y")

    @staticmethod
    def return_current_time(time_format):
        current_time = datetime.now()
        if time_format == "validation":
            return current_time.strftime("%H:%M:%S")
        elif time_format == "normal":
            return current_time.strftime("%H:%M")

    @staticmethod
    def return_current_date(time_format):
        if time_format == "google":
            return datetime.today().strftime("%Y-%m-%d")
        elif time_format == "normal":
            current_date = datetime.today()
            return current_date.strftime("%B %d, %Y")
