from requests import Response
from starlette.testclient import TestClient


def test_values_get_200(client: TestClient) -> None:
    response: Response = client.get(url='/api/values/')
    assert response.status_code == 200
    assert response.json() == {}
