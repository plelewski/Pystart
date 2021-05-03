from datetime import datetime, timedelta
from json import load, dump

class Meeting:
    def __init__(self, date: datetime, title: str):
        self.date = date
        self.title = title


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
        return date not in self.meetings

    def add_meeting(self, meeting: Meeting):
        if self.is_available(meeting.date):
            self.meetings[meeting.date] = meeting
        else:
            self.next_available_slot(meeting.date)

    def next_available_slot(self, date: datetime):
        meeting_date = date
        while not self.is_available(meeting_date):
            print('Termin zajęty')
            meeting_date += timedelta(minutes=60)
            print('Kolejny możliwy termin ', meeting_date.strftime('%d.%m.%Y %H:%M'))

        return meeting_date

calendar = Calendar()

with open('meetings.json') as file:
    data = load(file)
    for item in data:
        meeting = Meeting(datetime.strptime(item['date'], '%d.%m.%Y %H:%M'), item['title'])
        calendar.add_meeting(meeting)

if __name__ == '__main__':
    while True:
        option = input('Co chcesz zrobić? [l]ista, [d]odaj, [k]oniec ')
        if option == 'k':
            break
        elif option == 'l':
            for _, meeting in calendar.meetings.items():
                print(f'Spotkanie zaczyna się: {meeting.date}, jego tytuł: {meeting.title}')
        elif option == 'd':
            title = input('Podaj tytuł spotkania: ')
            date = input('Data spotkania w formacie dd.mm.rrrr hh:mm: ')
            meeting_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
            calendar.add_meeting(Meeting(meeting_date, title))

            with open('meetings.json', 'w') as file:
                data = []
                for meeting in calendar.meetings.values():
                    data.append({
                        'title': meeting.title,
                        'date' : meeting.date.strftime('%d.%m.%Y %H:%M')
                    })
                dump(data, file, indent=2)

        else:
            print('Nie wiem co zrobić')

# def test_check_next_available_slot():
#     birthday = Meeting(datetime(2020, 11, 9, 12, 00), 'Urodziny kogoś')
#     birthday2 = Meeting(datetime(2020, 11, 9, 13, 00), 'Urodziny kogoś innego')
#     birthday3 = Meeting(datetime(2020, 11, 9, 14, 00), 'Urodziny kolejnego')
#     calendar = Calendar()
#
#     calendar.add_meeting(birthday)
#     calendar.add_meeting(birthday2)
#     calendar.add_meeting(birthday3)
#
#     next_time_slot = calendar.next_available_slot(datetime(2020, 11, 9, 12, 00))
#
#     assert next_time_slot == datetime(2020, 11, 9, 15, 00)
#
# def test_add_meeting():
#     # given
#     birthday = Meeting(datetime(2020, 11, 9, 12, 00), 'Urodziny kogoś')
#     birthday2 = Meeting(datetime(2020, 11, 9, 12, 00), 'Urodziny kogoś innego')
#     calendar = Calendar()
#
#     # when
#     calendar.add_meeting(birthday)
#     calendar.add_meeting(birthday2)
#
#     # then
#     assert len(calendar.meetings) == 1
#
# def test_add_two_meetings():
#     # given
#     birthday = Meeting(datetime(2020, 11, 9, 12, 00), 'Urodziny kogoś')
#     birthday2 = Meeting(datetime(2021, 11, 9, 12, 00), 'Urodziny kogoś innego')
#     calendar = Calendar()
#
#     # when
#     calendar.add_meeting(birthday)
#     calendar.add_meeting(birthday2)
#
#     # then
#     assert len(calendar.meetings) == 2
