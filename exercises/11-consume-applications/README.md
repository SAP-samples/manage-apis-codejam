# Exercise 11 - Consume protected APIs by creating an application

In the previous exercise, we explored how we can add policies to our APIs but now we face a new issue, we require an API key to call our API. 

At the end of this exercise, you'll have successfully called an API proxy that implements the VerifyAPIKey policy in SAP API Management.

## Create an Application in API Business Hub Enterprise

We got familiar with the API Business Hub Enterprise in [exercise 06](../06-publish-api/README.md), where we published our first API to the developer portal. Now we will explore some additional functionality that the developer portal provide us, creating and managing applications, which can be subscribed to different products available within the API Business Hub Enterprise.

> Before proceeding, make sure that you've registered as a developer in the API Business Hub Enterprise. The instructions on how to achieve this can be found in the prerequisites - [Register as a developer in the API Business Hub Enterprise](../../prerequisites.md#register-as-a-developer-in-the-api-business-hub-enterprise)

👉 Navigate to the API Business Hub Enterprise and select the `My Workspace` link in the top navigator bar.

<p align = "center">
    <img alt="API Business Hub Enterprise - My Workspace" src="assets/api-business-hub-enterprise-my-workspace.gif" width="50%"/><br/>
    <i>API Business Hub Enterprise - My Workspace</i>
</p>

In `My Workspace` we can manage our applications. There are also some analytics capabilities available to us, e.g. cost, performance and errors. Let's proceed to create an application so that we can call an API proxy with the VerifyAPIKey policy in it.

👉 Click on the `Create New Application` button, specify a name, e.g. `VerifyAPIKey test`, and associate the `General Data` product which is where our Nager.Date (PublicHolidays_Nager_Date_API) API lives.

<p align = "center">
    <img alt="Create application in API Business Hub Enterprise" src="assets/create-application.gif" width="50%"/><br/>
    <i>Create application in API Business Hub Enterprise</i>
</p>

> In case you are unable to create an application in the API Business Hub Enterprise, check out the solution in the [troubleshooting page](../../troubleshooting.md#unable-to-create-application-exceptions-in-developer-portal).

Excellent, we've created an application and the `Application Key` is what we need to call our API.

👉 Copy the value in the Application Key field.

## Test API

Now that we have an API key, we can proceed to try calling our API again. Let's do that.

👉 Go to the `Test Environment` available in the API Business Hub Enterprise, select the `Public Holidays Worldwide` API and try calling any resource available. 

<p align = "center">
    <img alt="Public Holidays API - No API key in headers" src="assets/public-holidays-api-no-api-key.gif" width="50%"/><br/>
    <i>Public Holidays API - No API key in headers</i>
</p>

Ha! That failed right? I didn't specify the API key as a header parameter...

👉 Pass the API key from the application you created as a header parameter. Add a header parameter called APIKey and set as a value the application key.

<p align = "center">
    <img alt="Public Holidays API - with API key in headers" src="assets/public-holidays-api-with-api-key.gif" width="50%"/><br/>
    <i>Public Holidays API - with API key in headers</i>
</p>

Success!!!! You were able to call the API successfully. Meaning that we can now add some basic security to our APIs as well as learn who is calling our APIs.

🧭 Take some time to revisit the Monitor > APIs page in SAP Integration Suite. What's different? Can we now identify the application? Can we now identify the developer?
## Summary

We've learnt more about the functionality that's available in the API Business Hub Enterprise for developers and how applications are needed to consume API proxies that perform key validation by using the VerifyAPIKey policy. Now that we've learnt how we can add this basic security to our APIs, let's dive a bit deeper into policies.

## Further reading

* [Consume Applications](https://help.sap.com/docs/sap-api-management/sap-api-management/consume-applications?locale=en-US)
* [Test Runtime behaviour of APIs](https://help.sap.com/docs/sap-api-management/sap-api-management/test-runtime-behavior-of-apis-new-design?locale=en-US)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. What happens if we specify an invalid API key when we make our call?
    <details>
    <summary>🔦 Hint</summary>
    <i>Try sending a request with `ABCDEF` as the API key and check the HTTP response status code.</i>
    </details>
2. Explore the Cost, Performance Analytics and Error Analytics tabs that are available in My Workspace. You've made a couple of API calls, you should be able to see some information here.
3. Can you think of a way we can force an error in the `Public Holidays Worldwide` API so that we can see some data in the `Error Analytics` tab?

## Next

Continue to 👉 [Exercise 12 - Protecting our APIs](../12-protecting-apis/README.md)