package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import java.util.List;
import java.util.NoSuchElementException;

public class FindingElements extends BaseClass{
    static final String TABLE = "https://the-internet.herokuapp.com/tables";

    @Test 
    void findElementReturnsOne(){
        driver.get(TABLE);
        WebElement heading = driver.findElement(By.tagName("h3"));
        assertEquals("Data Tables", heading.getText());
    }

    @Test 
    void findElementsReturnsAll(){
        driver.get(TABLE);
        List<WebElement> rows = driver.findElements(By.cssSelector("#table1 tbody tr"));
        assertEquals(4, rows.size());
    }

    // assert 1. last name - smith, first name is John

    @Test 
    void findElementInELement(){
        driver.get(TABLE);
        WebElement firstrow = driver.findElements(By.cssSelector("#table1 tbody tr")).get(0);
        List <WebElement> cells = firstrow.findElements(By.tagName("td"));
        String lastName = cells.get(0).getText();
        String firstName = cells.get(1).getText();
        // to do assert
        assertEquals("Smith", lastName);
        assertEquals("John", firstName);
    }

    @Test 
    void nothingFound(){
        driver.get(TABLE);
        By missing=By.id("does-not-exist");
        assertThrows(NoSuchElementException.class, ()->driver.findElement(missing));
    }
    

}
