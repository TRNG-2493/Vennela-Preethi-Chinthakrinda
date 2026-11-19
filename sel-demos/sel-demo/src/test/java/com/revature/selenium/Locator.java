package com.revature.selenium;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;

public class Locator extends BaseClass{

    @BeforeEach 
    void openLoginPage(){
        driver.get("https://www/saucedemo.com/");
    }

    @Test 
    
    void findByIdAndName(){
        WebElement username = driver.findElement(By.id("user-name"));

        WebElement password = driver.findElement(By.name("password"));

        WebElement button = driver.findElement(By.className("submit-button"));

        WebElement sameButton = driver.findElement(By.cssSelector(("[data-test='login-button']")));

    }

    @Test 
    void findByXpath(){
        WebElement userName = driver.findElement(By.xpath("//input[@id='user-name']"));
        WebElement Pass = driver.findElement(By.xpath("//input[@id='password']"));

        WebElement loginBtn = driver.findElement(By.xpath("//input[@id='login-button']"));
    }

}
