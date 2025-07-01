
package com.shared;
import java.util.function.Function;

import org.springframework.stereotype.Component;

@Component("decrypt")
public class DecryptStep implements Function<String, String> {
    public String apply(String input) {
        return "[DECRYPTED] " + input;
    }
}

