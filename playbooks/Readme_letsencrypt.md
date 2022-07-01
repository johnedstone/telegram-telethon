### Lets Encyrpt
* Ths playbook uses this approach: [Reference](https://docs.bitnami.com/general/how-to/generate-install-lets-encrypt-ssl/#alternative-approach)
* This playbook will install lego and the cronjobs to renew the Let's Encrypt certs 
* `private_vars.yaml` allows one to use the server certs or Let's Encrypt certs
* Here is the sequence:
    * set ....
    * install_lego: yes
    * use_letsencrypt: no
    * lego_cron_install: yes
    * lego_cron_disable: yes
    * run the playbook
        * The Let's Encrypt certs must then be manually installed the first time for each domain as [described below](#manually-installing)
    * then set ....
    * use_letsencrypt: yes
    * lego_cron_disable: no
    * rerun the playbook: make sure to include at least `--tags prep_geolocation_restapi,lets_encrypt`

* To update lego, simply remove `/opt/bitnami/letsencrypt/apps/lego` and rerun the playbook.
```
sudo rm -i /opt/bitnami/apps/letsencrypt/lego
```

#### <a id=manually-installing></a>Manually installing the Let's Encrypt the first time
See above for the sequence
```
sudo /opt/bitnami/apps/letsencrypt/lego --path /opt/bitnami/apps/letsencrypt --http --http.webroot /opt/bitnami/apps/acme_validation --domains "www.xyz.net"  --email 'johndoe@johndoe.com' run --preferred-chain 'ISRG Root X1'

# After certs are in place, update private_vars.yaml to 'use_letsencrypt: yes' and 'lego_cron_disable: no' and rerun playbook
# This will restart bitnami.service. Check playbook output to confirm the certs are configured correctly

```
<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
