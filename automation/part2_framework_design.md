## Part 2: Test Framework Design

### 1)	Framework structure:

●	workflowpro-automation/  
○	tests/  
■	ui/  
■	api/  
■	integration/  
○	pages/  
■	LoginPage.py  
■	Dashboard.py  
■	ProjectPage.py  
○	utils/  
■	WaitUtils.py  
■	Driver.py  
○	config/  
■	env.properties  
■	tenants.properties  
■	users.properties  
○	reports/  

#### Explanation:  
tests/  
•	Contains all automated test cases  
•	Tests are grouped by UI, API, and integration type  


tests/ui/  
•	UI tests that validate user workflows  


tests/api/  
•	API tests used for backend validation and test data setup 

tests/integration/  
•	End-to-end tests combining API and UI flows

pages/  
•	Implements Page Object Model  
•	Contains locators and actions for each application page  

pages/LoginPage.py  
•	Login page elements and login actions  

pages/Dashboard.py  
•	Dashboard validations and navigation actions  

pages/ProjectPage.py  
•	Project-related UI interactions and validations  


utils/  
•	Common reusable utilities shared across tests  

utils/WaitUtils.py  
•	Centralized explicit wait logic  

utils/Driver.py  
•	Browser initialization logic  


config/  
•	External configuration files   

config/env.properties  
•	Environment-specific URLs and settings  

config/tenants.properties  
•	Tenant-specific URLs for multi-tenant testing  

config/users.properties  
•	User credentials grouped by role  


reports/  
•	Stores test execution reports, logs, and screenshots  

### 2)	Configuration management:
Configuration management ensures that test behaviour can be changed without modifying test code.
In this framework, configuration is externalized using property files to support multiple environments, tenants, browsers, and user roles.  
#### a)	Environment configuration (env.properties)  
•	Base URL and execution environment is stored in this file.  
•	This helps in determining the execution environment, avoiding hardcoded configuration in testing code, allowing browser change without changing the testing code  

#### b)	Tenant configuration (tenant.properties)  
•	Tenant specific URLs and IDs are stored in this file  
•	Ensures tenant isolation and avoids mixing company data  

#### c)	User and Role configuration (users.properties)  
•	Credentials grouped by role are stored in this file  
•	Allows role based testing without changing test logic  

### 3)	Identify missing requirements:  
•	How should test data be created, reused, and cleaned up?  
•	Are tests expected to run in parallel, and what are the limits?  
•	What reporting format is expected (HTML, logs, dashboards)?  
•	Are dedicated test environments and tenants available?  
•	Should mobile tests run for every feature or only critical flows?  
•	Are there rate limits, 2FA or IP restrictions for automation users?  
