# Helm K8s Monitoring System

BUILD AND DEPLOYMENT Product Team  

Helm K8s Monitoring System3.7.0

  * 1\. Introduction
  * 2\. Tools Needed
  * 3\. Chart Repo
  * 4\. Usage Examples
    * 4.1. Minimal
    * 4.2. Alerting configuration
      * Grafana Email Configuration
      * Alertmanager Email configuration

## 1\. Introduction

This chart contains basic configuration and usage examples for logging and
monitoring system.

  * [Grafana Loki](https://grafana.com/oss/loki/) and [Promtail](https://grafana.com/docs/loki/latest/clients/promtail/) are used for logging.

  * [Prometheus](https://prometheus.io/) and [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) are used for monitoring.

Documentation of values provided by:

  * kube-prometheus-stack Helm chart can be found on [GitHub](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack).

  * Loki Helm chart can be found on [GitHub](https://github.com/grafana/helm-charts/tree/main/charts/loki).

  * Promtail Helm chart can be found on [GitHub](https://github.com/grafana/helm-charts/tree/main/charts/promtail).

Documentation for custom values added in this chart can be found in [Bitbucket
(mgm internal only)](https://bitbucket.mgm-
tp.com/projects/A12/repos/helm_k8s-monitoring-system/browse/src/main/helm).

## 2\. Tools Needed

For a description of tools, general usage guidelines and handling secrets,
please see the [Helm A12 stack documentation on
GetA12](../../../../../../content/2022.06/BUILD_AND_DEPLOYMENT/3/asciidoc/a12-stack/index.html)

## 3\. Chart Repo

To use this Helm chart you need to add the mgm Artifactory to your Helm repos.

    
    
    helm repo add helm-repos https://artifacts.mgm-tp.com:443/artifactory/helm-repos --username <artfiactory-user> --password <artifactory-password>
    helm repo update

## 4\. Usage Examples

Before running anything, export `KUBECONFIG` to `/path/to/your/.kube/config`

    
    
    export KUBECONFIG=/path/to/your/.kube/config

#### 4.1. Minimal

This is `secrets.yaml` example.

__ |  Secrets must only be added to a repository in an encrypted way. Follow the instruction in Section 2 for handling secrets.   
---|---  
  
[examples/minimal_secrets.yaml](../../../../../../static/attachments/71974d530a9f664bb29172b832ebaa9adf97d174/e504abb5a1e7c6965d23daffbbc68381/minimal_secrets.yaml)

    
    
    dockerConfigJson:
      username: admin
      password: admin
    
    grafanaCredentials:
      username: admin
      password: admin

To deploy, you can use the following command:

    
    
    helm secrets upgrade monitoring-system helm-repos/k8s-monitoring-system \
        --install --create-namespace -n monitoring-system \
        -f secrets.yaml

#### 4.2. Alerting configuration

##### Grafana Email Configuration

To send alerts in Grafana you need to provide smtp configuration in
grafana.ini. See the following example on how to do this in your values:

    
    
    kube-prometheus-stack:
      grafana:
        grafana.ini:
          smtp:
            enabled: true
            host: some.smtp.server:25
            user: alerting@your-service.com
            password: some_password
            from_address: "alerting@your-service.com"
            from_name: "Grafana Alert"

The password should be added to an encrypted values file.

For a full list of configuration options see the [Grafana configuration
documentation](https://grafana.com/docs/grafana/latest/administration/configuration/).

Your alert rules can be configured in the Grafana UI then.

##### Alertmanager Email configuration

The kube-prometheus-stack already defines a lot of alerting rules in
Prometheus which are then sent to Alertmanager.

To be notified when an alert is fired you need to provide configuration for
your receivers.

See the following example on how to define receivers in your values:

    
    
    kube-prometheus-stack:
      alertmanager:
        config:
          global:
            smtp_from: "alertmanager <alerting@your-product.com>"
            smtp_smarthost: your.smtp.host:25
            smtp_auth_username: alerting@your-product.com
            smtp_auth_password: some_smtp_password
          route:
            group_by:
              - severity
            group_wait: 30s
            group_interval: 5m
            repeat_interval: 4h
            receiver: email
            routes:
              - matchers:
                  - alertname="Watchdog"
                receiver: email
          receivers:
          - name: email
            email_configs:
            - to: "Alert Receiver <alert.receiver@your-product.com>"

The password should be added to an encrypted secrets file.

For a full list of configuration options see the [Alertmanager configuration
documentation](https://prometheus.io/docs/alerting/latest/configuration/).

On how to define additional alerting rules see the [Prometheus alerting rules
documentation](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/).

Last updated 2023-01-30 18:14:18 +0100

