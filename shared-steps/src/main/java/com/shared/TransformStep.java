package com.shared;
import org.springframework.stereotype.Component;

import main.java.com.shared.pipeline.PaymentProcessStep;

@Component("transform")
public class TransformStep implements PaymentProcessStep {
    public String apply(String input) {
        return "[TRANSFORMED] " + input;
    }
}