import static org.junit.Assert.assertEquals;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class ServletTest {

    @Before
    public void init() {

    }

    @After
    public void clean(){
    }

    @Test
    public void matcherUrl() {
        String path = "https://localhost:4848/cratt/showcase?test=11";

        Pattern pattern = Pattern.compile(".*?cratt/(.*?)(?=\\?|$)");
        String targetPage = "index";

        Matcher matcher = pattern.matcher(path);
        if (matcher.find()) {
             targetPage = matcher.group(1);
        }
        
        String auxilaryParameters = "";
        pattern = Pattern.compile(targetPage + "(\\?.*)?");
        matcher = pattern.matcher(path);
        if (matcher.find()) {
            auxilaryParameters = matcher.group(1);
        }

        assertEquals("?test=11", auxilaryParameters);
        assertEquals("showcase",targetPage);
    }
}
