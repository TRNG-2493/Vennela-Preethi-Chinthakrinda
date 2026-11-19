package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.Select;

public class DropDownTest extends BaseClass{

    @BeforeEach 
    void openDropDown(){
        driver.get("https://the-internet.herokuapp.com/dropdown");
    }
    private Select dropdown(){
        return new Select(driver.findElement(By.id("dropdown")));
    }

    @Test 
    void testSelectByVisibleText(){
        dropdown().selectByVisibleText("Option 1");
        assertEquals("Option 1", dropdown().getFirstSelectedOption().getText());
    }

    @Test 
    void testSelectByValue(){
        dropdown().selectByValue("2");
        assertEquals("Option 2", dropdown().getFirstSelectedOption().getText());
    }

    /*@Test 
    void testSelectByIndex(){
        dropdown().selectByIndex("0");
        assertEquals(driver, driver);
    }*/

}
