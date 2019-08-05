## How to run wrattler-examples in Jupyterlab via Amazon SageMaker

Amazon SageMaker offers a hosted Jupyterlab platform which can be used to run
wrattler-examples on the cloud.

To try this out:

* Go to the AWS console https://us-east-2.console.aws.amazon.com/console/home and in the "Find Services" box, type SageMaker, then click on "Amazon SageMaker".
* On the left panel, under "Notebook" there should be a link to ```Lifecycle configurations```.  Click on this.
* Click "Create configuration" in the top right, then give your configuration a unique name.
* Paste the following into the "Start notebook" script editor:
```
#!/bin/bash
cd /home/ec2-user/ && git clone https://github.com/wrattler/wrattler-examples && cd wrattler-examples && git checkout sagemaker
cp /home/ec2-user/wrattler-examples/resources/* /home/ec2-user/SageMaker/
export PATH=/home/ec2-user/anaconda3/envs/JupyterSystemEnv/bin:$PATH
/home/ec2-user/anaconda3/bin/conda install nodejs
export CLIENT_URL=https://<SOME_UNIQUE_NOTEBOOK_NAME>.notebook.us-east-2.sagemaker.aws/proxy/8080/wrattler-app.js
jupyter lab clean
cd /home/ec2-user/wrattler-examples/ && jupyter labextension install jupyterlab_wrattler
echo Built jupyterlab_wrattler extension
```
then click "Create configuration".
* On the left hand sidebar, click on "Notebook instances", then click "Create notebook instance" in the top right.
* Give your notebook instance a name, the same as <SOME_UNIQUE_NOTEBOOK_NAME> that you put into the "Start notebook" script in the lifecycle configuration step.
* Click on "Additional configuration", and then select your Lifecycle configuration from the dropdown.
* Leave all other fields at default values, and click "Create notebook instance" at the bottom of the page.
* You should then be able to "Start" your notebook instance.  This will take a few minutes.  When it is done, and the Status is "InService", click "Open Jupyterlab".
* At the bottom of the Jupyterlab launcher window, click on "Terminal".  In the terminal, do:
```
cd wrattler-examples
docker-compose build
docker-compose up
```
* In the left hand window of Jupyterlab (file browser), try double-clicking on any ```.wrattler``` file.  It should launch in a new tab on the main panel.  If after a few seconds this tab is still blank, try reloading the page.