## Part 3: API + UI Integration Test  

The objective of this test is to validate the complete project creation flow across API, Web UI, and Mobile UI, while ensuring proper tenant isolation in a multi-tenant SaaS application.  
The test follows an API-first approach for test data setup, followed by UI validations, and finally security checks to ensure data isolation between tenants.  
### 1)	Assumptions:  
•	A valid authentication token is available for API calls  
•	Tenant IDs are known and configured  
•	Playwright, pytest, and BrowserStack setup is assumed  
•	Test data cleanup can be performed using API  

### 2)	Test Data Handling Strategy:  
•	Test data is created using API to reduce UI dependency  
•	Project ID returned from API is reused across UI and mobile validations  

### 3)	Cross-Platform Validation Strategy:  
•	Web validation ensures correct user experience on browsers  
•	Mobile validation ensures the same backend data is accessible across platforms  

### 4)	Tenant Isolation Strategy:  
•	Same test data is validated across multiple tenants  
•	Project visibility is restricted to the correct tenant only  
•	Prevents cross-company data leakage, which is critical for SaaS security  

### 5)	Edge Cases Considered:  
•	Slow API responses or temporary network delays  
•	Delayed UI rendering due to dynamic content  
•	Mobile responsiveness on different screen sizes  


### I implemented the same testing strategy using Selenium since that is the tool I am comfortable with. I am attaching the same named as selenium_solution.py.
