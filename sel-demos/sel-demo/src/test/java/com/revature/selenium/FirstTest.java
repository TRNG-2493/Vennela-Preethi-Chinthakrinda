package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class FirstTest {
    WebDriver driver = new ChromeDriver();


    @BeforeEach 
    void startBrowser(){
        driver = new ChromeDriver();
    }

    @AfterEach 
    void stopBrowser(){
        driver.quit();
    }


    @Test 
    public void testTitle(){
        // WebDriver driver = new ChromeDriver();
        driver.get("https://www.saucedemo.com");
        assertEquals("Swag Labs", driver.getTitle());
        // driver.quit();
        
    }

    @Test 
    public void testCurrentURL(){
        driver.get("https://www.saucedemo.com");
        assertEquals("https://www.saucedemo.com", driver.getCurrentUrl());

    }
    
}
