from .base import BaseIssuer
import json
import os
import requests
import time

class IasControllerIssuer(BaseIssuer):
        def __init__(self):
                super().__init__()

        def issue_credential(self, did):
                print(f"DEBUG: IAS issue_credential to DID: {did}")

                # wait 1 second for the DID to propagate through
                time.sleep(1)

                headers = {}
                headers["Content-Type"] = "application/json"
                headers["X-API-KEY"] = os.getenv("IAS_CONTROLLER_API_KEY")

                r = requests.post(
                        f"{os.getenv('IAS_CONTROLLER_URL')}/credentials/{did}/next",
                        headers=headers,
                )

                if r.status_code != 202:
                        print(f"Error from IAS issue cred API call: {r.status_code} {r.text}")

                return {}

        def revoke_credential(self, connection_id, credential_exchange_id):
                # IAS Controller revocation not implemented for these load tests
                print(f"DEBUG: IAS revoke_credential called for connection_id: {connection_id}, credential_exchange_id: {credential_exchange_id}")
                pass