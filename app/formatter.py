def format_report(parsed_list, start_time, end_time):
    lines = [
        "*Laporan AWOS dan RADAR*",
        f"{start_time} → {end_time}",
        ""
    ]

    for p in parsed_list:
        site = p.get("site_name", "-")
        status = p.get("status", "-")

        lines.append(f"• {site} → *{status}*")

    lines.append("")
    lines.append(f"Total valid: {len(parsed_list)}")

    return "\n".join(lines)