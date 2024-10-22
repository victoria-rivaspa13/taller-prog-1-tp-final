import json

def get_access_count(item):
    return item[1]

with open("server_log.txt", "r") as log_file:
    logs = log_file.readlines()  # lee líneas en vez de todo el contenido

ip_count = {}
page_count = {}
status_code_count = {}  # Diccionario para contar los códigos de estado
total_requests = 0
successful_requests = 0

# Procesar cada línea en los registros
for line in logs:
    parts = line.split()
    if len(parts) < 9:
        continue  # Saltea las líneas que no tienen suficientes partes

    ip = parts[0]
    page = parts[6]
    status_code = parts[8]

    # Cuenta los accesos de IP
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

    # Cuenta los accesos a la página
    if page in page_count:
        page_count[page] += 1
    else:
        page_count[page] = 1

    # Cuenta los códigos de estado
    if status_code in status_code_count:
        status_code_count[status_code] += 1
    else:
        status_code_count[status_code] = 1

    total_requests += 1

    # Cuenta los intentos exitosos
    if status_code == "200":
        successful_requests += 1

# Imprime las IPs y los accesos
print("IPs y accesos:")
for ip in ip_count:
    print(ip, ip_count[ip])

# Imprime las 3 páginas más visitadas
print("\n3 páginas más visitadas:")
top_pages = [(page, count) for page, count in page_count.items()]

# Ordena las páginas principales según el número de accesos en orden descendente
top_pages.sort(key=get_access_count, reverse=True)

# Imprime las top 3 páginas
for i in range(min(3, len(top_pages))):  # Asegúrate de no exceder la longitud de la lista
    print(top_pages[i][0], top_pages[i][1])

# Calcula e imprime el porcentaje de accesos exitosos
if total_requests > 0:
    success_percentage = (successful_requests / total_requests) * 100
else:
    success_percentage = 0

print("\nPorcentaje de accesos exitosos:", success_percentage, "%")

# Guarda los resultados de los códigos de estado para usarlos en el gráfico
with open('status_code_count.json', 'w') as json_file:
    json.dump(status_code_count, json_file)

# Imprime los códigos de estado y sus conteos para verificar
print("\nConteo de códigos HTTP:")
for code, count in status_code_count.items():
    print(f"Código {code}: {count}")
