import subprocess as sp
import re

class PingService:
    _address = str() # default
    _fields: list = ['time', 'icmp_seq', 'ttl']
    _result = dict()

    def __init__(self, address: str):
        self._address = address

    def ping(self) -> dict:
        output = sp.getoutput(f'ping -c 1 {self._address}')
        for field in self._fields:
            pattern = fr'{field}=(.*?) '
            self._result[field] = re.search(pattern, output).group(1)
        return self._result