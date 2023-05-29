# Exercise 13 - Editing API paths, operations, and documentation

In previous exercises, we've covered how to change the behaviour of our APIs using policies. Now we'll explore how we can modify the resource and information displayed for our API paths and operations. We'll also expand a bit on what we learnt about OpenAPI specifications in [exercise 01](../01-open-api-specification/README.md).

At the end of this exercise, you'll be familiar with the API Designer available in SAP API Management and how we can use it to model our APIs.

## Editing the YAML document using the API Designer

The API designer editor enables us to do the following:
- Import existing OpenAPIs
- Download APIs
- Generate equivalent HTML output views
- Save APIs
- Validate OpenAPI syntax

> The API designer supports OpenAPI specification 2.0 and OAS 3.0 versions.

As mentioned in the API Management scenario, there are scenarios where we wouldn't want to expose the entire API and we want to control/limit the number of paths/operations exposed for them. In our case, we want to only expose the `/A_BusinessPartner`, `/A_Customer` and `/A_Supplier` paths available in the `S4HC_API_BUSINESS_PARTNER`. Also, we don't want to expose the PATCH operations available for these APIs, only GET and POST operations.

👉 Go to the `S4HC_API_BUSINESS_PARTNER` API and select `Edit in API Designer` from the `Edit` menu.

Given the large size of the Business Partner Open API specification, it takes some time for the changes to be reflected in the UI. This is because whenever we change something, the UI on the left needs to render again all the paths and operations available. Unfortunately, we gotta be a bit patient here 😮‍💨.

We could manually start removing the paths and operations using the UI. That said, it might be easier to do this externally to avoid re-rending the UI every time we make a change.

***The large file was modified externally on your behalf. Please copy the contents of the OpenAPI specification included in the `API_BUSINESS_PARTNER_BusinessPartner_Customer_Supplier.yaml` file as we will use the **new version for the rest of the exercise.***

👉 Copy the contents of the `API_BUSINESS_PARTNER_BusinessPartner_Customer_Supplier.yaml` file in the assets folder of this exercise and replace the content (YAML - Yet Another Markup Language) in the editor.

// TODO: Show copy and paste

The new version only includes the following paths: `/A_BusinessPartner`, `/A_Customer`, `/A_Supplier`. Meaning that we are done with the first task mentioned at the beginning of the exercise. Now, we are just missing removing the PATCH operations exposed for some paths. To remove these operations, we can easily navigate to where they are in the YAML document by clicking the little return icon ⏎ that appears when hovering over the PATCH operations for each path.

👉 Click on the return icon for each PATCH operation, collapse the text in the YAML document and remove each one of them from the YAML document. Once removed all PATCH operations, save the API. *Note: The animation below shows you how to do it*

<p align = "center">
    <img alt="Remove PATCH operations from API" src="assets/remove-patch-method-using-quick-navigation.gif" width="85%"/><br/>
    <i>Remove PATCH operations from API</i>
</p>

We can follow a similar process if we want to remove a path, e.g. let's assume we want to remove the /A_Customer path, we can navigate to it, collapse the path and delete it.

## Editing the API using the API portal

Apart from manipulating the OpenAPI specification directly from SAP API Management, it is also possible to modify

👉 Go to the `S4HC_API_BUSINESS_PARTNER` API and select `Edit` from the `Edit` menu.

When we enter the basic edit mode. Here, we can modify the basic information of our API, e.g. Title, Host Alias, API Base Path, API state, and description. As well as the configuration set for our `Proxy Endpoint`, `Target Endpoint` and `Resources` exposed. This is the information that a developer will see when exploring the API from the API Business Hub Enterprise.

<p align = "center">
    <img alt="Edit API in API Portal" src="assets/edit-api-portal.gif" width="85%"/><br/>
    <i>Edit API in API Portal</i>
</p>

From here we can also modify the paths/operations exposed for our API. It can be a bit easier to edit it this way, as you will not be dealing with the raw text in the OpenAPI specification (YAML) but an intuitive UI.

👉 Go to the `Resource` tab and click the pencil icon ✏️ to edit the `Business Partner` resource.

<p align = "center">
    <img alt="Edit Business Partner resource" src="assets/edit-business-partner-resource.gif" width="85%"/><br/>
    <i>Edit Business Partner resource</i>
</p>

From here we can add/modify paths and their operations. Also, we can easily change the description of the different operations. Let's remove an operation and update a description and see the changes reflected in the API.

👉 Remove the POST operation of the /A_BusinessPartner path and update the GET operation description to `Retrieves general data fields of all the business partner records available in the SAP S/4HANA Cloud system.`. Once done, `Save` and `Deploy` the changes.

<p align = "center">
    <img alt="Update /A_BusinessPartner path using API portal" src="assets/remove-operation-and-update-description.gif" width="85%"/><br/>
    <i>Update /A_BusinessPartner path using API portal</i>
</p>

If we navigate back to the `Resources` tab of the `S4HC_API_BUSINESS_PARTNER` API, we can see that the `/A_BusinessPartner` path no longer has a POST operation and the description in the GET operation has been updated.

## Summary

You've made it to the last exercise of this CodeJam. Congratulations!!! 🎉 🙌. This is no easy feat as there is a lot to read/learn/process in the CodeJam and you need to dedicate some solid focus time to go through the exercises. Great job 👏👏👏!

In this exercise, we learnt how we can further modify the API proxies that we create in SAP API Management. You now have a solid understanding of some of the common tasks performed when managing the APIs available in your landscape using SAP API Management. 

## Further reading

* [Edit an API Proxy](https://help.sap.com/docs/sap-api-management/sap-api-management/edit-api-proxy?locale=en-US)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. No questions... just relax now, this is the last exercise :-)
