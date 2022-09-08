.DEFAULT_GOAL := help

instalar-dependencias: ## Instalar dependencias
	pip3.10 install -r requirements.txt

instalar-dependencias-teste: ## Instalar dependencias dos testes
	pip3.10 install -r requirements-test.txt


test: ## Executar testes
	pytest -sv .

run: ## python run app
	python3.10 .

run-docker: ## Executar no docker-compose
	docker-compose up

run-docker-background: ## Executar no docker-compose, detached
	docker-compose up -d

remover-docker: ## Remover docker no docker-compose
	docker-compose down

iniciar-teste-mongo: ## sInicia o mongodb no docker para teste
	docker run -d --rm --name=fastapi_mongodb_teste -p 27017:27017 --tmpfs=/data/db mongo

parar-teste-mongo: ## Parar o mongodb no docker de teste
	docker stop fastapi_mongodb_teste

clean: ## Efetua limpeza de temporarios.
	rm -rf ./.pytest_cache ; rm -rf ./.hypothesis ; rm -rf __pycache__ ; rm -rf ./testes/__pycache__ ; rm -rf ./agenda_api/__pycache__

help: ## Exibir ajuda.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
