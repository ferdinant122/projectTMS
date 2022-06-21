# Part 1: Flask App runs on Docker 
In this part the Flask App will run on Docker based on the Dcoker image we build

## Installation
### 1. Clone/Fork the git repo and create a virtual environment

on Mac
```
git clone https://github.com/randiltennakoon/flask_k8s.git
cd flask_k8s
pip install virtualenv
virtualenv env
```
### 2. Activate the virtual environment

on Mac
```
source env/bin/activate

OR

. env/bin/activate
```

### 3. Run the application
```
chmod +x build.sh
chmod +x run.sh

./build.sh
./run.sh
```

- [Docker image](https://hub.docker.com/repository/docker/randilt/flask_app)

- Navigate to `localhost:4449` to view the app. You can customize the `app.py` and `templates` as you prefer.

![](https://github.com/randiltennakoon/flask_k8s/blob/run_on_docker/flask_app.png?raw=true)




