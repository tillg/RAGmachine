# Helm K8s Persistence System

BUILD AND DEPLOYMENT Product Team  

Helm K8s Persistence System3.7.0

  * 1\. Introduction
  * 2\. Tools Needed
  * 3\. Chart Repo
  * 4\. Usage Examples

## 1\. Introduction

This chart contains basic configuration and usage examples for persistence
system using [NFS Subdir External Provisioner](https://github.com/kubernetes-
sigs/nfs-subdir-external-provisioner) chart.

Documentation for custom values added in this chart can be found in [Bitbucket
(mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_k8s-persistence-system/browse/src/main/helm).

## 2\. Tools Needed

For a description of tools, general usage guidelines and handling secrets,
please see the [Helm A12 Stack documentation on
GetA12](../../../../../../content/2022.06/BUILD_AND_DEPLOYMENT/3/asciidoc/a12-stack/index.html#anchor:_tools_needed).

## 3\. Chart Repo

To use this Helm chart, you need to add the mgm Artifactory to your Helm
repos.

    
    
    helm repo add helm-repos https://artifacts.mgm-tp.com:443/artifactory/helm-repos \
        --username <your-artifactory-username> \
        --password <your-artifactory-password>
    helm repo update

## 4\. Usage Examples

__ |  You must already have an NFS Server to be able to use this chart.   
---|---  
  
Before running anything, export `KUBECONFIG` to `/path/to/your/.kube/config`

    
    
    export KUBECONFIG=/path/to/your/.kube/config

After that, you can add a `values.yaml` file to configure some necessary
properties that needed for the deployment of this chart as follows.

[examples/values.yaml](../../../../../../static/attachments/baed61e3925a24d329074425bc71542637d6a99d/5fe311ecaac2532ab218f4babd26fa78/values.yaml)

    
    
    dockerConfigJson:
      username: your-artifactory-username
    
    nfs-subdir-external-provisioner:
      nfs:
        server: your-nfs-server-address
        path: path-to-your-nfs-export-directory

For a full list of configuration options, see the [NFS Subdir External
Provisioner configuration](https://github.com/kubernetes-sigs/nfs-subdir-
external-provisioner/blob/master/charts/nfs-subdir-external-
provisioner/README.md#configuration).

You also need to add the `secrets.yaml` in order to download image of NFS
Subdir External Provisioner from mgm Artifactory. Below is an unencrypted
example of the needed secret.

__ |  Secrets must only be added to a repository in an encrypted way. Follow the instruction in Section 2 for handling secrets.   
---|---  
  
[examples/secrets.yaml](../../../../../../static/attachments/baed61e3925a24d329074425bc71542637d6a99d/5eee362872d133708f38ac7a972c53e5/secrets.yaml)

    
    
    dockerConfigJson:
      password: your-artifactory-password

Finally, you can deploy the chart. The follow example commands will deploy a
release `persistence-system` to a namespace `persistence-system`. If the
namespace is not yet created, helm will also create the namespace for you.

    
    
    helm secrets upgrade persistence-system helm-repos/k8s-persistence-system \
        --install --create-namespace -n persistence-system \
        -f values.yaml \
        -f secrets.yaml

When the commands above run successfully, you can check to see if the storage
class and pod of namespace `persistence-system` are already created. After
that, you are good to go.

Last updated 2023-01-30 18:14:17 +0100

