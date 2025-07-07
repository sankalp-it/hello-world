
package com.shared;
import org.springframework.stereotype.Component;

import main.java.com.shared.pipeline.PaymentProcessStep;
@Component("invoke")
public class InvokeStep implements PaymentProcessStep {
    public String apply(String input) {
        return "[INVOKED] " + input;
    }
}