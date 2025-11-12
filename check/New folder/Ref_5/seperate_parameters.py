import re

Month_list=['spring','fall','autumn','autumne','winter','augusto','avril','juin','junio','marzo','oktober','summer','dezember'
            ,'abril','mayo','mars','décembre','septembre','juillet','octobre']

Last_Month_list = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def monthCheck(season):
    month_mapping = {
        'spring': 'March','fall': 'September','autumn': 'September','autumne': 'September','winter': 'December','augusto': 'August','avril': 'April',
        'juin': 'June','junio': 'June','marzo': 'March','oktober': 'October','octobre': 'October','summer': 'June','dezember': 'December',
        'abril': 'April','mayo': 'May','mars':'March','Décembre':'December','Septembre':'September','juillet':'July'
    }
    return month_mapping.get(season)

def all_details(Volume_issue):
    volume_match = re.search(r"Volume\s*(\d+[A-Z]?)", Volume_issue, re.IGNORECASE)
    issue_match = re.search(r"(?:Number|Numbers?|Numéro|Issue|No\.)\s*([\d &-]+)", Volume_issue, re.IGNORECASE)
    year_match = re.search(r"(\d{4})", Volume_issue, re.IGNORECASE)
    month_match = re.search(r"\b([A-Za-zÀ-ÿ/-]+) \d{4}", Volume_issue, re.IGNORECASE)
    part_match = re.search(r"Part\s*(\d+)", Volume_issue, re.IGNORECASE)

    Volume = volume_match.group(1) if volume_match else ""
    Issue = issue_match.group(1) if issue_match else ""
    if Issue.endswith(" & "):
        Issue = Issue.replace(" & ","")

    Year = year_match.group(1) if year_match else ""
    Month = month_match.group(1) if month_match else ""
    Part = part_match.group(1) if part_match else ""

    if Month:
        Month = re.split(r"[-/]", Month)[0]
        Month = monthCheck(Month.lower()) if Month.lower() in Month_list else Month
        Month = Month if Month in Last_Month_list else ""

    return Volume,Issue,Part,Year,Month