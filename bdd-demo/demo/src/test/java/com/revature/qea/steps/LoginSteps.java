package com.revature.qea.steps;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.HashMap;
import java.util.Map;
import java.time.Duration;

import static org.junit.jupiter.api.Assertions.assertEquals;

/** Step definitions for login.feature (final version from Cucumber Handout 1, topic 1.4). */
public class LoginSteps {
    private WebDriver driver;
    private ChromeOptions options = new ChromeOptions();
    private Map<String, Object> pref = new HashMap<>();

    @Before
    public void openBrowser() {

    // Disable Chrome password manager
    pref.put("credentials_enable_service", false);
    pref.put("profile.password_manager_enabled", false);
    pref.put("profile.password_manager_leak_detection", false);

    // Disable Safe Browsing
    pref.put("safebrowsing.enabled", false);

    // Apply preferences to Chrome
    options.setExperimentalOption("prefs", pref);

    // Launch Chrome with configured options
    driver = new ChromeDriver(options);
}

    
    @Given("I am on the login page")
    public void iAmOnTheLoginPage() {
        driver.get("https://www.saucedemo.com/");
    }

    @When("I log in with username {string} and password {string}")
    public void iLogInWith(String username, String password) {
        driver.findElement(By.id("user-name")).sendKeys(username);
        driver.findElement(By.id("password")).sendKeys(password);
        driver.findElement(By.id("login-button")).click();
    }

    @Given("I have logged in with username {string} and password {string}")
    public void iHaveLoggedInWith(String username, String password) {
        iLogInWith(username, password);
    }

    @When("I log out")
    public void iLogOut() {
        driver.findElement(By.id("react-burger-menu-btn")).click();
        new WebDriverWait(driver, Duration.ofSeconds(10))
                .until(ExpectedConditions.elementToBeClickable(By.id("logout_sidebar_link")))
                .click();
    }

    @Then("I should see the {string} page")
    public void iShouldSeeThePage(String expectedTitle) {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        String actualTitle = wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.cssSelector("[data-test='title']"))).getText();
        assertEquals(expectedTitle, actualTitle);
    }

    @Then("I should see the error {string}")
    public void iShouldSeeTheError(String expectedError) {
        String actualError = driver.findElement(By.cssSelector("[data-test='error']")).getText();
        assertEquals(expectedError, actualError);
    }

    @Then("I should be back on the login page")
    public void iShouldBeBackOnTheLoginPage() {
        new WebDriverWait(driver, Duration.ofSeconds(15))
                .until(ExpectedConditions.visibilityOfElementLocated(By.id("login-button")));
        String url = driver.getCurrentUrl();
        assertEquals("https://www.saucedemo.com/", url);
    }

    @After(order = 0)
    public void closeBrowser() {
        driver.quit();
    }
}