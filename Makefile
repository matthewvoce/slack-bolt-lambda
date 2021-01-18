# Makefile
deploy:
	pip3 install --upgrade -r requirements.txt
	rm -rf slack-bolt-lambda.zip
	rm -rf slack-bolt-lambda
	rm -rf vendor/*
	mkdir -p vendor/slack_bolt && cp -pr /usr/local/lib/python3.9/site-packages/slack_bolt/* vendor/slack_bolt/
	mkdir -p vendor/slack_sdk && cp -pr /usr/local/lib/python3.9/site-packages/slack_sdk/* vendor/slack_sdk/
	@zip -r slack-bolt-lambda.zip . -x "*.git*" -x "*.DS_Store*" -x "*.env*" -x "*.vscode*" -x "*Readme.md*" -x "*requirement.txt*" -x "*Makefile*"