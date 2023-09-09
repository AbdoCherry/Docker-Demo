# Importing necessary modules
import json
import utils

def lambda_handler(event, context):
    
    print('Let\'s test if volumes works - Test 2')
    try:
        env_vars = utils.load_envs()
        utils.load_mysql(env_vars = env_vars)
        utils.hello_world()
        
        return {
            'code' : 200,
            'message' : 'Lambda handler worked fine'
        }
        
    except Exception as e:
        return {
            'code' : 400,
            'message' : f'Error occured: {e}'
        }
        
    
response = lambda_handler({}, {})
print(json.dumps(response, indent = 2))