package com.revature.selenium;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage extends BaseClass{

    private final WebDriver driver;
    private final By username = By.id("user-name");
    private final By password = By.id("password");
    private final By loginButton = By.id("login-button");
    private final By errorMessage = By.cssSelector("[data-test='error']");

    public LoginPage(WebDriver driver){
        this.driver = driver;
    }

    public LoginPage open(){
        driver.get("https://www.saucedemo.com/");
        return this;
    }
// Successful Login -- goes to Inventory page
public InventoryPage loginAs(String user, String pass){
    driver.findElement(username).sendKeys(user);
    driver.findElement(password).sendKeys(pass);
    driver.findElement(loginButton).click();
    return new InventoryPage(driver);

}

// Failed login -- returns back to login page

}
