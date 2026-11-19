package com.revature.selenium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class PajeObjectTest extends BaseClass{


    @Test
    void standardUserSeesProducts(){
        LoginPage lp = new LoginPage(driver);
        lp.open();
        InventoryPage inventoryPage= lp.loginAs("standard_user", "secret_sauce");
        assertEquals("Products", inventoryPage.getTitle1());
        
    }

    @Test
    void standardUserSeesProductsLoginFactory(){
        LoginPageFactory lpf = new LoginPageFactory(driver);
        lpf.open();
        InventoryPage inventoryPage= lpf.loginAs("standard_user", "secret_sauce");
        assertEquals("Products", inventoryPage.getTitle1());
        
    }


}
