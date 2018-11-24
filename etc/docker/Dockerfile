FROM is-object-annotations-transformer/dev 

WORKDIR /opt/is

COPY src/ src
COPY setup.py ./
COPY etc/conf/*.json ./

RUN pip install .

CMD [ "is-object-annotations-transformer" ]