package Shop;
import java.util.ArrayList;

import Shop.Items.Item;
import Shop.Items.ItemTest;

public class ShoppingCart{

    ArrayList<Item> cart = new ArrayList<>();
    final int CART_CAPACITY_LIMITS = 5;
    
    public void addItem(Item item) throws Exception{
        if(cart.size() < CART_CAPACITY_LIMITS){
            cart.add(item);
        }
        else{
            throw new Exception("Cant add item cart is full");
        }
    }

    public void displayAllCartItem(){
        for (Item item : cart) {
            ItemTest.testItem(item);
        }
    }

    public int calculateItemsTotalPrice(){
        int totalPrice = 0;
        for (Item item : cart) {
            totalPrice += (item.getPrice() * item.getQuantity());
        }
        return totalPrice;
    }

    public int calculateItemsQuantity(){
        int itemsCount = 0;
        for (Item item : cart) {
            itemsCount += item.getQuantity();
        }
        return itemsCount;
    }

    public int getItemsCount() {
        return cart.size();
    }
    
}
