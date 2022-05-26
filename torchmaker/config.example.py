# General
SAGEMAKER_ROLE = 'TODO'
AWS_SAGEMAKER_SERVERLESS = True
if not AWS_SAGEMAKER_SERVERLESS:
    # serverless deployment does not need a instance type
    AWS_SAGEMAKER_INSTANCE_TYPE = "ml.c4.xlarge"
S3_MODEL_DATA_BUCKET = "TODO"

# CIFAR Model
TRAIN_CIFAR_BATCH_SIZE=8
TRAIN_CIFAR_EPOCHS=4
AWS_SAGEMAKER_CIFAR_ENDPOINT_NAME = "cifar-deployment-test6"
S3_CIFAR_MODEL_DATA_KEY = "DEMO-samples/cifar/model.tar.gz"
S3_CIFAR_MODEL_DATA_PATH = f"s3://{S3_MODEL_DATA_BUCKET}/{S3_CIFAR_MODEL_DATA_KEY}"