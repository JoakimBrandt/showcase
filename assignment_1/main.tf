terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "python_api" {
  name = "python_api:latest"
  keep_locally = false

  build {
    context    = "./python_api"
    tag = ["python_api:latest"]
    label = {
      author: "Joakim" 
    }
  }
}

resource "docker_container" "python_api" {
  image = docker_image.python_api.image_id
  name = "flask_application"
  ports {
    internal = 5000
    external = 5000
  }
}