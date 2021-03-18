#!/usr/bin/python

from router_details_service import RouterDetailsService
from ping_service import PingService
from datetime import datetime
from time import sleep
from colors import Colors

class NetworkScript:
    def _fetchData(self):
        now = datetime.now()
        pingResult = PingService('8.8.8.8').ping()
        sinr = RouterDetailsService().getSINR()

        print(f'''{Colors.BLUE}At: {now}{Colors.ENDC}
{Colors.GREEN}Ping [8.8.8.8] ---> time: {pingResult['time']}ms, icmp_seq: {pingResult['icmp_seq']}, ttl: {pingResult['ttl']}{Colors.ENDC}
{Colors.PINK}SINR: {sinr}{Colors.ENDC}''')

    def runScript(self):
        SEPARATOR = "==========================================================="
        while True:
            self._fetchData()
            print(SEPARATOR)
            sleep(5)

if __name__ == "__main__":
    NetworkScript().runScript()
