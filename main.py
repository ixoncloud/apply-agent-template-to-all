import configparser
import requests
import json

config = configparser.ConfigParser()
config.read("config.ini")
bearer_token = config.get("vars", "bearer_token")
api_application = config.get("vars", "api_application")
api_company = config.get("vars", "api_company")
template = config.get("vars", "template")

agents_url = "https://portal.ixon.cloud:443/api/agents"

headers = {
    "Accept": "application/json",
    "Api-Version": "2",
    "Api-Application": api_application,
    "Api-Company": api_company,
    "Authorization": "Bearer {}".format(bearer_token)
}

response = requests.get(agents_url, headers=headers).json()
agents = response["data"]

print("\nThis will apply template: {} to the following agents:\n".format(template))
for agent in agents:
    print(agent)
print("\n")

if input("THIS CHANGE CAN NOT BE REVERTED Are you sure? (y/n)") != "y":
    exit()

print("\n")
for agent in agents:
    apply_template_url = "https://portal.ixon.cloud:443/api/agents/{}/from-template".format(agent["publicId"])

    payload = {
        "template": {"publicId": template},
        "importDisplaySettings": True,
        "importLanSettings": True,
        "importFirewallSettings": True,
        "importPageLinks": True,
        "importServices": True,
        "importDataSettings": True
    }
    headers = {
        "Accept": "application/json",
        "Api-Version": "2",
        "Api-Application": api_application,
        "Api-Company": api_company,
        "Authorization": "Bearer {}".format(bearer_token),
        "Content-Type": "application/json",
    }

    response = requests.patch(apply_template_url, json=payload, headers=headers).json()
   

    print(json.dumps(agent) + " " + response["status"])




