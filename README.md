# yandex backend school REST API gift shop

# Все что использовалось
- MongoDB
- flask
- docker, docker-compose
- python3 libraries : numpy, pymongo
# Развертывание на сервере
```
# Установка докера
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo groupadd docker
sudo usermod -aG docker $USER

# Установка docker-compose в контейнере докера
sudo curl -L --fail https://github.com/docker/compose/releases/download/1.24.1/run.sh -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

git clone git@github.com:antikov/yandex-backend-school.git
cd yandex-backend-school
```

# Запуск
```
docker-compose up
```
# Тесты
```
docker run yandex-backend-school python tests/main.py
```