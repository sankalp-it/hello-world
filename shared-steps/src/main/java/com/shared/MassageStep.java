package com.shared;
import java.util.function.Function;

import org.springframework.stereotype.Component;

@Component("massage")
public class MassageStep implements Function<String, String> {
    public String apply(String input) {
        return "[MASSAGED] " + input;
    }
}