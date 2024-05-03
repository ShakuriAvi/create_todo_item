FROM public.ecr.aws/lambda/python:3.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["/app/my_lambda_function.lambda_handler"]
