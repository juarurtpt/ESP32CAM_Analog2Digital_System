FROM nikolaik/python-nodejs

WORKDIR /app

COPY /python_backend/requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

RUN npm install -g --unsafe-perm node-red node-red-dashboard

COPY /python_backend/scripts ./scripts

COPY /node_red_flow/main_flow.json ../root/.node-red/flows.json

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libqt5x11extras5

EXPOSE 1880
CMD ["node-red"]
