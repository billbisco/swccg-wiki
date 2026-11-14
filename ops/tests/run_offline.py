"""Run worker regressions with fixture credentials and only loopback sockets.

Usage: python ops/tests/run_offline.py [--temp-root PATH]
No Save Page Now requests or external Wiki/Git requests can leave this process.
"""
import argparse
import ipaddress
import os
import socket
import tempfile
import unittest
from pathlib import Path


def local_address(address):
    host = address[0]
    if host == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--temp-root", type=Path)
    args = parser.parse_args()
    if args.temp_root:
        args.temp_root.mkdir(parents=True, exist_ok=True)
        tempfile.tempdir = str(args.temp_root.resolve())
    os.environ["IA_S3_ACCESS"] = "offline-fixture"
    os.environ["IA_S3_SECRET"] = "offline-fixture"
    create_connection = socket.create_connection
    connect = socket.socket.connect

    def loopback_connection(address, *rest, **kwargs):
        if not local_address(address):
            raise AssertionError("External network is forbidden in worker tests")
        return create_connection(address, *rest, **kwargs)

    def loopback_connect(sock, address):
        if not local_address(address):
            raise AssertionError("External network is forbidden in worker tests")
        return connect(sock, address)

    socket.create_connection = loopback_connection
    socket.socket.connect = loopback_connect
    try:
        result = unittest.TextTestRunner(verbosity=2).run(
            unittest.defaultTestLoader.discover(str(Path(__file__).parent)))
        return 0 if result.wasSuccessful() else 1
    finally:
        socket.create_connection = create_connection
        socket.socket.connect = connect


if __name__ == "__main__":
    raise SystemExit(main())
