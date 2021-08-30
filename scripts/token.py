#!/usr/bin/python3
import os

from brownie import Token, accounts
from dotenv import load_dotenv

load_dotenv()


def main():
    INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
    return Token.deploy("Test Token", "TST", 18, 1e21, {"from": accounts[0]})
