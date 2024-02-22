# Terraform

This project is orchestrated by Terraform in a local environment. The only local provider used is the Docker resource, obtained from the Terraform registry.

**How to launch with Terraform**

1. Make sure that you have Terraform installed locally (alongside the CLI)
2. In a terminal, start with initializing the project with `terraform init`
3. Once the project is initialized, you can run the terraform apply with <br>`terraform apply --auto-approve` (or do it in segments of `terraform plan`, `terraform apply`, `yes`)
4. Once terraform has provisioned all the infrastructure, you can head on over to Postman or use a cURL command


### **Postman** <br>
Use Postman to send a POST request to the following, local, address once Terraform has initialized the docker container:
http://127.0.0.1:5000/uppercase

Please attach a raw body in JSON, example:
```
{
    "message": "I am extremely grateful for your services."
}
```

Response example:

```
{
    "data": "I AM EXTREMELY GRATEFUL FOR YOUR SERVICES.",
    "error": null,
    "status_code": 200
}
```

### **cURL** <br>
```
curl --location 'http://127.0.0.1:5000/uppercase' \
--header 'Content-Type: application/json' \
--data '{
    "message": "I am extremely grateful for your services."
}'
```