package com.revature.selenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
public abstract class BaseClass {

    protected WebDriver driver;

    @BeforeEach
    void startBrowser() {
        driver = new ChromeDriver();
    }

    @AfterEach
    void stopBrowser() {
        driver.quit();
    }
}