package com.revature.selenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.decorators.WebDriverDecorator;

public class LoginPageFactory {
    private final WebDriver driver;

    @FindBy(id="user-name")
    private WebElement username;
    
    @FindBy(id="password")
    private WebElement password;

    @FindBy(id="login-button")
    private WebElement loginButton;
    
    // WebElement loginButton = driver.findElement(By.id("login-button"))
    // simplifies the write of code - easy readable


    public LoginPageFactory(WebDriver driver){
        this.driver=driver;
        PageFactory.initElements(driver, this);
}

    public LoginPageFactory open(){
        driver.get("https://www.saucedemo.com/");
        return this;

    }

    public InventoryPage loginAs(String user, String pass){
        username.sendKeys(user);
        password.sendKeys(pass);
        loginButton.click();
        return new InventoryPage(driver);
    }

}
