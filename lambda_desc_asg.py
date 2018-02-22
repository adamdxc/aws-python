import boto3
import os

auto_scaling_grp_name = os.environ['asg_name']
asg_client = boto3.client('autoscaling')

def lambda_handler(event, context):
    # TODO implement
    
    response = asg_client.describe_auto_scaling_instances()
    auto_scaling_instances = response['AutoScalingInstances'] #Return a List
    enum_auto_scaling_instances = list(enumerate(auto_scaling_instances)) # enumerate is python build in function : https://docs.python.org/3/library/functions.html#enumerate
  
    #print(enum_auto_scaling_instances)
    
    total_instances = len(auto_scaling_instances) # count the item in a List
    
    for index, elem in enum_auto_scaling_instances:
        print(index, elem['InstanceId'])
        
    return 'Complete'
