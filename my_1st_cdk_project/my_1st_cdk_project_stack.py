from aws_cdk import (
    aws_s3 as _s3,
    aws_iam as _iam,
    aws_kms as _kms,
    core
    )

class MyArtifactBucketStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # print (self.node.try_get_context("prod")["kms_arn"])
        myKey = _kms.Key.from_key_arn(self,
                                      "myKeyId",
                                      self.node.try_get_context("prod")["kms_arn"])


        if is_prod:
            artifactBucket = _s3.Bucket(self,
                                        "myProdArtifactBucketId",
                                        versioned=True,
                                        encryption=_s3.BucketEncryption.KMS,
                                        encryption_key=myKey,
                                        removal_policy=core.RemovalPolicy.RETAIN)
        else:
            artifactBucket = _s3.Bucket(self,
                                 "myDevArtifactBucket",
                                 removal_policy=core.RemovalPolicy.DESTROY)
            