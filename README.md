# Mini-Project

This project is a proof of concept to build an api and automate its launch

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Setup AWS and user to use aws cli
AWS Account
AWS IAM user with cloudformation cli permission AWSCloudFormationStackSetAdministrationRole
	User could be setup like:  https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html
AWS aws tools configure:  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration

Other dependencies
python and basic knowlege 

### Installing

A step by step series of examples that tell you how to get the api running

Download the project from git

```
git clone https://github.com/davidtacheny/Mini-Project.git
```

run the command  

```
python launchcf.py
```

[1] % python launchcf.py
your cloudformation stack is running waiting 2 min
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    74  100    74    0     0     66      0  0:00:01  0:00:01 --:--:--    66
{
  "message": "Automation for the people",
  "timestamp": 1543514231.0
}
your api url is 'https://seqlbnznli.execute-api.eu-west-1.amazonaws.com'/call

## Running the tests

run a curl to validate the api
curl --request POST api-url
This test is built into the script

## Deployment

This script launches a cloudformation template that installs aws api gateway and a lambda job

## Clean Up

run:
aws cloudformation delete-stack --stack-name cfdtacheny

## TO DO

Do to time constraints I didn't get the python script in perfect python format.  
Add argparse to include delete stack

## Built With

python
aws tools
cloudformation 

## Contributing

Although no code is 100% original, thousands of engineers contributed to building the tools that made this happen
this work has been developed by david tacheny as original code
 
## Versioning

1.0

## Authors

David Tacheny
https://www.linkedin.com/in/davidtacheny/

## Acknowledgments

TekSystems
