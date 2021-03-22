FROM python:3.9.2-alpine3.12

ENV SECRET_KEY=asdq56w4e566+2535!!!!23+465sd6+f5@@@_A_SDPjiwjefionasdf
ENV APP_SETTINGS=config.ProductionConfig
ENV JWT_SECRET_KEY=s897561@#!dfs64FASA423465)asdfsdfijio&%^^%$
ENV DATABASE_URL=sqlite:///FGSH_server_db.db
ENV UPLOAD_FOLDER=../../static/upload_files

WORKDIR /usr/src/application

RUN pip install --upgrade pip

COPY ./requirements/ /usr/src/application/requirements/

RUN pip install --no-cache-dir -r /usr/src/application/requirements/production.txt

COPY ./ /usr/src/application/

RUN python manage.py db init

RUN python manage.py db migrate

RUN python manage.py db upgrade