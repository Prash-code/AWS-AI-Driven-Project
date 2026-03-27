from aws.cloudwatch import get_cpu
from aws.ssm import restart_service

def run_tool(tool_name):

    if tool_name == "check_cpu":
        cpu = get_cpu()
        if cpu > 80:
            restart_service()
            return f"CPU high ({cpu}%). Service restarted."
        return f"CPU normal ({cpu}%)"

    if tool_name == "restart_service":
        restart_service()
        return "Service restarted successfully"
