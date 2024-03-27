# Helm A12 Stack

BUILD AND DEPLOYMENT Product Team  

Helm A12 Stack3.7.0

  * 1\. Introduction
    * 1.1. Chart Overview
    * 1.2. Deployment Strategies
  * 2\. Tools Needed
  * 3\. Chart Repo
    * 3.1. Dependencies
    * 3.2. Umbrella Charts
  * 4\. Requirement Charts
    * 4.1. A12 Secrets
      * 4.1.1. Encryption / Decryption
      * 4.1.2. Deployment
    * 4.2. A12 Infrastructure
      * 4.2.1. Components
        * PostgreSQL
        * Solr and Zookeeper
        * Keycloak
        * Hazelcast Management Center
        * ActiveMQ Artemis Message Broker
      * 4.2.2. Deployment
  * 5\. Application Charts
    * 5.1. A12 Data Services
      * 5.1.1. Single Instance Deployment
      * 5.1.2. Multi Instance Deployment with Initialization
      * 5.1.3. Multi Instance Deployment without using Initialization job
    * 5.2. A12 Workflows and Camunda
    * 5.3. A12 Client
  * 6\. Usage Examples
    * 6.1. Individual charts
      * 6.1.1. A12 Secrets
      * 6.1.2. A12 Infrastructure
      * 6.1.3. A12 Data Services
      * 6.1.4. A12 Workflows and Camunda
      * 6.1.5. A12 Client
    * 6.2. Umbrella chart
  * 7\. Grafana dashboards
  * 8\. Local Cluster for Development
    * 8.1. Tool Suggestions
    * 8.2. Tips and Tricks
  * 9\. Migration instructions
    * 9.1. 3.6.0
      * 9.1.1. New values
        * a12-data-services
        * a12-infrastructure
      * 9.1.2. Deprecation
    * 9.2. 3.2.0
      * 9.2.1. New values
        * a12-infrastructure
        * a12-workflows
    * 9.3. 3.0.0
      * 9.3.1. New values
        * a12-infrastructure
        * a12-data-services
        * a12-workflows
        * a12-client
      * 9.3.2. Breaking changes
        * a12-secrets
        * a12-infrastructure
        * a12-data-services
        * a12-workflows
        * a12-client
    * 9.4. 2.0.0
      * 9.4.1. New values
        * a12-data-services
        * a12-workflows
        * a12-client
      * 9.4.2. Breaking changes
        * a12-data-services
        * a12-workflows
        * a12-client
        * a12-stack
      * 9.4.3. Deprecation
        * a12-stack
        * a12-data-services-solr

## 1\. Introduction

The Helm A12 Stack consists of a collection of Helm charts that aims to be an
out-of-the-box solution to deploy A12 based applications on Kubernetes. The
charts can be separated in two groups. One group consists of common
requirements for the application and the other group consists of charts for
the different parts of the A12 application itself.

It is the goal of the A12 stack charts to enable a deployment of an A12 based
applications including its supporting infrastructure with minimal
configuration effort but giving you the flexibility to adapt to your needs.

### 1.1. Chart Overview

We provide the following application specific charts:

A12 Client (see Section 5.3)

    

A chart to deploy the client for your A12 application

A12 Data Services (see Section 5.1)

    

A chart to deploy Data Services for your A12 application

A12 Workflows (see Section 5.2)

    

A chart to deploy Workflows and Camunda for your A12 application

And we also provide charts to deploy infrastructure required by the
application:

A12 Infrastructure (see Section 4.2)

    

An umbrella chart to provide necessary infrastructure for your A12 application

A12 Secrets (see Section 4.1)

    

A chart to create secrets for your application and infrastructure

![A12 Stack
Overview](../../../../../../static/image/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/fee259bf845f5899e0976aa28a6abf7b/a12-stack_overview.png)

The picture above shows the organization of the charts and the connections
between them. You can see that the a12-infrastructure chart is an umbrella
chart for lots of other third party charts. The blue box with the dotted
outline is no chart of its own but includes all charts for the actual A12
application.

Connections starting at an outer box mean that all the components in the box
have this connection. For example, all A12 application components have a
connection to Keycloak, all application and infrastructure components rely on
secrets generated with the a12-secrets chart.

### 1.2. Deployment Strategies

There are several strategies to deploy your application. You can for example
deploy all of your application and infrastructure components as a single unit,
deploy the infrastructure and application components as two separate units or
deploy each application and infrastructure component individually. Basically
you can group them however you like.

There are some pros and cons to each approach. If you have all of your
deployment description in one place, and you do a one shot deployment, this
may be convenient, but you may also lose track of your changes and may
accidentally mis-configure a deployed component.

Here are the pros and cons summarized for _individual deployment_ :

_Pros:_

  * Small value files are easier to handle

  * Errors can be spotted more easily with individual deployments

_Cons:_

  * Configuration of whole project is spread across different files

  * Configuration changes across different components is more involved

And these are the pros and cons summarized for the _umbrella deployment_ :

_Pros:_

  * Configuration changes of multiple components can be rolled out in a single deployment step

  * For small deployments with not much configuration it may be more convenient to have a single values file

_Cons:_

  * Large configuration files can become hard to handle

  * Deploying changes for many components at once may result in errors that are hard to track down

As your application evolves, the necessity of making changes to every part of
your deployment will decrease, and you will most likely just need to update
single components.

Table 1. Deployment Frequency Chart | Reason for redeployment | Frequency of deployment  
---|---|---  
a12-secrets | when secrets are changed | infrequent  
a12-infrastructure | infrastructure updates or configuration changes | infrequent  
a12-data-services, a12-workflows, a12-client | application updates or configuration changes | depending on development, decreasing with time  
  
We provide usage examples (see Section 6) showing the usage of individual
charts (see Section 6.1) and of an umbrella chart (see Section 6.2). It is up
to you which approach you choose.

## 2\. Tools Needed

To deploy an application using the Helm stack you will need the following
tools:

Tool | Version | Description  
---|---|---  
[Helm](https://helm.sh/) | 3.8.2 | A tool to generate Kubernetes manifests from templates and values  
[helm-secrets plugin](https://github.com/jkroepke/helm-secrets) | 3.13.0 | A plugin that enables helm to use encrypted values  
[SOPS](https://github.com/mozilla/sops/) | 3.7.2 | An editor for encrypted files that is used by helm-secrets  
[GnuPG](https://gnupg.org/) | 2.2.35 (LTS) or 2.3.4 (latest) | OpenPGP's implementation used by SOPS  
  
## 3\. Chart Repo

To use the Helm charts you need to add the mgm Artifactory to your Helm repos.

    
    
    helm repo add helm-repos https://artifacts.mgm-tp.com:443/artifactory/helm-repos --username <artifactory-user> --password <artifactory-password>
    helm repo update

You can use each chart as separate deployment unit, or you can add all charts
to an umbrella chart and deploy them as a whole. You can also group them in
other ways as you see fit.

### 3.1. Dependencies

If you want to use the charts separately there are dependencies between them
which influence the order in which you have to deploy the charts initially.
You don't need to follow this order when upgrading the charts.

![chart
dependencies](../../../../../../static/image/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/eee6e5b7048698587f6e3b91a6192047/chart_dependencies.png)

First you have to deploy the a12-secrets chart, as it will create secrets that
are referenced by the infrastructure and application charts. Then you can
deploy the a12-infrastructure chart which will provide the infrastructure
needed by the application.

You are not required to use the secrets or infrastructure chart but if you
choose not to do so, you will have to provide secrets and infrastructure
yourself and adapt the reference values in the application charts accordingly.

### 3.2. Umbrella Charts

To use more charts for one deployment you need to create an umbrella chart.
For this you have to create a `Chart.yaml` like this:

Make sure to update `LATEST_VERSION` to the latest version. To search for the
helm repo, please refer to [helm search
repo](https://helm.sh/docs/helm/helm_search_repo/).

    
    
    helm search repo helm-repos/a12-data-services
    
    
    apiVersion: v2
    name: projectX
    description: My awesome project
    
    type: application
    
    version: 1.0.0
    
    appVersion: 1.0.0
    
    dependencies:
      - name: a12-secrets
        version: "LATEST_VERSION"
        repository: "@helm-repos"
      - name: a12-infrastructure
        version: "LATEST_VERSION"
        repository: "@helm-repos"
      - name: a12-data-services
        version: "LATEST_VERSION"
        repository: "@helm-repos"
      - name: a12-workflows
        version: "LATEST_VERSION"
        repository: "@helm-repos"
      - name: a12-client
        version: "LATEST_VERSION"
        repository: "@helm-repos"

In the values for your umbrella chart you need to prefix the values with the
chart name in the dependencies, for example:

    
    
    a12-secrets:
        ...
    a12-infrastructure:
        ...
    ...

Below you can see the directory structure of `projectX` which has shared
values and secrets and uses an umbrella chart. Section Section 4.1 goes into
more detail regarding encrypting secrets.

    
    
    projectX
    ├── Chart.yaml
    ├── .sops.yaml
    ├── environments
    │   ├── dev
    │   │   ├── secrets.yaml
    │   │   └── values.yaml
    │   └── test
    │       ├── secrets.yaml
    │       └── values.yaml
    ├── secrets.yaml
    └── values.yaml

To deploy the `dev` environment of `projectX` you would go into the directory
`projectX` and execute:

    
    
    export KUBECONFIG=/path/to/your/.kube/config
    helm secrets upgrade your-release-name . --install \
        -n your-namespace --create-namespace \
        -f values.yaml \
        -f secrets.yaml \
        -f environments/dev/values.yaml \
        -f environments/dev/secrets.yaml

This will update or create a release `your-release-name` in the namespace
`your-namespace` on your Kubernetes cluster. If the namespace does not exist,
helm will create it. Helm will also use the secrets plugin to decrypt any
encrypted value files. If you have equal keys in your value files, files
specified later will take precedence over files earlier in the list.

## 4\. Requirement Charts

__ |  You should always have a look at the `values.yaml` file coming along with a chart to know about the parameters, its default value and its description. This would help you to understand the configurations and extensions of a helm chart.   
---|---  
  
### 4.1. A12 Secrets

The [A12 Secrets Helm chart (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_a12-secrets/browse/src/main/helm) consists of
templates for generating secrets that are referenced by the infrastructure
charts as well as by the application charts. Some secrets are shared by
infrastructure and application, e.g. the PostgreSQL secret will be used in the
infrastructure chart to initialize the DB as well as in the application charts
to connect to the DB.

There are many ways to deal with secrets. You could for example

  * use the [Helm secrets plugin](https://github.com/jkroepke/helm-secrets)

  * use the [Ansible Helm module](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/helm_module.html#ansible-collections-kubernetes-core-helm-module) and [Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)

  * use the [HashiCorp Vault](https://www.vaultproject.io/)

The Helm secrets plugin is used in this documentation, as it is the most
transparent for using encrypted secrets with Helm.

#### 4.1.1. Encryption / Decryption

Secrets must only be added to a repository in an encrypted way. To encrypt
your secrets, you need to create or import a [PGP key](https://gnupg.org/) and
create a file `.sops.yaml` to reference it for using with SOPS or helm-secrets
resp.

    
    
    ---
    creation_rules:
    # Encrypt with PGP (obtan via gpg --list-secret-keys)
    - pgp: '000111122223333444AAAADDDDFFFFGGGG000999'

You can also specify different secrets for different environments of your
project as you can see for example in this directory structure:

    
    
    projectX
    ├── a12-secrets
    │   ├── .sops.yaml
    │   ├── environments
    │   │   ├── dev
    │   │   │   ├── secrets.yaml
    │   │   │   └── env.yaml
    │   │   └── test
    │   │       ├── secrets.yaml
    │   │       └── env.yaml
    │   ├── secrets.yaml
    │   └── values.yaml
    └── a12-infrastructure
    ...

To create encrypted values, you simply create a yaml file containing secret
values and then use the `helm-secrets` plugin to encrypt it. Make sure that
you execute the following command from the directory where you have put the
`.sops.yaml` file. In the example this would be the path
`projectX/a12-secrets`.

    
    
    helm secrets enc environments/dev/secrets.yaml

To decrypt an encrypted file you execute

    
    
    helm secrets dec environments/dev/secrets.yaml

This will create a file `environments/dev/secrets.yaml.dec` containing your
decrypted secrets. Be sure not to add it to version control.

#### 4.1.2. Deployment

These are the minimum secrets you would need to supply when deploying a
minimal application built from the `fullstack-project-template`. Add these
lines to a file `secrets.yaml` and encrypt it:

    
    
    dockerConfigJson:
      username: "your artifactory user"
      password: "your artifactory password"
    postgresql:
      postgres:
        password: "the password for the PostgreSQL user"
      dataServices:
        password: "the password for the Data Services db user"
      camunda:
        password: "the password for the Camunda db user"
    jwt:
      secret: "your JWT secret"
    workflows:
      restClient:
        username: "username for the Workflows RestClient"
        password: "password for the Workflows RestClient"
    camunda:
      restClient:
        username: "username for the Camunda RestClient"
        password: "password for the Camunda RestClient"

Creation of a `dockerconfig.json` file is enabled by default and set to the
mgm artifactory but can be adapted as well. The creation of the PostgreSQL
secret as a whole has to be enabled explicitly as it is turned off by default.
The creation of the Data Services user password and the Camunda user password
within the PostgreSQL secret has to be enabled as well. Also enable generating
a JWT secret and secrets for the Workflows and Camunda RestClient. Add the
following lines to a file `values.yaml`.

    
    
    postgresql:
      enabled: true
      dataServices:
        enabled: true
      camunda:
        enabled: true
    jwt:
      enabled: true
    workflows:
      restClient:
        enabled: true
    camunda:
      restClient:
        enabled: true

To deploy your secrets execute the command below

    
    
    export KUBECONFIG=/path/to/your/.kube/config
    helm secrets upgrade a12-secrets helm-repos/a12-secrets --install \
        -n project-x --create-namespace \
        -f values.yaml \
        -f secrets.yaml

There is a complete list of all configuration values in the [A12 Secrets Helm
chart repository (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_a12-secrets/browse/src/main/helm).

### 4.2. A12 Infrastructure

The [A12 Infrastructure Helm chart (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_a12-infrastructure/browse/src/main/helm) is an
umbrella chart for third party charts. It also includes default values to
deploy necessary infrastructure components with minimal configuration effort.

#### 4.2.1. Components

The components included are:

  * PostgreSQL

  * Solr and Zookeeper

  * Keycloak

  * Hazelcast Management Center

  * ActiveMQ Artemis Message Broker

##### PostgreSQL

The postgres chart that is used for the a12-infrastructure is from bitnami.
You can find a complete list of all available configuration options in the
[Bitnami GitHub
Repository](https://github.com/bitnami/charts/tree/master/bitnami/postgresql).

Since we are also providing an [A12 PostgreSQL image (mgm internal
only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/image_a12-postgresql/browse) we added a few values
regarding this image to the configuration.

##### Solr and Zookeeper

A12 Data Services uses Solr as search index. We use the [Bitnami Solr Helm
chart](https://github.com/bitnami/charts/tree/master/bitnami/solr) to deploy a
single instance Solr server or Solr cloud. For Solr Cloud, you also have to
deploy Zookeeper which we use the [Bitnami Zookeeper Helm
chart](https://github.com/bitnami/charts/tree/master/bitnami/zookeeper) in our
infrastructure chart.

We also provide an [A12 Solr image (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/image_a12-solr/browse) which has the necessary A12
core/collection configuration already included. There are additional
configuration values regarding this image.

##### Keycloak

Keycloak can be used as an identity and access management solution for A12
UAA. For deploying the Keycloak IDP, we created a Helm chart which is
supporting new Quarkus based Keycloak (see [A12 Keycloak chart (mgm internal
only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_a12-keycloak/browse/src/main/helm)).

We also include the [Codecentric Keycloak Helm
chart](https://github.com/codecentric/helm-
charts/tree/master/charts/keycloak). This chart only supports legacy Keycloak
based on Wildfly. Legacy Keycloak support will be discontinued after June
2022.

##### Hazelcast Management Center

A12 Data Services can use Hazelcast as caching solution. The Hazelcast
management center provides insight about the behaviour of your caches. It is
not needed for the Hazelcast caches in Data Services to work. We use the
[Hazelcast Helm
chart](https://github.com/hazelcast/charts/tree/master/stable/hazelcast) to
deploy the management center.

##### ActiveMQ Artemis Message Broker

ActiveMQ Artemis can be deployed as a message broker for setting up the server
for CDDs, please refer to [Compose
Documents](../../../../../../content/2022.06/DATA_SERVICES/34/asciidoc/dataservices-
documentation-src/index.html#_compose_documents) for more details.

#### 4.2.2. Deployment

These are the minimum values you would need to supply when deploying a minimal
application built from the `fullstack-project-template` and having deployed
your secrets using the Section 4.1 chart. Add these lines to a file
`values.yaml` and adapt the domain name to your needs:

    
    
    global:
      cluster:
        domainName: project-x.mgm-tp.com
      keycloak:
        postgresql:
          enabled: false

Except from PostgreSQL, all A12 infrastructure components are disabled by
default. Deploying your infrastructure with these values will spin up a
postgres instance and will create two DBs with user credentials for Data
Services and Camunda.

To deploy the infrastructure just execute

    
    
    export KUBECONFIG=/path/to/your/.kube/config
    helm upgrade a12-infrastructure helm-repos/a12-infrastructure --install \
        -n project-x \
        -f values.yaml

## 5\. Application Charts

An A12 application usually consists of a client application with Data Services
as backend. Optionally, Workflows and Camunda can be attached.

The following section will walk you through the deployment process for an
application built based on the fullstack-project-template including Workflows
and Camunda.

__ |  You should always have a look at the `values.yaml` file coming along with a chart to know about the parameters, its default value and its description. This would help you to understand the configurations and extensions of a helm chart.   
---|---  
  
### 5.1. A12 Data Services

The [A12 Data Services Helm Chart (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_a12-data-services/browse/src/main/helm)
supports you in deploying an A12 Data Services application in a cluster safe
way including initialization of models and documents.

The example below shows the basic usage of the Helm chart values. For a more
complete description of all available values see the link to the repository
above.

#### 5.1.1. Single Instance Deployment

For deploying a single instance of Data Services with documents and models
built into the image, you don't need cluster-safe configuration and
initialization. The values below show some basic configuration, assuming you
have built a project based on the fullstack-project-template. For it to work,
you just need to adapt the `image.repository`, `image.version` and
`global.cluster.domainName` to your needs. This will deploy a single instance
of your Data Services on your Kubernetes cluster.

    
    
    init:
      enabled: false
    
    image:
      repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.projectx/a12-data-services
      version: 1.0.0
    
    configValues:
      clusterSafe: false
    
    additionalEnvVars: |
      - name: SPRING_DATASOURCE_DRIVERCLASSNAME
        value: "org.postgresql.Driver"
      - name: SPRING_JPA_PROPERTIES_HIBERNATE_TEMP_USEJDBCMETADATADEFAULTS
        value: "false"
      - name: SPRING_JPA_DATABASEPLATFORM
        value: "org.hibernate.dialect.PostgreSQL9Dialect"
      - name: SPRING_QUARTZ_PROPERTIES_ORG_QUARTZ_JOBSTORE_DRIVERDELEGATECLASS
        value: "org.quartz.impl.jdbcjobstore.PostgreSQLDelegate"
      - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
        value: "LOCAL"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CLIENT_REST_GENERATEDTOKENEXPIRATIONHEADERNAME
        value: "id_token_expiration"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CONTEXTPATH
        value: "/api"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
        value: "*"
      - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
        value: Authorization
      - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_EXPIRATIONSECONDS
        value: "43200"
    
    uaa:
      enabled: true
      unsecuredUrls: "/actuator/health/**,actuator/prometheus,/api/attachment/thumbnail/**"
    
    ingress:
      enabled: false
    
    sizing:
      replicaCount: 1
    
    solr:
      enabled: true
    
    global:
      cluster:
        domainName: project-x.mgm-tp.com

Save the values above in a file called `values.yaml` and execute the following
command to deploy your Data Services:

    
    
    export KUBECONFIG=/path/to/your/.kube/config
    helm upgrade a12-data-service helm-repos/a12-data-services --install \
        -n project-x \
        -f values.yaml

#### 5.1.2. Multi Instance Deployment with Initialization

If you want to deploy multiple instances of your Data Services, you need to
enable the initialization job and the cluster safe values. The initialization
job takes care of importing models and documents. In the example below, the
models and documents are assumed to be included in the init image. Please
adapt the `init.image.repository`, `init.image.version` , `image.repository`,
`image.version` and `global.cluster.domainName` to your needs.

    
    
    init:
      enabled: true
      dataServices:
        image:
          repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.projectx/a12-data-services-init
          version: 1.0.0
        additionalEnvVars: |
          - name: SPRING_DATASOURCE_DRIVERCLASSNAME
            value: "org.postgresql.Driver"
          - name: SPRING_JPA_DATABASEPLATFORM
            value: "org.hibernate.dialect.PostgreSQL9Dialect"
    
    image:
      repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.projectx/a12-data-services
      version: 1.0.0
    
    configValues:
      clusterSafe: true
    
    additionalEnvVars: |
      - name: SPRING_DATASOURCE_DRIVERCLASSNAME
        value: "org.postgresql.Driver"
      - name: SPRING_JPA_PROPERTIES_HIBERNATE_TEMP_USEJDBCMETADATADEFAULTS
        value: "false"
      - name: SPRING_JPA_DATABASEPLATFORM
        value: "org.hibernate.dialect.PostgreSQL9Dialect"
      - name: SPRING_QUARTZ_PROPERTIES_ORG_QUARTZ_JOBSTORE_DRIVERDELEGATECLASS
        value: "org.quartz.impl.jdbcjobstore.PostgreSQLDelegate"
      - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
        value: "LOCAL"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CLIENT_REST_GENERATEDTOKENEXPIRATIONHEADERNAME
        value: "id_token_expiration"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CONTEXTPATH
        value: "/api"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
        value: "*"
      - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
        value: Authorization
      - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_EXPIRATIONSECONDS
        value: "43200"
    
    uaa:
      enabled: true
      unsecuredUrls: "/actuator/health/**,actuator/prometheus,/api/attachment/thumbnail/**"
    
    ingress:
      enabled: false
    
    sizing:
      replicaCount: 2
    
    solr:
      enabled: true
    
    global:
      cluster:
        domainName: project-x.mgm-tp.com

Save the values above in a file called `values.yaml` and execute the command
below to deploy your Data Services.

    
    
    export KUBECONFIG=/path/to/your/.kube/config
    helm upgrade a12-data-service helm-repos/a12-data-services --install \
        -n project-x \
        -f values.yaml

#### 5.1.3. Multi Instance Deployment without using Initialization job

The data-services chart, by default, uses an initialization job to bootstrap
models and documents. The data-services pods require special privileges to
check if the init job has completed. In some cluster environments, you may not
be allowed to create the RBAC rules necessary for these privileges.

Here, we are demonstrating an alternative method of performing the
initialization of models and documents. For this, you need to deploy data-
services using a two-step approach. First, you have to deploy a single
instance of data-services and disable the cluster-safe settings.

This will cause the data-services container to perform the initialization at
startup. Your project needs to be configured according to the full-stack-
project template, with documents and models included and referenced in the
application's properties.

    
    
    a12-data-services:
    
      init:
        enabled: false
    
      configValues:
        clusterSafe: false
    
      sizing:
        replicaCount: 1
    
      ingress:
        management:
          enabled: true

Then you have to wait for the initialization to be complete. You can do this
by exposing the management endpoint of data-services and checking on its
health.

    
    
    #!/usr/bin/env bash
    
    INIT_TIMEOUT="${INIT_TIMEOUT:-180}"
    
    pattern='"status":"UP"'
    result=''
    count=1
    echo "Waiting for init to finish"
    while [[ $count -le $INIT_TIMEOUT && ! $result =~ $pattern ]]
    do
      result=$(curl --connect-timeout 1 --silent -w '\n%{http_code}\n' http://data-services-mgmt.${NAME_SPACE}.${DOMAIN}/actuator/health)
      echo -n .
      count=$(( $count + 1 ))
      sleep 1
    done
    
    if [[ ! $result =~ $pattern ]]
    then
      echo "A timeout occurred when waiting for init to finish"
      exit 1
    else
      echo "Initialization completed"
      exit 0
    fi

As an alternative, you could also monitor the log output of the data-services
pod for a line containing `Started ServerApplication`.

When the single data-services instance is up, initialization has completed,
and you can deploy multiple instances of data-services with cluster-safe
settings enabled.

    
    
    a12-data-services:
    
      init:
        enabled: false
    
      configValues:
        clusterSafe: true
    
      sizing:
        replicaCount: 2

### 5.2. A12 Workflows and Camunda

The [A12 Workflows Helm chart (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_a12-workflows/browse) supports you in deploying
A12 Workflows and Camunda. The example below shows some minimum values you
would need to deploy Workflows and Camunda built with the fullstack-project-
template. As above, you will have to adapt the values for the images and the
domain name.

    
    
    workflows:
      image:
        repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.projectx/workflows-service
        version: 1.0.0
      additionalEnvVars: |
        - name: MGMTP_A12_WORKFLOWS_CAMUNDASERVICE_URL
          value: "http://a12-workflows-camunda:8080/engine-rest"
        - name: MGMTP_A12_WORKFLOWS_DATASERVICES_URL
          value: "http://a12-data-services-data-services:8080/api"
        - name: MGMTP_A12_WORKFLOWS_QUERY_URL
          value: "http://a12-workflows-camunda:8080/engine-rest/v2/rpc"
        - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
          value: "LOCAL"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CLIENT_REST_UAABASE_URL
          value: "http://a12-workflows-workflows:8080/api"
        - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
          value: "Authorization"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_LOCALCONFIG_USERRESOURCES
          value: "classpath:data/users/admin.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_ACCESSRIGHTSRESOURCE
          value: "classpath:data/roles.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
          value: "*"
    
    camunda:
      image:
        repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.projectx/camunda
        version: 1.0.0
      additionalEnvVars: |
        - name: MGMTP_A12_WORKFLOWS_CAMUNDA_DELEGATES_WORKFLOWSSERVICE_URL
          value: "http://a12-workflows-workflows:8080/api"
        - name: MGMTP_A12_DATASERVICES_CLIENT_CONFIGURATION_BASEURL
          value: "http://a12-data-services-data-services:8080/api"
        - name: MGMTP_A12_DATASERVICES_DOCUMENTS_VALIDATION_PARTIALFORMODELS
          value: "ParallelGatewayProcess"
        - name: MGMTP_A12_DATASERVICES_JSONRPC_ALLOWEDOPERATIONS
          value: "LIST_DOCUMENTS"
        - name: MGMTP_A12_DATASERVICES_JSONRPC_ENABLED
          value: "true"
        - name: MGMTP_A12_WORKFLOWS_CAMUNDA_FILTERING_ENABLED
          value: "true"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CLIENT_REST_AUTHENTICATIONTYPE
          value: "LOCAL"
        - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
          value: "LOCAL"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CLIENT_REST_UAABASE_URL
          value: "http://a12-workflows-workflows:8080/api"
        - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
          value: "Authorization"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_LOCALCONFIG_USERRESOURCES
          value: "classpath:data/users/admin.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_ACCESSRIGHTSRESOURCE
          value: "classpath:data/roles.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
          value: "*"
        - name: MGMTP_A12_DATASERVICES_INITIALIZATION_IMPORT_MODELS_PATH
          value: "classpath:models"
    
    global:
      cluster:
        domainName: project-x.mgm-tp.com

Save the values above in a file called `values.yaml` and execute the following
command to deploy your Workflows and Camunda:

    
    
    export KUBECONFIG=/path/to/your/.kube/config
    helm upgrade a12-workflows helm-repos/a12-workflows --install \
        -n project-x \
        -f values.yaml

### 5.3. A12 Client

The [A12 Client chart (mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_a12-client/browse) supports you in deploying an
A12 Client application. The example below shows some minimum values you would
need to deploy the client built with the fullstack-project-template. As in the
other examples, you will have to adapt the values for the image and the domain
name.

    
    
    image:
      repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.projectx/client
      version: 1.0.0
    ingress:
      additionalAnnotations: |-
        kubernetes.io/ingress.class: nginx
        nginx.ingress.kubernetes.io/configuration-snippet: |
          more_set_headers "Content-Security-Policy: default-src * 'unsafe-inline' 'unsafe-eval'; frame-ancestors 'self'; object-src 'none'; img-src data: 'self'";
        nginx.ingress.kubernetes.io/proxy-body-size: 20m
      workflows:
        enabled: true
        additionalAnnotations: |-
          kubernetes.io/ingress.class: nginx
          nginx.ingress.kubernetes.io/configuration-snippet: |
            more_set_headers "Content-Security-Policy: default-src * 'unsafe-inline' 'unsafe-eval'; frame-ancestors 'self'; object-src 'none'; img-src data: 'self'";
          nginx.ingress.kubernetes.io/proxy-body-size: 20m
          nginx.ingress.kubernetes.io/rewrite-target: /api/$2
      camunda:
        enabled: true
    
    global:
      cluster:
        domainName: project-x.mgm-tp.com

And again save the values above in a file called `values.yaml` and execute the
following command to deploy your Workflows and Camunda:

    
    
    export KUBECONFIG=/path/to/your/.kube/config
    helm upgrade a12-client helm-repos/a12-client --install \
        -n project-x \
        -f values.yaml

## 6\. Usage Examples

In this section, we provide values and secrets examples to deploy prebuilt
`full-stack-project-template` images with two approaches:

  * Deploy charts individually

  * Deploy the whole stack with an umbrella chart

__ |  Please be aware our prebuilt `full-stack-project-template` images are for testing only purpose, `DO NOT` use it on your production.   
---|---  
  
To see all values are available for the chart, please refer to [helm show
values](https://helm.sh/docs/helm/helm_show_values/)

    
    
    helm show values helm-repos/a12-data-services

Before running anything, export `KUBECONFIG` to `/path/to/your/.kube/config`.

    
    
    export KUBECONFIG=/path/to/your/.kube/config

Get the storage class of your cluster, you will need it in later steps.

    
    
    kubectl get storageclasses

### 6.1. Individual charts

#### 6.1.1. A12 Secrets

This is secrets.yaml example.

__ |  Secrets must only be added to a repository in an encrypted way. Follow the instructions in Section 4.1.1.   
---|---  
  
[examples/individual/01-a12-secrets/secrets.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/c861b60808f17bcbdfeb1dd252643628/secrets.yaml)

    
    
    dockerConfigJson:
      password: admin
    
    postgresql:
      postgres:
        password: postgres123
      dataServices:
        password: postgresds
      camunda:
        password: postgresc
    
    hazelcastManagementCenter:
      password: hazelcast13!
    
    jwt:
      secret: OKUCkYrHdZriMULWuAu3IkDrhmQzp8COfn/uokk4KE4=
    
    workflows:
      restClient:
        password: admin
    
    camunda:
      restClient:
        password: admin
    
    mgmtBasicAuth:
      htpasswd: admin:$apr1$ng96daxy$bmdY0ot61jBZb4qmt3MMu1

This is values.yaml example.

[examples/individual/01-a12-secrets/values.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/8d13cea617d061c402a7adfba8680152/values.yaml)

    
    
    dockerConfigJson:
      username: admin
    
    postgresql:
      enabled: true
      dataServices:
        enabled: true
      camunda:
        enabled: true
    
    hazelcastManagementCenter:
      enabled: true
      username: admin
    
    jwt:
      enabled: true
    
    workflows:
      restClient:
        enabled: true
        username: admin
    
    camunda:
      restClient:
        enabled: true
        username: admin
    
    mgmtBasicAuth:
      enabled: true

To deploy, you can use the following command:

    
    
    helm secrets upgrade a12-secrets helm-repos/a12-secrets --install \
        -n project-x --create-namespace \
        -f values.yaml \
        -f secrets.yaml

#### 6.1.2. A12 Infrastructure

This is values.yaml example. You must change `127-0-0-1` to the IP of your
cluster, and `storageClass` to the class of your cluster.

[examples/individual/02-a12-infrastructure/values.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/0a209ce2e52752bc67edf3bee8d68f24/values.yaml)

    
    
    solr:
      enabled: true
      ingress:
        enabled: true
        hostname: "solr.127-0-0-1.nip.io"
        annotations: |-
          kubernetes.io/ingress.class: nginx
          nginx.ingress.kubernetes.io/auth-type: basic
          nginx.ingress.kubernetes.io/auth-secret: a12-secrets-mgmt-basic-auth
          nginx.ingress.kubernetes.io/auth-realm: 'Authentication Required'
    
      cloudEnabled: true
      cloudBootstrap: true
      replicaCount: 1
      persistence:
        storageClass: "nfs-subdir-client"
    
    zookeeper:
      enabled: true
      persistence:
        storageClass: "nfs-subdir-client"
      replicaCount: 1
    
    a12Artemis:
      enabled: true
    
    hazelcast:
      enabled: true
      mancenter:
        enabled: true
        persistence:
          storageClass: "nfs-subdir-client"
      custom:
        mancenter:
          ingress:
            enabled: true
            hosts:
              - "hazelcast.127-0-0-1.nip.io"
    
    postgresql:
      enabled: true
      persistence:
        storageClass: "nfs-subdir-client"
    
    global:
      cluster:
        domainName: 127-0-0-1.nip.io
      dataServices:
        postgresql:
          enabled: true
      camunda:
        postgresql:
          enabled: true

To deploy, you can use the following command:

    
    
    helm upgrade a12-infrastructure helm-repos/a12-infrastructure --install \
        -n project-x \
        -f values.yaml

#### 6.1.3. A12 Data Services

This is values.yaml example. You must change `127-0-0-1` to the IP of your
cluster, and `storageClass` to the class of your cluster.

[examples/individual/03-a12-data-
services/values.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/d0402af7c4bfd6fb11da0cea08a876e5/values.yaml)

    
    
    init:
      enabled: true
      dataServices:
        image:
          repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.bd.test-only-images-full-stack-template/bap-server-init
          version: 2022.02-a3bcb2e-test-only
        additionalEnvVars: |
          - name: SPRING_DATASOURCE_DRIVERCLASSNAME
            value: "org.postgresql.Driver"
          - name: SPRING_JPA_DATABASEPLATFORM
            value: "org.hibernate.dialect.PostgreSQL9Dialect"
    
    image:
      repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.bd.test-only-images-full-stack-template/bap-server
      version: 2022.02-a3bcb2e-test-only
    
    configValues:
      clusterSafe: true
    
    additionalEnvVars: |
      - name: SPRING_DATASOURCE_DRIVERCLASSNAME
        value: "org.postgresql.Driver"
      - name: SPRING_JPA_PROPERTIES_HIBERNATE_TEMP_USEJDBCMETADATADEFAULTS
        value: "false"
      - name: SPRING_JPA_DATABASEPLATFORM
        value: "org.hibernate.dialect.PostgreSQL9Dialect"
      - name: SPRING_QUARTZ_PROPERTIES_ORG_QUARTZ_JOBSTORE_DRIVERDELEGATECLASS
        value: "org.quartz.impl.jdbcjobstore.PostgreSQLDelegate"
      - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
        value: "LOCAL"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CLIENT_REST_GENERATEDTOKENEXPIRATIONHEADERNAME
        value: "id_token_expiration"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CONTEXTPATH
        value: "/api"
      - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
        value: "*"
      - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
        value: Authorization
      - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_EXPIRATIONSECONDS
        value: "43200"
    
    uaa:
      enabled: true
      unsecuredUrls: "/actuator/health/**,actuator/prometheus,/api/attachment/thumbnail/**"
    
    ingress:
      enabled: false
    
    persistence:
      storageClass: nfs-subdir-client
      accessModes: [ "ReadWriteOnce" ]
    
      solr:
        enabled: true
        cloud: true
    
    global:
      cluster:
        domainName: 127-0-0-1.nip.io

To deploy, you can use the following command:

    
    
    helm upgrade a12-data-services helm-repos/a12-data-services --install \
        -n project-x \
        -f values.yaml

Sometimes it might take much longer to deploy on a local cluster due to the
limitation of the computer. It might cause the liveness checking failed, you
might consider increasing the `initialDelaySeconds`.

#### 6.1.4. A12 Workflows and Camunda

This is values.yaml example. You must change `127-0-0-1` to the IP of your
cluster, and `storageClass` to the class of your cluster.

[examples/individual/04-a12-workflows/values.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/e8ce48d366c408dfc4006158ef45f774/values.yaml)

    
    
    workflows:
      image:
        repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.bd.test-only-images-full-stack-template/workflows-service
        version: 2022.02-a3bcb2e-test-only
      additionalEnvVars: |
        - name: MGMTP_A12_WORKFLOWS_CAMUNDASERVICE_URL
          value: "http://a12-workflows-camunda:8080/engine-rest"
        - name: MGMTP_A12_WORKFLOWS_DATASERVICES_URL
          value: "http://a12-data-services-data-services:8080/api"
        - name: MGMTP_A12_WORKFLOWS_QUERY_URL
          value: "http://a12-workflows-camunda:8080/engine-rest/v2/rpc"
        - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
          value: "LOCAL"
        - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
          value: "Authorization"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_LOCALCONFIG_USERRESOURCES
          value: "classpath:data/users/admin.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_ACCESSRIGHTSRESOURCE
          value: "classpath:data/roles.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
          value: "*"
    
    camunda:
      image:
        repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.bd.test-only-images-full-stack-template/camunda
        version: 2022.02-a3bcb2e-test-only
      additionalEnvVars: |
        - name: MGMTP_A12_WORKFLOWS_CAMUNDA_DELEGATES_WORKFLOWSSERVICE_URL
          value: "http://a12-workflows-workflows:8080/workflows/api"
        - name: MGMTP_A12_DATASERVICES_CLIENT_CONFIGURATION_BASEURL
          value: "http://a12-data-services-data-services:8080/api"
        - name: MGMTP_A12_DATASERVICES_DOCUMENTS_VALIDATION_PARTIALFORMODELS
          value: "ParallelGatewayProcess"
        - name: MGMTP_A12_DATASERVICES_JSONRPC_ALLOWEDOPERATIONS
          value: "LIST_DOCUMENTS"
        - name: MGMTP_A12_DATASERVICES_JSONRPC_ENABLED
          value: "true"
        - name: MGMTP_A12_WORKFLOWS_CAMUNDA_FILTERING_ENABLED
          value: "true"
        - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
          value: "LOCAL"
        - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
          value: "Authorization"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_LOCALCONFIG_USERRESOURCES
          value: "classpath:data/users/admin.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_USER_ACCESSRIGHTSRESOURCE
          value: "classpath:data/roles.yaml"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
          value: "*"
        - name: MGMTP_A12_DATASERVICES_INITIALIZATION_IMPORT_MODELS_PATH
          value: "classpath:models"
      solr:
        enabled: true
        cloud: true
    
    global:
      cluster:
        domainName: 127-0-0-1.nip.io

To deploy, you can use the following command:

    
    
    helm upgrade a12-workflows helm-repos/a12-workflows --install \
        -n project-x \
        -f values.yaml

Sometimes it might take much longer to deploy on a local cluster due to the
limitation of the computer. It might cause the liveness checking failed, you
might consider increasing the `initialDelaySeconds`.

#### 6.1.5. A12 Client

This is values.yaml example. You must change `127-0-0-1` to the IP of your
cluster, and `storageClass` to the class of your cluster.

[examples/individual/05-a12-client/values.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/93eba26ea241e64fbf35a5d7beba86ed/values.yaml)

    
    
    image:
      repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.bd.test-only-images-full-stack-template/frontend
      version: 2022.02-a3bcb2e-test-only
    ingress:
      additionalAnnotations: |-
        kubernetes.io/ingress.class: nginx
        nginx.ingress.kubernetes.io/configuration-snippet: |
          more_set_headers "Content-Security-Policy: default-src * 'unsafe-inline' 'unsafe-eval'; frame-ancestors 'self'; object-src 'none'; img-src data: 'self'";
        nginx.ingress.kubernetes.io/proxy-body-size: 20m
      workflows:
        enabled: true
      camunda:
        enabled: true
    
    global:
      cluster:
        domainName: 127-0-0-1.nip.io

To deploy, you can use the following command:

    
    
    helm upgrade a12-client helm-repos/a12-client --install \
        -n project-x \
        -f values.yaml

### 6.2. Umbrella chart

This is secrets.yaml example.

__ |  Secrets must only be added to a repository in an encrypted way. Follow the instructions in Section 4.1.1.   
---|---  
  
[examples/umbrella/secrets.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/312347cf60ed380b2cda6598211522fd/secrets.yaml)

    
    
    a12-secrets:
      dockerConfigJson:
        password: admin
    
      postgresql:
        postgres:
          password: postgres123
        dataServices:
          password: postgresds
        camunda:
          password: postgresc
    
      hazelcastManagementCenter:
        password: hazelcast13!
    
      jwt:
        secret: OKUCkYrHdZriMULWuAu3IkDrhmQzp8COfn/uokk4KE4=
    
      workflows:
        restClient:
          password: admin
    
      camunda:
        restClient:
          password: admin
    
      mgmtBasicAuth:
        htpasswd: admin:$apr1$ng96daxy$bmdY0ot61jBZb4qmt3MMu1
    
      artemis:
        password: admin

This is values.yaml example. You must change `127-0-0-1` to the IP of your
cluster, and `storageClass` to the class of your cluster.

[examples/umbrella/values.yaml](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/ce5fd6dcbffd941ab4082643f770284e/values.yaml)

    
    
    a12-secrets:
      dockerConfigJson:
        username: admin
    
      postgresql:
        enabled: true
        dataServices:
          enabled: true
        camunda:
          enabled: true
    
      hazelcastManagementCenter:
        enabled: true
        username: admin
    
      jwt:
        enabled: true
    
      workflows:
        restClient:
          enabled: true
          username: admin
      camunda:
        restClient:
          enabled: true
          username: admin
    
      mgmtBasicAuth:
        enabled: true
    
      artemis:
        enabled: true
        username: admin
    
    a12-infrastructure:
      solr:
        enabled: true
        ingress:
          enabled: true
          hostname: "solr.127-0-0-1.nip.io"
          annotations: |-
            kubernetes.io/ingress.class: nginx
            nginx.ingress.kubernetes.io/auth-type: basic
            nginx.ingress.kubernetes.io/auth-secret: a12-secrets-mgmt-basic-auth
            nginx.ingress.kubernetes.io/auth-realm: 'Authentication Required'
        cloudEnabled: true
        customInit:
          enabled: true
        persistence:
          storageClass: "nfs-subdir-client"
    
      zookeeper:
        enabled: true
        persistence:
          storageClass: "nfs-subdir-client"
    
      a12Artemis:
        enabled: true
        persistence:
          storageClass: "nfs-subdir-client"
    
      hazelcast:
        enabled: true
        mancenter:
          enabled: true
          persistence:
            storageClass: "nfs-subdir-client"
        custom:
          mancenter:
            ingress:
              enabled: true
              hosts:
                - "hazelcast.127-0-0-1.nip.io"
    
      postgresql:
        enabled: true
        persistence:
          storageClass: "nfs-subdir-client"
    
    a12-data-services:
      init:
        enabled: true
        dataServices:
          image:
            repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.projecttemplate/full-stack-template-test-only/server-init
            version: 2022.06-build00054-SNAPSHOT
          additionalEnvVars: |
            - name: SPRING_DATASOURCE_DRIVERCLASSNAME
              value: "org.postgresql.Driver"
            - name: SPRING_JPA_DATABASEPLATFORM
              value: "org.hibernate.dialect.PostgreSQL9Dialect"
    
      image:
        repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.projecttemplate/full-stack-template-test-only/server
        version: 2022.06-build00054-SNAPSHOT
    
      additionalEnvVars: |
        - name: SPRING_DATASOURCE_DRIVERCLASSNAME
          value: "org.postgresql.Driver"
        - name: SPRING_JPA_PROPERTIES_HIBERNATE_TEMP_USEJDBCMETADATADEFAULTS
          value: "false"
        - name: SPRING_JPA_DATABASEPLATFORM
          value: "org.hibernate.dialect.PostgreSQL9Dialect"
        - name: SPRING_QUARTZ_PROPERTIES_ORG_QUARTZ_JOBSTORE_DRIVERDELEGATECLASS
          value: "org.quartz.impl.jdbcjobstore.PostgreSQLDelegate"
        - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
          value: "LOCAL"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CLIENT_REST_GENERATEDTOKENEXPIRATIONHEADERNAME
          value: "id_token_expiration"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CONTEXTPATH
          value: "/api"
        - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
          value: "*"
        - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
          value: Authorization
        - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_EXPIRATIONSECONDS
          value: "43200"
    
      uaa:
        enabled: true
        unsecuredUrls: "/actuator/health/**,actuator/prometheus,/api/attachment/thumbnail/**"
    
      ingress:
        enabled: false
    
      persistence:
        storageClass: nfs-subdir-client
        accessModes: [ "ReadWriteOnce" ]
    
      solr:
        enabled: true
        cloud: true
    
      cdd:
        dirtyDocuments:
          consumer:
            enabled: true
          producer:
            enabled: true
    
    a12-workflows:
      workflows:
        image:
          repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.projecttemplate/full-stack-template-test-only/workflows-service
          version: 2022.06-build00054-SNAPSHOT
        additionalEnvVars: |
          - name: MGMTP_A12_WORKFLOWS_CAMUNDASERVICE_URL
            value: "http://a12-workflows-camunda:8080/engine-rest"
          - name: MGMTP_A12_WORKFLOWS_DATASERVICES_URL
            value: "http://a12-data-services-data-services:8080/api"
          - name: MGMTP_A12_WORKFLOWS_QUERY_URL
            value: "http://a12-workflows-camunda:8080/engine-rest/v2/rpc"
          - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
            value: "LOCAL"
          - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
            value: "Authorization"
          - name: MGMTP_A12_UAA_AUTHENTICATION_USER_LOCALCONFIG_USERRESOURCES
            value: "classpath:data/users/admin.yaml"
          - name: MGMTP_A12_UAA_AUTHENTICATION_USER_ACCESSRIGHTSRESOURCE
            value: "classpath:data/roles.yaml"
          - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
            value: "*"
    
      camunda:
        image:
          repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.projecttemplate/full-stack-template-test-only/camunda
          version: 2022.06-build00054-SNAPSHOT
        additionalEnvVars: |
          - name: MGMTP_A12_WORKFLOWS_CAMUNDA_DELEGATES_WORKFLOWSSERVICE_URL
            value: "http://a12-workflows-workflows:8080/workflows/api"
          - name: MGMTP_A12_DATASERVICES_CLIENT_CONFIGURATION_BASEURL
            value: "http://a12-data-services-data-services:8080/api"
          - name: MGMTP_A12_DATASERVICES_DOCUMENTS_VALIDATION_PARTIALFORMODELS
            value: "ParallelGatewayProcess"
          - name: MGMTP_A12_DATASERVICES_JSONRPC_ALLOWEDOPERATIONS
            value: "LIST_DOCUMENTS"
          - name: MGMTP_A12_DATASERVICES_JSONRPC_ENABLED
            value: "true"
          - name: MGMTP_A12_WORKFLOWS_CAMUNDA_FILTERING_ENABLED
            value: "true"
          - name: MGMTP_A12_UAA_AUTHENTICATION_TYPES
            value: "LOCAL"
          - name: MGMTP_A12_UAA_AUTHENTICATION_JWT_HEADERNAME
            value: "Authorization"
          - name: MGMTP_A12_UAA_AUTHENTICATION_USER_LOCALCONFIG_USERRESOURCES
            value: "classpath:data/users/admin.yaml"
          - name: MGMTP_A12_UAA_AUTHENTICATION_USER_ACCESSRIGHTSRESOURCE
            value: "classpath:data/roles.yaml"
          - name: MGMTP_A12_UAA_AUTHENTICATION_CORS_ALLOWEDORIGINS
            value: "*"
          - name: MGMTP_A12_DATASERVICES_INITIALIZATION_IMPORT_MODELS_PATH
            value: "classpath:models"
        solr:
          enabled: true
          cloud: true
    
    a12-client:
      image:
        repository: docker-repos.dockerregistry.mgm-tp.com/com.mgmtp.a12.projecttemplate/full-stack-template-test-only/frontend
        version: 2022.06-build00054-SNAPSHOT
      ingress:
        additionalAnnotations: |-
          kubernetes.io/ingress.class: nginx
          nginx.ingress.kubernetes.io/proxy-body-size: 20m
        workflows:
          enabled: true
        camunda:
          enabled: true
    
    global:
      cluster:
        domainName: 127-0-0-1.nip.io
      dataServices:
        postgresql:
          enabled: true
      camunda:
        postgresql:
          enabled: true

To deploy, you can use the following command:

    
    
    helm dependency update
    helm secrets upgrade project-x-umbrella . --install \
        -n project-x-umbrella --create-namespace \
        -f values.yaml \
        -f secrets.yaml

Sometimes it might take much longer to deploy on a local cluster due to the
limitation of the computer. It might cause the liveness checking failed, you
might consider increasing the `initialDelaySeconds`.

## 7\. Grafana dashboards

In order to monitor the A12 based applications deployed in the a12-stack
chart, we have created a pre-configured dashboard. The dashboard in JSON can
be downloaded from the link below for importing into your Grafana application.

  * [Spring Boot applications monitoring dashboard](../../../../../../static/attachments/1d56bcc0695017605ed81d8ebcefdfc6f99e9ad2/be9491e1b27f17e56755d1e86af05318/spring_boot_applications_monitoring.json)

## 8\. Local Cluster for Development

### 8.1. Tool Suggestions

For local development purpose, you might want to have your own cluster to play
around with the provided charts and examples from A12 Build and Deployment
team. Furthermore, you can use this for running your developed applications
and many other components.

We have tested several tools and would suggest using
[minikube](https://minikube.sigs.k8s.io/docs/) as a good candidate because

  * Easy to set up on local machine with good documentation

  * Supports multi-platform (Linux, macOS, Windows)

  * [Addons](https://minikube.sigs.k8s.io/docs/handbook/deploying/#addons) with the ability to enable `nginx` ingress out-of-the-box

**A12 stack** charts can run normally on a standard `minikube` cluster.
Obviously, the speed of deployment and running application cannot be
comparable to a dedicated cluster. However, it would provide you a minimal
viable environment to quickly test your deployment script.

### 8.2. Tips and Tricks

Below are with some helpful notes for you to speed up your development speed
as well as being aware of some common issues that might happen during your
daily work.

  * Update `storageClass` in persistence block of all the charts to the available/desire storage class you want to use in the cluster. If you use **minikube** (v1.26.1), the default storage class would be `standard`.

  * Enable nginx ingress addon in `minikube` and follow the instruction to tunnel access to your application in the browser.

  * Adjust `resources` request in your component to the available resource on your local cluster.

  * Adjust the `livenessProbe.initialDelaySeconds` so that it could wait for the application to be started before performing liveness check-up, especially the ones that may take time to boot up like `data-services` or `workflows-camunda`.

## 9\. Migration instructions

Below you can find tables with values that have changed with each respective
chart version. The changes are described in respect of the preceding chart
version.

### 9.1. 3.6.0

#### 9.1.1. New values

##### a12-data-services

New value | Remarks  
---|---  
cdd.dirtyDocuments.async.enabled | Enable asynchronous processing of dirty document  
cdd.dirtyDocuments.consumer.enabled | Enable/disable CDD dirty documents consumer  
cdd.dirtyDocuments.queueName | Name of the JMS queue for dirty documents targeted for reindexing the CDDs  
cdd.dirtyDocuments.producer.enabled | Enable/disable CDD dirty documents producer  
cdd.artemis.enabled | Enable using Artemis as message broker in Data Services  
cdd.artemis.mode | Mode in which Artemis can operate  
cdd.artemis.url | URL to connect to external message broker service  
cdd.artemis.secret.name | Specifies the secrets name to use for Artemis admin user  
cdd.artemis.secret.usernameKey | Specifies the admin username key name in secrets  
cdd.artemis.secret.password | Specifies the admin password key name in secrets  
cdd.modelReadonlyAfterStartUp.enabled | Enable/disable compose document model readonly after startup  
cdd.solr.collectionName | Collection name of CDD search service  
cdd.solr.urls | List of URLs to remote solr server(s). If not in cloud mode, only the first URL will be considered  
  
##### a12-infrastructure

New value | Remarks  
---|---  
a12Artemis.enabled | New value to enable ActiveMQ Artemis  
  
#### 9.1.2. Deprecation

a12-keycloak chart is now deprecated and will be removed in version 4.0.0.
Please use ``keycloakBitnami`` instead

### 9.2. 3.2.0

#### 9.2.1. New values

##### a12-infrastructure

New value | Remarks  
---|---  
a12Keycloak.enabled | New value to enable Quarkus based Keycloak  
  
##### a12-workflows

New value | Remarks  
---|---  
workflows.contextPath | New value for setting workflows context path, set to `/workflows` by default  
  
### 9.3. 3.0.0

#### 9.3.1. New values

##### a12-infrastructure

New value | Remarks  
---|---  
nameOverride | override for chart specific Kubernetes object names  
global.secrets.name | previously hard coded  
  
##### a12-data-services

New value | Remarks  
---|---  
ingress.additionalAnnotations | additional possibility to configure ingress  
ingress.management.additionalAnnotations | additional possibility to configure ingress  
init.dataServices.envVarsFromConfigMap.useDefault | environments variables have been moved to ConfigMap  
init.dataServices.envVarsFromConfigMap.customConfigMapName | custom ConfigMap can be used for environment variables  
init.dataServices.attachments.temporaryPath | previously hard coded  
init.dataServices.attachments.storagePath | previously hard coded  
init.dataServices.modelsPath | previously hard coded  
init.dataServices.documentsPath | previously hard coded  
attachments.temporaryPath | previously hard coded  
attachments.storagePath | previously hard coded  
configValues.envVarsFromConfigMap.useDefault | environments variables have been moved to ConfigMap  
configValues.envVarsFromConfigMap.customConfigMapName | custom ConfigMap can be used for environment variables  
global.secrets.name | previously hard coded  
global.infrastructure.name | previously hard coded  
  
##### a12-workflows

New value | Remarks  
---|---  
workflows.actuatorConfig.enabled | actuator config analogous to data-services chart  
workflows.actuatorConfig.basePath | actuator config analogous to data-services chart  
workflows.actuatorConfig.probeEndpointsEnabled | actuator config analogous to data-services chart  
workflows.actuatorConfig.prometheusEndpointEnabled | actuator config analogous to data-services chart  
workflows.actuatorConfig.exposeEndpoints | actuator config analogous to data-services chart  
workflows.serviceMonitor.enabled | ServiceMonitor config analogous to data-services chart  
workflows.serviceMonitor.endpoint.path | ServiceMonitor config analogous to data-services chart  
workflows.serviceMonitor.endpoint.port | ServiceMonitor config analogous to data-services chart  
workflows.serviceMonitor.endpoint.extraFields | ServiceMonitor config analogous to data-services chart  
workflows.serviceMonitor.extraFields | ServiceMonitor config analogous to data-services chart  
workflows.ingress.backend.additionalAnnotations | additional possibility to configure ingress  
workflows.ingress.management.additionalAnnotations | additional possibility to configure ingress  
workflows.uaa.unsecuredUrls | previously hard coded  
workflows.envVarsFromConfigMap.useDefault | environments variables have been moved to ConfigMap  
workflows.envVarsFromConfigMap.customConfigMapName | custom ConfigMap can be used for environment variables  
camunda.actuatorConfig.enabled | actuator config analogous to data-services chart  
camunda.actuatorConfig.basePath | actuator config analogous to data-services chart  
camunda.actuatorConfig.probeEndpointsEnabled | actuator config analogous to data-services chart  
camunda.actuatorConfig.prometheusEndpointEnabled | actuator config analogous to data-services chart  
camunda.actuatorConfig.exposeEndpoints | actuator config analogous to data-services chart  
camunda.serviceMonitor.enabled | ServiceMonitor config analogous to data-services chart  
camunda.serviceMonitor.endpoint.path | ServiceMonitor config analogous to data-services chart  
camunda.serviceMonitor.endpoint.port | ServiceMonitor config analogous to data-services chart  
camunda.serviceMonitor.endpoint.extraFields | ServiceMonitor config analogous to data-services chart  
camunda.serviceMonitor.extraFields | ServiceMonitor config analogous to data-services chart  
camunda.ingress.webApps.additionalAnnotations | possibility to configure ingress  
camunda.ingress.management.additionalAnnotations | additional possibility to configure ingress  
camunda.uaa.unsecuredUrls | previously hard coded  
camunda.uaa.jwt.secret.name | previously hard coded  
camunda.uaa.jwt.secret.key | previously hard coded  
camunda.envVarsFromConfigMap.useDefault | environments variables have been moved to ConfigMap  
camunda.envVarsFromConfigMap.customConfigMapName | custom ConfigMap can be used for environment variables  
global.secrets.name | previously hard coded  
global.infrastructure.name | previously hard coded  
  
##### a12-client

New value | Remarks  
---|---  
sizing.requests.memory | sizing requests analogous to other Helm charts  
sizing.requests.cpu | sizing requests analogous to other Helm charts  
sizing.limits.memory | sizing requests analogous to other Helm charts  
sizing.limits.cpu | sizing requests analogous to other Helm charts  
ingress.default.additionalAnnotations | possibility to configure ingress  
ingress.workflows.additionalAnnotations | possibility to configure ingress  
  
#### 9.3.2. Breaking changes

##### a12-secrets

Old value | New value | Remarks  
---|---|---  
postgresql.data-services | postgresql.dataServices | renamed  
data-services | dataServices | renamed  
  
##### a12-infrastructure

Old value | New value | Remarks  
---|---|---  
global.data-services.releaseName | global.dataServices.name | renamed  
  
##### a12-data-services

Old value | New value | Remarks  
---|---|---  
enabled | - | removed, no use  
init.data-services | init.dataServices | renamed  
servicemonitor | serviceMonitor | renamed  
global.cluster.domainname | global.cluster.domainName | renamed  
  
##### a12-workflows

Old value | New value | Remarks  
---|---|---  
enabled | - | removed, no use  
workflows.data-services | workflows.dataServices | renamed  
workflows.uaa.authentication.type | workflows.uaa.authentication.types | renamed  
ingress.webApps.contentSecurityPolicy | - | removed in favor of additionalAnnotations  
global.cluster.domainname | global.cluster.domainName | renamed  
global.data-services.releaseName | global.dataServices.name | renamed  
  
##### a12-client

Old value | New value | Remarks  
---|---|---  
enabled | - | removed, no use  
name | nameOverride | renamed  
ingress.default.contentSecurityPolicy | - | removed in favor of additionalAnnotations  
global.domainname | global.domainName | renamed  
global.data-services.releaseName | global.dataServices.name | renamed  
global.workflows.releaseName | global.workflows.name | renamed  
  
### 9.4. 2.0.0

#### 9.4.1. New values

##### a12-data-services

New value | Remarks  
---|---  
init.images | Docker images needed for initialization  
init.models | models initialization config  
init.documents | documents initialization config  
restClient | data-services REST client config  
uaa.unsecuredUrls | unsecured URLs needed for probes  
uaa.jwt.secret | reference to a12-secrets  
uaa.restClient | UAA REST client config  
configValues.clusterSafe | cluster safe data-services configuration  
configValues.heap | Java heap config  
configValues.jmx | JMX connectivity configuration  
configValues.actuatorConfig | Spring Boot actuator configuration  
database.connectionURI | one URI for self deployed or external DB, default value set to a12-infrastructure deployed postgres  
database.secret | reference to password secret for data-services postgres user, default value set to a12-secrets deployed postgres secret  
solr.enabled | enable solr specific environment variables  
solr.cloud | set solr environment variables to use solr cloud or single instance  
solr.urls | URL for solr service, default value set to a12-infrastructure deployed solr  
  
##### a12-workflows

New value | Remarks  
---|---  
workflows.javaOpts | Java options to be given at container startup  
workflows.heap | Java heap config  
workflows.jmx | JMX connectivity configuration  
workflows.additionalVolumeMounts | Kubernetes volume mounts  
workflows.additionalVolumes | Kubernetes volumes  
workflows.restClient | data-services REST client config  
workflows.uaa.jwt.secret | reference to a12-secrets  
workflows.uaa.authentication | UAA auth config  
workflows.uaa.restClient | UAA REST client config  
camunda.javaOpts | Java options to be given at container startup  
camunda.heap | Java heap config  
camunda.jmx | JMX connectivity configuration  
camunda.webApps.contentSecurityPolicy | CSP for camunda webapps ingress  
camunda.database.connectionURI | one URI for self deployed or external DB, default value set to a12-infrastructure deployed postgres  
camunda.database.secret | reference to password secret for data-services postgres user, default value set to a12-secrets deployed postgres secret  
camunda.restClient | data-services REST client config  
camunda.uaa.restClient | UAA REST client config  
global.data-services.releaseName | needed for generating references to data-services service  
  
##### a12-client

New value | Remarks  
---|---  
uaa.keycloak.url | URL of keycloak instance  
global.data-services.releaseName | needed for generating references to data-services service  
global.workflows.releaseName | needed for generating references to workflows and camunda service  
  
#### 9.4.2. Breaking changes

##### a12-data-services

Old value | New value | New value in another chart | Remarks  
---|---|---|---  
ingress.basicAuth | - | - | removed  
init.bapserver | init.data-services | - | renamed  
init.database | - | - | removed, use database  
init.solr | - | - | removed  
init.keycloak | - | - | removed  
uaa.oauth2.springProfile | - | - | to be set explicitly in configValues.springProfiles  
image.pullSecret | - | a12-secrets.dockerConfigJson | moved to a12-secrets chart  
configValues.jwtSecret | - | a12-secrets.jwt.secret | moved to a12-secrets chart  
postgresql | - | a12-infrastructure.postgresql | moved to a12-infrastructure chart  
database.enabled | - | - | removed  
database.external | - | - | removed  
database.external.username | database.username | - | renamed  
database.admin.password | - | a12-secrets.postgresql.postgres.password | moved to a12-secrets chart  
database.user.password | - | a12-secrets.postgresql.data-services.password | moved to a12-secrets chart  
a12-data-services-solr | - | a12-infrastructure.solr | moved to a12-infrastructure chart, a12-data-services solr chart was deprecated in favor of bitnami solr chart  
hazelcastcluster | hazelcast | - | renamed  
hazelcastcluster.springProfile | - | - | to be set explicitly in configValues.springProfiles  
hazelcastcluster.mancenter | - | a12-secrets.hazelcastManagementCenter | moved to a12-secrets  
hazelcast | - | a12-infrastructure.hazelcast | moved to a12-infrastructure  
  
##### a12-workflows

Old value | New value | New value in another chart | Remarks  
---|---|---|---  
workflows.bapserver | workflows.data-services | - | renamed  
workflows.ingress.frontend | - | a12-client.ingress.workflows | moved to a12-client  
workflows.ingress.backend.basicAuth | - | - | removed  
camunda.serviceName | - | - | removed  
camunda.ingress.restApi | - | a12-client.ingress.camunda | moved to a12-client  
camunda.ingress.webApps.basicAuth | - | - | removed  
camunda.database.enabled | - | - | removed  
camunda.database.external | - | - | removed  
camunda.database.external.username | camunda.database.username | - | renamed  
camunda.database.admin.password | - | a12-secrets.postgresql.postgres.password | moved to a12-secrets chart  
camunda.database.user.password | - | a12-secrets.postgresql.camunda.password | moved to a12-secrets chart  
image.pullSecret | - | a12-secrets.dockerConfigJson | moved to a12-secrets chart  
postgresql | - | a12-infrastructure.postgresql | moved to a12-infrastructure chart  
  
##### a12-client

Old value | New value | Value in another chart | Remarks  
---|---|---|---  
ingress.api.host | - | - | removed  
ingress.api.basicAuth | - | - | removed  
- | ingress.workflows | a12-workflows.workflows.ingress.frontend | moved from a12-workflows  
- | ingress.camunda | a12-workflows.camunda.ingress.restApi | moved from a12-workflows  
image.pullSecret | - | a12-secrets.dockerConfigJson | moved to a12-secrets chart  
  
##### a12-stack

Old value | New value in another chart | Remarks  
---|---|---  
imageCredentials | a12-secrets.dockerConfigJson | moved to a12-secrets  
keycloak | a12-infrastructure.keycloak | moved to a12-infrastructure  
realmFile | a12-secrets.keycloak.realmSecret.json | moved to a12-secrets  
basicAuth | a12-secrets.mgmtBasicAuth | moved to a12-secrets  
tls | a12-secrets.tls | moved to a12-secrets  
global.prometheus_enabled | - | removed  
  
#### 9.4.3. Deprecation

##### a12-stack

The a12-stack umbrella chart has been deprecated. Configuration values have
been moved to other charts (see previous section).

##### a12-data-services-solr

Deprecated in favor of bitnami solr chart. Configuration is done in the
a12-infrastructure chart.

Last updated 2023-01-30 18:15:14 +0100

