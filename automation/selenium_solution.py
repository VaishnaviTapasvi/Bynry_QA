
"""
Tool Used: Python + Selenium + Requests
This is a conceptual implementation written to demonstrate
testing strategy and approach.

"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_project_creation_flow():
    """
    Validates project creation flow using:
    1. API for test data creation
    2. Selenium UI validation for web
    3. Tenant isolation check
    """

    # Test Configuration
    
    api_url = "https://api.workflowpro.com/api/v1/projects"
    tenant_a_url = "https://company1.workflowpro.com/login"
    tenant_b_url = "https://company2.workflowpro.com/login"

    headers = {
        "Authorization": "Bearer valid_token",
        "X-Tenant-ID": "company_1"
    }

    project_name = "Test Project"

    
    # 1: API – Create Project
    
    payload = {
        "name": project_name,
        "description": "Created via API for integration testing",
        "team_members": ["user1", "user2"]
    }

    response = requests.post(api_url, json=payload, headers=headers)
    assert response.status_code == 201

    project_id = response.json().get("id")
    assert project_id is not None

    
    # 2: Web UI – Verify Project Display
    
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    driver.get(tenant_a_url)

    driver.find_element(By.ID, "email").send_keys("admin@company1.com")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "login").click()

    # Wait for dashboard to load
    wait.until(EC.presence_of_element_located((By.ID, "dashboard")))

    # Verify project appears in UI
    project_element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//div[text()='{project_name}']")
        )
    )

    assert project_element.is_displayed()

    
    # 3: Mobile: Check mobile accessibility
   
    """
    Mobile validation would be performed using:
    - Mobile browser or
    - Cloud platforms like BrowserStack

    Steps (conceptual):
    - Launch mobile session
    - Login using Tenant A credentials
    - Verify project is visible on mobile UI
    """

    
    # 4: Security: Verify tenant isolation
    
    driver.get(tenant_b_url)

    driver.find_element(By.ID, "email").send_keys("admin@company2.com")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "login").click()

    wait.until(EC.presence_of_element_located((By.ID, "dashboard")))

    project_elements = driver.find_elements(
        By.XPATH, f"//div[text()='{project_name}']"
    )

    assert len(project_elements) == 0

    driver.quit()
