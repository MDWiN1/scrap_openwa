from datetime import datetime, timedelta
from app.config import WIB
from app.openwa_client import get_messages
from app.parser import is_valid_report, parse_message
from app.formatter import format_report
from app.telegram_client import send_long_message


# def get_time_range():
#     now = datetime.now(WIB)
#
#     today_7am = now.replace(hour=7, minute=0, second=0, microsecond=0)
#
#     end_time = today_7am
#     start_time = end_time - timedelta(hours=24)
#
#     return start_time, end_time

def get_time_range():
    end_time = datetime.now(WIB)
    start_time = end_time - timedelta(hours=24)
    return start_time, end_time


def filter_messages(messages, start_time, end_time):
    results = []
    for msg in messages:
        #print(messages)
        body = msg.get("body", "")
        timestamp = msg.get("timestamp")
        #print(body)

        if not body or not timestamp:
            continue

        msg_time = datetime.fromtimestamp(timestamp, tz=WIB)

        if not (start_time <= msg_time < end_time):
            continue

        if not is_valid_report(body):
            continue

        #parsed = parse_message(body)
        parsed = parse_message(body)
        print("ini parsed :", parsed)
        if parsed:
            results.append(parsed)

    return results


def main():
    print("Running job...")

    messages = get_messages()
    print(messages)
    print(len(messages))
    start_time, end_time = get_time_range()

    parsed_list = filter_messages(messages, start_time, end_time)
    print(parsed_list)

    report = format_report(parsed_list, start_time, end_time)

    send_long_message(report)

    print("Done. Report sent.")


if __name__ == "__main__":
    main()