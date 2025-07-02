package com.shared;
import org.springframework.stereotype.Component;

import main.java.com.shared.pipeline.PaymentProcessStep;

@Component("massage")
public class MassageStep implements PaymentProcessStep {
    public String apply(String input) {
        return "[MASSAGED] " + input;
    }
}