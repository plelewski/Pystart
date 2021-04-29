from json import load, dump


class Meeting:
    def __init__(self, start_time: str, title: str):
        self.start_time = start_time
        self.title = title

    def get_info(self):
        return f'Godzina startu: {self.start_time}, Tytuł: {self.title}'

class Calendar:
    def __init__(self):
        self.items = []

    def add_meeting(self, meeting:Meeting):
        self.items.append(meeting)

    def get_items(self):
        return sorted(self.items, key=lambda x: x.start_time)


if __name__ == '__main__':
    calendar = Calendar()

    try:
        with open('meetings.json') as data:
            meetings = load(data)
    except FileNotFoundError:
        print('brak pliku')
        quit()

    for m in meetings['meeting']:
        calendar.add_meeting(Meeting(m['start_time'], m['title']))

    while True:
        answer = input('Co chcesz zrobić: [w]yświetl spotkania / [d]odaj spotkanie / [k]oniec ')
        if answer == 'k':
            break
        elif answer == 'w':
            for c in calendar.get_items():
                print(c.get_info())
        else:
            new_start_time = input('Podaj datę spotkania w formacie yyyy.mm.dd hh24: ')
            new_title = input('Podaj tytuł spotkania: ')
            calendar.add_meeting(Meeting(new_start_time, new_title))

    data = {}
    data['meeting'] = []
    for cc in calendar.get_items():
        data['meeting'].append(
            {
                "start_time": cc.start_time,
                "title": cc.title
            }
        )

    with open('meetings.json', 'w') as f:
        dump(data, f, indent=2)
