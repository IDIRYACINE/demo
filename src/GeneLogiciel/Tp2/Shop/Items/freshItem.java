package Shop.Items;

public class freshItem implements ItemInterface{

    private String name;
    private Double price;
    private int quantity;
    private String expirationDate;
    
    public freshItem (String name , Double price , int quantity,String expirationDate){
        this.name = name;
        this.price = price;
        this.quantity = quantity;
        this.expirationDate = expirationDate;  
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
        return expirationDate;
    }

    
}
