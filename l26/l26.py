import requests
#
# url = "https://www.google.com"
# response = requests.get(url)
#
# response.raise_for_status()
#
# print("HTML код страницы (начало): ")
# print(response.text[:200])



# payload = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
#
# r = requests.get('https://httpbin.org/get', params=payload)
# print(f"Итоговый URL с параметрами: {r.url}")

# response = requests.get('https://api.github.com/events')
#
# data = response.json()
#
# if data:
#     print(f"Тип последнего события на GitHub: {data[0]['type']}")



# url = "http://dvmn.org/filer/canonical/1542890876/16/"
# response = requests.get(url)
# response.raise_for_status()
#
# filename = 'dvmn.svg'
# with open(filename, 'wb') as f:
#     f.write(response.content)
#
# print(f"Файл {filename} успешно скачан!")



# r_put = requests.put("https://httpbin.org/put", data={"key": "value"})
#
# r_delete = requests.delete("https://httpbin.org/delete")
#
# r_head = requests.head("https://httpbin.org/get")
#
# print(f"Статус DELETE-запроса: {r_delete.status_code}")