#!/usr/bin/env python3
# -*- conding: utf-8 -*-

"""Python Amazon module"""

import boto3


def aws_ses() -> None:
    # ses = boto3.client("ses", "us-east-1")
    # ses_client = boto3.client("s3", "us-east-1")
    # s_3 = boto3.resource("s3", region_name="us-east-1")  # , "us-east-1")

    # # resources = ses_client.verify_email_identity(
    # #     EmailAddress="boutique@relyance.ai"
    # # )

    # for bucket in s_3.buckets.all():
    #     print(f"BUCKET NAME --> {bucket.name}")
    # # print(f"resources ---> {ses_client}")
    # print(f"ses_client ---> {ses_client}")
    # # print(f"ses ---> {ses2}")

    # return

    # The calls to AWS STS AssumeRole must be signed with the access key ID
    # and secret access key of an existing IAM user or by using existing temporary
    # credentials such as those from another role. (You cannot call AssumeRole
    # with the access key for the root account.) The credentials can be in
    # environment variables or in a configuration file and will be discovered
    # automatically by the boto3.client() function. For more information, see the
    # Python SDK documentation:
    # http://boto3.readthedocs.io/en/latest/reference/services/sts.html#client

    # create an STS client object that represents a live connection to the
    # STS service
    sts_client = boto3.client('sts')

    # Call the assume_role method of the STSConnection object and pass the role
    # ARN and a role session name.
    assumed_role_object = sts_client.assume_role(
        RoleArn="arn:aws:iam::580082088342:role/RoleForAmazonSESIntegration",
        RoleSessionName="AssumeRoleSession1"
    )

    # From the response that contains the assumed role, get the temporary
    # credentials that can be used to make subsequent API calls
    credentials = assumed_role_object['Credentials']

    # Use the temporary credentials that AssumeRole returns to make a
    # connection to Amazon S3
    s3_resource = boto3.resource(
        's3',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )

    # Use the Amazon S3 resource object that is now configured with the
    # credentials to access your S3 buckets.
    for bucket in s3_resource.buckets.all():
        print(bucket.name)
