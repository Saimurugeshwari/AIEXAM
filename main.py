import os
from google.cloud import secretmanager
from ui.main_ui import build_ui


def load_gcp_credentials_from_secret(secret_id="aiexam-service-key", project_id="aiexam-adk-hackathon-project"):
    """Fetch service account key from Secret Manager and set as GOOGLE_APPLICATION_CREDENTIALS."""
    client = secretmanager.SecretManagerServiceClient()

    secret_path = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(name=secret_path)
    key_json = response.payload.data.decode("UTF-8")

    # Save to a temporary file
    temp_path = "temp_google_key.json"
    with open(temp_path, "w") as f:
        f.write(key_json)

    # Set environment variable for all downstream API calls
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = temp_path
    print(f"Loaded GCP key from Secret Manager → {temp_path}")


if __name__ == "__main__":
    load_gcp_credentials_from_secret()  # Securely load key
    demo = build_ui()
    demo.launch()



