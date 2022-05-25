#!/usr/bin/env python3

# Downloads or deletes files from selected bucket on the HCP.

import click
import glob
import os
import json
import sys
import time

from NGPIris import log, WD
from NGPIris.hcp import HCPManager
from NGPIris.hci import hci as HCI

##############################################


def query_hci(query, index, password):
    HCI.create_template(index, query)
    token = HCI.generate_token(password)
    hci_query = HCI.pretty_query(token)

    return hci_query

@click.group()
@click.pass_context
def utils(ctx):
    """Advanced commands for specific purposes"""
    pass

@utils.command()
@click.option('-i',"--index",help="List indices present on NGPi", default="all", required=True)
@click.pass_obj
def indices(ctx, index):
    """Displays file hits for a given query"""
    hcim = ctx['hcim']
    token = hcim.generate_token()
    index_list = hcim.get_index(token, index=index)
    pretty = json.dumps(index_list)
    print(json.dumps(pretty, indent=4))

def main():
    pass

if __name__ == "__main__":
    main()