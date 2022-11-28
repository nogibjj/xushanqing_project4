install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py mylib/*.py
deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 103231894850.dkr.ecr.us-east-1.amazonaws.com
	docker build -t ids-proj .
	docker tag ids-proj:latest 103231894850.dkr.ecr.us-east-1.amazonaws.com/fast_food_repository:latest
	docker push 103231894850.dkr.ecr.us-east-1.amazonaws.com/fast_food_repository:latest
