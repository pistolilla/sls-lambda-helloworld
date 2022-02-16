# Serverless Installation
To install Serverless (sls), follow these steps

## General installation
Install nodejs, npm and sls on your local.  
This commands are for Linux:
```
sudo apt install nodejs
sudo npm install -g serverless
```
Confirm installation by running:
```
sls --version
```

## Troubleshooting
### Module npm not found
*npm: command not found*
```
sudo apt-get install npm
```

### Upgrade Node.js
*Error: Serverless Framework v3 does not support Node.js vX.X.X. Please upgrade Node.js to the latest LTS version (v12.13.0 is a minimum supported version)*

```
curl -fsSL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
```