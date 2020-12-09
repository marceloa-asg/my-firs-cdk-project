"""
Custom VPC Stack.
"""
from aws_cdk import aws_ec2 as _ec2
from aws_cdk import aws_s3 as _s3
from aws_cdk import core


class CustomVpcStack(core.Stack):
    """Custom VPC stack. """

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        prod_configs = self.node.try_get_context('envs')['prod']

        custom_vpc = _ec2.Vpc(
            self,
            "customVpcId",
            cidr=prod_configs['vpc_configs']['vpc_cidr'],
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                _ec2.SubnetConfiguration(
                    name="publicSubnet", cidr_mask=prod_configs['vpc_configs']['vpc_mask'], subnet_type=_ec2.SubnetType.PUBLIC
                ),
                _ec2.SubnetConfiguration(
                    name="privateSubnet", cidr_mask=prod_configs['vpc_configs']['vpc_mask'], subnet_type=_ec2.SubnetType.PRIVATE
                ),
                _ec2.SubnetConfiguration(
                    name="dbSubnet", cidr_mask=prod_configs['vpc_configs']['vpc_mask'], subnet_type=_ec2.SubnetType.ISOLATED
                )
            ]
        )
        core.Tags.of(custom_vpc).add("Owner", "Mystique")

        core.CfnOutput(self,
                       "customVpcOutput",
                       value=custom_vpc.vpc_id,
                       export_name="customVpcId")

        my_bkt = _s3.Bucket(self,"mycustombucket")
        core.Tags.of(my_bkt).add( "Owner", "Mystique")
