import json

def get_access_count(item):
    return item[1]

def read_logs(file_name):
    with open(file_name, "r") as log_file:
        return log_file.readlines()

logs = read_logs("server-log.txt")

ip_count = {}
page_count = {}
status_code_count = {}
total_requests = 0
successful_requests = 0

for line in logs:
    parts = line.split()
    if len(parts) < 9:
        continue

    ip = parts[0]
    page = parts[6]
    status_code = parts[8]

    ip_count[ip] = ip_count.get(ip, 0) + 1

    page_count[page] = page_count.get(page, 0) + 1

    status_code_count[status_code] = status_code_count.get(status_code, 0) + 1

    total_requests += 1

    if status_code == "200":
        successful_requests += 1

print("IPs y accesos:")
for ip, count in ip_count.items():
    print(ip, count)

print("\n3 páginas más visitadas:")
top_pages = sorted(page_count.items(), key=get_access_count, reverse=True)[:3]
for page, count in top_pages:
    print(page, count)

success_percentage = (successful_requests / total_requests * 100) if total_requests > 0 else 0
print("\nPorcentaje de accesos exitosos:", success_percentage, "%")

with open('status_code_count.json', 'w') as json_file:
    json.dump(status_code_count, json_file)

def read_and_count(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        return len(lines)

ok_count = read_and_count("ok.txt")
error_count = read_and_count("errors.txt")

print(f"\nTotal de accesos exitosos (200): {ok_count}")
print(f"Total de errores (500): {error_count}")
