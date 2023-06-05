# Optional Exercise 01 - Expose integration flow via API Management

In this exercise, we will expose our integration flow via API Management and take advantage of the functionality provided by API Management to govern and monitor the calls made to the integration flow. Once the API is created we will expose it via the API Business Hub Enterprise (Developer Portal). 

To achieve the above we create an API in API Management that will act as a proxy to our integration flow and we will leverage an OpenAPI specification to create it. Remember that we learnt about OpenAPI specifications in [exercise 01](../01-open-api-specification/README.md) of this CodeJam.

<p align = "center">
    <img alt="To be - Including SAP Cloud Integration Integration Flow" src="../../assets/diagrams/exercise-14.png" width="85%"/><br/>
    <i>To be - Including SAP Cloud Integration Integration Flow</i>
</p>

## Create API by importing OpenAPI specification

An OpenAPI specification for an integration flow is included in the assets of this CodeJam - [integration-flow-openapi-spec-1.0.0.json](../../assets/cloud-integration/integration-flow-openapi-spec-1.0.0.json). The spec describes the endpoint that's being exposed in SAP Cloud Integration and the data structure of the request and response expected from our endpoint.

> If you are interested in knowing the ins and outs of the integration flow that we will be calling. The integration flow was developed as part of the [Connecting Systems and Services using SAP Integration Suite CodeJam](https://github.com/SAP-samples/connecting-systems-services-integration-suite-codejam). 
> 🔐 In our case, the CodeJam facilitator will provide you with the URL and credentials required to call the integration flow.

👉 Open the specification file located under the assets folder in the root of the repository, e.g. `./assets/cloud-integration/integration-flow-openapi-spec-1.0.0.json` and check that the following components match the ones provided by your instructor. 
- `.servers.url`: Replace the value `https://your-tenant-free-tier-gfm1c35e.it-cpi018-rt.cfapps.eu10-654.hana.ondemand.com` with the value configured for `cpi_host` variable in the Postman environment that communicates with the integration flow.
- *(Optional)* `.paths`: Check the value in paths matches the value in the Postman environment, e.g. `/http/request-employee-dependants-cc`.

Once we've updated the specification file, we can use this to create an API in SAP API Management. Once the API is created we will add it to the Developer Portal. First, let's go ahead and create the API.

> In case you wonder how the OpenAPI spec included in the assets was created.... The file was generated from a Postman collection, with the help of the [postman-to-openapi](https://github.com/joolfe/postman-to-openapi) CLI. The output of the utility isn't the file that's in the repo but it was great starting point to define the API specification. 

👉 Navigate to the `Develop > APIs` component of SAP Integration Suite and click the `Import API` button. Select the recently modified OpenAPI spec and create a version for the API, e.g. v1. Check that everything is fine after importing the file and click the `Save` button. Once saved, you can `Deploy` the API.

<p align = "center">
    <img alt="Import OpenAPI specification to create API" src="assets/import-spec-create-api.gif" width="100%"/><br/>
    <i>Import OpenAPI specification to create API</i>
</p>

To expose the API in the Developer Portal (API Business Hub Enterprise) we first need to add it to a Product and include the API within it. Let's go ahead, create the product and publish it.

👉 In the `Develop > APIs` component of SAP Integration Suite, click the `Create button` in the `Products` tab. Enter a name and a title, e.g. `Business Partners` and include the `Request_Employee_Dependants_v1` API. Lastly, click the `Publish button`.

> For a detailed step by step instruction on creating a Product, checkout [exercise 06](../06-publish-api/README.md).

After publishing the product, we can navigate to the API Business Hub Enterprise and see the `Business Partners` product we just published and the `Request_Employee_Dependants_v1` API.

![API Business Hub Enterprise - Business Partners product](assets/api-business-hub-enterprise-bp-product.gif)
<p align = "center">
<i>API Business Hub Enterprise - Business Partners product</i>
</p>

## Send a message to the integration flow via API Management 

Now that we've created the `Request_Employee_Dependants_v1` API, we can communicate with our integration flow through API Management.

- *From the API Management UI*

    👉 Go to the API and *"try out"* the API from the `Resources` tab.

    <p align = "center">
        <img alt="Send message to integration flow via API Management UI" src="assets/test-integration-flow-from-api-management.gif" width="100%"/><br/>
        <i>Import OpenAPI specification to create API</i>
    </p>

    > ⚠️ The response is an HTTP 401. Why do you think we get that error? Are we missing something in our request? ❓❓
        <details>
        <summary>Hint 🔦</summary>
        <br>
        A Bearer token. The same that we send when communicating directly with Cloud Integration.
        </details>

- *From Postman*
  
    👉 Update the `client_id` and `client_secret` variable in the `Manage APIs CodeJam` Postman environment with the details provided by the instructor. Also, update the `cpi_proxy_url` with the deployed URL shown in API Management.

    <p align = "center">
        <img alt="API Proxy URL" src="assets/api-proxy-url.png" width="85%"/><br/>
        <i>API Proxy URL</i>
    </p>

    👉 Once updated, retrieve an access token using the Token request and then send a message to the integration flow by using the `cloud-integration > Request Employee Dependants Proxy` request in Postman.

    > 👀 In the gif below, you'll notice that you need to specify a `Bearer Token` in the Authorization tab of the request. This is because we are not managing the authentication process with Cloud Integration in API Management. We will alter this behaviour in the [next section](#add-policies-to-the-request_employee_dependants_v1-api).

    ![Send message via API Management from Postman](assets/send-message-via-api-management-from-postman.gif)
    <p align = "center">
    <i>Send message via API Management from Postman</i>
    </p>

At the moment we've set up an API (`Request_Employee_Dependants_v1`) in API Management that is a proxy for our integration flow. By doing this we can use API Management to add common API functionality to our API, e.g. secure the API, modify headers, transform message formats, or implement [rate limits](https://help.sap.com/docs/SAP_CLOUD_PLATFORM_API_MANAGEMENT/66d066d903c2473f81ec33acfe2ccdb4/bf441dc839034613b059cb508ad610f7.html?locale=en-US).

## Add policies to the Request_Employee_Dependants_v1 API

To communicate with the integration flow we need to send a Bearer token in the request headers. This Bearer token is obtained by first authenticating against the token server using the `clientid` and `clientsecret` we got from the [Cloud Integration runtime service key](../../prerequisites.md#create-sap-cloud-integration-runtime-client-credentials) that was created as part of the CodeJam prerequisites.

Although it is possible to create a service key and share the details with a new consumer of the service, this approach might not be ideal as an administrator will need to be involved whenever new/update credentials is required. It is not self-service, meaning we cannot use the API Business Hub Enterpise to manage our application/credentials.

Given that the communication to our integration flow can now go through API Management, we can use API Management to change how we keep our service secure. In our case, we will apply the following policies:
1. [Business Technology Platform connectivity](https://api.sap.com/policytemplate/Cloud_Platform_Connectivity): This policy template helps us communicate with APIs hosted on SAP BTP and that are protected by the BTP OAuth, e.g. our integration flow. The template will be used to authenticate against Cloud Integration using our [existing service key](../../prerequisites.md#create-sap-cloud-integration-runtime-client-credentials).
2. [Verify API Key](https://help.sap.com/docs/SAP_CLOUD_PLATFORM_API_MANAGEMENT/66d066d903c2473f81ec33acfe2ccdb4/4d15a0427494452dbb42a319e9bb420f.html?locale=en-US): Creating an application in the Developer Portal will generate for us an Application Key. We can use this Application Key to authenticate our calls to a Product API in API Management.

### Business Technology Platform connectivity

The Business Technology Platform connectivity policy is available in the Business Accelerator Hub - https://api.sap.com/policytemplate/Cloud_Platform_Connectivity. To import it into our tenant, we will need to copy it from the Discover section in API Management.

🧭 Take some time to explore what's documented for the [Business Technology Platform connectivity policy template](https://api.sap.com/policytemplate/Cloud_Platform_Connectivity). Pay particular attention to the `getcredential` and `getoauthtoken` steps as these are the steps that we will need to update later.

👉 Navigate to `Discover > APIs` component of SAP Integration Suite, search for `Connectivity`, select `Connect to SAP Business Technology Platform Services` and copy the `Business Technology Platform connectivity` artefact.

![Discover - Connect to SAP Business Technology Platform service](assets/discover-connect-btp-connectivity.png)
<p align = "center">
<i>Discover - Connect to SAP Business Technology Platform service</i>
</p>

Now that the policy template is available on our tenant, we can proceed to apply it in our `Request_Employee_Dependants_v1` API.

👉 Enter Edit mode for the `Request_Employee_Dependants_v1` API. Go to Policies, select the `Policy Template button` and apply the connectivity policy template. Now, in the `TargetEndpoint.PreFlow` section, update the `clientid` and `clientsecret` in the `getcredential` step and the `OAuth token URL` in the `getauthtoken` step with the details found in our service key. Finally, update the policy, save and re-deploy the API.

![Apply Business Technology Platform connectivity policy template](assets/apply-btp-connectivity-policy.gif)
<p align = "center">
<i>Apply Business Technology Platform connectivity policy template</i>
</p>

![Update policy and deploy API](assets/update-policy-and-deploy.gif)
<p align = "center">
<i>Update policy, save and deploy API</i>
</p>

> Detailed step by step screenshots on how to apply the policy template can be found in step 4 of this [tutorial](https://developers.sap.com/tutorials/cp-starter-isuite-api-management.html#be2bb154-9208-4ace-b635-a986f7f049cc).

The `Request_Employee_Dependants_v1` API was once again deployed. What will happen if we send a request to our API now? You can test this using the `cloud-integration > After applying BTP connectivity policy template` request included in the Postman collection.

### Verify API Key

As our API is available via the API Business Hub Enterprise, we want developers interested in consuming the service to create an application (subscribe) and use the application key to authenticate.

👉 Enter Edit mode for the `Request_Employee_Dependants_v1` API. Go to Policies, select the `ProxyEndpoint.PreFlow` flow and add the `Verify API Key` policy. Enter a name and set `request.header.APIKey` as the value of the APIKey @ref attribute. Finally, update the policy, save and re-deploy the API.

![Add Verify API Key policy](assets/add-verify-api-key-policy.gif)
<p align = "center">
<i>Add Verify API Key policy</i>
</p>

> Detailed step by step screenshots on how to add the Verify API Key policy can be found from step 10 - step 13 of this [tutorial](https://developers.sap.com/tutorials/hcp-apim-verify-api.html#b9f8a3d2-554e-482a-a8d1-b8af157da3dd).

The `Request_Employee_Dependants_v1` API was once again deployed. What will happen if we send a request to our API now? You can test this using the `cloud-integration > After Verify API Key policy` request included in the Postman collection. 

Do you get an authentication error? That's good. It means that our policy is working. Now let's get an application key that we can use to authenticate against the API.

## Create an application in the API Business Hub Enterprise

The API Business Hub Enterprise can be the central point where developers in our organisation can discover APIs available in the company, create applications to communicate with these APIs and self-manage the applications.

👉 Navigate to the API Business Hub Enterprise and create an application (subscribe) for the `Business Partners - Request Employee Dependants` API.

![Create Benefits Platform app](assets/benefits-platform-app.gif)
<p align = "center">
<i>Create Benefits Platform app</i>
</p> 

Note the `Application Secret` and `Application Key` that have been generated for us. As we added the Verify API Key policy to our API, we will now need to specify this `Application Key` in the `APIKey` header of our request.

> In case you face an "Unable to Create Application" error, check out the solution in [troubleshooting](../../troubleshooting.md#unable-to-create-application-exception-in-developer-portal) document. 

👉 Update the `ABHE-application-apiKey` variable in the Postman environment with the `Application Key` of the application, e.g. *UWuWAcWMMeX5bJgd49GbBoW6keEoq7lv*. Now, try sending a request using the `cloud-integration > After Verify API Key policy` request included in the Postman collection.

🧭 We've sent several messages to our integration flow via API Management. Take some time to check the monitoring capabilities available to us in API Management (`Monitor > APIs`, Analyze section). You should see the successful and failed requests here.

![API Management - Analyse section](assets/api-management-analyse.png)
<p align = "center">
<i>API Management - Analyse section</i>
</p>

## Summary

Congratulations on completing this optional exercise!!! 🎉 🙌. This is no easy feat as there is a lot to read/learn/process in the CodeJam and you need to dedicate some solid focus time to go through the exercises. Great job 👏👏👏!

We've achieved a lot in this exercise. We used an OpenAPI specification to create an API in API Management. We also modified how we communicate with our integration flow by applying/adding policies to our API and deployed the changes several times.

## Further reading

* [API Management - Security Best Practices blog post](https://blogs.sap.com/2017/08/22/sap-cloud-platform-api-management-api-security-best-practices/)
* [Security Best Practices - Policy Templates](https://api.sap.com/package/SecurityBestPractices/policytemplate)
* [Additional Attributes in OpenAPI Specification](https://help.sap.com/docs/SAP_CLOUD_PLATFORM_API_MANAGEMENT/66d066d903c2473f81ec33acfe2ccdb4/35f357c811f546c5ae3451df42f61ea0.html?locale=en-US)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. How can we restrict which products/APIs are visible to developers in the API Business Hub Enterprise?
2. How long does it take for a request to be processed? Where can you find this information in API Management? What other information about our requests is available here?

[^1]: OpenAPI Specification: [https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#infoObject](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#infoObject)
