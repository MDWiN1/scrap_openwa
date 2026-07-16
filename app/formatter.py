def format_report(parsed_list, start_time, end_time):
    text = "*Laporan AWOS dan RADAR*\n"
    text += f"{start_time} → {end_time}\n\n"

    for p in parsed_list:
        text += f"- {p['type']} {p['station']} → *{p['status']}*\n"

    text += f"\nTotal valid: {len(parsed_list)}"

    return text