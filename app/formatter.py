def format_report(parsed_list, start_time, end_time):
    # 1. Initialize headers for each message block
    lines_radar = ["*Laporan RADAR*", f"{start_time} → {end_time}", ""]
    lines_awos = ["*Laporan AWOS*", f"{start_time} → {end_time}", ""]
    lines_aws = ["*Laporan AWS*", f"{start_time} → {end_time}", ""]

    # 2. Track counts individually for accurate totals
    count_radar = 0
    count_awos = 0
    count_aws = 0

    # 3. Sort data into respective blocks using substring matching ('in')
    for p in parsed_list:
        site = p.get("site_name", "-")
        status = p.get("status", "-")
        site_upper = site.upper()

        if "RADAR" in site_upper:
            lines_radar.append(f"• {site} → *{status}*")
            count_radar += 1
        elif "AWOS" in site_upper:
            lines_awos.append(f"• {site} → *{status}*")
            count_awos += 1
        elif "AWS" in site_upper:
            lines_aws.append(f"• {site} → *{status}*")
            count_aws += 1

    # 4. Append individual totals to the bottom of each list
    lines_radar.extend(["", f"Total valid: {count_radar}"])
    lines_awos.extend(["", f"Total valid: {count_awos}"])
    lines_aws.extend(["", f"Total valid: {count_aws}"])

    # 5. Convert each list to text and return them as a list of messages
    messages = []
    if count_radar > 0:
        messages.append("\n".join(lines_radar))
    if count_awos > 0:
        messages.append("\n".join(lines_awos))
    if count_aws > 0:
        messages.append("\n".join(lines_aws))

    return messages