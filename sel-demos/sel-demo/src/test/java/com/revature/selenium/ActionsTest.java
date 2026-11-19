package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;

public class ActionsTest extends BaseClass{

    @Test 
    void testTabInTheTextBox(){
        driver.get("https://the-internet.herokuapp.com/key_presses");
        WebElement box = driver.findElement(By.id("target"));
        new Actions(driver).click(box).sendKeys(Keys.TAB).perform();
        assertEquals("You entered: TAB", driver.findElement(By.id("result")).getText());

    }

    @Test
    void dragAOntoB() {
        driver.get("https://the-internet.herokuapp.com/drag_and_drop");
        WebElement boxA = driver.findElement(By.id("column-a"));
        WebElement boxB = driver.findElement(By.id("column-b"));
        assertEquals("A", boxA.getText());
        new Actions(driver).dragAndDrop(boxA, boxB).perform();
        assertEquals("B", driver.findElement(By.id("column-a")).getText());
}

}
