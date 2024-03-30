import time



from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys 

app = Flask(__name__)
CORS(app)

def is_logged_in(driver):
    try:
        # Check if a greeting message or user profile icon is visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Welcome,')]")))
        return True
    except TimeoutException:
        return False

@app.route('/run-python-script', methods=["POST"])
def run_python_script():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        name = data.get("name")
        duration = data.get("duration")

        p1 = data.get("p1")
        p2 = data.get("p2")
        p3 = data.get("p3")

        print(p2)

        options = Options()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get("https://codeforces.com/")

        contests_link = driver.find_element(By.LINK_TEXT, "Enter")
        contests_link.click()

        username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "handleOrEmail")))
        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

        username_field.clear()
        password_field.clear()

        username_field.send_keys(username)
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN) 
 

        # Click the login button
        # login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.submit[value='Enter']")))
        # login_button.click()


        # Wait for successful login
        if is_logged_in(driver):
            print("Login successful!")
        else:
            print("Login unsuccessful!")

        # Optionally, print out the page source
        # print(driver.page_source)

        # Adjust wait conditions as needed for the subsequent steps

        # Example: Wait for GYM link to be clickable
        gym_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "GYM")))
        gym_link.click()

        # Example: Wait for Mashups link to be clickable
        mashup_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "MASHUPS")))
        mashup_link.click()

        # Example: Wait for Create new mashup link to be clickable
        create_new = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Create new mashup")))
        create_new.click()

        print(name)
        print(duration)

        name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "contestName")))
        duration_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "contestDuration")))

        name_field.clear()
        duration_field.clear()

        name_field.send_keys(name)
        duration_field.send_keys(duration)

        # problem_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "problemQuery")))
        # # problem_field.clear()
        # print(p1)

        # problem_field.send_keys(p1)

        # # time.sleep(5)

        # # WebDriverWait(10)
        # print(4)
        # add_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "_MashupContestEditFrame_addProblemLink")))
        # add_field.click()

        # print(5)
        # # problem_field.clear()

        # problem_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "problemQuery")))
        # # problem_field.clear()
        # print(6)
        # problem_field.send_keys(p2)
        # print(7)

        problem_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'problemQuery')))
        # p1 = 'Your first input'  # Replace with your actual input
        print(1)
        # Send keys to the problem_field
        problem_field.send_keys(p1)
        print(2)
        # Click the add button
        
        add_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, '_MashupContestEditFrame_addProblemLink')))
        add_field.click()
        print(problem_field)
        print(3)
        # Re-locate the problem_field after clicking the add button
        # problem_field.clear()
        # print(problem_field)
        problem_field2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'problemQuery')))
        # p2 = 'Your second input'  # Replace with your actual input

        # Send keys to the updated problem_field
        print(problem_field2)
        print(7)
        problem_field2.send_keys(p2)
        print(8)


        # add_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "_MashupContestEditFrame_addProblemLink")))
        # add_field.click()

        # problem_field.clear()

        # problem_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "problemQuery")))
        

        # problem_field.send_keys(p3)

        # add_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "_MashupContestEditFrame_addProblemLink")))
        # add_field.click()

        return jsonify({"message": "Login successful!"})

    except (TimeoutException, NoSuchElementException) as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)