import static org.junit.Assert.assertTrue;

import java.util.ArrayList;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.idir.tp.MysqlHelper;
import com.idir.tp.Personne;

public class DatabaseTest {

    @Before
    public void init() {
        try {
            MysqlHelper.getInstance().connect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @After
    public void clean(){
        MysqlHelper.getInstance().disconnect();
    }

    @Test
    public void connectToDatabase() {
        boolean connected;

        try {
            MysqlHelper.getInstance().connect();
            connected = true;
        } catch (Exception e) {
            e.printStackTrace();
            connected = false;
        }

        assertTrue(connected);
    }

    @Test
    public void registerPersonne() {
        boolean registered;

        try {
            registered = MysqlHelper.getInstance().registerPersonne("test", "test", "test");
        } catch (Exception e) {
            e.printStackTrace();
            registered = false;
        }

        assertTrue(registered);
    }

    @Test
    public void loadAllPersonnes() {
        boolean loaded;
        ArrayList<Personne> data;
        try {
            data =  MysqlHelper.getInstance().loadAllPersonnes();
            System.out.println(data.get(0).getNom());
            loaded = true;
        } catch (Exception e) {
            e.printStackTrace();
            loaded = false;
        }

        assertTrue(loaded);
    }
}
