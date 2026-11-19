package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.time.Duration;
import java.util.NoSuchElementException;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class WaitTest extends BaseClass {
    @Test 
    void withoutWait(){
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2");
        driver.findElement(By.cssSelector("#start button")).click();
        // String text = driver.findElement(By.id("finish")).getText();
        // System.out.println(text);
        assertThrows(NoSuchElementException.class, ()-> driver.findElement(By.id("finish")));

    }
    
    @Test
    void testImplicitWait(){
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2");
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.findElement(By.cssSelector("#start button")).click();
        driver.findElement(By.id("finish")).getText();
        assertEquals("Hello World!", driver.findElement(By.id("finish")).getText());

    }

    @Test
    void testExplicitWait(){
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2");
        //driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.findElement(By.cssSelector("#start button")).click();
        //driver.findElement(By.id("finish")).getText();
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        WebElement finish = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("finish")));
        assertEquals("Hello World!", finish.getText());

    }
}
