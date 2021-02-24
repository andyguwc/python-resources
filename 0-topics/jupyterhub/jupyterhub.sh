##################################################
# jupyterhub basics
##################################################

'''
jupyterhub basics
'''
# https://portworx.com/how-to-deploy-ha-jupyterhub-on-amazon-kubernetes-service/

Runs Jupyter notebook in a multi-tenant model

Stateful workload that depends on a reliable persistence layer

The basic principles of operation are:
The Hub spawns the proxy (in the default JupyterHub configuration).
The proxy forwards all requests to the Hub by default.
The Hub handles login, and spawns single-user notebook servers on demand.
The Hub configures the proxy to forward url prefixes to single-user notebook servers.


##################################################
# jupyterhub on minikub (local dev)
##################################################

# https://minimalist-jupyterhub.readthedocs.io/en/latest/cheat-localdev.html

# https://kienmn97.medium.com/manually-deploy-jupyterhub-on-kubernetes-for-a-single-machine-dbcd9c9e50a4


##################################################
# jupyterhub and k8s
##################################################

'''
Kubernets and Juputerhub statefulness
'''
# https://portworx.com/how-to-deploy-ha-jupyterhub-on-amazon-kubernetes-service/

The JupyterHub platform has three essential components—hub, proxy, and single-user Notebook server. The hub is the heart of the platform that orchestrates the lifecycle of a Notebook. The proxy acts as the front-end to route requests to the hub, which is exposed to the outside world through an HTTP load balancer or in Kubernetes, an ingress controller. When a user logs into the platform, the hub provisions a single-user Notebook instance for them. Each user gets a dedicated instance of the Notebook that is completely isolated from the other users. In Kubernetes, the instance is mapped to a pod.

After a specific period of inactivity, the hub automatically culls the pod associated with the inactive user. When the same user logs in again, the hub schedules a pod that contains the state persisted during the previous session. 

Behind the scenes, JupyterHub creates a persistent volume claim (PVC) and a persistent volume for each user. Even though the pod gets deleted as part of the culling process, the PV is retained, which gets attached to the new pod when an existing user logs in. 

Apart from the dedicated storage required by the common database and each user, JupyterHub also supports shared storage volumes that are available to all the users. This shared storage is used to populate common datasets, files, and other objects that will be available to all users of the system. 

# https://zero-to-jupyterhub.readthedocs.io/en/stable/kubernetes/amazon/step-zero-aws-eks.html


'''
setup EKS in AWS
'''
# https://zero-to-jupyterhub.readthedocs.io/en/stable/kubernetes/amazon/step-zero-aws-eks.html
# https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html

Setup Cluster
- VPC
- IAM role for EKS service role 
    - AmazonEKSClusterPolicy
    - AmazonEKSServicePolicy
    - AmazonEC2ContainerRegistryReadOnly
- Security Group for EKS control plane
- EKS cluster using the IAM role and Security Group defined
- Configure kubectl and iam authenticator to talk to the cluster via CLI

Launch and configure EKS worker nodes

Create a AWS authentication ConfigMap 

Preparing authenticator for Helm


'''
setup Helm
'''
# https://zero-to-jupyterhub.readthedocs.io/en/stable/kubernetes/setup-helm.html
helm is a useful tool for installing, upgrading and managing applications on a k8s cluster

Charts are abstractions describing how to install packages onto a Kubernetes cluster. When a chart is deployed, it works as a templating engine to populate multiple yaml files for package dependencies with the required variables, and then runs kubectl apply to apply the configuration to the resource and install the package.



'''
setup JupyterHub
'''

# https://zero-to-jupyterhub.readthedocs.io/en/stable/jupyterhub/installation.html
source code for helm chart https://github.com/jupyterhub/helm-chart
create config.yaml (these are values overriding the helm templates)

To use JupyterHub, enter the external IP for the proxy-public service in to a browser. JupyterHub is running with a default dummy authenticator so entering any username and password combination will let you enter the hub.

Installation part - run helm upgrade 

helm upgrade --cleanup-on-fail \
  --install $RELEASE jupyterhub/jupyterhub \
  --namespace $NAMESPACE \
  --create-namespace \
  --version=0.10.6 \
  --values config.yaml


'''
customized configurations
'''
# https://zero-to-jupyterhub.readthedocs.io/en/stable/resources/reference.html#helm-chart-configuration-reference
# customize existing docker image
- user environment determined by dockerfile
- set environment variables which affects user specific environment


'''
user storage
'''
# https://zero-to-jupyterhub.readthedocs.io/en/stable/jupyterhub/customizing/user-storage.html
# 10GB hard drive mounted to home directory, everything a user writes to home directory will remain, and else will be reset
# Jupyter lab autosaves files

A PersistentVolumeClaim (PVC) specifies what kind of storage is required. Its configuration is specified in your config.yaml file.

A PersistentVolume (PV) is the actual volume where the user’s data resides. It is created by Kubernetes using details in a PVC.

Next, we need to customize the user environment by passing the appropriate storage configuration. Add the below text to config.yaml.


singleuser:
  storage:
    dynamic:
      storageClass: px-jhub-sc
    extraVolumes:
      - name: jhub-shared
        persistentVolumeClaim:
          claimName: px-jhub-shared-vol
    extraVolumeMounts:
      - name: jhub-shared
        mountPath: /home/shared  
 

Notice that the home directory is taking advantage of dynamic provisioning while the shared volume is based on the PVC created in the previous step. Each time a new user logs in, a PVC and PV are dynamically created for her based on the specified storage class. The shared PVC, px-jhub-shared-vol, is attached to each pod, accessible as the /home/shared directory.


'''
other configs
'''
# synchronize a folder
# use nbgitpuller to synchronize a folder in user's filestystem with a git repo whenever user starts their server

# user profiles
# Each configuration is a set of options for Kubespawner, which defines how Kubernetes should launch a new user server pod. Any configuration options passed to the profileList configuration will overwrite the defaults in Kubespawner (or any configuration you’ve added elsewhere in your helm chart).
# Can also customize user resources

# Expanding and contracting the size of the cluster


'''
Spawner
'''
# https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html
# KubeSpawner
A JupyterHub spawner that spawn pods in a Kubernetes Cluster. Each server spawned by a user will have its own KubeSpawner instance.





##################################################
# jupyterhub and k8s adminstrator
##################################################

'''
admin
'''
# https://zero-to-jupyterhub.readthedocs.io/en/stable/administrator/index.html
setup admin users

'''
authentication and authorization
'''
# https://zero-to-jupyterhub.readthedocs.io/en/stable/administrator/authentication.html
Authentication is about identity, while authorization is about permissions.
All authenticator classes derive from the Authenticator base class

hub:
  config:
    Authenticator:
      admin_users:

# authenticators
OAuth2 based authentication
- github oauth (setup client_id, client_secret, oauth callback, and permit reading profile data


'''
autoscaling
'''
A cluster autoscaler will help add and remove nodes from the cluster
For a node to scale down, it must be free from pods that arent allowed to be disrupted


'''
security
'''
Enabling and disabling network policies
- HTTPS
- Load balancers


'''
tutorials
'''
Good for many users

Super basic walkthrough https://www.youtube.com/watch?v=Mk6ZHVIw0Xs
- create a standard k8s cluster with cpu, memory requirements, and number of nodes
- launch jupyterhub 
 - config.yaml can set up jupyterhub and create users


'''
authentication
'''
# Okta https://subhasisray.medium.com/okta-integration-in-jupyterhub-running-on-kubernetes-cluster-d1eacd5f047b

# Github https://jupyterhub.readthedocs.io/en/stable/reference/config-ghoauth.html










