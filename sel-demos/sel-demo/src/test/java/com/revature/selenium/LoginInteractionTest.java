package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class LoginInteractionTest extends BaseClass{
    static final String LOGIN = "https://the-internet.herokuapp.com/login";
    @BeforeEach 
    void openPage(){
        driver.get(LOGIN);
    }

    @Test 
    void testValidLogin(){
        WebElement username = driver.findElement(By.id("username"));
        username.sendKeys("tomsmith");
        driver.findElement(By.id("password")).sendKeys("SuperSecretPassword!");
        driver.findElement(By.cssSelector("button[type='submit']")).click();
        assertEquals("https://the-internet.herokuapp.com/secure", driver.getCurrentUrl());
        String message = driver.findElement(By.id("flash")).getText();
        assertTrue(message.contains("You logged into a secure area!"));

    }

    @Test 
    void testInvalidLogin(){
        WebElement username = driver.findElement(By.id("username"));
        username.sendKeys("wrongusername");
        driver.findElement(By.id("password")).sendKeys("wrongpassword");
        driver.findElement(By.cssSelector("button[type='submit']")).click();

    }

}
