data "aws_caller_identity" "current" {}

locals {
  account_id          = data.aws_caller_identity.current.account_id
  ecr_repository_name = "tornado-lambda-container"
  ecr_image_tag       = "latest"
}

resource "aws_ecr_repository" "repo" {
  name = local.ecr_repository_name


  provisioner "local-exec" {
    command = <<EOF
          docker login -u AWS -p $(aws ecr get-login-password --region ${var.region}) |  docker login --username AWS --password-stdin ${local.account_id}.dkr.ecr.${var.region}.amazonaws.com
           cd ..
           docker build -t ${local.ecr_repository_name}:${local.ecr_image_tag} .
           docker push ${local.ecr_repository_name}:${local.ecr_image_tag}
       EOF
  }
}
