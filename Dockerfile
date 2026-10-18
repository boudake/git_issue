
# Use a Spark image compatible with your cluster
FROM apache/spark:4.2.0-python3

USER root
WORKDIR /opt/app

# Copy the Python project
COPY pyproject.toml ./
COPY src/ ./src/
COPY config/ ./config/

# Install the project and its Python dependencies
RUN python3 -m pip install --no-cache-dir .

# Make the source package available to Python
ENV PYTHONPATH=/opt/app/src

# Submit the application to the existing Spark cluster
CMD ["/opt/spark/bin/spark-submit", \
     "--master", "spark://spark-master:7077", \
     "--conf", "spark.driver.host=ecommerce-job", \
     "--conf", "spark.driver.bindAddress=0.0.0.0", \
     "--conf", "spark.driver.port=7078", \
     "--conf", "spark.blockManager.port=7079", \
     "/opt/app/src/ecommerce_toml/main.py"]
