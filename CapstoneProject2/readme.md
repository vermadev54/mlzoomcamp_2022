
## Capstone Project-1: Ham & Spam Messages Classification

This project will help public to filter spam message.

## Context 
Spam messages are those that are sent to a lot of people without their permission and usually promote products, services, or business opportunities.

The proportion of scam messages among spam has sharply increased in recent times. Scam messages frequently use an alluring or fake deal to trick recipients into providing money or personal information. According to statistics from the Singapore Police Force, over $8 million more was stolen through scams between January and June 2020!

A step toward creating a tool for scam message identification and early scam detection is classifying spam messages.

##  [Dataset link]([https://www.kaggle.com/datasets/muhammadahmedansari/ham-spam-messages-dataset]))


## Build Directory

```sh
.
├── latest
└── mttjgieyrchlblg6
    ├── README.md
    ├── apis
    │   └── openapi.yaml
    ├── bento.yaml
    ├── env
    │   ├── docker
    │   │   ├── Dockerfile
    │   │   └── entrypoint.sh
    │   └── python
    │       ├── install.sh
    │       ├── requirements.txt
    │       └── version.txt
    ├── models
    │   └── spam_classification
    │       ├── 7suybouyqkbdblg6
    │       │   ├── custom_objects.pkl
    │       │   ├── model.yaml
    │       │   └── saved_model.pkl
    │       └── latest
    └── src
        ├── locustfile.py
        ├── notebook.ipynb
        ├── predict.py
        └── train.py
```

## Input/Output
Request :

```sh
curl -X 'POST' \
  'http://localhost:3000/classify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C'\''s apply 08452810075over18'\''s"
}'
```

Response:
```sh
{
  "Message": "Spam"
}
```


## Instructions to run:

Build bentoml 
```sh
bentoml build
```

Containerize the model
```sh
bentoml containerize spam_classify:mttjgieyrchlblg6 --platform linux/amd64
```

Run locally
```sh
docker run -it --rm -p 3000:3000 spam_classify:mttjgieyrchlblg6
```

Docker tagging and pushing image to AWS ECR

Docker taggging
```sh
docker tag spam_classify:mttjgieyrchlblg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/spam_classification:latest
```

Pushing image to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/spam_classification:latest
```

## Deployment in AWS ECS 




## AWS configuration 


