import aws_cdk as core
import aws_cdk.assertions as assertions

from s3stack.s3resource.s3resource_stack import S3StackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3stack/s3stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3StackStack(app, "s3stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
