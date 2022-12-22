
## Capstone Project-1: Tweet sentiment classification

This project will help businesses to understand their consumers.

Twitter allows businesses to engage personally with consumers. However, there’s so much data on Twitter that it can be hard for brands to prioritize which tweets or mentions to respond to first.

That's why sentiment analysis has become a key instrument in social media marketing strategies.

Sentiment analysis is a tool that automatically monitors emotions in conversations on social media platforms.

##  [Dataset link]([https://www.kaggle.com/competitions/tweet-sentiment-extraction/data])


## Build Directory

```sh
v37k55t5e66pzlg6
├── README.md
├── apis
│   └── openapi.yaml
├── bento.yaml
├── env
│   ├── docker
│   │   ├── Dockerfile
│   │   └── entrypoint.sh
│   └── python
│       ├── install.sh
│       ├── requirements.txt
│       └── version.txt
├── models
│   └── tweet_classification
│       ├── 7bxzvbd47chyflg6
│       │   ├── custom_objects.pkl
│       │   ├── model.yaml
│       │   └── saved_model.pkl
│       └── latest
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
  "text": "Sooo SAD I will miss you here in San Diego!!!"
}'
```

Response:
```sh
{
  "sentiment": "Negative"
}
```


## Instructions to run:

Build bentoml 
```sh
bentoml build
```

Containerize the model
```sh
bentoml containerize tweet_classify:v37k55t5e66pzlg6 --platform linux/amd64
```

Run locally
```sh
docker run -it --rm -p 3000:3000 tweet_classify:v37k55t5e66pzlg6
```

Docker tagging and pushing image to AWS ECR

Docker taggging
```sh
docker tag tweet_classify:v37k55t5e66pzlg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/tweet-classify:latest
```

Pushing image to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/tweet-classify:latest
```

## Deployment in AWS ECS 

https://user-images.githubusercontent.com/34676681/208122028-139b7bc9-256d-4dd9-b248-640dc8be61b4.mov

## AWS configuration 

https://user-images.githubusercontent.com/34676681/208124024-5442a824-060e-4d02-9883-6017a0f75e7b.mov




