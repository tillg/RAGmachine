# Helm K8s Ingress System

BUILD AND DEPLOYMENT Product Team  

Helm K8s Ingress System3.7.0

  * 1\. Introduction
  * 2\. Tools Needed
  * 3\. Chart Repo
  * 4\. Usage Examples

## 1\. Introduction

This chart contains basic configuration and usage examples for supported
ingress systems. Currently, only the [NGINX
ingress](https://kubernetes.github.io/ingress-nginx/) is supported.

Documentation of values provided by the NGINX ingress Helm chart can be found
on [GitHub](https://github.com/kubernetes/ingress-
nginx/tree/main/charts/ingress-nginx).

Documentation for custom values added in this chart can be found in [Bitbucket
(mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_k8s-ingress-system/browse/src/main/helm).

## 2\. Tools Needed

For a description of tools, general usage guidelines and handling secrets,
please see the [Helm A12 stack documentation on
GetA12](../../../../../../content/2022.06/BUILD_AND_DEPLOYMENT/3/asciidoc/a12-stack/index.html)

## 3\. Chart Repo

To use this Helm chart you need to add the mgm Artifactory to your Helm repos.

    
    
    helm repo add helm-repos https://artifacts.mgm-tp.com:443/artifactory/helm-repos/ --username <artifactory-user> --password <artifactory-password>
    helm repo update

## 4\. Usage Examples

By default, we use [Using a self-provisioned
edge](https://kubernetes.github.io/ingress-nginx/deploy/baremetal/#using-a-
self-provisioned-edge) for network load balancing. Therefore, the ingress-
nginx service is a NodePort service.

In traditional cloud environments, network load balancers are available on-
demand. To use this chart, you simply have to change the service type in your
`values.yaml` like this:

[examples/values.yaml](../../../../../../static/attachments/3e2d542ce4dbd80ef84effd5e02c8ec3bd9bfff4/ec79ef45d05c35836805f5bb551ff015/values.yaml)

    
    
    ingress-nginx:
      controller:
        service:
          type: "LoadBalancer"

The chart is configured to pull the ingress image from artifactory. You need
to provide credentials for this. Create a `secrets.yaml` with the following
contents:

__ |  Secrets must only be added to a repository in an encrypted way. Follow the instruction in Section 2 for handling secrets.   
---|---  
  
[examples/secrets.yaml](../../../../../../static/attachments/3e2d542ce4dbd80ef84effd5e02c8ec3bd9bfff4/a30f894d7b9dee4be125eb8ff7e0a1db/secrets.yaml)

    
    
    dockerConfigJson:
      username: admin
      password: admin

To deploy the ingress system you can use the following command:

    
    
    helm secrets upgrade ingress-system helm-repos/k8s-ingress-system \
        --install --create-namespace -n ingress-system \
        --kubeconfig /path/to/your/.kube/config \
        -f values.yaml -f secrets.yaml

Last updated 2023-01-30 18:14:17 +0100

