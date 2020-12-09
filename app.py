#!/usr/bin/env python3
"""App """
from aws_cdk import core
from resource_stacks.custom_vpc import CustomVpcStack

app = core.App()
STACKTEAMSUPPORTEMAIL="stack-team-support-email"
STACKLEVELTAGGING="stack-level-tagging"

CustomVpcStack(app, "my-custom-vpc")
core.Tags.of(app).add(key=STACKTEAMSUPPORTEMAIL,
                      value=app.node.try_get_context('envs')['prod'][STACKTEAMSUPPORTEMAIL])
core.Tags.of(app).add(key=STACKLEVELTAGGING,
                      value=app.node.try_get_context('envs')['prod'][STACKLEVELTAGGING])
app.synth()
