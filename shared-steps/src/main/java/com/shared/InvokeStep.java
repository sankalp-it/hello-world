
package com.shared;
import java.util.function.Function;

import org.springframework.stereotype.Component;
@Component("invoke")
public class InvokeStep implements Function<String, String> {
    public String apply(String input) {
        return "[INVOKED] " + input;
    }
}