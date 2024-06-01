
# RLab

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/brij1197/RLab.git
    ```
2. Navigate to the project directory:
    ```bash
    cd RLab
    ```

## Part-1
To run this project, use the below command:
```bash
python3 -m unittest test_matrix_search
```

Or, to run this project using the Dockerfile:
```bash
docker build -t console-app-py .
```
And,
```bash
docker run -it console-app-py
```

## Part-2
To run this project, first we need to install the requirements:
```bash
pip3 install -r requirements.txt
```

Then run the project using the below command:
```bash
python3 main.py
```

Or, to run this project using the Dockerfile:
```bash
docker build -t console-app-py .
```
And,
```bash
docker run -it console-app-py
```
