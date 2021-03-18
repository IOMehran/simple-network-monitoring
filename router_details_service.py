import requests
import json

class RouterDetailsService:
    _routerEndpoint: str = 'http://192.168.1.1' # default
    _dataTosend: dict = {"cmd":113,"method":"GET","sessionId":"","language":"EN"}
    _httpClient = requests.Session()

    def _sendDataToRouter(self):
        return self._httpClient.post(f'{self._routerEndpoint}/cgi-bin/http.cgi', json.dumps(self._dataTosend)).text
        
    def getSINR(self):
        return json.loads(self._sendDataToRouter())['sinr']