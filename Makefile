install:
	pip install -r requirements.txt
	python -m textblob.download_corpora
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py
test:
	python -m pytest -vv --cov=mylib --cov=main tests/test_*.py
build:
	docker build -t deploy-python-microservice .
run:
	docker stop python-microservice-container
	docker rm python-microservice-container
	docker run -p 127.0.0.1:8080:8080 -d -it --name=python-microservice-container deploy-python-microservice
deploy:
	aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 260074246793.dkr.ecr.ap-south-1.amazonaws.com
	docker build -t fastapi-wiki .
	docker tag fastapi-wiki:latest 260074246793.dkr.ecr.ap-south-1.amazonaws.com/fastapi-wiki:latest
	docker push 260074246793.dkr.ecr.ap-south-1.amazonaws.com/fastapi-wiki:latest
all: install lint test deploy