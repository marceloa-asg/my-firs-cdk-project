#!/usr/bin/env python3

from aws_cdk import core

from my_1st_cdk_project.my_1st_cdk_project_stack import MyArtifactBucketStack

app = core.App()

env_dev = core.Environment(account=app.node.try_get_context("dev")["account"], 
                          region=app.node.try_get_context("dev")["region"])
env_prod = core.Environment(account=app.node.try_get_context("prod")["account"], 
                          region=app.node.try_get_context("prod")["region"])

print (app.node.try_get_context("dev")["region"])
MyArtifactBucketStack(app, "myDevStack", env=env_dev)
MyArtifactBucketStack(app, "myProdStack", is_prod=True, env=env_prod)

app.synth()
