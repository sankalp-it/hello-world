package com.shared.pipeline;

import java.util.List;
import java.util.function.Function;

public class PaymentProviderProcessor {
    private final List<Function<String, String>> steps;

    public PaymentProviderProcessor(List<Function<String, String>> steps) {
        this.steps = steps;
    }

    public String process(String input) {
        String result = input;
        for (Function<String, String> step : steps) {
            result = step.apply(result);
        }
        return result;
    }
}