# To set the Azure Provider source and version being used
terraform {
    required_providers {
        azapi = {
            source  = "azure/azapi"
            version = "~>1.5"
        }
        azurerm = {
            source  = "hashicorp/azurerm"
            version = "=3.0.0"
        }
        # random = {
        #     source  = "hashicorp/random"
        #     version = "~>3.0"
        # }
    }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
    features {}

    skip_provider_registration = true   # Pour éviter que Terraform enregistre le provider et télécharge automatiquement des plugins

    subscription_id            = var.subscription_id       
    tenant_id                  = var.tenant_id      
}

# Pour la création de clé ssh
provider "tls" {
  # Version can be specified if necessary
}
