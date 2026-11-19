package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;

public class TestAlerts extends BaseClass{
    @Test 
    void testJSAlert(){
        driver.get("https://the-internet.herokuapp.com/javascript_alerts");
        driver.findElement(By.xpath("//button[text()='Click for JS Alert']")).click();
        Alert jsAlert=driver.switchTo().alert();
        assertEquals("I am a JS Alert", jsAlert.getText());
        jsAlert.accept();
        assertEquals("You successfully clicked an alert", driver.findElement(By.id("result")).getText());
    }

    @Test 
    void testJSConfirm(){
        driver.get("https://the-internet.herokuapp.com/javascript_alerts");
        driver.findElement(By.xpath("//button[text()='Click for JS Confirm']")).click();
        Alert jsConfirm=driver.switchTo().alert();
        assertEquals("I am a JS Confirm", jsConfirm.getText());
        jsConfirm.dismiss();
        assertEquals("You clicked: Cancel", driver.findElement(By.id("result")).getText());
    }

    @Test 
    void testJSPrompt(){
        driver.get("https://the-internet.herokuapp.com/javascript_alerts");
        driver.findElement(By.xpath("//button[text()='Click for JS Prompt']")).click();
        Alert jsPrompt=driver.switchTo().alert();
        assertEquals("I am a JS prompt", jsPrompt.getText());
        jsPrompt.dismiss();
        assertEquals("You entered: null", driver.findElement(By.id("result")).getText());
    }


}
