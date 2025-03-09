import requests
import yaml

# URLs for OpenAPI and Validator List
OPENAPI_URL = "https://raw.githubusercontent.com/TheSPSDAO/SPS-Validator/master/apps/sps-validator-ui/openapi.yaml"
VALIDATOR_URL = "https://splinterlands-validator-api.splinterlands.com/validators?limit=10&active=true"

# Local file for extra endpoints
CUSTOM_ENDPOINTS_FILE = "custom_endpoints.yml"

def fetch_openapi_yaml():
    """Fetch the remote OpenAPI YAML from GitHub."""
    response = requests.get(OPENAPI_URL)
    if response.status_code == 200:
        return yaml.safe_load(response.text)
    else:
        print(f"Failed to fetch OpenAPI YAML. Status code: {response.status_code}")
        return None

def fetch_validators():
    """Fetch the top 10 validators."""
    response = requests.get(VALIDATOR_URL)
    if response.status_code == 200:
        data = response.json()
        return [{"url": v["api_url"]} for v in data.get("validators", []) if "api_url" in v]
    else:
        print(f"Failed to fetch validators. Status code: {response.status_code}")
        return []

def load_custom_endpoints():
    """Load custom OpenAPI endpoints from local file."""
    try:
        with open(CUSTOM_ENDPOINTS_FILE, "r") as file:
            return yaml.safe_load(file).get("paths", {})
    except Exception as e:
        print(f"Error loading custom endpoints: {e}")
        return {}

def update_openapi_servers():
    """Update the OpenAPI YAML with servers and missing endpoints."""
    openapi_data = fetch_openapi_yaml()
    if not openapi_data:
        return

    servers = fetch_validators()
    if not servers:
        print("No valid servers found.")
        return

    # Update the servers section
    openapi_data["servers"] = servers

    # Merge custom endpoints
    custom_paths = load_custom_endpoints()
    openapi_data["paths"].update(custom_paths)

    # Save updated OpenAPI spec
    with open("openapi.yaml", "w") as file:
        yaml.dump(openapi_data, file, default_flow_style=False)

    print("Updated OpenAPI YAML successfully.")

if __name__ == "__main__":
    update_openapi_servers()
