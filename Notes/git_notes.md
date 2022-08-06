# SSH keys in Github

## Generate SSH keys
1. Generate ssh keys, go to ```~/.ssh```(if exist) directory and type:

    ```bash
    ssh-keygen -o
    ```

    **Note:** It will generate the ssh keys with default key name  **_id_rsa_** . Using the default name will allow SSH clients to automatically locate the keys so it is strongly recommend you use the default name (simply leave the field blank or fill it with id_rsa).

2. Copy public key:
    
    ```bash
    cat KEY_FILENAME.pub
    ```
    Example:

    ```bash
    cat id_rsa.pub
    ```

## Set SSH key in Github

1. In Github go to **Settings ->  SSH and GPG keys -> New SSH key** 

2. Paste the copied publied key in the Key section and add field the Title section.

