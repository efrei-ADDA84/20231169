#=================== providers.tf ======================
variable "subscription_id" {
    type        = string
    default     = "765266c6-9a23-4638-af32-dd1e32613047"
}

variable "tenant_id" {
    type        = string
    default     = "413600cf-bd4e-4c7c-8a61-69e73cddf731"
}

#=================== main.tf ======================
variable "location" {
    type        = string
    default     = "francecentral"
    description = "Location of the resource group."
}

variable "resource_group_name" {
    type        = string
    default     = "ADDA84-CTP"
}

variable "virtual_network_name" {
    type        = string
    default     = "network-tp4"
}

variable "id_efrei" {
    type        = number
    default     = 20231169
}

variable "admin_username" {
    type        = string
    default     = "devops"
    description = "The username for the local account that will be created on the new VM."
}

# # 
# variable "resource_group_name_prefix" {
#   type        = string
#   default     = "rg"
#   description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
# }