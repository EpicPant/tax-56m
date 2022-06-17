import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome("./chromedriver")
driver.get("https://etax23.ird.gov.hk/ird/login/jsp/LandingPage.jsp")


login_btn = '/html/body/div/div/div[3]/div[2]/div/table[3]/tbody/tr/td[1]/div[2]/div/div/input[1]'

driver.find_element(by=By.XPATH, value=login_btn).click()

def login(driver):
    login_name = '/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[3]/td/input'
    login_password = '/html/body/div/div[2]/div[2]/div/form/table/tbody/tr[5]/td/input'
    login_submit = '/html/body/div/div[2]/div[2]/div/form/span/table/tbody/tr/td/a'

    # login form handling
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, login_name))
        ).send_keys('Login Name Here')

        driver.find_element(by=By.XPATH, value=login_password).send_keys('Login Passwords Here')
        driver.find_element(by=By.XPATH, value=login_submit).click()
    except TimeoutException:
        print('login form not found, timed out')

    # detect alert after login
    try:
        WebDriverWait(driver, 5).until(
            EC.alert_is_present()
        )
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        print('no alert, time out')

def online_service(driver):
    # IFRAME -> BUTTON
    iframe = '/html/frameset/frame'
    driver.switch_to.frame(driver.find_element(by=By.XPATH, value=iframe))

    # ONLINE SERVICE TAB
    online_service = '/html/body/div/div/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div/table[2]/tbody/tr/td[2]/span/a'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, online_service))
    ).click()

    # go to 56m form
    filing_56m = '/html/body/div/div/div/table/tbody/tr[1]/td[2]/div/div[2]/div[2]/div/table[7]/tbody/tr[12]/td[1]/a'

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, filing_56m))
        ).click()
    except TimeoutException:
        print('no filing button found, timed out')


    # continue button
    continue_button = '/html/body/div/div[2]/div[2]/div/div[8]/div/a'

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, continue_button))
        ).click()

    except TimeoutException:
        print('continue button not found, timed out')

    # continue button
    continue_button = '/html/body/div/div[2]/div[2]/div/div[9]/div/a[2]'

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, continue_button))
        ).click()
    except TimeoutException:
        print('continue button 2 not found, timed out')

def employer_info(driver):
    # Prepare and submit now button
    entry_mode = '/html/body/div/div[2]/div[2]/div/form/table[2]/tbody/tr[4]/td[2]/input'
    continue_button = '/html/body/div/div[2]/div[2]/div/div[5]/div/a[3]'

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, entry_mode))
        ).click()
    except TimeoutException:
        print('Prepare and Submit now button not found')

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, continue_button))
        ).click()
    except TimeoutException:
        print('continue button in entry mode page not found, timed out')


    # Employer Info

    #Employer File Number
    file_number = '/html/body/div/div[2]/div[2]/div/form/table[2]/tbody/tr[1]/td[3]/input[1]'
    file_number_end = '/html/body/div/div[2]/div[2]/div/form/table[2]/tbody/tr[1]/td[3]/input[2]'

    identification_code = '/html/body/div/div[2]/div[2]/div/form/table[3]/tbody/tr/td[2]/input'

    self_selected_key = '/html/body/div/div[2]/div[2]/div/form/div[4]/table[1]/tbody/tr/td[3]/input'

    create_new_data = '/html/body/div/div[2]/div[2]/div/form/div[4]/table[2]/tbody/tr[1]/td[2]/input'

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, file_number))
        ).send_keys('6C1')

        driver.find_element(by=By.XPATH, value=file_number_end).send_keys('38344070')
        driver.find_element(by=By.XPATH, value=identification_code).send_keys('63GK89Z2')
        driver.find_element(by=By.XPATH, value=self_selected_key).send_keys('22109588')
        driver.find_element(by=By.XPATH, value=create_new_data).click()

    except TimeoutException:
        print('cannot find employer file number input, timed out')

    input('Press any key to continue')

    try:
        continue_to_mode = '/html/body/div/div[2]/div[2]/div/div[5]/a[2]'
        driver.find_element(by=By.XPATH, value=continue_to_mode).click()
    except:
        print('cannot find continue to mode button, timed out')

    try:
        confirm_employer_info = '/html/body/div/div[2]/div[2]/div/form/table[2]/tbody/tr[1]/td[1]/input'
        driver.find_element(by=By.XPATH, value=confirm_employer_info).click()

        continue_button = '/html/body/div/div[2]/div[2]/div/div[5]/a[2]'
        driver.find_element(by=By.XPATH, value=continue_button).click()
    except:
        print('cannot find confirm employer info yes button, timed out')

def mode(driver):
    # 補充
    mode_selection = '/html/body/div/div[2]/div[2]/div/form/table[4]/tbody/tr[1]/td[1]/input[1]'
    continue_button = '/html/body/div/div[2]/div[2]/div/div[4]/div/a[2]'
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, mode_selection))
        ).click()
        driver.find_element(by=By.XPATH, value=continue_button).click()

    except TimeoutException:
        print('cannot find 補充 mode, timed out')


def filing(driver):

    #CHOOSE 56M and Year
    form_56m = '/html/body/div/div[2]/div[2]/div/form[1]/table[5]/tbody/tr[1]/td[1]/input'
    year_input = '/html/body/div/div[2]/div[2]/div/form[1]/table[5]/tbody/tr[1]/td[2]/select/option[2]'
    continue_button = '/html/body/div/div[2]/div[2]/div/div[5]/a[2]'

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, form_56m))
    ).click()

    try:
        WebDriverWait(driver, 5).until(
            EC.alert_is_present()
        )
        alert = driver.switch_to.alert
        alert.accept()

        iframe = '/html/frameset/frame'
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, iframe))
        )
        driver.switch_to.frame(driver.find_element(by=By.XPATH, value=iframe))
    except TimeoutException:
        print('no alert, time out')

    driver.find_element(by=By.XPATH, value=year_input).click()
    driver.find_element(by=By.XPATH, value=continue_button).click()

def form_filler(driver, data):
    form_language = '/html/body/div/div[2]/div[2]/div/form[2]/table[1]/tbody/tr[1]/td[4]/input'
    supplementary_form = '/html/body/div/div[2]/div[2]/div/form[2]/table[1]/tbody/tr[5]/td[2]/input'
    for_individual = '/html/body/div/div[2]/div[2]/div/form[2]/table[6]/tbody/tr/td[1]/input'
    sallutation_male = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[1]/tbody/tr[1]/td[3]/input[2]'
    sallutation_female = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[1]/tbody/tr[1]/td[6]/input'
    surname_field = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[1]/tbody/tr[2]/td[3]/input'
    given_name_field = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[1]/tbody/tr[3]/td[3]/input'
    hkid_long = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[2]/tbody/tr[1]/td[3]/input[1]'
    hkid_short = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[2]/tbody/tr[1]/td[3]/input[2]'
    sex_male = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[3]/tbody/tr/td[3]/input[2]'
    sex_female = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[3]/tbody/tr/td[4]/input'
    # marital_status = '/html/body/div/div[2]/div[2]/div/form[2]/div[4]/table[4]/tbody/tr/td[3]/input[2]'
    address_1 = '/html/body/div/div[2]/div[2]/div/form[2]/table[8]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/input'
    address_2 = '/html/body/div/div[2]/div[2]/div/form[2]/table[8]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/input'
    address_3 = '/html/body/div/div[2]/div[2]/div/form[2]/table[8]/tbody/tr[3]/td[2]/table/tbody/tr[4]/td/input'
    address_area = '/html/body/div/div[2]/div[2]/div/form[2]/table[8]/tbody/tr[3]/td[2]/table/tbody/tr[5]/td/input[2]'
    phone = '/html/body/div/div[2]/div[2]/div/form[2]/table[9]/tbody/tr/td[2]/input'
    continue_button = '/html/body/div/div[2]/div[2]/div/div[8]/a[4]'

    driver.find_element(by=By.XPATH, value=form_language).click()
    driver.find_element(by=By.XPATH, value=supplementary_form).click()
    driver.find_element(by=By.XPATH, value=for_individual).click()
    if data[2] == 'M':
        driver.find_element(by=By.XPATH, value=sallutation_male).click()
        driver.find_element(by=By.XPATH, value=sex_male).click()
    else:
        driver.find_element(by=By.XPATH, value=sallutation_female).click()
        driver.find_element(by=By.XPATH, value=sex_female).click()
    driver.find_element(by=By.XPATH, value=surname_field).send_keys(data[0])
    driver.find_element(by=By.XPATH, value=given_name_field).send_keys(data[1])
    driver.find_element(by=By.XPATH, value=hkid_long).send_keys(data[4])
    driver.find_element(by=By.XPATH, value=hkid_short).send_keys(data[5])
    driver.find_element(by=By.XPATH, value=address_1).send_keys(data[6])
    if str(data[7]) != '-':
        driver.find_element(by=By.XPATH, value=address_2).send_keys(data[7])
    if str(data[8]) != '-':
        driver.find_element(by=By.XPATH, value=address_3).send_keys(data[8])
    if str(data[9]) != '-':
        driver.find_element(by=By.XPATH, value=phone).send_keys(data[9])
    driver.find_element(by=By.XPATH, value=address_area).click()
    driver.find_element(by=By.XPATH, value=continue_button).click()



def form_filler_income(driver, data, end):
    job_title = '/html/body/div/div[2]/div[2]/div/form[3]/table[1]/tbody/tr/td[2]/input'
    start_date = '/html/body/div/div[2]/div[2]/div/form[3]/table[2]/tbody/tr[2]/td/input[1]'
    start_month = '/html/body/div/div[2]/div[2]/div/form[3]/table[2]/tbody/tr[2]/td/input[2]'
    start_year = '/html/body/div/div[2]/div[2]/div/form[3]/table[2]/tbody/tr[2]/td/input[3]'
    end_date = '/html/body/div/div[2]/div[2]/div/form[3]/table[2]/tbody/tr[2]/td/input[4]'
    end_month = '/html/body/div/div[2]/div[2]/div/form[3]/table[2]/tbody/tr[2]/td/input[5]'
    end_year = '/html/body/div/div[2]/div[2]/div/form[3]/table[2]/tbody/tr[2]/td/input[6]'
    service_fee = '/html/body/div/div[2]/div[2]/div/form[3]/table[3]/tbody/tr[9]/td[4]/input'
    always_no = '/html/body/div/div[2]/div[2]/div/form[3]/table[3]/tbody/tr[12]/td[3]/input'
    add_new = '/html/body/div/div[2]/div[2]/div/div[9]/a[4]'
    save_draft = '/html/body/div/div[2]/div[2]/div/div[9]/a[5]'

    driver.find_element(by=By.XPATH, value=job_title).send_keys('Casual Worker')
    driver.find_element(by=By.XPATH, value=start_date).send_keys(data[13])
    driver.find_element(by=By.XPATH, value=start_month).send_keys(data[12])
    driver.find_element(by=By.XPATH, value=start_year).send_keys(data[11])
    driver.find_element(by=By.XPATH, value=end_date).send_keys(data[16])
    driver.find_element(by=By.XPATH, value=end_month).send_keys(data[15])
    driver.find_element(by=By.XPATH, value=end_year).send_keys(data[14])
    driver.find_element(by=By.XPATH, value=service_fee).send_keys(data[10])
    driver.find_element(by=By.XPATH, value=always_no).click()
    if end is True:
        driver.find_element(by=By.XPATH, value=save_draft).click()
    else:
        driver.find_element(by=By.XPATH, value=add_new).click()


if __name__ == '__main__':
    login(driver)
    online_service(driver)
    employer_info(driver)
    mode(driver)

    starting_batch = int(input('Starting Batch No#'))
    # no_of_batch = int(input('How many batch to run: '))

    # for i in range(no_of_batch):
    csv_reader = pd.read_csv('56m.csv', nrows=30, skiprows=30 * (starting_batch - 1))

    for index, row in csv_reader.iterrows():
        should_end = False
        if index == 30:
            should_end = True
        # PASS ROW TO FORM_FILLIER()
        filing(driver)
        form_filler(driver, row)
        form_filler_income(driver, row, should_end)
        print('Finished #{0}'.format(index + 1))
        
        # if len(csv_reader.index) != 30:
        #     break

    input('Press any key to close')
    driver.close()