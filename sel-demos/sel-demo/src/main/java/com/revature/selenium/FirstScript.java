package com.revature.selenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class FirstScript {
    public static void main(String[] args) {
        
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--start-maximized");
        options.addArguments("--headless=new");
        options.addArguments("window-size=1280,800");

        // Initialize the WebDriver
        WebDriver driver = new ChromeDriver(options);
        
        // Open a page
        driver.get("https://www.saucedemo.com");
        System.out.println("Title: " + driver.getTitle());
        System.out.println("URL ::"+driver.getCurrentUrl());

        // driver.close(); // closes current browser
        driver.quit(); // closes all browsers windows

    }
}