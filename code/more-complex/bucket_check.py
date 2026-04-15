import boto3

session = boto3.Session(profile_name='default')

s3 = session.client('s3')

try:
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"Found bucket! {bucket['name']}")

except Exception as e:
    print(f"Authentication error: {e}")
    print(f"Try running 'aws sso login' in your terminal first.")
