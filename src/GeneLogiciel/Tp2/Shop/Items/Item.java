package Shop.Items;
public class Item implements ItemInterface{
    private String name;
    private Double price;
    private int quantity;

    public Item (String name , Double price , int quantity){
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
    
    @Override
    public String getName(){
        return name;
    }

    @Override
    
    public Double getPrice(){
        return price;
    }

    @Override
    public int getQuantity(){
        return quantity;
    }

    @Override
    public String getExpirationDate(){
        return "";
    }

    
}
