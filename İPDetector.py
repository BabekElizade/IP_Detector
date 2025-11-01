import requests
while True:
    print("(c) və (C) ilə çıxış edə bilərsiniz!")
    İP_input = input("IP unvanini daxil et: ")
    if(İP_input == "C" or İP_input == "c"):
        break
    url = f"https://ipinfo.io/{İP_input}/json"
    response = requests.get(url)
    data = response.json()

    print("\nMəlumat:")
    print("IP:", data.get("ip"))
    print("Ölkə:", data.get("country"))
    print("Şəhər:", data.get("city"))
    print("Provayder:", data.get("org"))

