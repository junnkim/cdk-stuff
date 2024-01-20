from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct
 
class S3ResourceStack(Stack):
 
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
 
        bucket = s3.CfnBucket(self, "CfnBucket",
            public_access_block_configuration= s3.CfnBucket.PublicAccessBlockConfigurationProperty(
                block_public_acls=False,
                block_public_policy=False,
                ignore_public_acls=False,
                restrict_public_buckets=False
            ),
            ownership_controls= s3.CfnBucket.OwnershipControlsProperty(
                rules=[s3.CfnBucket.OwnershipControlsRuleProperty(
                    object_ownership="ObjectWriter"
                )]
            )
        )
 
        bucket.apply_removal_policy(
            policy=RemovalPolicy.RETAIN, 
            apply_to_update_replace_policy=True
        )