#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3stack.s3stack_stack import S3StackStack


app = cdk.App()
S3StackStack(app, "S3StackStack",

    )

app.synth()
