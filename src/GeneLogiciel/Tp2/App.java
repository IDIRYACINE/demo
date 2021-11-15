import Shop.ShoppingCart;
import Shop.Items.Item;

public class App
{
    public static void main(String[] args) {
        ShoppingCart shoppingCart = new ShoppingCart();
        createItemsAndPopulateCart(shoppingCart);
        formatAndPrintCartInfos(shoppingCart);
        
    }

    public static void createItemsAndPopulateCart(ShoppingCart shoppingCart){
        String[] names = {"bread","salmon","cofee","water","milk"};
        int[] quantities = {500,101,101,50000,101};
        Double[] prices = {1.0,3.0,3.0,2.0,3.0};
        Item tempItem;
        for(int i=0 ;i<names.length ;i++){
            tempItem = new Item(names[i],prices[i],quantities[i]);
            try {
                shoppingCart.addItem(tempItem);
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }

    public static void formatAndPrintCartInfos(ShoppingCart shoppingCart){
        String CURRENCY = "DA";
        shoppingCart.displayAllCartItem();
        System.out.println("Total Items Count is : " + shoppingCart.getItemsCount());
        System.out.println("Total Items Quantity is : " + shoppingCart.calculateItemsQuantity());
        System.out.println("Total Items Price is : " + shoppingCart.calculateItemsTotalPrice() +" "+ CURRENCY);

    }
    
}