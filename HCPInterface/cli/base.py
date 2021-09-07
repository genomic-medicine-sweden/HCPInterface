import click
import sys

from HCPInterface import log, version
from HCPInterface.hcp import HCPManager
from HCPInterface.hci import hci
from HCPInterface.cli.functions import delete, search, upload
from HCPInterface.cli.hci_functions import hci

@click.group()
@click.option("-ep","--endpoint",help="Endpoint URL",type=str,default="")
@click.option("-id","--access_key_id",help="Amazon key identifier",type=str,default="")
@click.option("-key","--access_key",help="Amazon secret access key",type=str,default="")
@click.option('-c',"--credentials", help="File containing ep, id & key; instead of using the CLI.",type=str,default="")
@click.option("-b","--bucket",help="Bucket name",type=str, required=True)
@click.version_option(version)
@click.pass_context
def root(ctx, endpoint, access_key_id, access_key, bucket, credentials):
    """HCP interfacing tool"""
    #Invalid input checks
    if credentials != "" and (endpoint != "" or access_key_id != "" or access_key != ""):
        log.error("Credentials were provided both through a file and the CLI. Make up your mind")
        sys.exit(-1)

    ctx.obj = {}
    hcpm = HCPManager(endpoint, access_key_id, access_key, bucket=bucket,credentials_path=credentials)
    hcpm.attach_bucket(bucket)
    ctx.obj["hcpm"] = hcpm


root.add_command(hci)
root.add_command(delete)
root.add_command(search)
root.add_command(upload)
