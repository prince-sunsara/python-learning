""" 
CREATING COMMAND LINE UTILITES:
    > Command line utilities are programs that can be run from the terminal or command interface, and they are an essential part of many development workflows.
    > In python, You can create your own command line utilites using the built-in 'argparse' module.
"""
import argparse 
import requests

def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

# add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save it")
parser.add_argument("-o", "--output", help="name of the file", default=None)

# parse the argument
args = parser.parse_args()

# use the arguments in your code
print(args.url)
print(args.output)
download_file(args.url, args.output)