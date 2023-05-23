# Optional Exercise 02 - API Security Best Practices

We've covered different policies during this CodeJam but it will be impossible to cover every single policy type that's available in SAP API Management. That said, it is still good to be familiar with what's available as every company/project has different requirements/needs that we might need to address via API policies.

At the end of this exercise, you'll be familiar with different API Security Best Practices and examples that are available in SAP Community.

## Best Practices

I want to bring to your attention a wonderful blog post series that was published by [Divya Mary](https://people.sap.com/divya.mary) and [Sven Huberti](https://people.sap.com/svenhuberti) in SAP Community. In the blog post series, she goes through the details of different policy types and best practices that you can apply in SAP API Management to protect your APIs.

<p align = "center">
    <img alt="Different API policies covered in the API Security Best Practices blog post series" src="assets/different-api-management-policies.png" width="85%"/><br/>
    <i>Different API policies covered in blog post series</i>
</p>

Below is a list of the different policy types and examples of how to use them.

> Although the screenshots in the blog post series are from a previous version of SAP API Management but the logic behind applying the policies is still valid.

| Policy Type | Example |
|-------------|---------|
|  [Access Control](https://help.sap.com/docs/sap-api-management/sap-api-management/access-control?locale=en-US)   | [Part 1 – Restrict access to API based on IP Addresses](https://blogs.sap.com/2017/08/07/restrict-access-to-api-based-on-ip-addresses/) |
|   [Quota](https://help.sap.com/docs/sap-api-management/sap-api-management/quota?locale=en-US)  | [Part 2 –  Rate limit API calls with Retry time](https://blogs.sap.com/2017/08/10/sap-cloud-platform-api-management-rate-limiting-api-calls/) |
|   [Javascript](https://help.sap.com/docs/sap-api-management/sap-api-management/javascript?locale=en-US), [Quota](https://help.sap.com/docs/sap-api-management/sap-api-management/quota?locale=en-US)  | [Part 3 – Rate limit API calls for OData Batch calls](https://blogs.sap.com/2017/08/10/sap-cloud-platform-api-management-rate-limiting-for-odata-batch-calls/) |
|   [XSL Transform](https://help.sap.com/docs/sap-api-management/sap-api-management/xsl-transform?locale=en-US)  | [Part 4 – Data masking of sensitive data from API response](https://blogs.sap.com/2017/08/18/sap-api-management-data-masking-for-sensitive-data-in-odata-rest-apis/) |
|   [JSON Threat protection](https://help.sap.com/docs/sap-api-management/sap-api-management/json-threat-protection?locale=en-US)  | [Part 5 – JSON Threat protection against injection attacks](https://blogs.sap.com/2017/08/18/sap-api-management-json-threat-protection-against-injection-attacks/) |
|   [XML Threat protection](https://help.sap.com/docs/sap-api-management/sap-api-management/xml-threat-protection?locale=en-US)  | [Part 6 – XML Threat protection against injection attacks](https://blogs.sap.com/2017/08/18/sap-cloud-platform-api-management-xml-threat-protection-against-injection-attacks/) |
|  [Message Logging](https://help.sap.com/docs/sap-api-management/sap-api-management/message-logging-policy?locale=en-US)   | [Part 7 – Log all API interactions](https://blogs.sap.com/2017/08/21/sap-cloud-platform-api-management-log-all-api-interactions/) |
|   [Regular Expression Protection](https://help.sap.com/docs/sap-api-management/sap-api-management/regular-expression-protection?locale=en-US)  | [Part 8 – Threat protection against SQL injection attacks](https://blogs.sap.com/2017/08/21/sap-cloud-platform-api-management-threat-protection-against-sql-injection-attacks/) |
|   [Quota](https://help.sap.com/docs/sap-api-management/sap-api-management/quota?locale=en-US) per application  | [Part 12 –  Rate limit API call per developer](https://blogs.sap.com/2017/08/11/sap-api-management-rate-limiting-api-calls-per-application/) |


## Summary

Now that you are familiar with the basic functionality of SAP Business Accelerator Hub and the Business Partner API, we are ready to start interacting with the services from which our integration will be extracting data.

## Further reading

* [API Security Best Practices Blog Series](https://blogs.sap.com/2017/08/22/sap-cloud-platform-api-management-api-security-best-practices/)

---

If you finish earlier than your fellow participants, you might like to ponder these questions. There isn't always a single correct answer and there are no prizes - they're just to give you something else to think about.

1. Can you think of any APIs, that you've interacted with, that have similar security best practices?
2. Are there any API projects, that you've been involved in, where an API policy could have simplified the implementation?
