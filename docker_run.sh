pwd=$(pwd)
exec docker run -p 8080:8080 -v $pwd:/app -it yandex-backend python app.py