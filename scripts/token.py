#!/usr/bin/python3
import os

from brownie import Token, accounts


def main():
    account = accounts.load("razzle-dazzle-wallet")
    return Token.deploy("Razzle Dazzle", "RD", 18, 1e21, {"from": account})
