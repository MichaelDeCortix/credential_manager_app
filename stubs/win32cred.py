"""Stub module for win32cred (Windows-only) to enable development on Linux."""

CRED_TYPE_GENERIC = 1
CRED_PERSIST_LOCAL_MACHINE = 2

_credentials_store: list[dict] = []


def CredEnumerate(filter_val, flags):
    """Return all stored credentials."""
    result = []
    for cred in _credentials_store:
        entry = dict(cred)
        blob = entry.get("CredentialBlob", b"")
        if isinstance(blob, str):
            entry["CredentialBlob"] = blob.encode("utf-16-le")
        result.append(entry)
    return result


def CredWrite(credential, flags):
    """Write a credential to the in-memory store."""
    for i, cred in enumerate(_credentials_store):
        if cred["TargetName"] == credential["TargetName"]:
            _credentials_store[i] = dict(credential)
            return
    _credentials_store.append(dict(credential))


def CredDelete(target_name, cred_type, flags):
    """Delete a credential from the in-memory store."""
    for i, cred in enumerate(_credentials_store):
        if cred["TargetName"] == target_name:
            _credentials_store.pop(i)
            return
    raise Exception("Credential not found")
