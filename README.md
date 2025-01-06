# AMP for Open WebUI with the CML AI Inference Service

![](/catalog-icon.png)

## Overview

The Open WebUI for AI Inference Service in CML project provides a ready-to-use implementation of an open-source web interface for deploying AI models using Cloudera Machine Learning (CML). This project leverages Cloudera's AI Inference Service and AMP (Applied Machine Learning Prototypes) capabilities of CML to facilitate seamless interaction with deployed machine learning models via a web UI.

The project includes scripts to set up dependencies, configure the environment, and launch the Open WebUI, providing users with an efficient way to interact with their models without needing to manage complex API integrations.

**The Open WebUI offers the following features:**

1. **Simplified Model Interaction:** Provides a user-friendly interface to interact with deployed AI models without writing code.

2. **Seamless Integration with CML:** Leverages CML’s AI Inference Service to streamline the deployment and management of machine learning models.

3. **Scalable and Customizable:** Easily scalable within the CML environment and customizable to fit specific use cases.

Below illustrates an example of the deployed AMP and leverages a simple query using Cloudera's AI Inference Service and the Open WebUI. The second example includes attaching a sample document to use as context for summarization.

![](/assets/simple-example.png)

![](/assets/example-with-attachments.png)


## Deployment

Deploy from the AMP catalog as shown below. If you do not see it in the community catalog, you can add `https://raw.githubusercontent.com/kevinbtalbert/CML_AMP_OpenWebUI-for-CML-AI-Inference/refs/heads/main/catalog-entry.yaml` to your AMP custom catalog entries.

![](/assets/amp-deployment-1.png)

![](/assets/amp-deployment-2.png)

Enter the required base URL for your inference service instance. You can locate this by navigating to the Model Endpoints in CML as shown below and copy/paste this into the variable slot in the AMP deployment window.
![](/assets/model-endpoints.png)

Select the "Copy" icon to copy the URL.
![](/assets/model-endpoints-details.png)

As shown in the example below and on the deployment, paste it as the AMP variable and deploy the AMP.
![](/assets/amp-deployment-3.png)

After the AMP is deployed, either click "Open" or navigate to the Applications tab of the project to open the application there.

![](/assets/amp-deployment-4.png)

## Usage
This was tested using the modern runtime below on the most recent version at the time, `2024.10`.
```yaml
   - editor: PBJ Workbench
   - kernel: Python 3.11
   - edition: Standard
```

