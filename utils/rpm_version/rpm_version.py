#!/usr/bin/env python3
import argparse
import requests
import re
from lxml import html

BASE_URL="http://rpm-repo.argo.grnet.gr/ARGO/"

def main():
    #Setup argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--environment", help="Environment devel or prod", required=True, choices=["devel","prod"])
    parser.add_argument("-d","--distribution", help="OS distribution centos6 or centos7", required=True, choices=["centos6","centos7"])
    parser.add_argument("-a","--artifact", help="Artifact to query", required=True)
    parser.add_argument("-p","--position", help="Position of the artifact [1 for latest, 2 for the one before the latest etc.]", type=int, default=1)
    args = parser.parse_args()
    
    #Fetch sorted page
    repo_url = BASE_URL + args.environment + "/" + args.distribution + "/?C=M;O=D"
    r = requests.get(repo_url)
    
    #Create html tree and get list with the rpms
    tree = html.fromstring(r.content)
    artifacts = tree.xpath('//tr/td[2]/a[@href]/text()')

    #Print Artifact if found
    num = 1
    for artifact in artifacts:
        if artifact.startswith(args.artifact) and artifact.endswith('rpm'):
            if num == args.position:
                print(artifact)
                exit(0)
            num+=1
    print("Artifact was not found")

if __name__ == "__main__":
    main()