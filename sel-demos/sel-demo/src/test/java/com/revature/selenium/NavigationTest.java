package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class NavigationTest extends BaseClass{
    WebDriver driver = new ChromeDriver();
    String HOME = "https://the-internet.herokuapp.com/";
    String LOGIN = "https://the-internet.herokuapp.com/two_factor";

    @Test 
    void getOpenPages(){
        driver.get(HOME);
        assertEquals("https://the-internet.herokuapp.com/", driver.getCurrentUrl());
        assertEquals("The Internet", driver.getTitle());

    }

    @Test 
    void backAndForward(){
        driver.get(HOME);
        driver.navigate().to(LOGIN);
        assertEquals("LOGIN", driver.getCurrentUrl());

        driver.navigate().back();
        assertEquals("https://the-internet.herokuapp.com/", driver.getCurrentUrl());

        driver.navigate().forward();
        assertEquals("LOGIN", driver.getCurrentUrl());

        driver.navigate().refresh();
        assertEquals("https://the-internet.herokuapp.com/", driver.getCurrentUrl());
    }

}
