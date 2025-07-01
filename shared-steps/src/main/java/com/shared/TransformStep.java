package com.shared;
import java.util.function.Function;

import org.springframework.stereotype.Component;

@Component("transform")
public class TransformStep implements Function<String, String> {
    public String apply(String input) {
        return "[TRANSFORMED] " + input;
    }
}