---
marp: true
style: |
  section {
    font-family: "72";
  }

  section.lead h1{
    text-align: center;
  }
  section.lead h2{
    text-align: center;
  }

  section.centersingleimage p {
    text-align: center;
  }

  section.frontpage h1 {
    font-weight: bold;
    font-size: 30px
  }

  section.frontpage p {
    font-size: 20px
  }
---
<!-- 
<!-- _class: frontpage ->
<br/><br/><br/><br/><br/><br/><br/><br/>

# SAP CodeJam: Managing APIs in your landscape with SAP API Management

<br/>

Antonio Maradiaga 
*Developer Advocate @ SAP*

![bg vertical](assets/TechEd_Front.png)

<br/><br/>
2023

<!-- ---
# SAP CodeJam
*Connecting systems and services
using SAP Integration Suite*

<br/>
Antonio Maradiaga

*Developer Advocate @ SAP*

<br/><br/>
October, 2022


![bg](https://fakeimg.pl/800x600/ffffff/fff/)
![bg width:100%](assets/sitbarcelona-logo.avif)
 -->

<!-- paginate: false -->

![bg](assets/art/CodeJam_Art_ManageAPIs_Madrid.png)

---
<!-- paginate: false -->

![bg width:100% height:90%](tmp/IntegrationLandscape-VirtualSummit.png)

---
<!-- paginate: true -->

# SAP Integration Suite

![SAP Integration Suite](assets/sap-integration-suite-services.png)

--- 

# SAP CodeJam - API Management scenario


<!-- _class: centersingleimage -->
![width:22cm height:14cm](assets/diagrams/final-data-flow.png)


--- 

# [SAP CodeJam - Repository](https://github.com/SAP-samples/manage-apis-codejam/)
 
 <!-- _class: centersingleimage -->
![width:24cm height:14cm](assets/repository.png)

--- 

<!-- _footer: "*[Troubleshooting](https://github.com/SAP-samples/manage-apis-codejam/blob/main/troubleshooting.md#troubleshooting): Whenever you face an issue, make sure to check this page first.*" -->

# SAP CodeJam - Exercises (Part 1)

<br/>

* [Exercise 01 - The OpenAPI specification](./exercises/01-open-api-specification/README.md#exercise-01---the-openapi-specification)
* [Exercise 02 - Getting familiar with the SAP Business Accelerator Hub](./exercises/02-getting-familiar-business-accelerator-hub/README.md#exercise-02---getting-familiar-with-the-sap-business-accelerator-hub)
* [Exercise 03 - Discover and import an API](./exercises/03-discover-and-import-api/README.md#exercise-03---discover-and-import-an-api)
* [Exercise 04 - Deploy an API](./exercises/04-deploy-an-api/README.md)
* [Exercise 05 - Testing an API using the API Test Console](./exercises/05-testing-api/README.md)
* [Exercise 06 - Publishing our API](./exercises/06-publish-api/README.md)
* [Exercise 07 - Import an API using an OpenAPI specification](./exercises/07-import-api-openapi-spec/README.md)

<br/><br/>

--- 

<!-- _footer: "*[Troubleshooting](https://github.com/SAP-samples/manage-apis-codejam/blob/main/troubleshooting.md#troubleshooting): Whenever you face an issue, make sure to check this page first.*" -->

# SAP CodeJam - Exercises (Part 2)

<br/>

* [Exercise 08 - Add an SAP SuccessFactors Employee Central API](./exercises/08-add-ssff-employee-central-api/README.md)
* [Exercise 09 - Monitoring APIs](./exercises/09-monitoring-apis/README.md)
* [Exercise 10 - API policies](./exercises/10-api-policies/README.md)
* [Exercise 11 - Consume protected APIs by creating an application](./exercises/11-consume-applications/README.md)
* [Exercise 12 - Protecting our APIs](./exercises/12-protecting-apis/README.md)
* [Exercise 13 - Editing API paths, operations, and documentation](./exercises/13-api-designer/README.md)
<br/><br/><br/><br/>
--- 

<!-- _footer: "*[Troubleshooting](https://github.com/SAP-samples/manage-apis-codejam/blob/main/troubleshooting.md#troubleshooting): Whenever you face an issue, make sure to check this page first.*" -->

# SAP CodeJam - Exercises (Optional)

<br/><br/>

* [Optional Exercise 01 - Expose integration flow via API Management](./exercises/optional-01-expose-integration-flow-api-management/README.md)
* [Optional Exercise 02 - API Security Best Practices](./exercises/optional-02-security-best-practices/README.md)

<br/><br/><br/><br/><br/><br/><br/><br/>

--- 
<!-- _class: centersingleimage -->

# [Exercise 01 - OpenAPI specification](./exercises/01-open-api-specification/README.md)
<br/><br/>
![](exercises/01-open-api-specification/assets/OpenAPI_Specification_Logo_Pantone1.png)
<br/><br/><br/><br/><br/>

--- 
<!-- _class: centersingleimage -->

# [Exercise 02 - Getting familiar with the SAP Business Accelerator Hub](./exercises/02-getting-familiar-business-accelerator-hub/README.md)

![width:25cm height:14cm](exercises/02-getting-familiar-business-accelerator-hub/assets/S4HANACloud-API-BusinessPartner.png)

--- 
<!-- _class: centersingleimage -->

# [Exercise 03 - Discover and import an API](./exercises/03-discover-and-import-api/README.md#exercise-03---discover-and-import-an-api)

![width:20cm height:14cm](exercises/03-discover-and-import-api/assets/discover-search.gif)

--- 
<!-- _class: centersingleimage -->

# [Exercise 04 - Deploy an API](./exercises/04-deploy-an-api/README.md)

![width:20cm height:14cm](exercises/04-deploy-an-api/assets/deploy-api.gif)

--- 
<!-- _class: centersingleimage -->

# [Exercise 05 - Testing an API using the API Test Console](./exercises/05-testing-api/README.md)

![width:20cm height:14cm](exercises/05-testing-api/assets/access-test-api-console.gif)


--- 
<!-- _class: centersingleimage -->

# [Exercise 06 - Publishing our API](./exercises/06-publish-api/README.md)

![width:20cm height:14cm](exercises/06-publish-api/assets/associate-api-and-publish.gif)

--- 
<!-- _class: centersingleimage -->

# [Exercise 07 - Import an API using an OpenAPI specification](./exercises/07-import-api-openapi-spec/README.md)

![width:20cm height:14cm](exercises/07-import-api-openapi-spec/assets/import-openapi-spec.gif)


--- 
<!-- _class: centersingleimage -->

# [Exercise 08 - Add an SAP SuccessFactors Employee Central API](./exercises/08-add-ssff-employee-central-api/README.md)

![width:20cm height:14cm](exercises/08-add-ssff-employee-central-api/assets/discover-copy-ssff-api.gif)

--- 
<!-- _class: centersingleimage -->

# [Exercise 09 - Monitoring APIs](./exercises/09-monitoring-apis/README.md)

![width:20cm height:14cm](exercises/09-monitoring-apis/assets/monitor-apis-dashboard.png)

--- 
<!-- _class: centersingleimage -->

# [Exercise 10 - API policies](./exercises/10-api-policies/README.md)

![width:20cm height:14cm](exercises/10-api-policies/assets/apply-policy-template.gif)

--- 
<!-- _class: centersingleimage -->

# [Exercise 11 - Consume protected APIs by creating an application](./exercises/11-consume-applications/README.md)

![width:20cm height:14cm](exercises/11-consume-applications/assets/create-application.gif)

--- 
<!-- _class: centersingleimage -->

# [Exercise 12 - Protecting our APIs](./exercises/12-protecting-apis/README.md)

![width:20cm height:14cm](exercises/12-protecting-apis/assets/add-spike-arrest-policy.gif)

--- 
<!-- _class: centersingleimage -->

# [Exercise 13 - Editing API paths, operations, and documentation](./exercises/13-api-designer/README.md)

![width:20cm height:14cm](exercises/13-api-designer/assets/edit-business-partner-resource.gif)

--- 
<!-- _class: lead -->

# Thank you for attending!!!
<br/>

- Issues: You can [create an issue](https://github.com/SAP-samples/manage-apis-codejam/issues/new) in this repository if you find a bug or have questions about it.
- [Feedback](https://github.com/SAP-samples/manage-apis-codejam/issues/new?assignees=&labels=feedback&template=session-feedback-template.md&title=Feedback): If you can spare a couple of minutes at the end of the session, please help us improve for next time by giving me some feedback.

<br/><br/><br/><br/>
