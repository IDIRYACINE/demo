package Shop.Items;
public class ItemTest {

    public static void testItem(ItemInterface item){
        System.out.println(item.getName());
        System.out.println(item.getQuantity());
        System.out.println(item.getPrice());
        System.out.println(item.getExpirationDate());

    }
    
}
