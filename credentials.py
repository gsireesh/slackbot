import json, os

def load_credentials(required_fields, credentials_file=None):
	if credentials_file:
		with open(credentials_file, 'r') as cred_file:
			file_creds = json.loads(cred_file.read())

	credentials = {}
	for field in required_fields:
		if field in os.environ:
			credentials[field] = os.environ[field]
		elif field in file_creds:
			credentials[field] = file_creds[field]

	return credentials
