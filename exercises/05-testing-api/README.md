# Exercise 05 - Testing an API using the API Test Console

At the end of this exercise, you'll have successfully tested an API available via SAP API Management by using the API Test Console available in SAP Integration Suite.

## API Test Console

It is possible to test our APIs available in SAP API Management directly from SAP Integration Suite.

👉 Navigate to the `API Test Console` - `Test > APIs`

![Navigate to API Test Console](assets/access-test-api-console.gif)
<p align = "center">
<i>Navigate to API Test Console</i>
</p>

The API Test Console will list all APIs that are available in our SAP API Management instance. After selecting an API, e.g. `S4HC_API_BUSINESS_PARTNER`, all the resources available will be listed in the dropdown. 

The top part of the console allows us to set the authentication, the HTTP method that we want to use, headers and query parameters, and a request payload (request body) that can be specified to call the API resource.

> ℹ️ In the API Test Console you'll notice the `Url Params` button. Throughout the exercises, whenever query parameters are mentioned, we are refering to the parameters that we can include as Url Params.

The bottom part of the console will display the response from calling our API. Here we will see if our API call was successful or not. 

## Test an API

We are now ready to test our API. Let's go ahead and select the API we've created and select a resource.

👉 Select the `S4HC_API_BUSINESS_PARTNER` from the APIs list and the `/A_BusinessPartner` resource, e.g. `https://your-tenant.test.apimanagement.eu10.hana.ondemand.com:443/API_BUSINESS_PARTNER/A_BusinessPartner`. 

Now, let's call our service. No need to specify any authentication, HTTP method, headers or query parameters.

👉 Click the `Send` button at the bottom right corner of the screen. 

A response similar to the one below will be displayed on our screen.

![Test API - 401 Unauthorized](assets/api-call-unauthorised.png)
<p align = "center">
<i>Test API - 401 Unauthorized</i>
</p>

> Excellent, we get an error! This is deliberate so that we can get familiar with what an error looks like in the API Test Console.

The underlying service, through [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) (401 Unauthorized), is telling us that we are not authorised to call it. This can be that the username/password combination we specified is incorrect, or that we haven't specified any authorization details (which is our case).

### Adding Authentication details

At the top of the API Test Console, there is a link that says `Authentication: None`. We haven't specified any credentials to authenticate against our API. In this case, we can specify a username and password to authenticate against it.

👉 Click the `Authentication: None` link to specify a username and password that will be used to authenticate against the service. 
> 🔐 *Your instructor will provide you with the username and password you can use.*

![Add Basic Authentication](assets/add-basic-authentication.gif)
<p align = "center">
<i>Add Basic Authentication</i>
</p>

<details>
<summary><i>What happens if we send a request now that we've specified credentials?</i></summary>
<br>

Unfortunately, we will get a different error message. The error that surfaces in the UI is not as intuitive as the one we saw previously. Nothing to worry about, we will fix it in the next section. Can you think of something that we can do in our browser to find out more about the request we are making? 

![Unable to fetch response error](assets/unable-to-fetch-response.png)
<p align = "center">
<i>Unable to fetch response error - HTTP 500 error</i>
</p>

</details>

### Add a query parameter

We know that there may be many Business Partners in our system, so it is a good practice to try to minimise the impact of our call in the system and just retrieve the data that we need. This prevents adding unnecessary load to our system. In our case, we are interested in testing connectivity so we can limit the results (Business Partners) returned by the API. 

Fortunately, the Business Partner API is an OData API, meaning that we can use the OData query options to limit the response returned by the service. 

> If you want to learn more about OData and the system query options available, make sure to check out this Back to Basic episode with Developer Advocate DJ Adams - [Back to basics: OData - the Open Data Protocol - Part 3 - System query options](https://www.youtube.com/watch?v=Bln2A0_OauY&t=835s)

👉 Add a query parameter in the request to retrieve the top 5 Business Partners ($top=5). Click the `Url Params` button, add a record with key $top and value `5` and then send the request again.

![Add $top query parameter to request](assets/add-top-query-parameter.gif)
<p align = "center">
<i>Add $top query parameter to request</i>
</p>

👏 🎉 Excellent! We managed to send a request to the SAP S/4HANA Cloud Business Partner API. That said, the response is in XML format and we might prefer handling a JSON payload. Let's do something more....

### Add a header parameter

By including header parameters in our request we can pass additional information to the server in our request. For example, the authentication we added previously ends up being added to our [request headers](https://developer.mozilla.org/en-US/docs/Glossary/Request_header) as an `Authorization` header, e.g. `Authorization = Basic NRWHQC1FT1YHLrvbyaOfvpo7Y2SyTVPlsEWrYYrbwaCdnO7u`. By using [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) we can tell the service that we would prefer the response to be in a different format, e.g. JSON. Let's go ahead and do that.

> Note: Not every API available out there will handle the HTTP Header we are specifying here. You will need to check the API documentation to see if it is possible.

👉 Add a header parameter in the request to specify that we prefer a JSON response. Click the `Headers` button, add a record with the key `Accept` and value `application/json` and then send the request again.

![Add Accept HTTP header to request](assets/add-accept-header.gif)
<p align = "center">
<i>Add Accept HTTP header to request</i>
</p>

Nice! Our response is now in JSON format.

## Summary

In this exercise, we got familiar with the API Test Console. We were also able to modify our request, by including HTTP headers and query parameters, and successfully tested our API. Let's proceed to publish it so that other developers within our organization can discover it in the API Business Hub Enterprise.

## Further reading

* [Test APIs documentation](https://help.sap.com/docs/sap-api-management/sap-api-management/test-apis?locale=en-US)
* [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers):
  * [Accept](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept)
  * [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
* [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. What would happen if you try testing an undeployed API?
   <details>
    <summary>Hint 🔦</summary>
    <i>You can un-deploy the API deployed in exercise 04. Then head to the API Test Console and trigger an API request. <br /><b>🚨 Make sure to redeploy it after running this test as we will be using the API in future exercises.🚨</b></i>
    </details>
2. We used the API Test Console to test our API. Which other tools can you use to test an API published in SAP API Management?
3. Why do you think that the API Test Console allows us to select the HTTP Method we can use to call a resource?
4. What would happen if the user that we use to authenticate against our API doesn't have the required roles/privileges to call the API? Which HTTP response status code are we likely to get?

## Next

Continue to 👉 [Exercise 06 - Publishing our API](../06-publish-api/README.md)