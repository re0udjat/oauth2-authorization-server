def get_client(client_id: str, clients: list) -> dict:
    client = next(filter(lambda item: item["client_id"] == client_id, clients), None)
    return client