#!/usr/bin/env python3
"""App """
from aws_cdk import core
from resource_stacks.custom_vpc import CustomVpcStack

app = core.App()

CustomVpcStack(app, "my-custom-vpc")
core.Tags.of(app).add(key="stack-team-support-email",
                      value=app.node.try_get_context('envs')['prod']["stack-team-support-email"])
core.Tags.of(app).add(key="stack-level-tagging",
                      value=app.node.try_get_context('envs')['prod']["stack-level-tagging"])
app.synth()
