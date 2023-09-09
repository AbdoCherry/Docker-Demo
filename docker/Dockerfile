##############################
#### Multistage - STAGE I ####
##############################

# Specifying our Base Image
FROM python:3.11-slim AS build

# Specifying our working directory
WORKDIR /app

# Copying all the code content, only if .dockerignore exists
COPY src/requirements.txt .

# Installing our python modules
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

##############################
### Multistage - STAGE II ####
##############################

# Final Base Image
FROM python:3.11-slim AS final

# Copying our files from first stage
COPY --from=build /usr/local /usr/local
COPY src/ /app/src/

CMD [ "python3", "app/src/app.py"]