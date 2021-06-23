from web3 import Web3
from typing import Any, Dict
import sys
import getopt
import yaml


class Web:
    def __init__(self) -> None:
        self.ip = 'localhost'  # default ip
        self.port = '8545'  # default port
        self.filename = 'abi.yml'  # default abi file
        self.set_opts()

    def set_opts(self) -> None:
        opts, args = getopt.getopt(sys.argv[1:], 'i:p:n:', ['ip', 'port'])

        for opt, arg in opts:
            if opt == '-i':
                self.ip = arg
            if opt == '-p':
                self.port = arg
            if opt == '-n':
                self.filename = arg

    def connect_to_web3(self) -> Any:
        w3 = Web3(Web3.HTTPProvider(f'http://{self.ip}:{self.port}'))

        if w3.isConnected():
            return w3
        else:
            return None

    def get_abi(self) -> Dict:
        abi = None
        try:
            with open(self.filename) as f:
                abi = yaml.load(f, Loader=yaml.FullLoader)
        except FileNotFoundError:
            print('Please, check your file name.')

        return abi


if __name__ == '__main__':
    conn = Web()
    conn.connect_to_web3()
