#!/usr/bin/env python3

from aws_cdk import core

from my_1st_cdk_project.my_1st_cdk_project_stack import My1StCdkProjectStack


app = core.App()
My1StCdkProjectStack(app, "my-1st-cdk-project")

app.synth()
