from .models import Credential
import win32cred
from pythoncom import com_error


class CredentialManager:
    @staticmethod
    def get_all_credentials():
        credentials = []
        creds = win32cred.CredEnumerate(None, 0)
        for cred in creds:
            try:
                service_name = cred['TargetName']
                username = cred['UserName']
                credential_blob = cred['CredentialBlob']
                
                password = None
                for encoding in ['utf-16-le', 'utf-16', 'utf-8', 'ascii', 'latin-1']:
                    try:
                        password = credential_blob.decode(encoding).rstrip('\x00')
                        break
                    except UnicodeDecodeError:
                        continue
                
                if password is None:
                    print(f"Warning: Unable to decode password for {service_name}")
                    continue
                
                credentials.append(Credential(service_name, username, password))
            except Exception as e:
                print(f"Error processing credential: {e}")
                continue

        return credentials
    
    @staticmethod
    def add_credential(credential: Credential) -> None:
        try:
            cred = {
                'Type': win32cred.CRED_TYPE_GENERIC,
                'TargetName': credential.service_name,
                'UserName': credential.username,
                'CredentialBlob': str(credential.password),
                'Comment': "Managed by Credential Manager App",
                'Persist': win32cred.CRED_PERSIST_LOCAL_MACHINE
            }
            win32cred.CredWrite(cred, 0)
        except com_error as e:
            raise Exception(f"Failed to add credential: {str(e)}")
    
    @staticmethod
    def update_credential(credential: Credential) -> None:
        CredentialManager.add_credential(credential)  # CredWrite overwrites existing credentials

    @staticmethod
    def delete_credential(service_name: str, username: str) -> None:
        try:
            win32cred.CredDelete(service_name, win32cred.CRED_TYPE_GENERIC, 0)
        except com_error:
            pass  # Credential doesn't exist, nothing to delete