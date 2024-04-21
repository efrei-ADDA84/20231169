# Utilisation d'un réseau et sous-réseau existants
data "azurerm_virtual_network" "existing_vnet" {
    name                = var.virtual_network_name
    resource_group_name = var.resource_group_name
}

# Utilisation d'un subnet existant 
data "azurerm_subnet" "existing_subnet" {
    name                 = "internal"
    virtual_network_name = data.azurerm_virtual_network.existing_vnet.name
    resource_group_name  = var.resource_group_name
}


# Create a ressource group ====> groupe de ressources déjà existant
data "azurerm_resource_group" "existing_rg" {                                   # data a la place de resource 
    name     = var.resource_group_name              
    # location = var.location                        
}


# Create a network interface 
resource "azurerm_network_interface" "my_terraform_if" {
    name                = "LJ-nic"                                              # nom de l'interface réseau
    location            = var.location
    # resource_group_name = var.resource_group_name
    resource_group_name  = data.azurerm_resource_group.existing_rg.name

    ip_configuration {
        name                          = "internal"     
        subnet_id                     = data.azurerm_subnet.existing_subnet.id
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id          = azurerm_public_ip.my_terraform_public_ip.id
    }
}


# Create a public IP address
resource "azurerm_public_ip" "my_terraform_public_ip" {
    name                 = "LJ-public-ip"                                       # nom de l'adresse IP publique
    location             = var.location
    # resource_group_name  = var.resource_group_name
    resource_group_name  = data.azurerm_resource_group.existing_rg.name
    allocation_method    = "Dynamic"           
}


# Create a virtual machine 
resource "azurerm_linux_virtual_machine" "my_terraform_vm" {
    name                    = "devops-${var.id_efrei}"             
    location                = var.location
    # resource_group_name     = var.resource_group_name
    resource_group_name     = data.azurerm_resource_group.existing_rg.name
    size                    = "Standard_D2s_v3"
    admin_username          = var.admin_username
    network_interface_ids   = [azurerm_network_interface.my_terraform_if.id]
    

    os_disk { 
        name                    = "LJ_os_disk"            # nom du disque OS
        caching                 = "ReadWrite"
        storage_account_type    = "Standard_LRS"          # type de disque géré  
    }

    source_image_reference {
        publisher = "Canonical"
        offer     = "UbuntuServer"
        sku       = "18_04-lts-gen2"                      # OS : Ubuntu 20.04 n'est plus disponible
        version   = "latest"
    }
    
    computer_name  = "devops-${var.id_efrei}"

    admin_ssh_key {
        username   = var.admin_username
        public_key = tls_private_key.tls_key.public_key_openssh
    }

    disable_password_authentication = true

}