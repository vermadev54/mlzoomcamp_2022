## Midterm Project-1: Cars - Purchase Decision

This project will help any person to buy own car based on there current financial status.

##  [Dataset link](https://www.kaggle.com/datasets/gabrielsantello/cars-purchase-decision-dataset)


## Build Directory

```sh
├── 2qgpa2c54ksl7lg6
│   ├── README.md
│   ├── apis
│   │   └── openapi.yaml
│   ├── bento.yaml
│   ├── env
│   │   ├── docker
│   │   │   ├── Dockerfile
│   │   │   └── entrypoint.sh
│   │   └── python
│   │       ├── install.sh
│   │       ├── requirements.lock.txt
│   │       ├── requirements.txt
│   │       └── version.txt
│   ├── models
│   │   └── cars_purchase_decision_classify
│   │       ├── latest
│   │       └── r7w3ohs54kfo3lg6
│   │           ├── custom_objects.pkl
│   │           ├── model.yaml
│   │           └── saved_model.pkl
│   └── src
│       ├── locustfile.py
│       ├── notebook.ipynb
│       ├── predict.py
│       └── train.py
└── latest
```

## Input/Output
Request :

```sh
curl -X 'POST' \
  'http://localhost:3000/classify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Gender": 1,
  "Age": 35,
  "AnnualSalary": 100000
}'
```

Response:
```sh
{
  "status": "Purchased APPROVED"
}
```


## Instructions to run:

Build bentoml 
```sh
bentoml build
```

Containerize the model
```sh
bentoml containerize cars_purchase_decision_classify:2qgpa2c54ksl7lg6 --platform linux/amd64
```

Run locally
```sh
docker run -it --rm -p 3000:3000 cars_purchase_decision_classify:2qgpa2c54ksl7lg6
```

Docker tagging and pushing image to AWS ECR

Docker taggging
```sh
docker tag cars_purchase_decision_classify:2qgpa2c54ksl7lg6 818606151817.dkr.ecr.us-east-1.amazonaws.com/cars-purchase-decision-clasification:latest
```

Pushing image to AWS ECR
```sh
docker push 818606151817.dkr.ecr.us-east-1.amazonaws.com/cars-purchase-decision-clasification:latest
```

## Deployment in AWS ECS 

https://user-images.githubusercontent.com/34676681/200217175-ae1bcfb1-0401-435e-85fc-264ff8be2efb.mov


## AWS configuration 

https://user-images.githubusercontent.com/34676681/200217722-de5b5f3d-afb3-44ea-822f-cd352279c0a8.mov




