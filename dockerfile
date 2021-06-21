FROM python:3
WORKDIR /app
COPY . .
RUN pip3 install pyyaml

# CMD ["python3", "second_part.py"]
ENTRYPOINT ["python3", "second_part.py"]