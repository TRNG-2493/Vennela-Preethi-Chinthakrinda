package com.revature.selenium;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class InventoryPage extends BaseClass {

    private final WebDriver driver;
    private final By title=By.cssSelector("[data-test='title']");
    private final By cartBadge=By.cssSelector("[data-test='shopping-cart-badge']");


    public InventoryPage(WebDriver driver){
        this.driver=driver;
    }

    String getTitle1(){
        //String title1=new WebDriverWait(driver, Duration.ofSeconds(10)).until(ExpectedCondition.visibilityOfAllElementsLocatedBy(title)).get
        
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        String title1 = wait.until((ExpectedConditions.visibilityOfElementLocated(title))).getText();


        return title1;
    }

    // addItem - add the items and assert the count

    // cart count
}
