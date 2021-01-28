import logging
import sys

# -----------------------------------------------------------------
# Prefix 'vendor' to path for local modules
sys.path.insert(1, "vendor")
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
# -----------------------------------------------------------------

# Process_before_response must be True when running on FaaS
app = App(process_before_response=True)

## Write slack bolt functions here
# This will match any message that contains 👋
@app.message(":wave:")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>!")

SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)


def handler(event, context):
    # Visit the logs in cloudwatch for this project
    for key, value in event.items():
        if key == "body":
            print(f"[SLACK MESSAGE BODY]: {value}")
            # Return challenge for authentication with slack
            if "challenge" in value:
                return value

    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)
