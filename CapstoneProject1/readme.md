
## Capstone Project-1: Tweet sentiment classification

This project will help businesses to understand their consumers.

Twitter allows businesses to engage personally with consumers. However, there’s so much data on Twitter that it can be hard for brands to prioritize which tweets or mentions to respond to first.

That's why sentiment analysis has become a key instrument in social media marketing strategies.

Sentiment analysis is a tool that automatically monitors emotions in conversations on social media platforms.

##  [Dataset link]([https://www.kaggle.com/datasets/gabrielsantello/cars-purchase-decision-dataset](https://www.kaggle.com/competitions/tweet-sentiment-extraction))


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
docker tag tweet_classify:v37k55t5e66pzlg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/cars-purchase-decision-clasification:latest
```

Pushing image to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/cars-purchase-decision-clasification:latest
```

## Deployment in AWS ECS 

https://user-images.githubusercontent.com/34676681/200217175-ae1bcfb1-0401-435e-85fc-264ff8be2efb.mov


## AWS configuration 

https://user-images.githubusercontent.com/34676681/200217722-de5b5f3d-afb3-44ea-822f-cd352279c0a8.mov
