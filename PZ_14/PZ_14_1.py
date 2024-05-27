# В исходном текстовом файле(radio_stations.txt)
# найти все домены из URL-адресов (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio).

import re

with open('radio_stations.txt', 'r', encoding='utf-8') as f:
    for line in f:
        regex = r"http://([^:]+)"
        line = line.strip()
        p = re.search(regex, line)
        if p:
            print(p.group(1))