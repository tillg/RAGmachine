# A12 Build and Deployment Pipelines

BUILD AND DEPLOYMENT Product Team  

A12 Build and Deployment Pipelines3.7.0

  * 1\. Introduction
  * 2\. Pipeline Overview
    * 2.1. Setup Pipelines
    * 2.2. Deployment Pipelines
    * 2.3. Build Pipeline
    * 2.4. On-Demand Deployment Pipelines
    * 2.5. Cleanup Pipeline
  * 3\. Pipeline Operation

## 1\. Introduction

The A12 Build and Deployment Pipelines are a collection of pre-made Jenkins
pipelines to help you build your application and create deployments on the TPI
dev cluster using the Helm A12 Stack charts.

There are pipelines available to create different environments on the cluster,
as well as pipelines to deploy application specific infrastructure. Pipelines
for building and deploying the application itself to different environments
are also included.

## 2\. Pipeline Overview

There are different strategies how to deploy your application. You can find a
section on general deployment strategies in the [Helm A12 stack charts
documentation on
GetA12](../../../../../../content/2022.06/BUILD_AND_DEPLOYMENT/3/asciidoc/a12-stack/index.html,anchor#_deployment_strategies).

Basically it is about how you want to group your deployment configuration and
if you want to deploy infrastructure and application components individually
or all at once. There are different pipelines supporting different deployment
strategies.

The following picture gives an overview of the provided pipelines and their
results.

![pipeline
overview](../../../../../../static/image/1d40e6eb4bf87d79cfdb495a16266e83bc1c74d0/3f35d65b4b71896355fc7234c578516e/pipelines_overview.png)

The arrows in yellow are the setup pipelines, the arrow in green is the build
pipeline and the arrow in purple is the deployment pipeline.

To keep the image smaller, some setup pipelines have been omitted. For a
complete list, see the table in the next section.

### 2.1. Setup Pipelines

The following table gives an overview over all setup pipelines.

Pipeline | Purpose  
---|---  
CreateEnvironment | Provision an environment on TPI Dev Cluster.  
CreateSecrets | Create secrets in a specific environment.  
DeployDatabase | Deploy Postgres database to a specific environment. This should be used only for development purposes.  
DeploySolr | Deploy Solr to a specific environment.  
DeployHazelcastManagementCenter | Deploy Hazelcast Management Center to a specific environment.  
DeployKeycloak | Deploy Keycloak to a specific environment.  
  
### 2.2. Deployment Pipelines

Actual application deployment is done using the following pipelines.

Pipeline | Purpose  
---|---  
DeployApplication | Deploy an application to a previously provisioned environment on the TPI Dev Cluster containing the infrastructure.  
DeployUmbrella | Provision an environment on TPI Dev Cluster and deploy an application including infrastructure into it.  
  
### 2.3. Build Pipeline

The build pipeline creates Docker images of your application and publishes
these images to a Docker registry. For a successful build of the main branch,
the deployment pipeline is triggered to deploy the application into a testing
environment.

After being deployed, a simple e2e test job will be executed. This is only an
example of how to perform e2e test in your application.

### 2.4. On-Demand Deployment Pipelines

The on-demand pipelines can be used to trigger deployments for testing.

Pipeline | Purpose  
---|---  
DeployOnDemandIndividual | Create infrastructure and deploy an application using multiple deployment pipelines.  
DeployOnDemandUmbrella | Create infrastructure and deploy an application using a single deployment pipeline.  
  
### 2.5. Cleanup Pipeline

The cleanup pipeline is created to support decommissioning an environment.

## 3\. Pipeline Operation

The pipelines themselves are located in

  * [full-stack-project-template (mgm internal only)](https://bitbucket.mgm-tp.com/projects/A12/repos/full-stack-project-template/browse) or your _application repo_ respectively for _Build and Deploy On-Demand Pipeline_.

  * [full-stack-project-deployment-template (mgm internal only)](https://bitbucket.mgm-tp.com/projects/A12/repos/full-stack-project-deployment-template/browse) or your _deployment repo_ respectively for _Setup and Deployment Pipelines_.

The pipelines use the [Helm A12 stack charts (mgm internal
only)](../../../../../../content/2022.06/BUILD_AND_DEPLOYMENT/3/asciidoc/a12-stack/index.html)
to deploy your application and infrastructure using the configuration from the
[full-stack-project-deployment-template](https://bitbucket.mgm-
tp.com/projects/A12/repos/full-stack-project-deployment-template/browse) or
your _deployment repo_ respectively.

To use the pipeline you need to perform the following tasks:

  * Download the template projects (from [Starting with Fullstack Project Template](../../../../../../content/2022.06/OVERALL/202206/asciidoc/fullstack_project_template/index.html#_getting_started))

  * Setup credentials in Jenkins

  * Adapt the pipelines

  * Create Jenkins jobs to use the pipelines

  * Adapt the deployment values

For a complete guide on how to set up the pipelines, please see the
documentation in the [full-stack-project-template (mgm internal
only)](https://bitbucket.mgm-tp.com/projects/A12/repos/full-stack-project-
template/browse/jenkinsPipelines/README.md) and [full-stack-project-
deployment-template (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/full-stack-project-deployment-
template/browse/jenkinsPipelines/README.md).

After having performed all the steps described above, you can go to your
Jenkins instance and deploy your application. The jobs only need a minimal set
of parameters. See the application deployment job as an example below.

![deploy to
environment](../../../../../../static/image/1d40e6eb4bf87d79cfdb495a16266e83bc1c74d0/0f25733b5ae43a571645bfc851034da8/jenkins_deploy_1-deploy-
to-environment.png)

Last updated 2023-01-30 18:14:17 +0100

