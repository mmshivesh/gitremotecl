#!/usr/bin/env python3
import requests, argparse, os, json
'''
1. Create a folder from the input ==>DONE
2. cd into the folder ==>DONE
3. Initialize empty git ==>DONE
4. Create a remote repo with specific params ==>DONE
5. Create a first commit
'''
from pprint import pprint
parser = argparse.ArgumentParser(description="Create a remote git repo easily from the command line")
parser.add_argument('foldername', metavar='local_repo_name', help='Local repository name')
parser.add_argument('-r', dest='remotename', metavar='repo_name', help='Remote repo name. Uses localRepoName if not specified')
parser.add_argument('-d', dest='description', help='Description for the repository')
parser.add_argument('-p', help='Create a private repo', default=False, action='store_true')

remotehost = parser.add_mutually_exclusive_group()
remotehost.add_argument('-gh',help='Use GitHub (default)', action='store_true')
remotehost.add_argument('-gl',help='Use GitLab*', action='store_true')
remotehost.add_argument('-bb',help='Use BitBucket*', action='store_true')

args = parser.parse_args()

if args.remotename==None:
	args.remotename = (args.foldername).replace(' ', '-')
if args.bb==False and args.gl==False:
	args.gh=True
print(args)
os.mkdir(args.foldername)
os.system(f"git init ./{args.foldername}")
os.chdir(f'./{args.foldername}')

if args.gh:
	oauth_token = '<YOUR TOKEN HERE>'
	head = {'Authorization': 'token {}'.format(oauth_token)}
	url = f'https://api.github.com/user/repos'
	payload = {
		"name": args.remotename,
		"description": args.description,
		"private": args.p
	}
	r = requests.post(url, headers=head, json=payload)
	# print(r.status_code,r.content)
	jsonresponse = json.loads(r.content)
	if r.status_code == 201:
		print("Created Successfully")
	os.system("git remote add origin {}".format(jsonresponse['clone_url']))
	pass
elif args.gl:
	print("WIP")
elif args.bb:
	print("WIP")
